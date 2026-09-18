# Controlled Source Baseline

| Control | Value |
|---|---|
| Task | TASK-001 — Establish Controlled Source Baseline (Phase P0 — Discovery & Governance) |
| Programme | AHDA Regional Project Management Platform (RPMO) |
| Baseline date | 2026-09-18 |
| Register status | ISSUED — see §6 for open items |
| Source archive | `Project Files.zip` (archived 2026-09-16); all locations below are relative to its `Project Files/` root |
| Owner | Engagement Architect / PMO |

## 1. Purpose and how to cite this baseline

This register is the single reference for **which documents govern delivery, in which order, and at which version**. It is the file TASK-001's acceptance criteria require every later task to cite.

Every later task's Detailed Description must contain the sentence:

> Sources and precedence per TASK-001 (`docs/baseline/controlled-source-baseline.md`).

A task that needs a specific rule cites the governing document by its register ID (§3), e.g. `CSB-WF-11 §7.2`. Nothing outside §3 may be cited as authoritative for functional behaviour.

## 2. Authority order

When two sources disagree, the higher-ranked source wins. Conflicts are resolved by this precedence and controlled change, never by implementing both readings.

| Rank | Source | Authoritative for | Stated in |
|---|---|---|---|
| 1 | Latest controlled WF/FG specification (WF-01–WF-15, FG-01–FG-06) | Domain business behaviour, entities, controls, source-owned APIs/events, user stories, acceptance criteria, TBCs | Blueprint v2.0 §1, §2 and §24; Step 14A §1 (precedence row 1) |
| 2 | Step 14A Platform Functional Integration & Reconciliation Review v1.0 (QA CLOSED) | Cross-domain ownership, integration decisions ICD-01–ICD-20, numbering reconciliation, screen additions, platform-level conflict resolution | Step 14A §1 (row 2); Blueprint v2.0 §24 |
| 3 | Functional Blueprint v2.0 (QA CLOSED) | Integrated platform summary: roles, navigation, canonical screen/component inventory (242 entries), lifecycles, PTBC register; must not override a rank-1 rule | Blueprint v2.0 §2, §24, §25 |
| 4 | Project Scope | Contractual requirement breadth and context; requirements authority within its own domain only | Blueprint v2.0 §24; Step 14A §1 (row 4), §25 |

Rules that follow from the order:

- Blueprint v2.0 "is the integrated platform summary and must not be used to override a controlled source-domain rule" (Blueprint v2.0 §1).
- Workflow numbering is the controlled WF-01–WF-15 sequence. Blueprint v1.0's legacy sequence (WF-02 Activation … WF-16 Notifications) is superseded (Step 14A §3; Blueprint v2.0 §25 gate M).
- Unresolved AHDA values (thresholds, SLAs, retention, providers, formulas) stay PTBC / source TBC; they are not invented downstream (Step 14A governance rule; Blueprint v2.0 Appendix F).
- The PM Platform Development & Cybersecurity Guide and AHDA cybersecurity policies are governance authorities inside their own domain (Step 14A §1 row 4). They do not rank above a WF/FG spec for functional behaviour and are listed in §3.3, not §3.1.

## 3. Baseline register

Column meanings: **Self-declared status** is copied from the document's own control table. **QA status** is this register's classification: `CLOSED` (explicit QA-closed marker in the document), `DEV-READY` (development-ready baseline with no standalone QA marker; reviewed and reconciled by Step 14A, whose DoD 14A-DOD-01 confirms all 21 specs in the authoritative register), `PENDING`, or `SUPERSEDED`. **SHA-256** is the first 16 hex characters of the file digest at baseline date; a different digest means the file has changed and this register must be re-issued.

### 3.1 Governing documents (ranks 1–4)

| ID | Document | Version | Self-declared status | QA status | Location (relative to `Project Files/`) | SHA-256 |
|---|---|---|---|---|---|---|
| CSB-BP2 | Functional Blueprint v2.0 | 2.0 | QA CLOSED — CONTROLLED PLATFORM BASELINE | CLOSED | `Functional Blueprint/Project_Management_Platform_Functional_Blueprint_v2.0_QA_CLOSED.docx` | `cb2b4675e3509160` |
| CSB-14A | Step 14A Platform Functional Integration & Reconciliation Review | 1.0 | INTEGRATION-READY — Controlled Reconciliation Baseline; 0 unresolved blocking findings | CLOSED | `Functional Blueprint/Project_Management_Platform_Platform_Functional_Integration_Reconciliation_Review_v1.0_QA_CLOSED.docx` | `e0a9c11e3c7c0dc1` |
| CSB-WF-01 | WF-01 Project Creation & Registration | 1.0 | Development-Ready Functional Baseline | DEV-READY | `P1 — Project Establsihment/Project_Management_Platform_WF-01_Project_Creation_Registration_Functional_Specification_v1.0.docx` | `b2c707d34abfd974` |
| CSB-WF-02 | WF-02 Project Progress Update | 1.0 | Development-Ready Functional Baseline | DEV-READY | `P2 — Project Execution and Performace/Project_Management_Platform_WF-02_Project_Progress_Update_Functional_Specification_v1.0.docx` | `423075069ef8ac31` |
| CSB-WF-03 | WF-03 Schedule & Baseline Management | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P2 — Project Execution and Performace/Project_Management_Platform_WF-03_Schedule_Baseline_Management_Functional_Specification_v1.0.docx` | `3070f0ea517f775d` |
| CSB-WF-04 | WF-04 Task Management | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P2 — Project Execution and Performace/Project_Management_Platform_WF-04_Task_Management_Functional_Specification_v1.0.docx` | `edfddfb9c99a2b76` |
| CSB-WF-05 | WF-05 Milestone Management | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P2 — Project Execution and Performace/Project_Management_Platform_WF-05_Milestone_Management_Functional_Specification_v1.0.docx` | `de1bcc197ac43dc4` |
| CSB-WF-06 | WF-06 Risk Management | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P3 — Risk, Issue, and Challenge Control/Project_Management_Platform_WF-06_Risk_Management_Functional_Specification_v1.0.docx` | `31d86a98619d3318` |
| CSB-WF-07 | WF-07 Issue & Challenge Management | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P3 — Risk, Issue, and Challenge Control/Project_Management_Platform_WF-07_Issue_Challenge_Management_Functional_Specification_v1.0.docx` | `169a5a8f5488c979` |
| CSB-WF-08 | WF-08 Project Change Request | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P4 — Project Governance & Change Control/Project_Management_Platform_WF-08_Project_Change_Request_Functional_Specification_v1.0.docx` | `07ae2f0d3a36d4e7` |
| CSB-WF-09 | WF-09 Project Suspension & Resumption | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P4 — Project Governance & Change Control/Project_Management_Platform_WF-09_Project_Suspension_Resumption_Functional_Specification_v1.0.docx` | `66279f59a1fb3f43` |
| CSB-WF-10 | WF-10 Project Completion & Closure | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P4 — Project Governance & Change Control/Project_Management_Platform_WF-10_Project_Completion_Closure_Functional_Specification_v1.0.docx` | `9d2dee987d6e6b2e` |
| CSB-WF-11 | WF-11 Shared Approval Framework | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P4 — Project Governance & Change Control/Project_Management_Platform_WF-11_Shared_Approval_Framework_Functional_Specification_v1.0.docx` | `7e005a8df59d0336` |
| CSB-WF-12 | WF-12 Document Management | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P5 — Collaboration & Records/Project_Management_Platform_WF-12_Document_Management_Functional_Specification_v1.0.docx` | `16272134ffd9d8be` |
| CSB-WF-13 | WF-13 External Entity Update & Review | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P5 — Collaboration & Records/Project_Management_Platform_WF-13_External_Entity_Update_Review_Functional_Specification_v1.0.docx` | `656dc549a5d0cf72` |
| CSB-WF-14 | WF-14 KPI & Financial Progress | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P2 — Project Execution and Performace/Project_Management_Platform_WF-14_KPI_Financial_Progress_Functional_Specification_v1.0.docx` | `f8cc14615deb766a` |
| CSB-WF-15 | WF-15 Notifications, Reminders & Escalations | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P6 — Shared Communications & Escalation/Project_Management_Platform_WF-15_Notifications_Reminders_Escalations_Functional_Specification_v1.0.docx` | `7360e9464d8f1676` |
| CSB-FG-01 | FG-01 Dashboards | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P7 — Management Intelligence/Project_Management_Platform_FG-01_Dashboards_Functional_Specification_v1.0.docx` | `b76c186124242558` |
| CSB-FG-02 | FG-02 Reports, Filters & Export | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P7 — Management Intelligence/Project_Management_Platform_FG-02_Reports_Filters_Export_Functional_Specification_v1.0.docx` | `78723a586bc07382` |
| CSB-FG-03 | FG-03 Users, Roles & Permissions | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P8 — Platform Administration/Project_Management_Platform_FG-03_Users_Roles_Permissions_Functional_Specification_v1.0.docx` | `20fd78f766b3ce42` |
| CSB-FG-04 | FG-04 Master Data & Configuration | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P8 — Platform Administration/Project_Management_Platform_FG-04_Master_Data_Configuration_Functional_Specification_v1.0.docx` | `51f8eecc5e377213` |
| CSB-FG-05 | FG-05 Integration Monitoring | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0; contains a Document QA section | CLOSED | `P9 — Technical Operations & Governance/FG-05_Integration_Monitoring_Functional_Specification_v1.0_QA_Closed.docx` | `88ec7d2fa431b4e9` |
| CSB-FG-06 | FG-06 Audit & Activity | 1.0 | DEVELOPMENT-READY — Functional Baseline v1.0 | DEV-READY | `P9 — Technical Operations & Governance/Project_Management_Platform_FG-06_Audit_Activity_Functional_Specification_v1.0.docx` | `eb9a4a0f1513b74b` |
| CSB-SCOPE | Client Original Project Scope (Arabic; no version or date field) | — | Client-issued RFP scope | PENDING — the "adjusted" scope named in TASK-001 is not on file; see §6 item 1 | `Relevant Folders/Client Original Project Scope.docx` | `98d7a1eced0efb6f` |

Count: 2 platform documents + 21 WF/FG specifications + 1 scope = **24 governing documents**.

### 3.2 Superseded — do not cite as authoritative

| ID | Document | Version | Status | Location | SHA-256 |
|---|---|---|---|---|---|
| CSB-BP1 | Functional Blueprint v1.0 | 1.0 | SUPERSEDED by CSB-BP2 (Blueprint v2.0 cover, §24, §25 gate M). Retained as historical baseline only; its workflow numbering is obsolete. | `Functional Blueprint/Project_Management_Platform_Functional_Blueprint_v1.0.docx` | `68b8abaf849a502b` |

Any reference to "Blueprint v1.0", "the Blueprint" without a version, or the legacy WF-02 Activation … WF-16 Notifications numbering is a defect and must be corrected to CSB-BP2 or the governing WF/FG spec.

### 3.3 Domain governance inputs (authoritative within their own domain only)

| ID | Document | Version | Status | Role | Location | SHA-256 |
|---|---|---|---|---|---|---|
| CSB-CYBER-GUIDE | PM Platform Development & Cybersecurity Implementation Guide | unversioned | As supplied | Architecture, secure-SDLC, IAM, audit/logging, backup/DR baseline (Step 14A §25) | `Relevant Folders/PM_Platform_Development_and_Cybersecurity_Guide.docx` | `81b725edf83635c7` |
| CSB-CYBER-POLICIES | AHDA Cybersecurity Policy set CS-001-2025 … CS-033-2025 (33 PDFs, Arabic) | 2025 | As supplied | Applied through the guide and spec controls; implementation subject to AHDA cybersecurity governance | `Relevant Folders/Cyber Policies/` | not individually hashed |
| CSB-MASTER-PLAN | AHDA Master Plan | unversioned | Contextual | Strategic reference only; does not override functional ownership (Step 14A §25) | `Relevant Folders/AHDA Master Plan.xlsx` | `fd8385c2cd3fbd37` |

### 3.4 Downstream baselines (derived from §3.1; not authoritative over it)

Listed so later tasks cite the right version. None is QA closed. Where one of these conflicts with §3.1, §3.1 wins.

| ID | Document | Version | Self-declared status | QA status | Location | SHA-256 |
|---|---|---|---|---|---|---|
| CSB-14B | Step 14B Requirements Traceability Assessment | 1.0 | CONDITIONALLY READY for Step 15; 7 Important + 1 documentation findings open | PENDING | `RTM/Project_Management_Platform_Step_14B_Assessment_v1.0.docx` | `217b4b7ac5ec766b` |
| CSB-14B-RTM | Step 14B Requirements Traceability Matrix (19,533 rows; 210 of 242 canonical components linked) | 1.0 | Issued with open findings | PENDING | `RTM/Project_Management_Platform_Step_14B_RTM_v1.0.xlsx` (+ `Part_1`–`Part_4` splits) | `d6cf3428a81220d3` |
| CSB-15 | Step 15 Build Prioritization (DOCX + XLSX) | 1.0 | SUBSTANTIVELY COMPLETE — PENDING QA CLOSURE | PENDING | `Prioritization/Project_Management_Platform_Step_15_Build_Prioritization_v1.0.docx` / `.xlsx` | `3f148a2d86b6b9f9` / `aebc88944ca41a14` |
| CSB-16 | Step 16 Frontend Package + Registers | 1.0 | HANDOFF ISSUED WITH OPEN CONTRACT GATES — NOT QA CLOSED | PENDING | `Front End Package/Project_Management_Platform_Step_16_Frontend_Package_v1.0.docx` / `..._Registers_v1.0.xlsx` | `036b745ded8c76ce` / `bb915aded6d4d001` |
| CSB-17 | Step 17 Backend Package + Registers | 1.0 | ISSUED WITH OPEN CONTRACT GATES — NOT QA CLOSED | PENDING | `Back End Package/Project_Management_Platform_Step_17_Backend_Package_v1.0.docx` / `..._Registers_v1.0.xlsx` | `d1a512e03517943c` / `3a4989e73ef397c5` |
| CSB-18 | Step 18 UAT Catalogue (DOCX + XLSX) | 1.0 | DRAFT UAT CATALOGUE — OPEN ACCEPTANCE GATES | PENDING | `UAT Catalogue/Project_Management_Platform_Step_18_UAT_Catalogue_v1.0.docx` / `.xlsx` | `d7a0cea6d64ef88a` / `7abddbffae510fc5` |

Not baselined (working notes, no controlling role): `Relevant Folders/Process Architecture .docx`, `Relevant Folders/Designing and preparing Steps.xlsx`.

## 4. Acceptance-criteria check (TASK-001)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Register lists every controlled document with version, QA status and file location | PASS | §3.1–§3.4; 24 governing + 1 superseded + 3 domain inputs + 6 downstream |
| 2 | Authority order is written down and referenced by TASK id from every later task's Detailed Description | PARTIAL — written down (§2); **0 of 101** later tasks (TASK-002…TASK-102) currently cite TASK-001 | Scan of `AHDA_RPMO_Platform_Implementation_Plan.xlsx`, sheet *Implementation Plan*, column G, 2026-09-18. Action: insert the §1 sentence into each Detailed Description at the next workbook revision |
| 3 | No task cites Blueprint v1.0 as authoritative | PASS | Same scan across columns C/G/H/M of all 102 tasks plus sheets *Architecture Decisions*, *Release Checklist*, *Open Questions*: no citation of Blueprint v1.0. ADR-004 and ADR-005 cite v2.0 explicitly. ADR-006, OQ-002 ("Blueprint Appendix B") and the Release Checklist penetration-test gate ("Blueprint Section 22.1") omit the version; both locators exist only in v2.0 (Appendix B = 242-entry inventory; §22.1 Engineering invariants) so they resolve correctly — add "v2.0" at the next workbook revision to remove the ambiguity |

Workbook validation note ("cross-check the 33 WF/FG + Blueprint + Step 14A file count against the RTM's stated 242 canonical components"): the governing file count is 21 + 1 + 1 = **23**, not 33. The number 33 matches Blueprint v2.0 Appendix D (33-row ownership register), not a document count. The 242 canonical components are confirmed in Blueprint v2.0 Appendix B (233 Blueprint v1.0 entries + SCR-160–SCR-167 + MOD-019, per Step 14A §6) and in the Step 14B Assessment (210 of 242 linked). The two figures measure different things and are not expected to reconcile to each other.

## 5. Change control for this register

1. A governing document changes version → the new file is added to §3.1 with its digest, the prior row moves to §3.2, and the register's baseline date is updated. Domain detail changes go to the WF/FG spec first; platform structure changes go to Blueprint v2.x (Blueprint v2.0 §24 change-control rule).
2. A file's digest differs from §3 → treat the file as uncontrolled until the change is reviewed and this register re-issued.
3. This file is edited only on a branch named `chore/task-001-*` and reviewed by the register owner.

## 6. Open items

| # | Item | Impact | Owner | Linked |
|---|---|---|---|---|
| 1 | **Adjusted Project Scope is not on file.** TASK-001 names an "adjusted Project Scope"; the only scope document is the client's original RFP scope. Step 14B finding 14B-F-001 ("Confirm the applicable adjusted scope") is still open. | Rank-4 authority is provisional; scope-coverage findings in TASK-002 cannot close until the adjusted scope is supplied and registered here | PMO / AHDA | TASK-002, 14B-F-001, OQ-002 |
| 2 | 101 later tasks do not yet cite TASK-001 (§4 row 2). | Acceptance criterion 2 unmet on the workbook side | Workbook owner | TASK-002…TASK-102 |
| 3 | 20 of 21 WF/FG specs carry no standalone QA-closed marker; closure is evidenced through Step 14A (14A-DOD-01 PASS) and Blueprint v2.0 Appendix E. FG-05 is the only spec with an explicit QA section and its filename deviates from the naming pattern (`FG-05_…_QA_Closed.docx`, no `Project_Management_Platform_` prefix). | Auditors reading a spec in isolation will see DEVELOPMENT-READY, not QA CLOSED | Engagement Architect | — |
| 4 | Controlled documents live only in `~/Downloads/Project Files.zip`, outside version control. | Digest drift cannot be detected automatically | PMO / DevOps | Recommend committing the 24 governing files (≈3.5 MB) under `docs/baseline/sources/` or registering a document-store URL per row |
| 5 | Three unversioned "Blueprint" references in the workbook (ADR-006, OQ-002, Release Checklist). | Low — they resolve to v2.0, but violate the citation rule in §3.2 | Workbook owner | §4 row 3 |
| 6 | Blueprint v1.0 remains in the same folder as v2.0. | Risk of accidental citation | PMO | Move to an `Archive/` subfolder at next archive refresh |
