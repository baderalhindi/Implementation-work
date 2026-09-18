# PTBC / TBC Governance Tracker

| Control | Value |
|---|---|
| Task | TASK-004 — Stand Up PTBC / TBC Governance Tracker (Phase P0 — Discovery & Governance); depends on TASK-002 |
| Programme | AHDA Regional Project Management Platform (RPMO) |
| Issue date | 2026-09-18 |
| Tracker | `docs/governance/ptbc-tbc-tracker.xlsx` (8 sheets) — this note is its governance rule set and the diff-reviewable extract |
| Tracker status | **ISSUED — 0 of 48 PTBC values approved; 0 of 511 source TBCs resolved.** Acceptance of the tracker as the single governance register is pending (§10). No AHDA value is approved or proposed by this task. |
| Owner | Requirements governance lead (14B-F-008 owner) / PMO |

Sources and precedence per TASK-001 (`docs/baseline/controlled-source-baseline.md`). Documents are cited by their `CSB-*` register ID. Counts and gate classes are those fixed by Step 14B Assessment v1.1 (`docs/rtm/step-14b-rtm-assessment-v1.1.md`, §8); task packages and waves are those of TASK-003 (`docs/planning/wave-to-phase-crossreference.md`, Appendix A).

## 1. Purpose

Forty-eight platform TBC themes (PTBC-001–PTBC-048, CSB-14A §19.2 = CSB-BP2 Appendix F.2) consolidate 511 source-level TBCs that the 21 WF/FG specifications leave to AHDA: approval limits, materiality thresholds, KPI formulas, risk matrices, retention periods, RPO/RTO, providers, hosting. Until now they were spread over four registers (CSB-14A §19, CSB-14B-RTM `08_PTBC_Impact` / `14_Source_TBC`, CSB-15 `11_TBC_PTBC_Gates`, CSB-17 `Governance_Values`) and the workbook's Open Questions sheet, with no status field and no link from a workbook task to the theme that gates it.

This tracker is the one place where a value's state is recorded. It exists so that no task, ADR, seed script, fixture, runbook or test invents an AHDA business value: a value exists only when its PTBC row shows `APPROVED` with a decision reference, signatory and date.

## 2. What was consolidated and what was verified

| Source | What the tracker takes from it | Verification on 2026-09-18 |
|---|---|---|
| CSB-14A §19.2 / CSB-BP2 App. F.2 / CSB-14B-RTM `08_PTBC_Impact` | The 48 rows: category, theme, source families, resolution gate, integrated treatment — copied verbatim into the "as recorded" columns | **48 of 48 rows word-identical across the three registers** (the workbook validation note asks for a 10-row spot check; all 48 were compared programmatically). 0 wording differences. |
| CSB-14A §19.3 via 14B v1.1 §8 | The four gate classes and the 34-label → 4-class normalisation | Reproduced: 7 / 31 / 9 / 1 themes; 71 / 375 / 53 / 12 source TBCs by earliest gate |
| CSB-14B-RTM `14_Source_TBC` | The 511 source TBCs with owner spec, original wording, source location, PTBC themes, analytical RTM rows | 511 rows; owners match CSB-14A §19.1 exactly; TBC→PTBC direction and PTBC→TBC direction agree for all 511; 90 multi-theme; 106 with no RTM row (analytical gap per 14B v1.1 §8); identical to CSB-15 `11_TBC_PTBC_Gates` |
| CSB-15 `11_TBC_PTBC_Gates`, `02_Build_Packages` | Step 15 issue category, planning gate, work permitted now, value restriction, affected packages, package wave | 559 rows (48 + 511) read; PTBC gate labels identical to CSB-14A |
| Workbook (Implementation Plan, Open Questions, Architecture Decisions, Release Checklist) | Task register (102), the 10 Open Questions, 6 ADRs, 15 release gates | Blocking tasks resolved from description to ID (finding 004-F-005); 17 tasks cite a PTBC ID explicitly |
| TASK-003 cross-reference Appendix A | Task → Step 15 package → wave | 102 of 102 tasks resolved |

## 3. Governance rule for every task

1. **A gated value is not a design input.** If a task's Detailed Description, Acceptance Criteria, seed data, fixtures, runbook or configuration would fix an AHDA value that a PTBC row lists as `OPEN`, the task builds the *mechanism* (versioned configuration, fail-closed resolution, non-production fixtures) and records the value as `TBC — PTBC-xxx`. This is the CSB-14A governance rule, the CSB-15 "no production default inferred" restriction and 16-F-005 applied to the workbook.
2. **Where the value may be resolved is fixed by the gate class**, not by the task's convenience:

| Gate class (CSB-14A §19.3) | PTBC themes | Source TBCs | What may be built before the value exists |
|---|---|---|---|
| BEFORE BUILD / SIT | 7 | 71 | Resolve only what is needed to connect to real enterprise systems or to fix mandatory security architecture; generic adapters and configuration mechanisms may be built earlier (CSB-14A §19.3). SIT and performance-test gates are classed here (14B v1.1 §8). |
| BEFORE UAT | 31 | 375 | Populate workflow authorities, master data, matrices, thresholds, evidence rules and the dashboard/report catalogue before the affected UAT scenarios run (CSB-14A §19.3). |
| BEFORE PRODUCTION | 9 | 53 | Finalise security classification, privileged access, SIEM/logging, retention, backup/DR, production operators, providers and operational SLAs before go-live (CSB-14A §19.3). |
| MAY REMAIN CONFIGURABLE | 1 | 12 | Business labels, reminder offsets, display preferences and similar values may change after go-live if their configuration lifecycle is governed (CSB-14A §19.3). |

3. **Working baselines are not values.** The workbook carries working assumptions (WCAG 2.1 AA, 150 named users, GCP topology, MFA for R01 only, In-App + Email channels). They are listed on the PTBC row in the column "Working baseline in workbook (NOT an approved value)" and nowhere else; the "Approved value / decision reference" column is empty for all 48 rows.
4. **Status moves on evidence only**, using the vocabulary in `07_Status_Vocabulary`: `OPEN` → `PROPOSED` (candidate put to the accountable AHDA function, reference recorded) → `APPROVED` (decision record, signatory, date) → `IMPLEMENTED` (configured and verified). `DEFERRED` is valid only for a *May Remain Configurable* theme with an AHDA decision record (today only PTBC-042).
5. **A task that touches a gated value cites the PTBC ID.** The link register (§6, `03_Task_Links`) is the control; the workbook rows should carry the same IDs at the next revision (finding 004-F-006).
6. **The "as recorded" columns are read-only.** A wording, gate or association change is a CSB-14A / CSB-14B change, not a tracker edit; the tracker records proposals (e.g. §8 004-F-001) in separate "proposed" columns until the owning register is re-issued.

## 4. PTBC register (48 themes)

Condensed from `01_PTBC_Register`; the sheet adds the as-recorded treatment, Step 15 issue category and planning gate, value restriction, source TBC IDs, RTM row counts, packages, Release Checklist gates and the empty approval columns. Tasks listed here are DIRECT and SPEC links; package-inherited links are in the sheet.

| PTBC | Category | Theme | Source specs (expanded) | Gate (as recorded) | Gate class | Status | Working baseline | OQ / ADR | Workbook tasks TASK-… (DIRECT + SPEC) |
|---|---|---|---|---|---|---|---|---|---|
| PTBC-001 | Business Governance | Approval authority matrices and decision limits | WF-01; WF-03; WF-08; WF-09; WF-10; WF-11 | Before UAT | BEFORE UAT | OPEN | — | OQ-005 | 035, 036, 041, 042, 045, 046, 047, 054, 060, 061, 062, 063, 064, 065 (+3 package-inherited) |
| PTBC-002 | Business Governance | Project Activation authority and readiness policy | WF-01; WF-03; FG-04 | Before UAT | BEFORE UAT | OPEN | yes | — | 034, 041, 042, 045, 046, 047, 054 (+4 package-inherited) |
| PTBC-003 | Business Governance | External Entity participation eligibility and onboarding authority | WF-01; WF-13; FG-03 | Before External UAT | BEFORE UAT | OPEN | — | OQ-007 | 028, 029, 030, 031, 032, 033, 041, 042, 066, 067, 068 (+5 package-inherited) |
| PTBC-004 | Business Governance | Completion/Closure readiness criteria and disposition policy | WF-10 | Before closeout UAT | BEFORE UAT | OPEN | — | — | 063, 064, 065 |
| PTBC-005 | Business Governance | Suspension/Resumption reasons, readiness and review governance | WF-09 | Before suspension UAT | BEFORE UAT | OPEN | — | — | 062, 064, 065 |
| PTBC-006 | Business Governance | Milestone achievement evidence/review governance | WF-05 | Before milestone UAT | BEFORE UAT | OPEN | — | — | 050, 051, 054 |
| PTBC-007 | Business Governance | Risk acceptance/escalation authority | WF-06 | Before risk UAT | BEFORE UAT | OPEN | — | — | 055, 056, 059 |
| PTBC-008 | Business Governance | Issue/Challenge severity-priority/escalation governance | WF-07 | Before concern UAT | BEFORE UAT | OPEN | — | — | 057, 058, 059 |
| PTBC-009 | Business Governance | Change materiality/threshold governance | WF-08; FG-04 | Before change UAT | BEFORE UAT | OPEN | — | OQ-005 | 034, 035, 060, 061, 065 (+3 package-inherited) |
| PTBC-010 | Business Governance | Dashboard/Report publication authority and SoD | FG-01; FG-02; FG-04 | Before admin UAT | BEFORE UAT | OPEN | — | — | 034, 069, 070, 071, 072 (+3 package-inherited) |
| PTBC-011 | Business Governance | Audit Reviewer, retention-hold and disposal authorities | FG-06 | Before audit/records UAT | BEFORE UAT | OPEN | — | — | 033, 073, 074 (+1 package-inherited) |
| PTBC-012 | Business Governance | Sensitive read/export audit policy | FG-02; FG-06 | Before production | BEFORE PRODUCTION | OPEN | — | — | 033, 071, 072, 073, 074 |
| PTBC-013 | Configuration | Project type/classification/priority/sector/location catalogues | WF-01; FG-04 | Before UAT data load | BEFORE UAT | OPEN | — | — | 034, 041, 042 (+4 package-inherited) |
| PTBC-014 | Configuration | Business calendar, timezone and working-day policy | WF-02; WF-03; WF-11; FG-04 | Before SLA/schedule UAT | BEFORE UAT | OPEN | — | — | 034, 035, 036, 044, 045, 046, 047, 054 (+3 package-inherited) |
| PTBC-015 | Configuration | Schedule Health thresholds and calendar override policy | WF-03 | Before schedule UAT | BEFORE UAT | OPEN | — | — | 045, 046, 047, 054 |
| PTBC-016 | Configuration | Task priority/category/reminder/blocked thresholds | WF-04 | Before task UAT | BEFORE UAT | OPEN | — | — | 048, 049, 054 |
| PTBC-017 | Configuration | Risk scales/dimensions/matrix | WF-06; FG-04 | Before risk UAT | BEFORE UAT | OPEN | — | OQ-006 | 034, 052, 055, 056, 059 |
| PTBC-018 | Configuration | Issue/Challenge categories/severity/priority master data | WF-07; FG-04 | Before concern UAT | BEFORE UAT | OPEN | — | — | 034, 057, 058, 059 |
| PTBC-019 | Configuration | Evidence/document categories and mandatory evidence policies | WF-01; WF-02; WF-03; WF-04; WF-05; WF-06; WF-07; WF-08; WF-09; WF-10; WF-12; FG-04 | Before workflow UAT | BEFORE UAT | OPEN | — | — | 034, 037, 038, 041, 042, 044, 045, 046, 047, 048, 049, 050, 051, 054, 055, 056, 057, 058, 059, 060, 061, 062, 063, 064, 065 (+3 package-inherited) |
| PTBC-020 | Configuration | Notification reminder offsets/escalation timing | WF-15; WF-01; WF-02; WF-03; WF-04; WF-05; WF-06; WF-07; WF-08; WF-09; WF-10; WF-11; WF-12; WF-13; WF-14 | Before notification UAT | BEFORE UAT | OPEN | — | — | 035, 036, 037, 038, 039, 040, 041, 042, 044, 045, 046, 047, 048, 049, 050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 060, 061, 062, 063, 064, 065, 066, 067, 068 |
| PTBC-021 | Configuration | Dashboard catalogue/defaults/personalization scope | FG-01 | Before dashboard UAT | BEFORE UAT | OPEN | yes | OQ-002; ADR-006 | 069, 070, 071, 072 |
| PTBC-022 | Configuration | Report catalogue/default access/saved-view sharing | FG-02 | Before report UAT | BEFORE UAT | OPEN | yes | OQ-002; ADR-006 | 069, 070, 071, 072 |
| PTBC-023 | Configuration | Overall Project Health rule/presentation policy | WF-02; FG-04; FG-01; FG-02 | Before executive UAT | BEFORE UAT | OPEN | — | — | 034, 044, 045, 054, 069, 070, 071, 072 |
| PTBC-024 | Configuration | KPI catalogue/formulas/targets/condition thresholds | WF-14; FG-04 | Before KPI UAT | BEFORE UAT | OPEN | — | OQ-006 | 034, 052, 053, 054, 055 |
| PTBC-025 | Configuration | Financial condition/variance/forecast terminology and thresholds | WF-14; FG-04 | Before financial UAT | BEFORE UAT | OPEN | — | OQ-006 | 034, 052, 053, 054, 055 |
| PTBC-026 | Cybersecurity | Platform criticality and data classification | CSB-CYBER-GUIDE; FG-03; WF-12; WF-14; FG-06 | Before production security sign-off | BEFORE PRODUCTION | OPEN | — | — | 010, 020, 023, 028, 029, 030, 031, 032, 033, 037, 038, 052, 053, 054, 073, 074, 083, 090 (+32 package-inherited) |
| PTBC-027 | Cybersecurity | MFA/PAM/privileged administration policy | CSB-CYBER-GUIDE; FG-03 | Before production | BEFORE PRODUCTION | OPEN | yes | — | 010, 020, 023, 028, 029, 030, 031, 032, 033, 083, 090 (+13 package-inherited) |
| PTBC-028 | Cybersecurity | Sensitive payload/change-set visibility and redaction rules | FG-05; FG-06 | Before security UAT | BEFORE UAT | OPEN | — | — | 033, 073, 074, 075, 076, 092 (+17 package-inherited) |
| PTBC-029 | Cybersecurity | Audit/SIEM forwarding catalogue and integration | CSB-CYBER-GUIDE; FG-06; FG-05 | Before production | BEFORE PRODUCTION | OPEN | — | — | 010, 020, 023, 033, 073, 074, 075, 076, 083, 090, 092 (+12 package-inherited) |
| PTBC-030 | Cybersecurity | Export watermark/classification/attachment policy | FG-02; FG-06; WF-15 | Before production | BEFORE PRODUCTION | OPEN | yes | ADR-005 | 010, 033, 039, 040, 071, 072, 073, 074 (+2 package-inherited) |
| PTBC-031 | Cybersecurity | External identity proofing / Nafath applicability | WF-13; FG-03; FG-05 | Before External integration UAT | BEFORE UAT | OPEN | — | OQ-007 | 028, 029, 030, 031, 032, 033, 066, 067, 068, 075, 076, 092 (+3 package-inherited) |
| PTBC-032 | Integration | Production Integration catalogue and system owners | CSB-CYBER-GUIDE; FG-05 | Before integration build/SIT | BEFORE BUILD / SIT | OPEN | — | — | 010, 020, 023, 075, 076, 083, 090, 092 (+12 package-inherited) |
| PTBC-033 | Integration | Financial/KPI authoritative source systems and field authority | WF-14; FG-05 | Before financial integration SIT | BEFORE BUILD / SIT | OPEN | — | — | 052, 053, 054, 075, 076, 092 (+1 package-inherited) |
| PTBC-034 | Integration | Email/SMS provider topology and callbacks | WF-15; FG-05 | Before notification SIT | BEFORE BUILD / SIT | OPEN | yes | ADR-004 | 039, 040, 075, 076, 092 (+1 package-inherited) |
| PTBC-035 | Integration | Document storage/malware-scan provider and quarantine operations | WF-12; FG-05 | Before document SIT | BEFORE BUILD / SIT | OPEN | — | — | 037, 038, 075, 076, 092 (+1 package-inherited) |
| PTBC-036 | Integration | SSO/directory topology and group/claim mappings | FG-03; FG-05 | Before IAM SIT | BEFORE BUILD / SIT | OPEN | yes | — | 028, 029, 030, 031, 032, 033, 075, 076, 092 (+3 package-inherited) |
| PTBC-037 | Integration | Integration health/freshness/reconciliation thresholds | FG-05 | Before operations UAT | BEFORE UAT | OPEN | — | — | 075, 076, 092 (+2 package-inherited) |
| PTBC-038 | Integration | Retry/backoff/dead-letter policies | FG-05; INTEGRATION-ADAPTERS | Before SIT | BEFORE BUILD / SIT | OPEN | — | — | 075, 076, 092 (+3 package-inherited) |
| PTBC-039 | UX/Presentation | Arabic/English completeness and historical label policy | ALL; FG-01; FG-02; FG-06 | Before UAT | BEFORE UAT | OPEN | — | — | 032, 033, 036, 038, 040, 042, 045, 047, 049, 051, 053, 056, 058, 061, 064, 067, 069, 070, 071, 072, 073, 074, 076, 096 (+4 package-inherited) |
| PTBC-040 | UX/Presentation | Accessibility conformance target | FG-01; FG-02; COMMON-UI | Before UAT | BEFORE UAT | OPEN | yes | OQ-010 | 032, 036, 038, 040, 042, 045, 047, 049, 051, 053, 056, 058, 061, 064, 067, 069, 070, 071, 072, 074, 076, 086, 087 (+22 package-inherited) |
| PTBC-041 | UX/Presentation | Executive dashboard/report content and R07 scope | FG-01; FG-02; FG-03 | Before executive UAT | BEFORE UAT | OPEN | — | — | 028, 029, 030, 031, 032, 033, 069, 070, 071, 072 (+2 package-inherited) |
| PTBC-042 | UX/Presentation | Geospatial/map and advanced visualization requirement | FG-01 | Can remain configurable/deferred | MAY REMAIN CONFIGURABLE | OPEN | yes | OQ-004 | 002, 069, 070 |
| PTBC-043 | Technical Architecture | Performance/scale thresholds and cache/materialization TTLs | CSB-CYBER-GUIDE; FG-01; FG-02; FG-05; FG-06 | Before performance test | BEFORE BUILD / SIT | OPEN | yes | OQ-010 | 010, 020, 023, 033, 069, 070, 071, 072, 073, 074, 075, 076, 083, 086, 087, 090, 092 (+29 package-inherited) |
| PTBC-044 | Technical Architecture | Observability/logging/APM technology stack | CSB-CYBER-GUIDE; FG-05; FG-06 | Before production | BEFORE PRODUCTION | OPEN | yes | ADR-002 | 006, 010, 020, 023, 033, 073, 074, 075, 076, 083, 090, 092 (+31 package-inherited) |
| PTBC-045 | Technical Architecture | Immutable audit/tamper-evidence/archive implementation | FG-06 | Before production | BEFORE PRODUCTION | OPEN | — | — | 033, 073, 074 (+13 package-inherited) |
| PTBC-046 | Operations | Operational alert recipients, maintenance governance and production retry authority | FG-05 | Before operations UAT | BEFORE UAT | OPEN | — | — | 075, 076, 092 (+3 package-inherited) |
| PTBC-047 | Records/Retention | Document/report/audit/log retention and legal-hold policy | WF-12; FG-02; FG-05; FG-06 | Before production | BEFORE PRODUCTION | OPEN | — | — | 033, 037, 038, 071, 072, 073, 074, 075, 076, 092 (+13 package-inherited) |
| PTBC-048 | Records/Retention | Backup/DR RPO/RTO, backup retention and residency/hosting | CSB-CYBER-GUIDE; FG-05; FG-06 | Before production | BEFORE PRODUCTION | OPEN | yes | OQ-001; OQ-003; ADR-001 | 005, 010, 014, 015, 016, 017, 018, 019, 020, 023, 033, 073, 074, 075, 076, 083, 090, 092 (+24 package-inherited) |

Counts: Business Governance 12 · Configuration 13 · Cybersecurity 6 · Integration 7 · UX/Presentation 4 · Technical Architecture 3 · Operations 1 · Records/Retention 2 = 48. Gate classes: Before Build / SIT 7 · Before UAT 31 · Before Production 9 · May Remain Configurable 1.

## 5. Source TBC register (511 items) — summary

The 511 rows are in `02_Source_TBC_Register` with owner spec, original wording, source location (document :: section :: table row), PTBC themes, earliest gate class, Step 15 packages and empty resolution columns. All 511 are `OPEN — deferred to PTBC gate`; none is resolved.

| Owner spec | Source TBCs | Before Build / SIT | Before UAT | Before Production | May Remain Configurable | No RTM row |
|---|---|---|---|---|---|---|
| FG-01 | 30 | 2 | 26 | 1 | 1 | 6 |
| FG-02 | 30 | 4 | 21 | 4 | 1 | 10 |
| FG-03 | 25 | 3 | 1 | 20 | 1 | 2 |
| FG-04 | 30 | 2 | 25 | 3 | 0 | 9 |
| FG-05 | 34 | 18 | 12 | 4 | 0 | 11 |
| FG-06 | 31 | 1 | 20 | 10 | 0 | 5 |
| WF-01 | 17 | 1 | 14 | 0 | 2 | 1 |
| WF-02 | 26 | 1 | 25 | 0 | 0 | 4 |
| WF-03 | 18 | 2 | 16 | 0 | 0 | 4 |
| WF-04 | 18 | 1 | 17 | 0 | 0 | 4 |
| WF-05 | 16 | 1 | 15 | 0 | 0 | 3 |
| WF-06 | 20 | 1 | 19 | 0 | 0 | 3 |
| WF-07 | 16 | 3 | 12 | 0 | 1 | 3 |
| WF-08 | 24 | 1 | 21 | 1 | 1 | 5 |
| WF-09 | 20 | 2 | 18 | 0 | 0 | 4 |
| WF-10 | 25 | 4 | 20 | 1 | 0 | 5 |
| WF-11 | 18 | 2 | 15 | 1 | 0 | 6 |
| WF-12 | 30 | 2 | 23 | 4 | 1 | 6 |
| WF-13 | 28 | 3 | 21 | 2 | 2 | 9 |
| WF-14 | 30 | 6 | 23 | 0 | 1 | 3 |
| WF-15 | 25 | 11 | 11 | 2 | 1 | 3 |
| **Total** | 511 | 71 | 375 | 53 | 12 | 106 |

17 rows carry `ASSOCIATION UNDER REVIEW` with a proposed PTBC and gate class (finding 004-F-001 / 004-F-002, §8). The recorded 14B association stays controlling until the requirements governance lead confirms or rejects the proposal.

## 6. Task → PTBC links

`03_Task_Links` holds 676 task↔PTBC rows over 94 of the 102 tasks. Link strength: **DIRECT** (task text cites the PTBC, or the task blocks an Open Question that names it, or it produces the carrying ADR) — 50 rows; **SPEC** (task builds a source family of the theme) — 354; **PACKAGE** (Step 15 package impact only) — 272. The 8 unlinked tasks — TASK-001, TASK-003, TASK-004, TASK-089, TASK-094, TASK-095, TASK-097, TASK-102 — are governance or documentation tasks, or (TASK-089, TASK-102) gated by OQ-008 which has no PTBC theme.

| Task | Name | Wave | DIRECT (PTBC-…) | SPEC (PTBC-…) | PACKAGE-inherited (PTBC-…) | Cites in workbook |
|---|---|---|---|---|---|---|
| TASK-002 | Close Step 14B RTM Findings | W0 | 042 | — | — | — |
| TASK-005 | Resolve Hosting & Data Localisation Architecture Decision Record | W0 | 048 | — | — | — |
| TASK-006 | Ratify Application Technology Stack ADR | W0 | 044 | — | — | — |
| TASK-007 | Define Three-Tier Solution Architecture & Module Boundaries | W0 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-008 | Produce Canonical Entity-Relationship Diagram | W0 | — | — | 001, 002, 003, 009, 010, 013, 014, 019, 039 | — |
| TASK-009 | Define Platform API & Event Contract Conventions | W0 | — | — | 028, 029, 032, 033, 034, 035, 036, 037, 038, 043, 044, 046 | — |
| TASK-010 | Ratify Cybersecurity Control Overlay Mapping (CS-001-033) | W0 | 026, 030 | 027, 029, 032, 043, 044, 048 | — | 026, 030 |
| TASK-011 | Initialize Monorepo & Solution Structure | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-012 | Define Branching Strategy, PR Template & Code Owners | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-013 | Author Environment Variable Templates per Environment | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-014 | Build Local Development Environment (Docker Compose) | W1 | 048 | — | 026, 040, 043, 044 | — |
| TASK-015 | Configure Quality Gates: Lint, Format, Type-Check, Test in CI | W1 | 048 | — | 026, 040, 043, 044 | — |
| TASK-016 | Provision DEV / SIT / UAT / PROD Environment Separation | W1 | 048 | — | 026, 040, 043, 044 | — |
| TASK-017 | Author Infrastructure as Code for Approved Hosting Target | W1 | 048 | — | 026, 040, 043, 044 | — |
| TASK-018 | Build CI/CD Pipeline with Controlled Promotion Gates | W1 | 048 | — | 026, 040, 043, 044 | — |
| TASK-019 | Integrate Approved Secret Management Store | W1 | 048 | — | 026, 040, 043, 044 | — |
| TASK-020 | Provision Managed PostgreSQL with Backup & Encryption | W1 | 048 | 026, 027, 029, 032, 043, 044 | 040 | 048 |
| TASK-021 | Configure Network Security: WAF, Load Balancer & Segmentation | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-022 | Establish Container/Artifact Build & Dependency Scanning | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-023 | Define Backup, Restore & Disaster Recovery Runbook | W1 | 048 | 026, 027, 029, 032, 043, 044 | 040, 045, 047 | 048 |
| TASK-024 | Establish Database Migration Framework & Conventions | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-025 | Implement Core Platform Schema (Project, User, Org, Master Data) | W1 | — | — | 001, 002, 003, 009, 010, 013, 014, 019, 026, 027, 028, 031, 036, 039, 041 | — |
| TASK-026 | Define Indexing Strategy for Query, Filter, Sort & Pagination Paths | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-027 | Build Seed Data & Data-Integrity Validation Scripts | W1 | — | — | 002, 009, 010, 013, 014, 039 | — |
| TASK-028 | Integrate AD/LDAP and SSO Authentication | W1 | 036 | 003, 026, 027, 031, 041 | 028 | 036 |
| TASK-029 | Implement MFA & Privileged Access Controls | W1 | 027 | 003, 026, 031, 036, 041 | 028 | 027 |
| TASK-030 | Implement Server-Side RBAC & Data-Scope Authorization Engine | W1 | — | 003, 026, 027, 031, 036, 041 | 028 | — |
| TASK-031 | Build Users, Roles & Permissions Administration (FG-03 Backend) | W3 | — | 003, 026, 027, 031, 036, 041 | 028 | — |
| TASK-032 | Build Users, Roles & Permissions Administration (FG-03 Frontend) | W3 | — | 003, 026, 027, 031, 036, 039, 040, 041 | 028 | — |
| TASK-033 | Implement Authentication & Access Audit Logging | W1 | 011, 029 | 003, 012, 026, 027, 028, 030, 031, 036, 039, 041, 043, 044, 045, 047, 048 | — | 011, 029 |
| TASK-034 | Build Master Data & Configuration Service (FG-04 Backend) | W1 | — | 002, 009, 010, 013, 014, 017, 018, 019, 023, 024, 025 | 039 | — |
| TASK-035 | Build Shared Approval Framework (WF-11 Backend) | W2 | 001, 009 | 014, 020 | — | — |
| TASK-036 | Build Approvals UI: Inbox, My Requests & History (WF-11 Frontend) | W2 | — | 001, 014, 020, 039, 040 | — | — |
| TASK-037 | Build Document & Evidence Management (WF-12 Backend) | W2 | — | 019, 020, 026, 035, 047 | 028, 030 | — |
| TASK-038 | Build Document Library & Upload UI (WF-12 Frontend) | W2 | — | 019, 020, 026, 035, 039, 040, 047 | 028, 030 | — |
| TASK-039 | Build Notifications, Reminders & Escalations Runtime (WF-15 Backend) | W2 | — | 020, 030, 034 | 038, 046 | — |
| TASK-040 | Build Notification Center UI (WF-15 Frontend) | W2 | — | 020, 030, 034, 039, 040 | 038, 046 | — |
| TASK-041 | Build Project Creation & Registration (WF-01 Backend) | W2 | 002 | 001, 003, 013, 019, 020 | — | 002 |
| TASK-042 | Build Project Register & Creation UI (WF-01 Frontend) | W2 | — | 001, 002, 003, 013, 019, 020, 039, 040 | — | — |
| TASK-043 | Contract & Integration Tests for Project Lifecycle | W2 | — | — | 001, 002, 003, 013, 019 | — |
| TASK-044 | Build Progress Update & Overall Health (WF-02 Backend) | W4 | — | 014, 019, 020, 023 | — | — |
| TASK-045 | Build Progress & Schedule UI (WF-02/WF-03 Frontend) | W4 | — | 001, 002, 014, 015, 019, 020, 023, 039, 040 | — | — |
| TASK-046 | Build Schedule & Baseline Management (WF-03 Backend) | W3 | — | 001, 002, 014, 015, 019, 020 | — | — |
| TASK-047 | Build Schedule, Gantt & Baseline UI (WF-03 Frontend) | W3 | — | 001, 002, 014, 015, 019, 020, 039, 040 | — | — |
| TASK-048 | Build Task Management (WF-04 Backend) | W3 | — | 016, 019, 020 | — | — |
| TASK-049 | Build Task Boards & My Tasks UI (WF-04 Frontend) | W3 | — | 016, 019, 020, 039, 040 | — | — |
| TASK-050 | Build Milestone Management (WF-05 Backend) | W4 | — | 006, 019, 020 | — | — |
| TASK-051 | Build Milestone Register & Achievement UI (WF-05 Frontend) | W4 | 006, 019 | 020, 039, 040 | — | 006, 019 |
| TASK-052 | Build Financial Progress & KPI Performance (WF-14 Backend) | W3 | 017, 024, 025 | 020, 026, 033 | — | — |
| TASK-053 | Build Financial & KPI UI (WF-14 Frontend) | W3 | — | 020, 024, 025, 026, 033, 039, 040 | — | — |
| TASK-054 | Contract & Integration Tests for Execution Domain (WF-02/03/04/05/14) | W4 | — | 001, 002, 006, 014, 015, 016, 019, 020, 023, 024, 025, 026, 033 | — | — |
| TASK-055 | Build Risk Management (WF-06 Backend) | W3 | 017, 024, 025 | 007, 019, 020 | — | 017 |
| TASK-056 | Build Risk Register & Detail UI (WF-06 Frontend) | W3 | — | 007, 017, 019, 020, 039, 040 | — | — |
| TASK-057 | Build Issue & Challenge Management (WF-07 Backend) | W3 | — | 008, 018, 019, 020 | — | — |
| TASK-058 | Build Issue, Challenge & Escalation UI (WF-07 Frontend) | W3 | — | 008, 018, 019, 020, 039, 040 | — | — |
| TASK-059 | Contract & Regression Tests for Risk/Issue Domain (WF-06/07) | W3 | — | 007, 008, 017, 018, 019, 020 | — | — |
| TASK-060 | Build Change Request & Authorization (WF-08 Backend) | W4 | 001, 009 | 019, 020 | 028 | — |
| TASK-061 | Build Change Request UI (WF-08 Frontend) | W4 | — | 001, 009, 019, 020, 039, 040 | 028 | — |
| TASK-062 | Build Suspension & Resumption (WF-09 Backend) | W5 | — | 001, 005, 019, 020 | — | — |
| TASK-063 | Build Completion & Closure (WF-10 Backend) | W6 | — | 001, 004, 019, 020 | — | — |
| TASK-064 | Build Suspension & Closure UI (WF-09/WF-10 Frontend) | W6 | — | 001, 004, 005, 019, 020, 039, 040 | — | — |
| TASK-065 | Contract & Regression Tests for Governance Domain (WF-08/09/10) | W6 | — | 001, 004, 005, 009, 019, 020 | 028 | — |
| TASK-066 | Build External Entity Update & Review (WF-13 Backend) | W5 | 003, 031 | 020 | 028 | — |
| TASK-067 | Build External Participation UI (WF-13 Frontend) | W5 | 003, 031 | 020, 039, 040 | 028 | — |
| TASK-068 | Integrate Nafath Identity Verification (If Confirmed In Scope) | W5 | 003, 031 | 020 | 028 | 003, 031 |
| TASK-069 | Build Dashboard Projection & Definition Service (FG-01 Backend) | W5 | 021, 022 | 010, 023, 039, 040, 041, 042, 043 | 037 | — |
| TASK-070 | Build Dashboards UI (FG-01 Frontend) | W5 | 021, 022, 042 | 010, 023, 039, 040, 041, 043 | — | — |
| TASK-071 | Build Reports, Filters & Export Service (FG-02 Backend) | W5 | 021, 022 | 010, 012, 023, 030, 039, 040, 041, 043, 047 | — | — |
| TASK-072 | Build Reports Center UI (FG-02 Frontend) | W5 | 021, 022 | 010, 012, 023, 030, 039, 040, 041, 043, 047 | — | — |
| TASK-073 | Build Formal Audit & Activity Service (FG-06 Backend) | W1 | — | 011, 012, 026, 028, 029, 030, 039, 043, 044, 045, 047, 048 | — | — |
| TASK-074 | Build Audit & Activity UI (FG-06 Frontend) | W5 | — | 011, 012, 026, 028, 029, 030, 039, 040, 043, 044, 045, 047, 048 | — | — |
| TASK-075 | Build Integration Monitoring Runtime (FG-05 Backend) | W1 | — | 028, 029, 031, 032, 033, 034, 035, 036, 037, 038, 043, 044, 046, 047, 048 | — | — |
| TASK-076 | Build Integration Administration UI (FG-05 Frontend) | W5 | — | 028, 029, 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 043, 044, 046, 047, 048 | — | — |
| TASK-077 | Implement Platform-Wide Input Validation & Output Encoding | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-078 | Implement Rate Limiting, CORS & Secure HTTP Headers | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-079 | Implement CSRF Protection for Session-Based Flows | W1 | — | — | 003, 026, 027, 028, 031, 036, 041 | — |
| TASK-080 | Add Secret Scanning & Dependency Vulnerability Gate to CI | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-081 | Conduct Threat Modeling & Security Review for Sensitive Features | W5 | — | — | 003, 026, 027, 028, 029, 031, 032, 043, 044, 045, 047, 048 | — |
| TASK-082 | Commission External Penetration Test Before Production | W6 | — | — | 026, 027, 029, 032, 043, 044, 045, 047, 048 | — |
| TASK-083 | Implement Logging Redaction & Sensitive-Data Handling Policy | W1 | — | 026, 027, 029, 032, 043, 044, 048 | 011, 045, 047 | — |
| TASK-084 | Author Platform Test Strategy & Coverage Policy | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-085 | Implement Cross-Domain End-to-End Test Suite | W6 | — | — | 026, 027, 029, 032, 043, 044, 045, 047, 048 | — |
| TASK-086 | Execute Performance & Load Testing Against Capacity Targets | W6 | 040, 043 | — | 026, 027, 029, 032, 044, 045, 047, 048 | 043 |
| TASK-087 | Execute Platform-Wide Accessibility Audit | W6 | 040, 043 | — | 026, 027, 029, 032, 044, 045, 047, 048 | 040 |
| TASK-088 | Prepare & Execute UAT Catalogue Scenarios | W6 | — | — | 026, 027, 029, 032, 043, 044, 045, 047, 048 | — |
| TASK-090 | Integrate Application Performance Monitoring & Error Tracking | W1 | — | 026, 027, 029, 032, 043, 044, 048 | 040 | — |
| TASK-091 | Implement Health Checks & Uptime Monitoring | W1 | — | — | 026, 040, 043, 044, 048 | — |
| TASK-092 | Build Operational Dashboards & Alerting Thresholds (FG-05 Alerts) | W5 | 037 | 028, 029, 031, 032, 033, 034, 035, 036, 038, 043, 044, 046, 047, 048 | — | 037 |
| TASK-093 | Document Operational SLAs & On-Call Runbook | W6 | — | — | 026, 027, 029, 032, 043, 044, 045, 047, 048 | — |
| TASK-096 | Author End-User Guide & FAQ (Arabic + English) | W6 | — | 039 | — | — |
| TASK-098 | Define Release & Rollback Strategy | W6 | — | — | 026, 027, 029, 032, 043, 044, 045, 047, 048 | — |
| TASK-099 | Execute Staging/Pre-Production Soak Test | W6 | — | — | 026, 027, 029, 032, 043, 044, 045, 047, 048 | — |
| TASK-100 | Execute Production Go-Live | W6 | — | — | 026, 027, 029, 032, 043, 044, 045, 047, 048 | — |
| TASK-101 | Run Post-Launch Hypercare & Stabilization Period | W6 | — | — | 026, 027, 029, 032, 043, 044, 045, 047, 048 | — |

## 7. Open Questions → PTBC map

| OQ | PTBC | Blocking tasks (resolved to IDs) | Decision owner | Basis |
|---|---|---|---|---|
| OQ-001 | PTBC-048 | TASK-005; TASK-014; TASK-015; TASK-016; TASK-017; TASK-018; TASK-019; TASK-020 | AHDA IT / Cybersecurity | OQ-001 names PTBC-048 hosting/residency (14B v1.1 §3); blocking tasks listed by ID in the workbook |
| OQ-002 | PTBC-021; PTBC-022 | TASK-069; TASK-070; TASK-071; TASK-072 | PMO Engagement Lead / AHDA Business Sponsor | Count fixed by 14B v1.1 §6 (38/34); composition and naming stay at PTBC-021/022; "TASK for FG-01/FG-02 backend/frontend" = TASK-069–072 |
| OQ-003 | PTBC-048 | TASK-023 | AHDA IT / Cybersecurity | OQ-003 names PTBC-048; "TASK for backup/restore/DR runbook" = TASK-023 |
| OQ-004 | PTBC-042 | TASK-002; TASK-070 | PMO Engagement Lead | Closed by 14B v1.1 §5.3; the one deferred component (SCR-035 map view) sits at PTBC-042 and is built, if confirmed, by TASK-070 (FG-01 frontend) |
| OQ-005 | PTBC-001; PTBC-009 | TASK-035; TASK-060 | AHDA Business Sponsor / Portfolio Office | OQ-005 names PTBC-001/009; "TASK for WF-11 backend" = TASK-035, "TASK for WF-08 backend" = TASK-060 |
| OQ-006 | PTBC-017; PTBC-024; PTBC-025 | TASK-055; TASK-052 | AHDA Business Sponsor / Risk & Portfolio Office | OQ-006 names PTBC-017/024/025; "TASK for WF-06 backend" = TASK-055, "TASK for WF-14 backend" = TASK-052 |
| OQ-007 | PTBC-031; PTBC-003 | TASK-068; TASK-066; TASK-067 | AHDA IT (Identity) / Business Sponsor | OQ-007 names PTBC-031/003; Nafath = TASK-068, WF-13 backend/frontend = TASK-066/067 |
| OQ-008 | **none** | TASK-089; TASK-102 | AHDA IT / Data Owner | No PTBC theme covers legacy migration (see finding 004-F-003); nearest source TBC is TBC-DOC-018 |
| OQ-009 | **none** | TASK-093 | AHDA Contracts / PMO Engagement Lead | Contractual SLA table has no PTBC theme (see finding 004-F-004); operational thresholds are PTBC-037/046 |
| OQ-010 | PTBC-040; PTBC-043 | TASK-087; TASK-086 | AHDA Business Sponsor / AHDA IT | OQ-010 names PTBC-040/043; accessibility audit = TASK-087, performance/load = TASK-086 |

OQ-008 (legacy migration) and OQ-009 (contractual SLA table) gate values that no PTBC theme covers; the tracker carries them at gate class *Before Production* under the OQ ID (findings 004-F-003 / 004-F-004). ADR-001 ↔ PTBC-048, ADR-006 ↔ PTBC-021/022, ADR-004 ↔ PTBC-034, ADR-005 ↔ PTBC-030, ADR-002 ↔ PTBC-044. ADR-004 and ADR-005 ratify controlled-source positions (CSB-BP2 §15, ICD-17); they do not approve a provider, topology or marking policy, so PTBC-034 and PTBC-030 stay `OPEN`.

## 8. Findings

| Finding | Severity | Observation | Disposition | Owner | Due |
|---|---|---|---|---|---|
| 004-F-001 | IMPORTANT | PTBC-042 (Geospatial/map and advanced visualization) carries 17 source TBCs in the 14B crosswalk; 16 of them are not geospatial — the association follows the word "mapping" (e.g. TBC-PCR-17 GCP architecture/region, TBC-CHG-001 materiality thresholds, TBC-DOC-018 legacy document migration, TBC-NTF-024 event deduplication). 12 of these TBCs have PTBC-042 as their only theme and therefore inherit "May Remain Configurable" as their gate class; only TBC-DSH-008 is genuinely a map requirement. TBC-ISS-004 → PTBC-043 is the same pattern on the word "scale". | Proposed re-association and gate class recorded per TBC in 02_Source_TBC_Register (columns N–P); recorded 14B association stays controlling until confirmed. If confirmed: BEFORE BUILD / SIT 71 → 72; BEFORE UAT 375 → 383; BEFORE PRODUCTION 53 → 55; MAY REMAIN CONFIGURABLE 12 → 1 (05_Gate_Summary). | Requirements governance lead (14B-F-008 owner) | Before the 14B v1.1 §9 F-008 signature |
| 004-F-002 | IMPORTANT | PTBC-008 (Issue/Challenge severity-priority/escalation governance, WF-07) has zero source TBCs in the 14B crosswalk, although TBC-ISS-003 (severity labels), TBC-ISS-004 (priority scale / severity→priority rules) and TBC-ISS-016 (verification waiver by category) are its subject; they were associated with PTBC-018/042/043 instead. | Propose TBC-ISS-003, TBC-ISS-004 and TBC-ISS-016 as PTBC-008 source TBCs (keeping PTBC-018 where recorded); see 02_Source_TBC_Register. | Requirements governance lead | Before the F-008 signature |
| 004-F-003 | IMPORTANT | OQ-008 (legacy project-records source, format, volume, field mapping for migration/cutover) has no PTBC theme. The only related source TBC, TBC-DOC-018 (WF-12 legacy document migration scope), is associated with PTBC-042 and so classed May Remain Configurable. | Track the migration scope under OQ-008 with gate class BEFORE PRODUCTION in this tracker (04_Open_Questions); raise a CSB-14A §19.2 change request for a records-migration theme if the requirements governance lead agrees. No new PTBC ID is created here. | Requirements governance lead / AHDA IT (Data Owner) | Before migration rehearsal (Release Checklist "Data Migration Cutover Rehearsed") |
| 004-F-004 | MINOR | OQ-009 (contractual SLA table for the ~22-month operations period) has no PTBC theme. CSB-14A §19.3 lists "operational SLAs" under Before Production but no §19.2 row carries them; PTBC-037/046 cover operational thresholds and alert authority, not contractual response times. | Track under OQ-009 with gate class BEFORE PRODUCTION (04_Open_Questions); AHDA Contracts confirms the SLA table per 14B v1.1 §5.7. | AHDA Contracts / PMO Engagement Lead | Before Release Checklist "Operational Runbooks & On-Call Ready" |
| 004-F-005 | DOCUMENTATION | The Open Questions sheet names its blocking tasks by description ("TASK for WF-11 backend") rather than by ID for OQ-002 to OQ-010. | IDs resolved in 04_Open_Questions column D; adopt them in the workbook at the next revision. | Workbook owner | Next workbook revision |
| 004-F-006 | DOCUMENTATION | 66 tasks touch a PTBC-gated value by direct or source-family link but do not cite the PTBC ID in their Detailed Description / Acceptance Criteria (only 17 tasks cite any PTBC). 33 DIRECT links (Open Question or ADR based) are uncited, e.g. TASK-002→PTBC-042, TASK-005→PTBC-048, TASK-006→PTBC-044, TASK-014→PTBC-048, TASK-015→PTBC-048, TASK-016→PTBC-048, TASK-017→PTBC-048, TASK-018→PTBC-048. | Insert "Gated values: PTBC-xxx, … (docs/governance/ptbc-tbc-tracker.xlsx)" into each linked task's Detailed Description at the next workbook revision; 03_Task_Links column N marks the rows. | Workbook owner | Next workbook revision |
| 004-F-007 | DOCUMENTATION | PTBC-026 source-family cell reads "FG-03/12/14/06"; FG-12 and FG-14 do not exist (WF-12, WF-14 intended). Already dispositioned as 14B-F-007 in 14B v1.1 §7; carried here so the expanded column is not read as a new interpretation. | Keep the as-recorded cell; the "Source specs (expanded)" column shows WF-12/WF-14. | Document-control owner | With 14B-F-007 |
| 004-F-008 | DOCUMENTATION | CSB-15 11_TBC_PTBC_Gates and CSB-17 Governance_Values cite the mapping basis as "14A §15 PTBC"; the register is CSB-14A §19.2 (§15 is a different section). | Cite CSB-14A §19.2 at the next Step 15/17 re-issue. | Step 15 / Step 17 authors | Next re-issue |

004-F-001 detail — proposed re-associations (recorded association stays controlling):

| Source TBC | Recorded PTBC | Recorded gate class | Proposed PTBC | Proposed gate class | Why |
|---|---|---|---|---|---|
| TBC-RPT-02 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-022 | BEFORE UAT | Report screen mapping within SCR-130–140 is report-catalogue governance, not geospatial |
| TBC-IAM-003 | PTBC-036; PTBC-042 | BEFORE BUILD / SIT | PTBC-036 | BEFORE BUILD / SIT | Directory group→role mapping is already PTBC-036; drop PTBC-042 |
| TBC-IAM-019 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-027 | BEFORE PRODUCTION | Where role-permission mappings are administered is an admin-model decision (PTBC-027) or an FG-03/FG-04 boundary ICD; not geospatial |
| TBC-CFG-005 | PTBC-017; PTBC-042 | BEFORE UAT | PTBC-017 | BEFORE UAT | 5×5 risk matrix cell mapping is already PTBC-017; drop PTBC-042 |
| TBC-PCR-16 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-020 | BEFORE UAT | Registration notification recipients are notification configuration (PTBC-020) |
| TBC-PCR-17 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-048 | BEFORE BUILD / SIT | GCP architecture/services/region is the hosting decision (PTBC-048, ADR-001, OQ-001); must resolve before environment provisioning, not "configurable" |
| TBC-RSK-004 | PTBC-017; PTBC-042 | BEFORE UAT | PTBC-017 | BEFORE UAT | 5×5 risk matrix cell→rating mapping is already PTBC-017; drop PTBC-042 |
| TBC-ISS-003 | PTBC-018; PTBC-042 | BEFORE UAT | PTBC-008 | BEFORE UAT | Severity labels/colours are PTBC-008 (severity-priority governance) with PTBC-018; not geospatial |
| TBC-ISS-016 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-008 | BEFORE UAT | Waiving independent verification for low-governance categories is WF-07 governance (PTBC-008) |
| TBC-CHG-001 | PTBC-009; PTBC-042 | BEFORE UAT | PTBC-009 | BEFORE UAT | Materiality thresholds are already PTBC-009; drop PTBC-042 |
| TBC-CHG-009 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-009 | BEFORE UAT | Controlled Commitment catalogue is change-control governance (PTBC-009) |
| TBC-DOC-018 | PTBC-042 | MAY REMAIN CONFIGURABLE | (none — OQ-008) | BEFORE PRODUCTION | Legacy document migration scope has no PTBC theme; tracked by OQ-008 / TASK-089 / TASK-102 (finding 004-F-003) |
| TBC-EXT-011 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-003 | BEFORE UAT | Contribution field schemas per domain/type are external-participation configuration (PTBC-003) |
| TBC-EXT-026 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-003 | BEFORE UAT | Source-application adapter mapping per contribution type is WF-13 governance (PTBC-003) |
| PERF-TBC-029 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-033 | BEFORE BUILD / SIT | Integration API/data contracts once source systems are selected is PTBC-033 |
| TBC-NTF-024 | PTBC-042 | MAY REMAIN CONFIGURABLE | PTBC-020 | BEFORE UAT | Event-family deduplication between WF-11 and source domains is notification configuration (PTBC-020) |
| TBC-ISS-004 | PTBC-018; PTBC-043 | BEFORE BUILD / SIT | PTBC-008 | BEFORE UAT | Priority scale labels/severity→priority rules are PTBC-008 with PTBC-018; the PTBC-043 link is the word "scale", not performance |

## 9. TASK-004 acceptance-criteria check

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Tracker contains all 48 PTBC rows with category, source spec, resolution gate and current status | PASS | `01_PTBC_Register`: 48 rows, columns B–G and L; §4 above |
| 2 | Every task in this workbook that touches a PTBC-gated value (see Open Questions sheet) links back to the corresponding PTBC row by ID | PASS in the tracker — 94 tasks linked by ID in `03_Task_Links` (66 DIRECT/SPEC, 28 package-inherited only); all 10 Open Questions resolved to task IDs and PTBC IDs (§7). **PARTIAL in the workbook** — only 13 tasks cite a PTBC ID in their own text (finding 004-F-006) | `03_Task_Links` column N; `04_Open_Questions` |
| V1 | Validation note: spot-check 10 PTBC rows against Blueprint Appendix F.2 for exact wording | PASS — exceeded | All 48 rows compared against CSB-BP2 App. F.2 and CSB-14A §19.2: 0 differences (§2) |
| V2 | Validation note: no row has an invented value in the "selected" field before a gate gives AHDA the chance to approve it | PASS | "Approved value / decision reference", "Approved by", "Approval date" are empty on all 48 rows and all 511 TBC rows; asserted by the generator. Working baselines are quarantined in their own column |

## 10. Acceptance

This tracker becomes the controlled governance register when the first row below is signed. No AHDA approval of any value is claimed or implied; signatures here accept the *register*, not the values.

| Role | Accepts | Name | Date |
|---|---|---|---|
| Requirements governance lead (14B-F-008 owner) | The tracker as the single PTBC/TBC governance register; disposition of 004-F-001 and 004-F-002 (confirm or reject each proposed re-association) |  |  |
| PMO Engagement Lead / workbook owner | Task-link register (§6) and adoption of PTBC IDs and task IDs in the workbook (004-F-005, 004-F-006) |  |  |
| Engagement Architect | Gate rule (§3) as a Definition-of-Ready condition for every build task |  |  |

## 11. Open items

| # | Item | Owner | Gate |
|---|---|---|---|
| 1 | 48 PTBC values and 511 source TBCs are OPEN; earliest due are the 7 Before Build / SIT themes (PTBC-032–036, 038, 043) and PTBC-048 hosting (ADR-001, OQ-001), which blocks Phase P3 | AHDA functions per `01_PTBC_Register` column Q | Per row |
| 2 | 004-F-001 / 004-F-002 association review (17 source TBCs) | Requirements governance lead | Before the 14B v1.1 §9 F-008 signature |
| 3 | Legacy migration (OQ-008) and contractual SLA (OQ-009) values have no PTBC theme | Requirements governance lead / AHDA Contracts | Before Production |
| 4 | Workbook does not yet cite PTBC IDs on 66 linked tasks and names OQ blocking tasks by description | Workbook owner | Next workbook revision |
| 5 | 14B v1.1 is awaiting 0 of 8 signatures; the counts this tracker reproduces (511 → 48; 71/375/53/12) become QA-closed only with that signature | PMO | 14B v1.1 §9 |

## 12. Maintenance

- The xlsx is generated from the controlled sources and the workbook; the "as recorded" columns must never be hand-edited. Status, approval and resolution columns are hand-maintained.
- Edit only on a `chore/task-004-*` branch; re-issue the Tracker status line in `00_Control` and in the control table above whenever a status changes.
- When CSB-14A §19.2, CSB-14B-RTM or the workbook is re-issued, regenerate the "as recorded" and link columns and re-run the three checks in §2 before merging.
