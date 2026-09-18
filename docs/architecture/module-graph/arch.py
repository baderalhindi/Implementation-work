"""TASK-007 module/edge model. Single source for the diagram, the edge register and the checks.

Edge direction = runtime initiator -> receiver.
Types: S = synchronous typed application-service command (in-process, via <Module>.Contracts)
       P = typed projection / read-model query (read-only, via <Module>.Contracts.Projections)
       E = integration event through the caller's transactional outbox (asynchronous)
       C = durable callback through the caller's outbox (asynchronous, idempotent)
       R = direct repository / DbContext / table access across modules  -- PROHIBITED, must be 0
Layer rule: S and P edges never go to a higher layer. E and C may.
"""
from collections import defaultdict

# id, wf/fg, blueprint name, process area, layer, backend task(s), frontend feature, frontend task, bpk
MODULES = [
    ("Project",               "WF-01", "Project Creation & Registration",        "P1", 2, "041",      "projects",               "042", "BPK-014"),
    ("Progress",              "WF-02", "Project Progress Update",                "P2", 2, "044",      "progress",               "045", "BPK-022"),
    ("Schedule",              "WF-03", "Schedule & Baseline Management",         "P2", 2, "046",      "schedule",               "047", "BPK-015"),
    ("Task",                  "WF-04", "Task Management",                        "P2", 2, "048",      "tasks",                  "049", "BPK-016"),
    ("Milestone",             "WF-05", "Milestone Management",                   "P2", 2, "050",      "milestones",             "051", "BPK-017"),
    ("Risk",                  "WF-06", "Risk Management",                        "P3", 2, "055",      "risks",                  "056", "BPK-018"),
    ("ManagementConcern",     "WF-07", "Issue & Challenge Management",           "P3", 2, "057",      "issues-challenges",      "058", "BPK-019"),
    ("ChangeRequest",         "WF-08", "Project Change Request",                 "P4", 2, "060",      "change-requests",        "061", "BPK-020"),
    ("Suspension",            "WF-09", "Project Suspension & Resumption",        "P4", 2, "062",      "suspension-closure",     "064", "BPK-024"),
    ("Closure",               "WF-10", "Project Completion & Closure",           "P4", 2, "063",      "suspension-closure",     "064", "BPK-025"),
    ("Approval",              "WF-11", "Shared Approval Framework",              "P4", 1, "035",      "approvals",              "036", "BPK-011"),
    ("DocumentManagement",    "WF-12", "Document Management",                    "P5", 1, "037",      "documents",              "038", "BPK-010"),
    ("ExternalParticipation", "WF-13", "External Entity Update & Review",        "P5", 3, "066",      "external-participation", "067", "BPK-023"),
    ("FinancialKpi",          "WF-14", "KPI & Financial Progress",               "P2", 2, "052",      "financial-kpi",          "053", "BPK-021"),
    ("Notifications",         "WF-15", "Notifications, Reminders & Escalations", "P6", 1, "039",      "notifications",          "040", "BPK-012"),
    ("Dashboards",            "FG-01", "Dashboards",                             "P7", 4, "069",      "dashboards",             "070", "BPK-026"),
    ("Reports",               "FG-02", "Reports, Filters & Export",              "P7", 4, "071",      "reports",                "072", "BPK-027"),
    ("IdentityAccess",        "FG-03", "Users, Roles & Permissions",             "P8", 0, "031",      "identity-access",        "032", "BPK-006"),
    ("MasterDataConfig",      "FG-04", "Master Data & Configuration",            "P8", 0, "034",      "master-data-config (reserved)", "—", "BPK-007"),
    ("IntegrationMonitoring", "FG-05", "Integration Monitoring",                 "P9", 0, "075",      "integration-admin",      "076", "BPK-009"),
    ("AuditActivity",         "FG-06", "Audit & Activity",                       "P9", 0, "033, 073", "audit-activity",         "074", "BPK-008"),
]
M = {m[0]: m for m in MODULES}
LAYER = {m[0]: m[4] for m in MODULES}
WF = {m[0]: m[1] for m in MODULES}
ALL = [m[0] for m in MODULES]
L2 = [m[0] for m in MODULES if m[4] == 2]
LAYER_NAME = {
    0: "L0 Platform foundations",
    1: "L1 Shared runtimes",
    2: "L2 Source business domains",
    3: "L3 External intake",
    4: "L4 Management intelligence",
}

EDGES = []  # (caller, callee, type, contract, purpose, conditional)


def edge(callers, callees, t, contract, purpose, conditional=False):
    if isinstance(callers, str):
        callers = [callers]
    if isinstance(callees, str):
        callees = [callees]
    for a in callers:
        for b in callees:
            if a == b:
                continue
            EDGES.append((a, b, t, contract, purpose, conditional))


others = lambda x: [m for m in ALL if m != x]

# ---- L0 platform foundations: consumed by everything ----------------------------------------
edge(others("IdentityAccess"), "IdentityAccess", "S", "INT-023; ICD-12; BE-002",
     "Authorize action / scope / relationship / assignment / state / sensitivity for every protected operation")
edge([m for m in ALL if m not in ("MasterDataConfig", "IdentityAccess")], "MasterDataConfig", "S", "INT-022; ICD-13; BE-004; CSB-14A §9",
     "ResolveConfiguration(configType, businessContext, effectiveDate); pin applied version")
edge(others("AuditActivity"), "AuditActivity", "E", "INT-026; ICD-15; BE-007",
     "Publish durable typed AuditEvent for material business / admin / security actions")
edge([m for m in ALL if m not in ("Notifications", "Dashboards", "MasterDataConfig")], "Notifications", "E", "INT-018; ICD-09; BE-021; CSB-14A §11",
     "Emit typed NotificationIntent after durable commit (FG-03 per CSB-FG-03 US-IAM-PFM-010/DM-011/LIA-006/007/EXT-007; FG-05 INT-025; FG-06 EVT-024; FG-02 EVT-019; WF-11/WF-12 per CSB-BP2 §11/§13)")
edge(["IdentityAccess", "Notifications", "DocumentManagement", "FinancialKpi", "ExternalParticipation", "Reports", "Dashboards", "AuditActivity"],
     "IntegrationMonitoring", "E", "INT-024; INT-029; CSB-14A §13",
     "Adapter / runtime telemetry: invocation, sync run, queue, dead letter, reconciliation, audit-infrastructure signals")
edge("MasterDataConfig", "IntegrationMonitoring", "E", "EVT-021", "ConfigurationPublished / Activated (operational thresholds and health policy)")

# ---- Project master: identity and lifecycle consumed by every business-facing module -----------
edge([m for m in ALL if LAYER[m] >= 2 and m != "Project"], "Project", "P", "CSB-BP2 App D row 1; CSB-BP2 §9",
     "Read Project identity and lifecycle state; consumers reference, never clone")

# ---- Shared runtimes ---------------------------------------------------------------------------
edge(["Project", "Schedule", "ChangeRequest", "Suspension", "Closure"], "Approval", "S", "INT-013; INT-007; CSB-14A §8; BE-003",
     "Create approval instance for a frozen source revision (registration, baseline, change, suspension, completion / closure)")
edge(["Progress", "Milestone"], "Approval", "S", "INT-013; CSB-14A §8 (CONDITIONAL / DOMAIN REVIEW by default)",
     "Invoke WF-11 only where governance configuration requires formal approval", conditional=True)
edge("Approval", ["Project", "Schedule", "ChangeRequest", "Suspension", "Closure"], "C", "INT-014; INT-008; EVT-012; BE-003; BE-006",
     "Durable idempotent approve / reject / return callback; source performs its own transition")
edge("Approval", ["Progress", "Milestone"], "C", "INT-014 (only where the conditional WF-02 / WF-05 → WF-11 edge is enabled)",
     "Approval outcome callback for conditionally approved progress publication / milestone acceptance", conditional=True)
edge([m for m in L2] + ["ExternalParticipation", "Reports"], "DocumentManagement", "S", "INT-015; INT-030; ICD-08; BE-018; CSB-14A §10",
     "Create / link / pin exact CLEAN DocumentVersion as evidence; FG-02 promotes retained Report Snapshot")
edge("DocumentManagement", [m for m in L2] + ["ExternalParticipation", "Reports"], "E", "EVT-013",
     "DocumentVersionClean / Quarantined; source decides evidence sufficiency")
edge("Approval", "Notifications", "E", "CSB-BP2 §11 (WF-15 supplies assignment / reminder / escalation / outcome delivery)",
     "Assignment, reminder, escalation and outcome intents")

# ---- L2 lateral contracts (CSB-14A §15 / §16, rank-1 spec dependency tables) --------------------
edge("Project", "Schedule", "P", "INT-001; ICD-02; BE-011", "Activation readiness (baseline / schedule) read at Planned→Active command")
edge("Project", [m for m in L2 if m != "Project"] + ["Dashboards", "Reports"], "E", "EVT-001; EVT-002",
     "ProjectRegistered / ProjectApproved / ProjectActivated")
edge("Progress", "FinancialKpi", "P", "INT-017; EVT-016; BE-014",
     "Current / published financial and KPI projections pinned by source version and as-of at reporting cut-off")
edge("Progress", ["Schedule", "Task", "Milestone", "Risk", "ManagementConcern"], "P", "CSB-WF-02 §9.23 / §9.24 dependency tables (read via ICD-01 renumbering); BE-014",
     "Planned progress, physical-progress weighting, schedule health, task / milestone statistics, risk and concern summaries at reporting cut-off")
edge("Progress", ["Dashboards", "Reports", "Closure"], "E", "EVT-003", "ProgressPublished (official snapshot, period / version / as-of)")
edge("Schedule", "Task", "P", "INT-003", "Activity Execution Progress from linked Tasks; WF-03 never recalculates Tasks")
edge(["Schedule", "Risk", "ManagementConcern", "Milestone"], "Task", "S", "CSB-BP2 App D (Task / Subtask row)",
     "Link / create Tasks through the WF-04 typed contract")
edge("Schedule", ["Progress", "Dashboards", "Reports"], "E", "EVT-004", "BaselineActivated / RebaselineActivated")
edge("Task", "Schedule", "P", "CSB-BP2 App D (ProjectSchedule row: WF-04 links execution Tasks)", "Read Schedule Activity identity for Task linkage")
edge("Task", "Schedule", "E", "EVT-005", "TaskStatusChanged / TaskCompleted → WF-03 projection refresh")
edge("Milestone", "Schedule", "P", "ICD-04; BE-013", "Read stable ProjectMilestone identity and planned dates (split authority)")
edge("Milestone", ["Schedule", "Progress", "Dashboards", "Reports"], "E", "INT-004; EVT-006", "MilestoneAchievementAccepted (accepted Actual Achievement Date)")
edge("Risk", "ManagementConcern", "S", "INT-005; EVT-007; BE-015", "Materialize realized Risk into linked Issue (idempotent; pending-link state on partial failure)")
edge(["Risk", "ManagementConcern"], "ChangeRequest", "S", "INT-006; EVT-008", "Create / link Change Request where a controlled commitment change is required")
edge("ChangeRequest", "Schedule", "S", "INT-009; BE-012; BE-016", "Apply scoped, version-pinned ChangeAuthorization to rebaseline candidate")
edge("ChangeRequest", "FinancialKpi", "S", "INT-010; BE-016; BE-020", "Apply authorized budget / KPI target change")
edge("ChangeRequest", ["Dashboards", "Reports"], "E", "EVT-009", "ChangeApproved / ChangeAuthorizationCreated")
edge("Suspension", "Project", "S", "INT-011; BE-017", "Activate Suspension / Resumption on the Project master lifecycle (max one ActiveSuspension)")
edge("Suspension", ["Progress", "Schedule", "Task", "Milestone", "ChangeRequest", "FinancialKpi"], "P", "CSB-WF-09 §2 domain table",
     "Capability signals and readiness references for the Resumption readiness snapshot")
edge("Suspension", "Closure", "S", "CSB-WF-09 §2 (Closure row); CSB-WF-10 §2.1 (WF-09 row)", "Refer a non-resuming Project for terminal disposition")
edge("Project", [m for m in L2 if m != "Project"] + ["Dashboards", "Reports"], "E", "EVT-010; EVT-011",
     "ProjectSuspended / ProjectResumed / ProjectCompleted / ProjectClosed — emitted by the Project master after the WF-09 / WF-10 command succeeds; each domain applies its own suspended / terminal behaviour")
edge("Closure", "Project", "S", "INT-012; BE-017", "Activate Completed / Closed; enforce terminal read-only behaviour")
edge("Closure", ["Progress", "Schedule", "Task", "Milestone", "Risk", "ManagementConcern", "ChangeRequest", "Suspension", "FinancialKpi", "DocumentManagement"], "P",
     "CSB-WF-10 §2.1 ownership matrix; CSB-BP2 App D (Completion / Closure case row)",
     "Readiness / disposition gate projections (final report, reconciliation, dispositions, residuals, obligations, closeout completeness)")
edge("FinancialKpi", ["Progress", "Dashboards", "Reports"], "E", "EVT-016", "FinancialSnapshotPublished / KPIMeasurementPublished")

# ---- External intake ----------------------------------------------------------------------------
edge("ExternalParticipation", L2, "S", "INT-016; ICD-07; EVT-014; EVT-015; BE-019",
     "Apply accepted External Contribution through the target domain's allowlisted typed adapter; acknowledgment required before Applied")
edge("ExternalParticipation", ["Dashboards", "Reports"], "E", "EVT-015", "ExternalContributionApplied lineage")

# ---- Management intelligence ---------------------------------------------------------------------
edge(["Dashboards", "Reports"], L2 + ["ExternalParticipation", "Approval", "IntegrationMonitoring"], "P", "INT-019; INT-020; ICD-10; ICD-11; BE-010; BE-022; BPK-013",
     "Governed projections with semantic state, as-of, freshness, coverage and sensitivity; no raw table querying")
edge("Reports", "AuditActivity", "P", "INT-027; BE-024", "Authorized formal Audit export dataset (same or stricter redaction)")
edge(["Dashboards", "Reports"], "AuditActivity", "E", "EVT-018; EVT-019", "DashboardDefinitionPublished / ReportDefinitionPublished / ExportCompleted")

# ---- L0 lateral and upward events -----------------------------------------------------------------
edge("IdentityAccess", others("IdentityAccess"), "E", "EVT-020", "AccessGranted / AccessRevoked → authorization-cache invalidation; WF-11 inactive-assignee handling (CSB-FG-03 US-IAM-SYS-040)")
edge("MasterDataConfig", [m for m in ALL if m not in ("MasterDataConfig", "IdentityAccess", "IntegrationMonitoring")], "E", "EVT-021",
     "ConfigurationPublished / Activated → consumers refresh resolution cache; pinned versions unaffected")
edge("IntegrationMonitoring", "Notifications", "E", "INT-025; EVT-022; EVT-023", "Operational alert / recovery / dead-letter intents")
edge("IntegrationMonitoring", "Dashboards", "E", "EVT-022", "High-level integration health")
edge("AuditActivity", "IntegrationMonitoring", "E", "INT-029; EVT-024", "Audit infrastructure health / lag / integrity signals")
edge("AuditActivity", "Notifications", "E", "EVT-024", "AuditIntegrityFailure / AuditIndexRecovered")

# ---- Conditional (policy-gated) edges outside the baseline ---------------------------------------
edge("MasterDataConfig", "Approval", "S", "CSB-14A §8 (FG-04 row: OPTIONAL / policy-driven; exact families TBC)",
     "Sensitive configuration publication routed through WF-11 — the only upward synchronous call; excluded from the baseline until AHDA names the families", conditional=True)
edge("Approval", "MasterDataConfig", "C", "INT-014 (only if the FG-04 → WF-11 edge is enabled)",
     "Approval outcome callback for configuration publication", conditional=True)

# de-duplicate (same caller, callee, type) keeping first contract; merge purposes if repeated
seen = {}
for a, b, t, c, p, cnd in EDGES:
    k = (a, b, t)
    if k in seen:
        a0, b0, t0, c0, p0, cnd0 = seen[k]
        items = [x.strip() for x in c0.split(";")]
        c = "; ".join(items + [x.strip() for x in c.split(";") if x.strip() not in items])
        p = p0 if p in p0 else f"{p0} · {p}"
        seen[k] = (a0, b0, t0, c, p, cnd0 and cnd)
    else:
        seen[k] = (a, b, t, c, p, cnd)
EDGES = list(seen.values())


def check():
    errors = []
    ids = [m[0] for m in MODULES]
    assert len(ids) == 21, len(ids)
    assert len(set(ids)) == 21
    wfs = [m[1] for m in MODULES]
    assert len(set(wfs)) == 21 and all(w.startswith(("WF-", "FG-")) for w in wfs)
    for a, b, t, c, p, cond in EDGES:
        if a not in M or b not in M:
            errors.append(f"unknown module in edge {a}->{b}")
        if t == "R":
            errors.append(f"REPOSITORY EDGE {a}->{b}")
        if t in ("S", "P") and LAYER[b] > LAYER[a] and not cond:
            errors.append(f"upward {t} edge {a}({LAYER[a]})->{b}({LAYER[b]})")
    return errors


def counts():
    base = [e for e in EDGES if not e[5]]
    cond = [e for e in EDGES if e[5]]
    by = defaultdict(int)
    for e in base:
        by[e[2]] += 1
    touched = {e[0] for e in base} | {e[1] for e in base}
    return base, cond, by, touched


if __name__ == "__main__":
    errs = check()
    base, cond, by, touched = counts()
    print("modules:", len(MODULES), "modules on baseline graph:", len(touched))
    print("baseline edges:", len(base), dict(by), "conditional:", len(cond))
    print("errors:", errs or "none")
