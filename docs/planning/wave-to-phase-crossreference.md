# Wave-to-Phase Cross-Reference (W0–W6 ↔ P0–P18)

| Control | Value |
|---|---|
| Task | TASK-003 — Ratify Delivery Wave Plan (W0–W6) (Phase P0 — Discovery & Governance); depends on TASK-002 |
| Programme | AHDA Regional Project Management Platform (RPMO) |
| Issue date | 2026-09-18 |
| Document status | **ISSUED FOR PMO ACCEPTANCE — NOT YET ACCEPTED (0 of 1 signature, §10).** Becomes RATIFIED when §10 is signed. |
| Wave source | CSB-15 Step 15 Build Prioritization v1.0 (DOCX digest `3f148a2d86b6b9f9`, XLSX digest `aebc88944ca41a14`, both re-verified 2026-09-18), sheets `02_Build_Packages`, `03_Dependencies`, `04_Build_Waves` |
| Phase source | `AHDA_RPMO_Platform_Implementation_Plan.xlsx`, sheet *Implementation Plan*, column B (Phase), 102 tasks; SHA-256 `0c0ff4b0b495ae25` at issue date |
| Owner | PMO Engagement Lead (acceptance); Engagement Architect (maintenance) |

Sources and precedence per TASK-001 (`docs/baseline/controlled-source-baseline.md`). Documents are cited by their `CSB-*` register ID. This document adds no dates, sprint counts, effort or staffing: Step 15 states none and 15-D-004 reserves them for execution planning.

## 1. Purpose

Two plans describe the same delivery. CSB-15 sequences 31 build packages (BPK-001–031) into seven logical waves W0–W6 by dependency. The implementation-plan workbook groups 102 tasks into 19 phases P0–P18 by discipline. Neither replaces the other: the wave is the *dependency* view (what must exist before what), the phase is the *ownership* view (which team and directory). This document is the fixed join between them so that a change in either can be traced to the other.

It delivers the TASK-003 acceptance criterion — every phase mapped to exactly one wave in a cross-reference table (§4) — and the workbook validation check — no phase references a wave-owned deliverable before that wave's prerequisite waves are complete (§7). It also closes RTM-19532 (CSB-14B v1.1 §5.2.2): the Scope's 3-week/3-week phasing is normalised here rather than copied literally.

Two corrections to the task text as written in the workbook:

1. The acceptance criterion says "P1–P18". The workbook has **19 phases, P0–P18**; P0 (Discovery & Governance) is the phase TASK-003 itself belongs to. All 19 are mapped.
2. "1:1" is read as *each phase maps to exactly one wave*. Nineteen phases cannot map onto seven waves bijectively; the reverse index in §5 shows which phases share a wave.

## 2. Standing of the wave plan

| Fact | Position at 2026-09-18 | Consequence for this document |
|---|---|---|
| CSB-15 status | SUBSTANTIVELY COMPLETE — PENDING QA CLOSURE (TASK-001 §3.4: downstream baseline, `PENDING`) | The waves are a *proposed* planning baseline. Ratifying the mapping does not QA-close Step 15. |
| 15-D-001 "Approve package boundaries and waves as planning baseline" | OPEN; accountable AHDA sponsor / PMO; gate "before execution-plan baseline" | Acceptance of this document by the PMO engagement lead (§10) is the workbook-side half of 15-D-001. AHDA sponsor approval is recorded separately in CSB-15 `12_Decisions_Findings`. |
| CSB-14B v1.1 §9 signatures | 0 of 8 | F-002(b) "sequencing is normalised by TASK-003" is signed by the same PMO engagement lead and can be signed together with §10. |
| Authority | Step 15 is not a rank-1–4 source (TASK-001 §2). Where a wave sequence and a rank-1 WF/FG spec disagree, the spec wins. | §8 F-01 is decided on the WF-02 spec, not on Step 15 alone. |
| Wave ≠ date | CSB-15: "No dates, sprint counts, staffing … are inferred"; 04_Build_Waves col I: "Proposed logical wave; no dates, sprint count or resource promise." | RTM-19527 ("wave plan footprint ≤ 24 months") cannot be evidenced by this document — §11 item 3. |

## 3. The seven waves (as defined by CSB-15)

Copied from `04_Build_Waves` and the DOCX "Recommended logical build waves" table. Increment suffixes: I1 = minimum first-use capability, I2 = later extension, I3 = final operating evidence. BPK-031 (10 source-approved deferred RTM rows, P3) sits outside the MVP waves and is not mapped to any phase.

| Wave | Objective | Initial packages | Extensions scheduled in this wave | Exit evidence (abridged) |
|---|---|---|---|---|
| W0 | Resolve decisions and establish contracts | BPK-001, BPK-002, BPK-003, BPK-004 | — | Signed source reconciliation and disposition of 14B-F-001/002; exact source-to-control-to-UI/data/API links; decision records and approved values; approved delivery work-package acceptance |
| W1 | Establish secure foundation mechanisms | BPK-005, BPK-006, BPK-007, BPK-008, BPK-009 | — | Reproducible deployment and environment separation; denied cross-scope actions fail server-side; configuration fails closed and published versions are immutable; durable idempotent audit capture; typed replay-safe integration |
| W2 | Prove shared services and first registration | BPK-010, BPK-011, BPK-012, BPK-013, BPK-014 | — | Immutable CLEAN document versions; durable idempotent approval callbacks; notification retry never duplicates business action; projection contracts carry semantic state; first Project registered |
| W3 | Build operational domain records | BPK-015, BPK-016, BPK-018, BPK-019, BPK-021 | BPK-006-I2, BPK-007-I2 | Baseline activation distinct from approval; task permissions hold; versioned risk assessments; issue resolution evidence; financial/KPI records with pinned target versions |
| W4 | Integrate change, milestones and official progress | BPK-017, BPK-020, BPK-022 | BPK-011-I2, BPK-014-I2, BPK-015-I2, BPK-018-I2, BPK-019-I2 | Accepted milestone dates propagate via INT-004; replay-safe change application; published health snapshot pins its inputs and is owned solely by WF-02 |
| W5 | Enable external/governance and management views | BPK-023, BPK-024, BPK-026, BPK-027, BPK-028 | BPK-008-I2, BPK-009-I2, BPK-010-I2, BPK-012-I2, BPK-013-I2 | ENTITY isolation for external contributions; suspension restrictions observed by every consuming domain; R07 audience scope on dashboards; re-authorisation at export; audit review over durable capture |
| W6 | Prove closeout, handover and production readiness | BPK-025, BPK-029, BPK-030 | — | Completed and Closed distinct; migration reconciliation, training evidence, runbooks and handover acceptance; restore evidence, security testing and release authorisation recorded |

Package → domain, for reading the tables below: BPK-005 environments · 006 FG-03 identity · 007 FG-04 configuration · 008 FG-06 audit capture · 009 FG-05 integration runtime · 010 WF-12 documents · 011 WF-11 approvals · 012 WF-15 notifications · 013 FG-01/02 projection contracts · 014 WF-01 · 015 WF-03 · 016 WF-04 · 017 WF-05 · 018 WF-06 · 019 WF-07 · 020 WF-08 · 021 WF-14 · 022 WF-02 · 023 WF-13 · 024 WF-09 · 025 WF-10 · 026 FG-01 dashboards · 027 FG-02 reports · 028 FG-06 audit review · 029 migration/training/handover · 030 production readiness.

## 4. Phase → wave cross-reference

**Mapping rule.** A phase is mapped to the wave whose objective and *initial packages* (`04_Build_Waves` columns B–C) own the phase's defining scope. Where a phase's tasks belong to packages in more than one wave, the phase takes the wave that owns the majority of those packages; a tie goes to the earlier wave (the phase's entry wave). Extensions (I2/I3) do not count towards the phase wave. Every task whose own wave differs from its phase wave is listed individually in §6 — the phase wave is a label, the task wave is the constraint.

| Phase | Name | Tasks | Wave | Owning Step 15 packages / decisions | Basis | Deviating tasks (§6) |
|---|---|---|---|---|---|---|
| P0 | Discovery & Governance | TASK-001–004 (4) | **W0** | 15-D-001, BPK-001, BPK-002, BPK-003, BPK-004 | All four W0 governance packages are owned here: scope/precedence (BPK-001 → TASK-001/002), acceptance and allocation gaps (BPK-002 → TASK-002), delivery and service acceptance (BPK-004 → TASK-002 via the 14B-F-006 disposition, CSB-14B v1.1 §5.6), policy values and impact crosswalk (BPK-003 → TASK-004), plus the wave approval decision itself (15-D-001 → TASK-003). | none |
| P1 | Architecture Decisions | TASK-005–010 (6) | **W0** | 15-D-002, 15-D-005, BPK-003, BPK-005, BPK-007, BPK-009, BPK-014 | W0 objective is "resolve decisions and establish contracts". 15-D-005 requires irreversible hosting/topology/identity/provider decisions before any design commitment (ADR-001/002 → TASK-005/006); 15-D-002 requires the secure bootstrap and minimum shared contracts before initial foundation implementation (TASK-007/009). ADR-001 blocks every W1 environment task (OQ-001). | none |
| P2 | Project Setup & Foundation | TASK-011–015 (5) | **W1** | BPK-005 | BPK-005 Secure engineering and test environments, initial increment: secure build/release controls and test harness. | none |
| P3 | Infrastructure & DevOps | TASK-016–023 (8) | **W1** | BPK-005, BPK-030 | BPK-005 initial increment: separate environments, secrets exclusion, three-tier service boundary. Backup/DR drill evidence (TASK-023) is consolidated in BPK-030 at W6 (BPK-005 boundary column). | none |
| P4 | Database Foundation | TASK-024–027 (4) | **W1** | BPK-005, BPK-006, BPK-007, BPK-014 | Schema, migrations and seed data are the persistence part of BPK-005/BPK-006/BPK-007 initial increments; every W2 package has BPK-006-I1 and BPK-007-I1 as HARD prerequisites (03_Dependencies). | none |
| P5 | Identity & Access Management (FG-03) | TASK-028–033 (6) | **W1** | BPK-006, BPK-008 | BPK-006 Identity and contextual authorization (FG-03). Administration screens are BPK-006-I2, an extension scheduled in W3 (04_Build_Waves, W3 Extensions). | TASK-031, TASK-032 |
| P6 | Shared Platform Services | TASK-034–040 (7) | **W2** | BPK-007, BPK-010, BPK-011, BPK-012 | W2 objective is "prove shared services and first registration"; BPK-010 (WF-12), BPK-011 (WF-11) and BPK-012 (WF-15) are W2 initial packages. BPK-007 (FG-04, TASK-034) is a W1 foundation and is listed as a deviation. | TASK-034 |
| P7 | Project Establishment (WF-01) | TASK-041–043 (3) | **W2** | BPK-014 | BPK-014 Register projects and govern early lifecycle (WF-01), the W2 business slice. | none |
| P8 | Execution & Performance (WF-02/03/04/05/14) | TASK-044–054 (11) | **W3** | BPK-015, BPK-016, BPK-017, BPK-021, BPK-022 | Three of the five packages are W3 initial packages (BPK-015 WF-03, BPK-016 WF-04, BPK-021 WF-14); BPK-017 (WF-05) and BPK-022 (WF-02 official progress/health) are W4 and are listed as deviations. | TASK-044, TASK-045, TASK-050, TASK-051, TASK-054 |
| P9 | Risk & Issue Management (WF-06/07) | TASK-055–059 (5) | **W3** | BPK-018, BPK-019 | BPK-018 (WF-06) and BPK-019 (WF-07), both W3 initial packages. | none |
| P10 | Governance & Change Control (WF-08/09/10) | TASK-060–065 (6) | **W4** | BPK-020, BPK-024, BPK-025 | One package per wave — BPK-020 WF-08 (W4), BPK-024 WF-09 (W5), BPK-025 WF-10 (W6); the tie resolves to the entry wave W4, whose objective is "integrate change". WF-09/WF-10 tasks are listed as deviations. | TASK-062, TASK-063, TASK-064, TASK-065 |
| P11 | Collaboration & External Participation (WF-13) | TASK-066–068 (3) | **W5** | BPK-023 | BPK-023 Enable controlled external participation (WF-13), W5. Nafath (TASK-068) is the "real-provider integration" W5 extension, gated by PTBC-031. | none |
| P12 | Management Intelligence (FG-01/02) | TASK-069–072 (4) | **W5** | BPK-013, BPK-026, BPK-027 | BPK-026 (FG-01) and BPK-027 (FG-02), both W5. Their HARD prerequisite BPK-013 (governed projection contracts, W2) has no workbook task — see §8 finding F-03. | none |
| P13 | Technical Operations (FG-05/06) | TASK-073–076 (4) | **W1** | BPK-008, BPK-009, BPK-028 | BPK-008 Durable formal audit capture (FG-06) and BPK-009 Typed integration runtime (FG-05) are W1 foundations. The review/search UI (BPK-028) and provider monitoring (BPK-009-I2) are W5 and listed as deviations. | TASK-074, TASK-076 |
| P14 | Security Hardening & Compliance | TASK-077–083 (7) | **W1** | BPK-005, BPK-006, BPK-008, BPK-023, BPK-030 | BPK-005 "secure interfaces" and the BPK-006/BPK-008 control mechanisms are W1 (Step 15: production readiness "is not permission to postpone basic controls"). Threat-model and penetration-test evidence is consolidated in BPK-030 (W5/W6 deviations). | TASK-081, TASK-082 |
| P15 | Testing & QA | TASK-084–089 (6) | **W6** | BPK-005, BPK-029, BPK-030 | BPK-030 Prove production readiness and BPK-029 migration validation are W6. The test strategy (TASK-084) is part of the BPK-005 test harness and is a W1 deviation. | TASK-084 |
| P16 | Observability | TASK-090–093 (4) | **W1** | BPK-005, BPK-009, BPK-029, BPK-030 | Health checks and APM are BPK-005-I1 diagnostic logging (W1). Operational dashboards/alerting are BPK-009-I2 (W5) and the SLA/on-call runbook is BPK-029/030 evidence (W6); both listed as deviations. | TASK-092, TASK-093 |
| P17 | Documentation | TASK-094–097 (4) | **W6** | BPK-029 | BPK-029 Deliver migration, training and handover (W6) owns the handover package; API and onboarding documentation are produced from W1 but accepted with the handover package. | none |
| P18 | Release & Go-Live | TASK-098–102 (5) | **W6** | BPK-029, BPK-030 | BPK-030 Prove production readiness (W6): release authorisation, soak, go-live, hypercare. The ~22-month operate period that follows is outside the Step 15 waves (BPK-004/BPK-029 define its acceptance). | none |

Coverage: 19 of 19 phases mapped; 102 of 102 tasks carry a package and a wave (Appendix A).

## 5. Wave → phase index

| Wave | Phases (by phase wave) | Tasks by phase wave | Tasks by task wave (after §6 deviations) |
|---|---|---|---|
| W0 | P0, P1 | 10 | 10 |
| W1 | P2, P3, P4, P5, P13, P14, P16 | 38 | 32 |
| W2 | P6, P7 | 10 | 9 |
| W3 | P8, P9 | 16 | 13 |
| W4 | P10 | 6 | 7 |
| W5 | P11, P12 | 7 | 12 |
| W6 | P15, P17, P18 | 15 | 19 |
| **Total** | 19 | 102 | 102 |

W1 carries 32 tasks because the workbook splits Step 15's five W1 foundations across seven phases (P2, P3, P4, P5, P13, P14, P16) plus TASK-034. That is a true reflection of the plan, not an artefact of the mapping: Step 15 front-loads the secure foundation deliberately ("The build order begins with secure environments, contextual authorization, configuration, durable audit and typed integration mechanisms").

## 6. Task-level deviations from the phase wave

These 19 tasks are scheduled by their Step 15 package, not by their phase. A deviation to a *later* wave means the task must not start integrated acceptance before that wave's prerequisites exist; a deviation to an *earlier* wave means the task is a prerequisite of other phases and must not wait for its own phase.

| Task | Name | Phase (wave) | Package | Task wave | Reason |
|---|---|---|---|---|---|
| TASK-031 | Build Users, Roles & Permissions Administration (FG-03 Backend) | P5 (W1) | BPK-006-I2 | **W3** | BPK-006-I2 access administration is a W3 extension (04_Build_Waves). W1 delivers the backend evaluator only (TASK-030). |
| TASK-032 | Build Users, Roles & Permissions Administration (FG-03 Frontend) | P5 (W1) | BPK-006-I2 | **W3** | As TASK-031; the FG-03 administration UI is not required for first-use enforcement. |
| TASK-034 | Build Master Data & Configuration Service (FG-04 Backend) | P6 (W2) | BPK-007-I1 | **W1** | BPK-007-I1 is a W1 foundation and a HARD prerequisite of every W2 package (BPK-010/011/012/013/014). It must complete in W1 even though the workbook files it under P6. |
| TASK-044 | Build Progress Update & Overall Health (WF-02 Backend) | P8 (W3) | BPK-022 | **W4** | BPK-022 official progress/health is W4: its HARD prerequisites are the W3 projections from BPK-015/017/018/019/021 and the BPK-013 contract. The workbook lets it start after TASK-041 only (see §8 F-01). |
| TASK-045 | Build Progress & Schedule UI (WF-02/WF-03 Frontend) | P8 (W3) | BPK-022 | **W4** | WF-02 progress UI follows BPK-022 (W4). |
| TASK-050 | Build Milestone Management (WF-05 Backend) | P8 (W3) | BPK-017 | **W4** | BPK-017 milestone achievement is W4 (needs BPK-015-I1 baseline first). |
| TASK-051 | Build Milestone Register & Achievement UI (WF-05 Frontend) | P8 (W3) | BPK-017 | **W4** | Follows TASK-050 (BPK-017, W4). |
| TASK-054 | Contract & Integration Tests for Execution Domain (WF-02/03/04/05/14) | P8 (W3) | BPK-015/016/017/021/022 | **W4** | Covers all five P8 domains; cannot close before BPK-017/022 (W4). |
| TASK-062 | Build Suspension & Resumption (WF-09 Backend) | P10 (W4) | BPK-024 | **W5** | BPK-024 suspend/resume is W5 (needs every consuming domain at I2). |
| TASK-063 | Build Completion & Closure (WF-10 Backend) | P10 (W4) | BPK-025 | **W6** | BPK-025 completion/closure is W6 (needs BPK-020/022/023/024 at I2). |
| TASK-064 | Build Suspension & Closure UI (WF-09/WF-10 Frontend) | P10 (W4) | BPK-024; BPK-025 | **W6** | Covers WF-09 (W5) and WF-10 (W6); closes in W6. |
| TASK-065 | Contract & Regression Tests for Governance Domain (WF-08/09/10) | P10 (W4) | BPK-020/024/025 | **W6** | Covers WF-08/09/10; cannot close before BPK-025 (W6). |
| TASK-074 | Build Audit & Activity UI (FG-06 Frontend) | P13 (W1) | BPK-028 | **W5** | BPK-028 activity and audit review (FG-06 UI) is W5; W1 delivers capture only (TASK-073). |
| TASK-076 | Build Integration Administration UI (FG-05 Frontend) | P13 (W1) | BPK-009-I2 | **W5** | BPK-009-I2 provider monitoring, dead letters and reconciliation UI is a W5 extension. |
| TASK-081 | Conduct Threat Modeling & Security Review for Sensitive Features | P14 (W1) | BPK-023 inputs; evidence BPK-030 | **W5** | Workbook inputs (WF-12 W2, WF-13 W5 backends) are complete only in W5; evidence is consolidated in BPK-030. Per-package threat modelling should nevertheless start in W1 (§8 F-05). |
| TASK-082 | Commission External Penetration Test Before Production | P14 (W1) | BPK-030 | **W6** | BPK-030 security testing before production (W6); Release Checklist gate "External Penetration Test Passed". |
| TASK-084 | Author Platform Test Strategy & Coverage Policy | P15 (W6) | BPK-005-I1 (test harness) | **W1** | BPK-005-I1 test harness; the strategy must exist before the first W2 contract tests. |
| TASK-092 | Build Operational Dashboards & Alerting Thresholds (FG-05 Alerts) | P16 (W1) | BPK-009-I2 | **W5** | BPK-009-I2 operational alerting is a W5 extension and depends on TASK-075 I2. |
| TASK-093 | Document Operational SLAs & On-Call Runbook | P16 (W1) | BPK-029; BPK-030 | **W6** | Support/runbook evidence belongs to BPK-029/030 (W6); SLA values remain OQ-009. |

## 7. Validation check — no deliverable ahead of its prerequisite wave

Method: for each of the 102 tasks, every entry in the workbook *Depends On Task Name* column was resolved to a task and its task wave (Appendix A). A violation is a task whose wave is **earlier** than the wave of something it depends on — i.e. the workbook would let it complete before its own prerequisite exists. Result: **3 violations, all caused by workbook dependency rows, none by the mapping**; each is dispositioned in §8.

| # | Task (wave) | Depends on (wave) | Finding |
|---|---|---|---|
| V-1 | TASK-052 WF-14 Financial/KPI backend (W3) | TASK-044 WF-02 Progress backend (W4) | Dependency is inverted — §8 F-01 |
| V-2 | TASK-075 FG-05 Integration Monitoring runtime (W1) | TASK-039 WF-15 Notification runtime (W2) | Increment split — §8 F-02 |
| V-3 | TASK-077 Platform input validation (W1) | TASK-041 WF-01 backend (W2) | Dependency is unnecessary — §8 F-04 |

Wave-entry check (each wave's initial packages have all HARD prerequisites in earlier waves, per `03_Dependencies`): PASS for W0–W6 as published by CSB-15 (15-DOD-07 "acyclic initial graph"). The one prerequisite that has **no workbook task at all** is BPK-013 (§8 F-03); with the mapping above, W2 would exit without it and W4/W5 would start without their projection contract.

## 8. Findings for the workbook owner

None of these changes the phase→wave table. All are corrections to the workbook that the cross-reference exposed; they go into the next workbook revision alongside the TASK-001 §4 and TASK-002 §10.2 changes.

| # | Finding | Evidence | Required workbook change | Owner |
|---|---|---|---|---|
| F-01 | **TASK-052 (WF-14) depends on TASK-044 (WF-02); the real dependency runs the other way.** CSB-WF-02 §Functional boundary: WF-02 "does not duplicate maintenance of … financial actuals, KPI actuals … it consumes authoritative values from those modules"; US-PRG-SYS-011 "Retrieve latest financial-performance snapshot from its authoritative source". CSB-15 `03_Dependencies`: BPK-021-I1 → BPK-022, HARD, INT-017. | Rank-1 spec + Step 15 agree | TASK-052 *Depends On* → "Build Project Creation & Registration (WF-01 Backend)" only. TASK-044 *Depends On* → add TASK-046 (WF-03), TASK-050 (WF-05), TASK-052 (WF-14), TASK-055 (WF-06), TASK-057 (WF-07) and the BPK-013 task from F-03. | Workbook owner |
| F-02 | **TASK-075 (FG-05 runtime) depends on TASK-039 (WF-15), but BPK-009-I1 is a HARD prerequisite of BPK-012 (ICD-06).** Both directions are real at different increments: the typed integration runtime (Integration Definition/Instance/Invocation model, idempotent retry, dead-letter) precedes WF-15; the monitoring UX that consumes WF-15 telemetry (CSB-WF-15 §23.2, XFA-NTF-03) is BPK-009-I2 in W5. | CSB-15 `03_Dependencies` row BPK-009→BPK-012; CSB-WF-15 §23.2 | Split TASK-075 into I1 (W1: object model, retry, dead-letter, correlation; depends on TASK-028, TASK-073) and I2 (W5: provider monitoring, reconciliation, Operational Alert; depends on TASK-039), or move the TASK-039 dependency to TASK-076 and TASK-092. | Workbook owner / Engagement Architect |
| F-03 | **BPK-013 Governed projection contracts (W2, P0, foundation) has no workbook task.** It is a HARD prerequisite of BPK-022 (ICD-10/11), BPK-026 (INT-019) and BPK-027 (INT-020). TASK-009 covers the typed-event *format*; the semantic-state / freshness / coverage projection contract appears only inside TASK-069 (W5). | CSB-15 `02_Build_Packages` BPK-013; `03_Dependencies` | Add a P6 task "Define Governed Projection Contract (FG-01/FG-02 read model: source identity, version, semantic state CURRENT/PUBLISHED/HISTORICAL, freshness, coverage)" in W2, depending on TASK-009 and TASK-034; make it a dependency of TASK-044, TASK-069 and TASK-071. | Workbook owner |
| F-04 | TASK-077 platform-wide input validation/output encoding depends on TASK-041 (WF-01 backend). A cross-cutting middleware control must be in place *before* the first business API, not after it (BPK-005 "secure interfaces", W1). | CSB-15 BPK-005 scope | Remove the TASK-041 dependency; keep TASK-009. | Workbook owner |
| F-05 | TASK-081 threat modelling is gated on finished WF-12/WF-13 backends, which places it in W5. Threat modelling is design-time work; leaving it to W5 contradicts CSB-15 ("not permission to postpone basic controls") and 15-D-002 (bootstrap contracts reviewed before initial foundation implementation). | CSB-15 foundations table; 15-D-002 | Re-scope TASK-081 as a per-package activity started in W1 (identity, documents) with the WF-13/Nafath model added in W5; acceptance evidence still consolidated at BPK-030. | Security Lead |
| F-06 | Acceptance criterion text "P1–P18" omits P0. | Workbook column B | Replace with "P0–P18". | Workbook owner |
| F-07 | OQ-001 lists TASK-014 through TASK-020 as "all Phase P3"; TASK-014 and TASK-015 are P2. | Workbook *Open Questions* | Correct to TASK-016 through TASK-023 (all Phase P3); TASK-005 stays. | Workbook owner |

## 9. TASK-003 acceptance-criteria check

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Every phase in the workbook is mapped 1:1 to a wave (W0–W6) in a cross-reference table | **MET** — 19 of 19 phases (P0–P18), one wave each; 102 of 102 tasks carry a package and wave | §4, Appendix A |
| 2 | The mapping is reviewed and accepted by the PMO engagement lead | **PENDING** — 0 of 1 signature; no acceptance is claimed | §10 |
| V1 | No phase references a wave-owned deliverable before that wave's prerequisite waves are complete | **PASS for the mapping; 3 workbook dependency rows fail** and are dispositioned | §7, §8 F-01/F-02/F-04 |

## 10. Acceptance

The PMO engagement lead signs the statement below. On signature: this document's status becomes RATIFIED; RTM-19532 moves to TRACED (CSB-14B v1.1 §5.2.2); the CSB-14B §9 row "14B-F-002 (b) sequencing" may be signed by the same person; the workbook-side half of 15-D-001 is recorded in CSB-15 `12_Decisions_Findings`.

| Signatory | Signs that | Name / role | Date |
|---|---|---|---|
| PMO Engagement Lead | "The phase→wave table in §4 and the task-level deviations in §6 are the accepted cross-reference between the implementation-plan workbook (digest `0c0ff4b0b495ae25`) and the Step 15 wave plan (digests `3f148a2d86b6b9f9` / `aebc88944ca41a14`). The workbook changes in §8 are accepted for the next workbook revision." | | |

Change control: this file is re-issued whenever either source digest changes, a task is added/re-phased, or CSB-15 re-sequences a package. Edits are made only on a branch named `chore/task-003-*`.

## 11. Open items

| # | Item | Owner | Gate |
|---|---|---|---|
| 1 | §10 signature | PMO Engagement Lead | Before execution-plan baseline (15-D-001) |
| 2 | AHDA sponsor approval of the Step 15 package/wave baseline (15-D-001) and QA closure of CSB-15 — outside this task | AHDA sponsor / PMO | Before execution-plan baseline |
| 3 | RTM-19527 "wave plan footprint ≤ 24 months" cannot be evidenced until waves carry dates; CSB-15 defers effort/capacity/sequencing to 15-D-004 | Delivery lead | 15-D-004, before schedule commitment |
| 4 | Workbook changes F-01–F-07 (§8) | Workbook owner | Next workbook revision, with TASK-001 §4 and TASK-002 §10.2 changes |
| 5 | TASK-002 §9 signatures (0 of 8) — this document does not depend on them, but the Release Checklist gate "Step 14B RTM QA Closed" does | Named functions | Before UAT |

## Appendix A — Task register with package and wave (102 tasks)

Phase wave is from §4; task wave is the Step 15 package's wave. Rows in bold deviate from their phase wave (§6).

| Task | Phase | Phase wave | Name | Priority | Step 15 package / increment | Task wave |
|---|---|---|---|---|---|---|
| TASK-001 | P0 | W0 | Establish Controlled Source Baseline | P0 | BPK-001 | W0 |
| TASK-002 | P0 | W0 | Close Step 14B RTM Findings | P0 | BPK-001; BPK-002; BPK-004 (F-006 disposition) | W0 |
| TASK-003 | P0 | W0 | Ratify Delivery Wave Plan (W0-W6) | P0 | 15-D-001 | W0 |
| TASK-004 | P0 | W0 | Stand Up PTBC / TBC Governance Tracker | P0 | BPK-003 | W0 |
| TASK-005 | P1 | W0 | Resolve Hosting & Data Localisation Architecture Decision Record | P0 | 15-D-005 / ADR-001 | W0 |
| TASK-006 | P1 | W0 | Ratify Application Technology Stack ADR | P0 | 15-D-005 / ADR-002 | W0 |
| TASK-007 | P1 | W0 | Define Three-Tier Solution Architecture & Module Boundaries | P0 | BPK-005 (design) / 15-D-002 | W0 |
| TASK-008 | P1 | W0 | Produce Canonical Entity-Relationship Diagram | P0 | BPK-007, BPK-014 (data model) | W0 |
| TASK-009 | P1 | W0 | Define Platform API & Event Contract Conventions | P0 | BPK-009 (ICD-06 contracts) / 15-D-002 | W0 |
| TASK-010 | P1 | W0 | Ratify Cybersecurity Control Overlay Mapping (CS-001-033) | P0 | BPK-003 | W0 |
| TASK-011 | P2 | W1 | Initialize Monorepo & Solution Structure | P0 | BPK-005-I1 | W1 |
| TASK-012 | P2 | W1 | Define Branching Strategy, PR Template & Code Owners | P0 | BPK-005-I1 | W1 |
| TASK-013 | P2 | W1 | Author Environment Variable Templates per Environment | P0 | BPK-005-I1 | W1 |
| TASK-014 | P2 | W1 | Build Local Development Environment (Docker Compose) | P1 | BPK-005-I1 | W1 |
| TASK-015 | P2 | W1 | Configure Quality Gates: Lint, Format, Type-Check, Test in CI | P0 | BPK-005-I1 | W1 |
| TASK-016 | P3 | W1 | Provision DEV / SIT / UAT / PROD Environment Separation | P0 | BPK-005-I1 | W1 |
| TASK-017 | P3 | W1 | Author Infrastructure as Code for Approved Hosting Target | P0 | BPK-005-I1 | W1 |
| TASK-018 | P3 | W1 | Build CI/CD Pipeline with Controlled Promotion Gates | P0 | BPK-005-I1 | W1 |
| TASK-019 | P3 | W1 | Integrate Approved Secret Management Store | P0 | BPK-005-I1 | W1 |
| TASK-020 | P3 | W1 | Provision Managed PostgreSQL with Backup & Encryption | P0 | BPK-005-I1 | W1 |
| TASK-021 | P3 | W1 | Configure Network Security: WAF, Load Balancer & Segmentation | P0 | BPK-005-I1 | W1 |
| TASK-022 | P3 | W1 | Establish Container/Artifact Build & Dependency Scanning | P1 | BPK-005-I1 | W1 |
| TASK-023 | P3 | W1 | Define Backup, Restore & Disaster Recovery Runbook | P1 | BPK-005-I1 (runbook); BPK-030 (drill evidence) | W1 |
| TASK-024 | P4 | W1 | Establish Database Migration Framework & Conventions | P0 | BPK-005-I1 | W1 |
| TASK-025 | P4 | W1 | Implement Core Platform Schema (Project, User, Org, Master Data) | P0 | BPK-006-I1; BPK-007-I1; BPK-014 (Project identity) | W1 |
| TASK-026 | P4 | W1 | Define Indexing Strategy for Query, Filter, Sort & Pagination Paths | P1 | BPK-005-I1 | W1 |
| TASK-027 | P4 | W1 | Build Seed Data & Data-Integrity Validation Scripts | P1 | BPK-007-I1 | W1 |
| TASK-028 | P5 | W1 | Integrate AD/LDAP and SSO Authentication | P0 | BPK-006-I1 | W1 |
| TASK-029 | P5 | W1 | Implement MFA & Privileged Access Controls | P0 | BPK-006-I1 | W1 |
| TASK-030 | P5 | W1 | Implement Server-Side RBAC & Data-Scope Authorization Engine | P0 | BPK-006-I1 | W1 |
| **TASK-031** | P5 | W1 | Build Users, Roles & Permissions Administration (FG-03 Backend) | P1 | BPK-006-I2 | **W3** |
| **TASK-032** | P5 | W1 | Build Users, Roles & Permissions Administration (FG-03 Frontend) | P1 | BPK-006-I2 | **W3** |
| TASK-033 | P5 | W1 | Implement Authentication & Access Audit Logging | P0 | BPK-006-I1; BPK-008-I1 | W1 |
| **TASK-034** | P6 | W2 | Build Master Data & Configuration Service (FG-04 Backend) | P0 | BPK-007-I1 | **W1** |
| TASK-035 | P6 | W2 | Build Shared Approval Framework (WF-11 Backend) | P0 | BPK-011-I1 | W2 |
| TASK-036 | P6 | W2 | Build Approvals UI: Inbox, My Requests & History (WF-11 Frontend) | P0 | BPK-011-I1 | W2 |
| TASK-037 | P6 | W2 | Build Document & Evidence Management (WF-12 Backend) | P0 | BPK-010-I1 | W2 |
| TASK-038 | P6 | W2 | Build Document Library & Upload UI (WF-12 Frontend) | P0 | BPK-010-I1 | W2 |
| TASK-039 | P6 | W2 | Build Notifications, Reminders & Escalations Runtime (WF-15 Backend) | P0 | BPK-012-I1 | W2 |
| TASK-040 | P6 | W2 | Build Notification Center UI (WF-15 Frontend) | P1 | BPK-012-I1 | W2 |
| TASK-041 | P7 | W2 | Build Project Creation & Registration (WF-01 Backend) | P0 | BPK-014-I1 | W2 |
| TASK-042 | P7 | W2 | Build Project Register & Creation UI (WF-01 Frontend) | P0 | BPK-014-I1 | W2 |
| TASK-043 | P7 | W2 | Contract & Integration Tests for Project Lifecycle | P1 | BPK-014-I1 | W2 |
| **TASK-044** | P8 | W3 | Build Progress Update & Overall Health (WF-02 Backend) | P0 | BPK-022 | **W4** |
| **TASK-045** | P8 | W3 | Build Progress & Schedule UI (WF-02/WF-03 Frontend) | P0 | BPK-022 | **W4** |
| TASK-046 | P8 | W3 | Build Schedule & Baseline Management (WF-03 Backend) | P0 | BPK-015-I1 | W3 |
| TASK-047 | P8 | W3 | Build Schedule, Gantt & Baseline UI (WF-03 Frontend) | P1 | BPK-015-I1 | W3 |
| TASK-048 | P8 | W3 | Build Task Management (WF-04 Backend) | P0 | BPK-016-I1 | W3 |
| TASK-049 | P8 | W3 | Build Task Boards & My Tasks UI (WF-04 Frontend) | P1 | BPK-016-I1 | W3 |
| **TASK-050** | P8 | W3 | Build Milestone Management (WF-05 Backend) | P0 | BPK-017 | **W4** |
| **TASK-051** | P8 | W3 | Build Milestone Register & Achievement UI (WF-05 Frontend) | P1 | BPK-017 | **W4** |
| TASK-052 | P8 | W3 | Build Financial Progress & KPI Performance (WF-14 Backend) | P0 | BPK-021-I1 | W3 |
| TASK-053 | P8 | W3 | Build Financial & KPI UI (WF-14 Frontend) | P1 | BPK-021-I1 | W3 |
| **TASK-054** | P8 | W3 | Contract & Integration Tests for Execution Domain (WF-02/03/04/05/14) | P1 | BPK-015/016/017/021/022 | **W4** |
| TASK-055 | P9 | W3 | Build Risk Management (WF-06 Backend) | P0 | BPK-018-I1 | W3 |
| TASK-056 | P9 | W3 | Build Risk Register & Detail UI (WF-06 Frontend) | P1 | BPK-018-I1 | W3 |
| TASK-057 | P9 | W3 | Build Issue & Challenge Management (WF-07 Backend) | P0 | BPK-019-I1 | W3 |
| TASK-058 | P9 | W3 | Build Issue, Challenge & Escalation UI (WF-07 Frontend) | P1 | BPK-019-I1 | W3 |
| TASK-059 | P9 | W3 | Contract & Regression Tests for Risk/Issue Domain (WF-06/07) | P1 | BPK-018; BPK-019 | W3 |
| TASK-060 | P10 | W4 | Build Change Request & Authorization (WF-08 Backend) | P0 | BPK-020 | W4 |
| TASK-061 | P10 | W4 | Build Change Request UI (WF-08 Frontend) | P1 | BPK-020 | W4 |
| **TASK-062** | P10 | W4 | Build Suspension & Resumption (WF-09 Backend) | P0 | BPK-024 | **W5** |
| **TASK-063** | P10 | W4 | Build Completion & Closure (WF-10 Backend) | P0 | BPK-025 | **W6** |
| **TASK-064** | P10 | W4 | Build Suspension & Closure UI (WF-09/WF-10 Frontend) | P1 | BPK-024; BPK-025 | **W6** |
| **TASK-065** | P10 | W4 | Contract & Regression Tests for Governance Domain (WF-08/09/10) | P1 | BPK-020/024/025 | **W6** |
| TASK-066 | P11 | W5 | Build External Entity Update & Review (WF-13 Backend) | P0 | BPK-023 | W5 |
| TASK-067 | P11 | W5 | Build External Participation UI (WF-13 Frontend) | P1 | BPK-023 | W5 |
| TASK-068 | P11 | W5 | Integrate Nafath Identity Verification (If Confirmed In Scope) | P2 | BPK-023 (real-provider integration; PTBC-031) | W5 |
| TASK-069 | P12 | W5 | Build Dashboard Projection & Definition Service (FG-01 Backend) | P0 | BPK-026 (BPK-013-I1 contract not in workbook) | W5 |
| TASK-070 | P12 | W5 | Build Dashboards UI (FG-01 Frontend) | P0 | BPK-026 | W5 |
| TASK-071 | P12 | W5 | Build Reports, Filters & Export Service (FG-02 Backend) | P0 | BPK-027 | W5 |
| TASK-072 | P12 | W5 | Build Reports Center UI (FG-02 Frontend) | P1 | BPK-027 | W5 |
| TASK-073 | P13 | W1 | Build Formal Audit & Activity Service (FG-06 Backend) | P0 | BPK-008-I1 | W1 |
| **TASK-074** | P13 | W1 | Build Audit & Activity UI (FG-06 Frontend) | P1 | BPK-028 | **W5** |
| TASK-075 | P13 | W1 | Build Integration Monitoring Runtime (FG-05 Backend) | P0 | BPK-009-I1 (typed runtime); BPK-009-I2 (monitoring/reconciliation, W5) | W1 |
| **TASK-076** | P13 | W1 | Build Integration Administration UI (FG-05 Frontend) | P1 | BPK-009-I2 | **W5** |
| TASK-077 | P14 | W1 | Implement Platform-Wide Input Validation & Output Encoding | P0 | BPK-005-I1 | W1 |
| TASK-078 | P14 | W1 | Implement Rate Limiting, CORS & Secure HTTP Headers | P0 | BPK-005-I1 | W1 |
| TASK-079 | P14 | W1 | Implement CSRF Protection for Session-Based Flows | P1 | BPK-006-I1 | W1 |
| TASK-080 | P14 | W1 | Add Secret Scanning & Dependency Vulnerability Gate to CI | P0 | BPK-005-I1 | W1 |
| **TASK-081** | P14 | W1 | Conduct Threat Modeling & Security Review for Sensitive Features | P0 | BPK-023 inputs; evidence BPK-030 | **W5** |
| **TASK-082** | P14 | W1 | Commission External Penetration Test Before Production | P0 | BPK-030 | **W6** |
| TASK-083 | P14 | W1 | Implement Logging Redaction & Sensitive-Data Handling Policy | P1 | BPK-008-I1 | W1 |
| **TASK-084** | P15 | W6 | Author Platform Test Strategy & Coverage Policy | P0 | BPK-005-I1 (test harness) | **W1** |
| TASK-085 | P15 | W6 | Implement Cross-Domain End-to-End Test Suite | P0 | BPK-030 | W6 |
| TASK-086 | P15 | W6 | Execute Performance & Load Testing Against Capacity Targets | P1 | BPK-030 (PTBC-043) | W6 |
| TASK-087 | P15 | W6 | Execute Platform-Wide Accessibility Audit | P1 | BPK-030 (PTBC-040) | W6 |
| TASK-088 | P15 | W6 | Prepare & Execute UAT Catalogue Scenarios | P0 | BPK-030 | W6 |
| TASK-089 | P15 | W6 | Validate Data Migration, Rollback & Seed Integrity | P0 | BPK-029 | W6 |
| TASK-090 | P16 | W1 | Integrate Application Performance Monitoring & Error Tracking | P1 | BPK-005-I1 (diagnostic logging) | W1 |
| TASK-091 | P16 | W1 | Implement Health Checks & Uptime Monitoring | P1 | BPK-005-I1 | W1 |
| **TASK-092** | P16 | W1 | Build Operational Dashboards & Alerting Thresholds (FG-05 Alerts) | P1 | BPK-009-I2 | **W5** |
| **TASK-093** | P16 | W1 | Document Operational SLAs & On-Call Runbook | P1 | BPK-029; BPK-030 | **W6** |
| TASK-094 | P17 | W6 | Publish API Documentation (OpenAPI/Swagger) | P1 | BPK-029 (built from W1) | W6 |
| TASK-095 | P17 | W6 | Author Developer Onboarding & Architecture Guide | P1 | BPK-029 (built from W1) | W6 |
| TASK-096 | P17 | W6 | Author End-User Guide & FAQ (Arabic + English) | P2 | BPK-029 | W6 |
| TASK-097 | P17 | W6 | Compile Operational Handover Package | P2 | BPK-029 | W6 |
| TASK-098 | P18 | W6 | Define Release & Rollback Strategy | P0 | BPK-030 (authored from W1) | W6 |
| TASK-099 | P18 | W6 | Execute Staging/Pre-Production Soak Test | P1 | BPK-030 | W6 |
| TASK-100 | P18 | W6 | Execute Production Go-Live | P0 | BPK-030 | W6 |
| TASK-101 | P18 | W6 | Run Post-Launch Hypercare & Stabilization Period | P1 | BPK-030 | W6 |
| TASK-102 | P18 | W6 | Confirm Data Migration Cutover & Legacy Decommission | P1 | BPK-029 | W6 |
