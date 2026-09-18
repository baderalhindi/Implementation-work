# Step 14B Requirements Traceability Assessment — v1.1 (Findings Closure)

| Control | Value |
|---|---|
| Task | TASK-002 — Close Step 14B RTM Findings (Phase P0 — Discovery & Governance); depends on TASK-001 |
| Programme | AHDA Regional Project Management Platform (RPMO) |
| Supersedes | Step 14B Assessment v1.0, issued 13 September 2026 (CSB-14B, digest `217b4b7ac5ec766b`) with RTM v1.0 (CSB-14B-RTM, digest `d6cf3428a81220d3`). Both digests re-verified 2026-09-18 against the TASK-001 register. |
| Issue date | 2026-09-18 |
| Assessment status | **DISPOSITIONED — AWAITING AHDA SIGN-OFF (0 of 8 signatures recorded).** Becomes **QA CLOSED** when every row of §9 carries a signature; see §2. |
| Owner | Engagement Architect / PMO |

Sources and precedence per TASK-001 (`docs/baseline/controlled-source-baseline.md`). Documents are cited by their `CSB-*` register ID. Nothing in this assessment invents an AHDA value; where a value is still open it is deferred to a named PTBC gate.

## 1. Purpose

Step 14B v1.0 closed with seven IMPORTANT findings and one documentation finding open and a status of CONDITIONALLY READY. This revision records, for each of the eight findings:

1. the evidence examined in the controlled sources (§3–§8),
2. the disposition — the decision text that goes into the RTM,
3. the exact RTM records that change,
4. the accountable AHDA function that signs it (§9), and
5. what remains gated after signature.

It also fixes the dashboard/report count that TASK-069–TASK-072 (FG-01/FG-02 build tasks) and ADR-006 consume (§6). The workbook calls these "TASK-062+"; the FG-01/FG-02 tasks are TASK-069, 070, 071 and 072.

## 2. Status rule

The RTM status moves from CONDITIONALLY READY to QA CLOSED only on evidence, never by editing the status cell:

| Condition | Position at 2026-09-18 |
|---|---|
| All 8 findings have a written disposition with evidence | MET — §3–§8 |
| Each disposition names one accountable AHDA/PMO signatory and the exact statement they sign | MET — §9 |
| Every signatory has signed | NOT MET — 0 of 8 |
| RTM workbook v1.1 reissued with the cell changes in §10.1 | NOT MET — document-control action after signature |

Dispositions fall into two kinds, and the distinction matters for what AHDA is being asked to sign:

- **PRECEDENCE** — the answer already follows from the TASK-001 authority order (rank-1 WF/FG spec > rank-2 Step 14A > rank-3 Blueprint v2.0 > rank-4 Scope). AHDA signs to *acknowledge* the controlled outcome, not to choose it. F-001 (in part), F-003 (26 of 32), F-004, F-005, F-007, F-008.
- **DECISION** — no controlled source carries the value; AHDA chooses. F-001 (which scope is "adjusted"), F-002 (catalogue quantity acceptance; backup retention), F-003 (6 of 32), F-006.

## 3. Re-validation of the v1.0 coverage measures

Recomputed on 2026-09-18 from the four RTM part workbooks and the supporting-register workbook (TASK-002 validation note).

| Measure | v1.0 stated | Recomputed | Result |
|---|---|---|---|
| Master RTM rows | 19,533 | 19,533 (Parts 1–4, unique `RTM-*` IDs) | PASS |
| Fully traced | 14,682 (75.2%) | 14,682 = 75.16% | PASS |
| Traced — TBC dependent | 774 | 774 | PASS |
| Partially traced | 4,060 | 4,060 | PASS |
| Untraced | 7 | 7 — all carry 14B-F-006 | PASS |
| Deferred / out of MVP | 10 | 10 (RTM-1214, 14239–14241, 17911, 18972–18976) | PASS |
| Rows carrying a finding ID | — | F-001: 4 · F-002: 3 · F-004: 3,878 · F-005: 175 · F-006: 7 · F-003/F-007/F-008: register-level, no row IDs | Consistent with `10_Findings` |
| Canonical components with behaviour links | 210 of 242 | 210; 32 rows flagged `INVENTORY ONLY — BEHAVIOR GAP` in `04_Screen_Traceability` | PASS |
| Source TBC IDs / PTBC themes | 511 / 48 | 511 / 48; every source TBC has ≥1 PTBC theme | PASS — see §8 for gate normalisation |
| Compressed WF/FG shorthand that parses to a nonexistent ID | "for example PTBC-026 and EVT-002" | 5 distinct rows (§7) | Enumerated |

## 4. Disposition register (summary)

| Finding | Class | Kind | Disposition in one line | Signatory | Residual gate after signature |
|---|---|---|---|---|---|
| 14B-F-001 | IMPORTANT | PRECEDENCE + DECISION | CSB-SCOPE is registered as the scope of record; its Word-export, internal-hosting and "one time thing" wording is overridden by ICD-17, PTBC-048 and ICD-15 respectively. AHDA confirms no other "adjusted" scope exists. | AHDA scope owner / PMO | Hosting value at PTBC-048 (Before Production) |
| 14B-F-002 | IMPORTANT | DECISION | Output catalogue = 38 governed definitions (12 dashboards + 26 reports), 34 MVP-committed; sequencing normalised by TASK-003; backup tiers daily/weekly/monthly are a design requirement, values at PTBC-048. | AHDA Business Sponsor (quantities); AHDA IT/Cybersecurity (backup) | Retention/RPO/RTO values at PTBC-048 (Before Production) |
| 14B-F-003 | IMPORTANT | PRECEDENCE (26) + DECISION (6) | Each of the 32 components is assigned an owner and a behaviour source (§5.3 table); 26 link to existing spec behaviour; 3 are composed views; 1 is deferred under PTBC-042; 2 get a common-UI owner with a contract to write. | Functional architect (26 + 3 + 2); AHDA Business Sponsor (SCR-035) | Before affected UI build, per component |
| 14B-F-004 | IMPORTANT | PRECEDENCE | The 3,878 stories keep PARTIALLY TRACED; the join is made per story at Definition of Ready using the Step 16/17/18 registers; closure evidence is the story's bound UAT scenario. | WF/FG functional owners / solution architect | Before each story enters build |
| 14B-F-005 | IMPORTANT | PRECEDENCE | The 175 scope clauses are reconciled by the TASK-001 order: the design evidence already selected is the acceptance contract; a clause with no controlled evidence is a scope gap, not a design gap. | Business analyst / AHDA scope owner | Before source baseline freeze |
| 14B-F-006 | IMPORTANT | DECISION | The 7 delivery/service clauses leave the functional RTM and are traced to workbook tasks that own their acceptance criteria (§5.6 table). | Delivery manager / service transition lead | Per work package |
| 14B-F-007 | DOCUMENTATION | PRECEDENCE | Five compressed references are expanded explicitly (§7); no FG-12/14/15 exists; all resolve to WF-12/WF-14/WF-15. | Document-control owner | None |
| 14B-F-008 | IMPORTANT | PRECEDENCE | Crosswalk confirmed: 511/511 source TBCs map to a PTBC and therefore to one of the four 14A §19.3 gate classes; 106 TBCs with no RTM row and 4 PTBCs with zero rows are recorded as analytical gaps, not governance gaps. | Requirements governance lead | Values at each PTBC gate |

## 5. Dispositions

### 5.1 14B-F-001 — Adjusted scope and editorial wording

**Finding (v1.0).** Supplied scope is not identified as the adjusted controlled version and retains Word export, internal-hosting wording and audit editorial text. Affected: RTM-19421, RTM-19462, RTM-19468, RTM-19469.

**Evidence examined.**

| Item | Source | What it says |
|---|---|---|
| Scope on file | CSB-SCOPE `Relevant Folders/Client Original Project Scope.docx`, digest `98d7a1eced0efb6f` | Titled "ملخص نطاق العمل التقني" — a *summary* of the RFP, Arabic, no version/date field. No other scope document exists in the archive (TASK-001 §6 item 1). |
| Word export (¶95) | CSB-SCOPE ¶93–97 lists Excel, Word, PDF "and any other agreed formats" | CSB-14A §22 ICD-17 (FINAL): "FG-02 baseline exports are PDF/XLSX/CSV; DOCX export is not a committed baseline capability." CSB-FG-02 §9.1: "Other — Deferred". ADR-005 already ratifies this. |
| Internal hosting (¶145) | CSB-SCOPE ¶145 "استضافة النظام في البيئة الداخلية للهيئة"; ¶156 data localisation in KSA | CSB-14A §19.2 PTBC-048 (Before Production): "AHDA-approved KSA/hosting architecture and recovery targets." CSB-BP2 §22. ADR-001 and OQ-001 hold the same decision open. |
| Audit "one time thing" (¶151–152) | CSB-SCOPE ¶151 "تسجيل جميع العمليات والتغييرات Audit Trail.one time thing", ¶152 "تفعيل سجلات التدقيق Audit Logs one time thing." | CSB-14A ICD-15 (FINAL): formal Audit is immutable, continuous evidence. CSB-FG-06 BR-AUD-010/012/036/042. The phrase is an editorial note in the RFP summary, not a requirement. |

**Disposition.**

1. CSB-SCOPE is the applicable scope of record for this programme. The word "adjusted" in TASK-001/TASK-002 is satisfied by CSB-SCOPE *as reconciled by the rank-1–3 sources*; there is no separate adjusted scope document. AHDA confirms this by signature (§9). If AHDA holds a later contractual scope or change record, it is supplied, hashed, and added to the TASK-001 register before signature.
2. RTM-19421 (Word): acceptance contract = ICD-17. Status → TRACED — TBC DEPENDENT (ICD-17 is "FINAL / future TBC if requested"). Final Disposition → "DOCX excluded from baseline per ICD-17; reopen only by AHDA change record."
3. RTM-19462 (hosting): acceptance contract = PTBC-048. Status → TRACED — TBC DEPENDENT, gate Before Production. No provider or product is chosen here.
4. RTM-19468 / RTM-19469 (audit): acceptance contract = ICD-15 + BR-AUD controls already cited. Status → FULLY TRACED. Comments → "'one time thing' is RFP-summary editorial text; continuous durable audit governs."

**Residual after signature.** Hosting/residency value (PTBC-048, ADR-001, OQ-001) — Before Production.

### 5.2 14B-F-002 — Dashboard/report quantities, sequencing, backup schedule and retention

**Finding (v1.0).** Scope explicitly calls for clarification of dashboard/report quantities and implementation sequencing; backup frequencies/retention need the approved governing schedule. Affected: RTM-19531, RTM-19532, RTM-19477.

#### 5.2.1 Dashboard and report quantities (RTM-19531)

**Evidence examined.**

| Figure | Where it comes from | Standing |
|---|---|---|
| "3 dashboards and 10 reports" | CSB-SCOPE ¶228 — an RFP clarification note: "One section specifies 3 dashboards and 10 reports, while the BoQ separately references 24 dashboard/report outputs." The underlying RFP section is **not** in the scope summary; ¶79–92 lists 13 *example* report/dashboard topics "على سبيل المثال". | Rank 4, and not itself a requirement — a note asking for clarification. |
| "24 outputs" | The BoQ. **Not on file** in the controlled archive. | Commercial quantity; cannot be traced. |
| 12 dashboards | CSB-FG-01 §1 control table "Canonical Dashboard Inventory" and §5: DSH-001–DSH-012 (11 MVP; DSH-008 "Conditional/MVP when R08 enabled") plus ADM-036 Dashboard Configuration. DSH-009 renders inside SCR-040 (no separate page); DSH-001 is the ADM-001 landing content. | Rank 1. |
| 26 report definitions | CSB-FG-02 §5.1 "Recommended Standard Report Catalogue": 26 `RPT-*` rows — 23 MVP, RPT-EXT-001 "MVP when R08 enabled", RPT-EXC-001 and RPT-AUD-001 Conditional. FG-02 states the catalogue "is a design-ready baseline, not a confirmed final AHDA report catalogue. Final inclusion, naming, audience and publication are Configuration/TBC under ADM-037." | Rank 1, with the final list explicitly TBC (PTBC-022, Before report UAT). |
| 11 report screens | CSB-BP2 Appendix B / CSB-FG-02 §5.2: SCR-130–SCR-140 + MOD-060–062 + ADM-037. These are *screens that host reports*, not reports. OQ-002 and ADR-006 option (C) count these; they must not be added to the report count. | Rank 3, screen inventory. |

**Disposition.**

> The controlled output catalogue is **38 governed definitions: 12 dashboards (DSH-001–DSH-012) and 26 report definitions (FG-02 §5.1 RPT catalogue)**. Of these, **34 are MVP-committed (11 dashboards + 23 reports)**; the remaining 4 are conditional and named: DSH-008 and RPT-EXT-001 (enabled with role R08), RPT-EXC-001 and RPT-AUD-001 (Conditional). The RFP figure "3 dashboards + 10 reports" is contained within the MVP set; the BoQ figure "24 outputs" is exceeded by it. Neither RFP figure is carried into the build. Final naming/audience of individual reports remains configuration under ADM-037 (PTBC-022) and may change the *names*, not the *count*, without a change record.

Under the TASK-001 order this is the only admissible reading: FG-01/FG-02 (rank 1) define the functional catalogue; the Scope (rank 4) is "requirements authority within its own domain only" and here does not even state a requirement, only a clarification request. The decision AHDA is asked to make is commercial — that the BoQ's 24 outputs are satisfied by the 34 MVP definitions — which engineering cannot make (ADR-006).

RTM-19531: acceptance contract → "FG-01 §5 (12 DSH) + FG-02 §5.1 (26 RPT); 34 MVP"; status → TRACED — TBC DEPENDENT (PTBC-021/022 for composition/naming); Final Disposition → the quoted statement above.

#### 5.2.2 Implementation and launch sequencing (RTM-19532)

CSB-SCOPE ¶229 says the 3-week development / 3-week launch phasing "should be normalized in the implementation plan rather than copied literally". That is exactly TASK-003 (Ratify Delivery Wave Plan W0–W6), which depends on this task. The 24-month duration and ~22-month operate period are preserved in §5.6.

RTM-19532: acceptance contract → "TASK-003 wave-to-phase cross-reference (`docs/planning/wave-to-phase-crossreference.md`)"; requirement type stays Non-Functional; status → TRACED — TBC DEPENDENT until TASK-003 is accepted by the PMO engagement lead; the selected design evidence RTM-19312/RTM-19029 (BIA/DR plan, WF-11 boundary) is removed from this row — it is not sequencing evidence. Finding → none after TASK-003 acceptance.

#### 5.2.3 Backup schedule and retention (RTM-19477)

**Evidence examined.**

| Source | What it says about frequency / retention |
|---|---|
| CSB-SCOPE ¶157–158 | Backup, restore and DR are required; "the RFP specifies requirements for daily, weekly and monthly backup and data-retention periods." The periods themselves are not in the summary. |
| CSB-CYBER-GUIDE Appendix A row 36 (CS-022) | "Perform regular backups based on BIA; daily for critical components. **Confirm exact schedule/retention with AHDA**; monitor job success." Rows 35, 37 (CS-022) and 70 (CS-029) give process controls, not periods. Appendix D: "Backup/DR RTO, RPO, retention and test expectations — Before production architecture approval — AHDA IT/BCM". |
| CSB-CYBER-POLICIES CS-022-2025 (سياسة النسخ الاحتياطي) | 11-page scanned-image PDF (JPEG pages, no text layer). Not machine-readable in this review; any minimum retention it sets must be read by AHDA Cybersecurity and recorded at the PTBC-048 gate. |
| CSB-14A §19.2 PTBC-048 | "Backup/DR RPO/RTO, backup retention and residency/hosting — Before production — AHDA-approved KSA/hosting architecture and recovery targets." PTBC-047 covers document/report/audit/log retention. |
| Workbook | OQ-003 open; TASK-023 (Backup, Restore & DR Runbook) and Release Checklist gate "Backup & DR Restore Drill Passed" run against best-known targets. |

**Disposition.** The *mechanism* is fixed and buildable now: a three-tier backup schedule (daily, weekly, monthly), each tier with a configurable retention period, plus restore/DR procedures per CS-022/CS-029. The *values* (per-tier retention, RPO, RTO) are not in any controlled source and are deferred to PTBC-048 (Before Production), owner AHDA IT / Cybersecurity, who also confirm CS-022's minimums. No retention value is written into the RTM.

RTM-19477: acceptance contract → "Guide App. A rows 35–37 (CS-022) + row 70 (CS-029); tiered schedule daily/weekly/monthly with per-tier retention configurable; values PTBC-048"; status → TRACED — TBC DEPENDENT; buildability → YES (mechanism) / values CONDITIONAL; Finding → none (governance dependency carried by PTBC-048).

**Residual after signature.** PTBC-048 values — Before Production (OQ-003, Release Checklist backup gate).

### 5.3 14B-F-003 — The 32 inventory-only components

**Finding (v1.0).** 32 of 242 canonical components have only an inventory reference (Blueprint v2.0 Appendix B, "Retained from Blueprint v1.0; governed by latest controlled WF/FG semantics") and no explicit behaviour-level row in the RTM.

**Evidence examined.** Every one of the 32 IDs was searched across all 21 WF/FG specifications, CSB-BP2 and CSB-14A. All 32 appear only in Blueprint v2.0 Appendix B by ID; MOD-114, MOD-119 and MOD-124 additionally appear by ID in CSB-WF-13. The behaviour behind most of them exists in the owning specification under a different name, which is what the RTM's "explicit source-row reference" rule could not see. Step 16 `12_Findings_Gates` lists 35 IDs for this finding (adds MOD-016, ADM-048, ADM-053); those three have 5, 11 and 13 behaviour links respectively in `04_Screen_Traceability` and are **not** inventory-only — the count stays 32.

**Disposition per component.** Owner and behaviour source are assigned; canonical IDs are retained (no renumbering). Action codes: **LINK** = add the cited source rows to `04_Screen_Traceability` / `15_Links`; **COMPOSE** = component is a composed view of existing dashboards/lists, no new definition; **CONTRACT** = owner writes a short behaviour contract before build; **CLARIFY** = semantic note in Blueprint v2.x change register; **DEFER** = outside MVP pending an AHDA decision.

| # | ID | Name | Owner assigned | Behaviour source (controlled) | Action | Kind |
|---|---|---|---|---|---|---|
| 1 | SCR-034 | Edit Project Draft | WF-01 | CSB-WF-01 US-PCR-PM-013 (reopen/edit Draft), US-PCR-PM-003, US-PCR-PM-012; SCR-033 §8 | LINK | PRECEDENCE |
| 2 | MOD-001 | Delete Draft Confirmation | WF-01 | CSB-WF-01 US-PCR-PM-014 (cancel/delete draft); lifecycle row "Draft → Cancel Draft → Cancelled Draft; soft-cancel preferred" | LINK | PRECEDENCE |
| 3 | MOD-002 | Assign Project Manager | WF-01 | CSB-WF-01 US-PCR-PM-006 (assign PM and stakeholders), US-PCR-SYS-022 | LINK | PRECEDENCE |
| 4 | MOD-003 | Change Project Status | WF-01 (Project master) | No direct status edit exists in any spec. Lifecycle transitions are owned commands: activation (CSB-14A ICD-02), suspension/resumption (WF-09), completion/closure (WF-10), each approval-separated (ICD-05). | CLARIFY — "launcher for governed transition requests; never a free status edit" | PRECEDENCE |
| 5 | SCR-042 | Project Classification & Ownership | WF-01 | CSB-WF-01 process step 3 "Enter classification / ownership"; US-PCR-PM-004; US-PCR-PFM-004 | LINK | PRECEDENCE |
| 6 | SCR-043 | Project Stakeholders | WF-01 | CSB-WF-01 process step 7 "Add stakeholders"; US-PCR-PM-006 | LINK | PRECEDENCE |
| 7 | SCR-051 | Project Risks (workspace tab) | WF-06 | CSB-WF-06 SCR-080 "Primary Project/portfolio Risk list"; `GET /api/projects/{projectId}/risks`; screen decision "no new top-level WF-06 screen ID" | LINK — project-scoped SCR-080 | PRECEDENCE |
| 8 | SCR-052 | Project Issues (workspace tab) | WF-07 | CSB-WF-07 SCR-083 Issue Register, project scope; US-ISS-VW-001 | LINK | PRECEDENCE |
| 9 | SCR-053 | Project Challenges (workspace tab) | WF-07 | CSB-WF-07 SCR-085 Challenge Register, project scope; §"No new page ID is required for the MVP" | LINK | PRECEDENCE |
| 10 | MOD-017 | Submit Baseline | WF-03 | CSB-WF-03 process "Submit Baseline — Manual"; Baseline Candidate DRAFT → SUBMITTED; NOT-SCH-015; REV-SCH-018 already asks for MOD-010–018 reconciliation | LINK | PRECEDENCE |
| 11 | MOD-018 | Approve Baseline | WF-03 (+ WF-11 runtime) | CSB-WF-03 review → APPROVED_PENDING_ACTIVATION; CSB-14A §8 WF-03 row ("approval does not equal activation") | LINK | PRECEDENCE |
| 12 | MOD-091 | Publish Workflow Version | FG-04 | CSB-FG-04 US-CFG-CAD-017 (publish), MOD-092 Activate/Deactivate Configuration, ADM-031 Workflow List | LINK | PRECEDENCE |
| 13 | MOD-100 | Test Integration Connection | FG-05 | No test-connection story in CSB-FG-05; CSB-14A §6 keeps "technical configuration/secrets outside business config". | CONTRACT (FG-05 owner: is a connectivity probe an MVP admin action or an operations-runbook step?) | DECISION (functional architect) |
| 14 | MOD-101 | Enable / Disable Integration | FG-05 | CSB-FG-05 US-INT-ADM-028; INT-FLD-011 EnabledStatus, INT-FLD-029 ActivationStatus; BR-INT-008; ERR-INT-005 | LINK | PRECEDENCE |
| 15 | ADM-054 | System Settings | Platform technical config (FG-04 boundary) | CSB-14A §6 "ADM-054–057 RETAIN — Technical settings/version/health"; CSB-FG-04 §"Technical System Settings — not business governance" | LINK + CLARIFY (technical, not FG-04 governed configuration) | PRECEDENCE |
| 16 | ADM-056 | Environment / Version Information | Platform technical config | CSB-14A §6 ADM-054–057 row | LINK | PRECEDENCE |
| 17 | MOD-111 | Confirm Draft Deletion (shared) | Shared UI; pattern owner WF-01 | Generalisation of MOD-001; CSB-FG-04 US-CFG-CAD-043 (cancel unpublished Draft) | LINK | PRECEDENCE |
| 18 | MOD-113 | Select Department | Shared UI; data owner FG-04 (organization master), scope FG-03 DEPT | CSB-FG-03 DEPT scope; CSB-FG-04 organization master data | CONTRACT (picker contract: active departments only, scope-filtered) | PRECEDENCE |
| 19 | MOD-114 | Select Entity | Shared UI; reused by WF-13 | CSB-WF-13 shared-modal reuse list (MOD-112–125) | LINK | PRECEDENCE |
| 20 | MOD-119 | Select Date / Date Range | Shared UI; reused by WF-13 | CSB-WF-13 reuse list | LINK | PRECEDENCE |
| 21 | MOD-120 | Advanced Filters | Shared UI; semantics FG-02/FG-01 | CSB-FG-02 §6.1 parameter/filter model, MOD-061; CSB-FG-01 §9.3 filter model | LINK | PRECEDENCE |
| 22 | MOD-121 | Column Selector | Shared UI; semantics FG-02 | CSB-FG-02 MOD-061 Select Columns / Filters | LINK + CLARIFY (same behaviour as MOD-061) | PRECEDENCE |
| 23 | MOD-122 | Save Filter / View | Shared UI; semantics FG-02/FG-01 | CSB-FG-02 MOD-062 Save Report View, §10.2; CSB-FG-01 §14.2 Saved Dashboard Views | LINK + CLARIFY | PRECEDENCE |
| 24 | MOD-124 | Success / Submission Confirmation | Shared UI; reused by WF-13 | CSB-WF-13 reuse list | LINK | PRECEDENCE |
| 25 | SCR-007 | Global Search Results | Platform common UI; authorisation FG-03 | CSB-BP2 §20 header "global search"; CSB-14A §6 SCR-001–012 RETAIN. No search-scope contract exists. | CONTRACT (searchable entities, permission filtering per FG-03 §10.1) | DECISION (functional architect) |
| 26 | SCR-010 | Help Center | Platform common UI; content PMO | CSB-BP2 §20.1 menu 11 "Help & Knowledge: user guide; FAQ; support"; TASK-096 authors content | LINK to §20.1 + CONTRACT (static bilingual content pages) | PRECEDENCE |
| 27 | SCR-011 | User Guide | Platform common UI; content PMO | As SCR-010; CSB-SCOPE ¶65 "دليل المستخدم والتوثيق الفني" | LINK + CONTRACT | PRECEDENCE |
| 28 | SCR-012 | FAQ / Knowledge Base | Platform common UI; content PMO | As SCR-010; CSB-SCOPE ¶66. Duplicates SCR-125 Knowledge Base / SCR-126 FAQ, which CSB-WF-12 already declares "shared/help content" | LINK + CLARIFY (one help family: SCR-010/011/012 host; SCR-125/126 are aliases, no second implementation) | PRECEDENCE |
| 29 | SCR-021 | Portfolio Performance | FG-01 | Not in CSB-FG-01 §5 inventory; CSB-BP2 §20.1 menu 2 lists "performance"; CSB-14A §6 "other apparent needs are handled by composition/reuse rather than new IDs" | COMPOSE — DSH-002 Portfolio + SCR-020 Portfolio Overview; no new dashboard | PRECEDENCE |
| 30 | SCR-023 | Portfolio KPIs | FG-01 | As above; CSB-FG-01 DSH-012 KPI Dashboard | COMPOSE — DSH-012 with portfolio scope | PRECEDENCE |
| 31 | SCR-024 | Critical / Strategic Projects | FG-01 / WF-01 classification | As above; CSB-FG-01 §5.2 SCR-027 Projects Requiring Attention; classification via WF-01 priority master (PTBC-013) | COMPOSE — filtered SCR-025 register + DSH-002 widget | PRECEDENCE |
| 32 | SCR-035 | Project Location / Map View | FG-01 | CSB-14A / CSB-BP2 App. F PTBC-042: "Geospatial/map … Can remain configurable/deferred. Only implement if AHDA confirms business value/data quality." Step 15 15-D-006. | DEFER — status DEFERRED / OUT OF MVP unless AHDA confirms at PTBC-042 | DECISION (AHDA Business Sponsor) |

Result: 26 LINK (behaviour already specified), 3 COMPOSE, 2 CONTRACT to be written by the functional architect (MOD-100, SCR-007) plus picker contracts (MOD-113) and help-page contracts (SCR-010/011/012), 1 DEFER (SCR-035). The dashboard/report count in §6 is unaffected: rows 29–31 are compositions, not definitions.

**RTM changes.** `04_Screen_Traceability`: coverage result → `BEHAVIOR LINKED` for rows 1–12, 14–24, 26–28 with the cited source rows added to `RTM references`; rows 29–31 → `COMPOSED VIEW`; row 32 → `DEFERRED — PTBC-042`; rows 13, 25 → `CONTRACT PENDING` with gate "Before affected UI build". `11_Readiness` 14B-DOD-07 → PASS WITH 3 CONTRACTS PENDING (210 + 26 + 3 = 239 of 242 linked; 2 contract-pending; 1 deferred). OQ-004 → closed by this table.

### 5.4 14B-F-004 — Generic story references (3,878 rows)

**Finding (v1.0).** Story-level references are incomplete or generic for a material subset of the backlog.

**Evidence examined.** All 3,878 affected rows are Functional user-story rows, one per story ID (3,878 of the 4,079 indexed story IDs, spread across all 21 domains: 114 in WF-01 up to 242 in FG-02). Every one carries `Design Coverage Status = "Controlled behavior present; operation-level linkage incomplete"`. In the specifications the story backlog tables (e.g. CSB-FG-01 §17, CSB-FG-02 §15) carry role, story text and MVP flag only; where a spec adds a story-to-control matrix (e.g. CSB-WF-07 §7.4) it cites ranges such as `ISS-CC-01–26; SCR-083/084/085/086/087/088`. Consequently 2,575 of the rows have an empty control ID, 3,147 an empty screen ID and all 3,878 an empty API/operation cell. This is how the controlled specs are written, not a defect in them, and it is not closable by discovery.

Where the joins actually get made: CSB-16 registers `04_Screen_Contracts`, `06_Fields_Validation` (3,124 rows), `07_API_Consumption` (843 rows); CSB-17 `API_Contracts` (839) and `Backend_Trace` (19,534); CSB-18 `UAT_Scenarios` — one scenario per story (4,080 rows), currently `STORY INTENT ONLY` with the instruction "Domain owner must confirm observable results and exact acceptance/control binding before execution."

**Disposition.** The finding is accepted as a per-story build-entry gate, exactly as v1.0's own resolution gate states ("Before affected story enters build"). The controlled mechanism is:

1. A story is Ready for build only when its RTM row has an explicit control ID, screen/component ID and API operation ID drawn from the existing controlled registers (no new IDs), and its CSB-18 scenario is moved from `STORY INTENT ONLY` to bound.
2. The domain functional owner makes the join; the solution architect verifies it against CSB-16/17 registers.
3. The bound scenario is the closure evidence for that RTM row; its status then moves to FULLY TRACED. `14B-DOD-06` stays PARTIAL until the last story is bound.

No RTM row changes now beyond `Comments / Resolution` → "Per-story join at Definition of Ready; evidence = bound Step 18 scenario (TASK-002 §5.4)." This finding is therefore dispositioned, not counted as resolved, and its residual is tracked per story in CSB-18 `RTM_Disposition`, not in this assessment.

### 5.5 14B-F-005 — Source-clause acceptance reconciliation (175 rows)

**Finding (v1.0).** Source-scope clauses require acceptance reconciliation against selected controlled design evidence.

**Evidence examined.** The 201 scope clauses split into: 5 FULLY TRACED, 7 TBC-dependent, 7 UNTRACED (all F-006), 4 F-001, 3 F-002, 175 F-005 — all 175 PARTIALLY TRACED with `Design evidence identified; end-to-end scope acceptance reconciliation open`, each already carrying "Selected design evidence: RTM-xxxx; …" in its comments. Domains: 25 Platform delivery, 17 FG-03, 17 Platform operations, 14 FG-02, 11 WF-15, 10 FG-01, and the rest spread across the workflows.

**Disposition.** Reconciliation rule, applied by the TASK-001 order:

1. A scope clause whose selected design evidence is a FULLY TRACED or TBC-dependent rank-1/rank-2 row is *covered*; that row's acceptance/control statement is the clause's acceptance contract. The clause row's status → the evidence row's status. No new scope is added.
2. A scope clause whose evidence is itself PARTIALLY TRACED inherits that row's finding (in practice F-004) and closes with it.
3. A scope clause with no controlled evidence is a **scope gap for AHDA**, not a design gap: it is listed to the AHDA scope owner for one of accept-as-out-of-scope / raise change record. None of the 175 is in this class (all have selected evidence); the 7 clauses in this class are the F-006 rows.

The business analyst executes rule 1–2 row by row at RTM v1.1 reissue; the AHDA scope owner signs the rule (§9), not the 175 rows individually. `14B-DOD-01`, `-03`, `-15` move to PASS on reissue.

### 5.6 14B-F-006 — Delivery, migration, training and support obligations (7 rows, all UNTRACED)

**Finding (v1.0).** Delivery/service obligations lack a controlled acceptance contract in the WF/FG design set.

**Evidence examined.** The seven rows are contractual obligations from CSB-SCOPE §6, §10, §11, §13, not platform behaviour. No WF/FG spec can own them; the implementation-plan workbook already has the tasks that do.

| RTM ID | Clause (CSB-SCOPE) | Obligation | Owning task(s) in the workbook | Acceptance criteria source |
|---|---|---|---|---|
| RTM-19450 | ¶130 — Data Layer | Separate data tier (three-tier architecture) | TASK-007 Define Three-Tier Solution Architecture; ADR-003 | TASK-007 acceptance criteria; CSB-CYBER-GUIDE §3 |
| RTM-19488 | ¶175 — اجتماع إطلاق المشروع | Project kickoff | TASK-003 Ratify Delivery Wave Plan (W0) | PMO kickoff record accepted by AHDA sponsor |
| RTM-19500 | ¶186 — معالجة الملاحظات والأخطاء الفنية | Correct functional/technical defects before acceptance | TASK-088 (UAT execution) and Release Checklist "UAT Catalogue Executed & Signed Off" | Zero open Critical/High defects; signed AHDA UAT acceptance |
| RTM-19509 | ¶198 — Bug Fixes (operate period) | Corrective maintenance in operations | TASK-093 Operational SLAs & On-Call Runbook | SLA table (OQ-009, TBC until AHDA confirms) |
| RTM-19514 | ¶203 — الزيارات الدورية الشهرية | Monthly site visits | TASK-093 / TASK-097 Operational Handover Package | Named in the on-call/support model; cadence contractual |
| RTM-19527 | ¶220 — 24-month contract duration | Preserve the 24-month term | TASK-003 wave plan; TASK-097 | Wave plan footprint ≤ 24 months; handover before the operate period starts |
| RTM-19528 | ¶221 — ~22 months operations and support | Operate/maintain/support period | TASK-093, TASK-097, Release Checklist "Operational Handover Package Accepted" | Signed AHDA knowledge-transfer acknowledgment |

Not in the RTM but in the same clause family and dispositioned the same way: training and workshops (¶210–217) → TASK-096/TASK-097; data migration (¶165–171) → TASK-089/TASK-102 (OQ-008).

**Disposition.** The seven rows change `Requirement Type` to `Contractual / Delivery`, `Acceptance / Control Statement` to the owning task's acceptance criteria (table above), status → TRACED — TBC DEPENDENT where the criteria still contain an Open Question (RTM-19509, -19514, -19528 via OQ-009), otherwise FULLY TRACED. `Untraced` count → 0. The delivery manager / service transition lead owns the criteria and signs (§9); AHDA Contracts confirms the SLA table at OQ-009.

### 5.7 14B-F-007 — Mixed WF/FG shorthand — see §7

### 5.8 14B-F-008 — TBC → PTBC → RTM crosswalk — see §8

## 6. Dashboard and report count carried into TASK-069–TASK-072 and ADR-006

Single statement, to be copied verbatim into ADR-006 "Selected Option", OQ-002 "Status", and the acceptance criteria of TASK-069/070/071/072:

> **Output catalogue = 38 governed definitions: 12 dashboards (DSH-001–DSH-012, CSB-FG-01 §5) + 26 report definitions (CSB-FG-02 §5.1). MVP acceptance = 34 (11 dashboards + 23 reports). Conditional (not MVP-committed): DSH-008, RPT-EXT-001 (with role R08); RPT-EXC-001, RPT-AUD-001. Source: Step 14B Assessment v1.1 §5.2.1, approved by the AHDA Business Sponsor on ____.**

Consequences for the build tasks:

| Task | What the number means there |
|---|---|
| TASK-069 FG-01 backend | Definition catalogue seeds exactly 12 dashboard definitions; DSH-008 flagged conditional on R08. |
| TASK-070 FG-01 frontend | 12 dashboard experiences, DSH-009 composed inside SCR-040 (no route). SCR-021/023/024 are compositions (§5.3 rows 29–31), not additional dashboards. |
| TASK-071 FG-02 backend | Report definition catalogue seeds exactly 26 `RPT-*` definitions; 3 flagged conditional. Export formats PDF/XLSX/CSV (ICD-17, ADR-005). |
| TASK-072 FG-02 frontend | SCR-130–140 host the 26; the 11 screens are not counted as reports. |
| ADR-006 | Option (C) with the count corrected: the Blueprint's "11 SCR-13x report screens" is replaced by FG-02's 26 report definitions. |

## 7. 14B-F-007 — Compressed shorthand expansion

A regex scan of CSB-14A, CSB-BP2 and the RTM workbook for `WF-nn/…` and `FG-nn/…` lists that, read literally, name a WF above 15 or an FG above 06 found exactly five distinct source rows (mirrored into three RTM sheets). Only 21 specifications exist (WF-01–15, FG-01–06).

| Source row | Original text (preserved) | Literal misread | Explicit expansion |
|---|---|---|---|
| CSB-14A §3 register, WF-02 row, "Shared dependencies" (mirrored in RTM `03_WF_FG_Coverage`) | `FG-01/02/04/15/06` | FG-15 | FG-01, FG-02, FG-04, **WF-15**, FG-06 |
| CSB-14A §3 register, WF-04 row (mirrored in `03_WF_FG_Coverage`) | `FG-03/04/15/06` | FG-15 | FG-03, FG-04, **WF-15**, FG-06 |
| CSB-14A §16 EVT-002 ProjectActivated, "Primary Consumers" (mirrored in `06_API_Event`) | `WF-02/03/04/05/FG-01/02/15/06` | FG-15 | WF-02, WF-03, WF-04, WF-05, FG-01, FG-02, **WF-15**, FG-06 |
| CSB-14A §19.2 PTBC-026, "Source Specs / Families" (mirrored in `08_PTBC_Impact`) | `PM Cyber Guide, FG-03/12/14/06` | FG-12, FG-14 | Cyber Guide, FG-03, **WF-12**, **WF-14**, FG-06 |
| CSB-BP2 Appendix F.2 PTBC-026 | `FG-03/12/14/06` | FG-12, FG-14 | FG-03, **WF-12**, **WF-14**, FG-06 |

**Disposition.** The expansions above are recorded in the RTM sheets as an added `Expanded owners/consumers` column beside the preserved original text; CSB-14A and CSB-BP2 are corrected at their next controlled revision (Blueprint v2.x change register; CSB-14A is QA CLOSED and is not edited in place). No nonexistent WF/FG is adopted. `14B-F-007` → CLOSED on document-control owner signature.

## 8. 14B-F-008 — Source TBC → PTBC → RTM crosswalk

**Evidence examined** (`14_Source_TBC`, `08_PTBC_Impact`, CSB-14A §19).

| Measure | Result |
|---|---|
| Source TBCs | 511, all retained under original IDs; owners: 21 domains (FG-05 34 … WF-05 16), matching CSB-14A §19.1 exactly |
| Source TBCs with ≥1 PTBC theme | 511 of 511 (90 map to more than one theme) |
| Source TBCs with an *explicit* RTM reference | 0 — every link is `EXACT SOURCE ID; theme/impact links are 14B analysis` |
| Source TBCs with no RTM row at all (explicit or analytical) | 106 (listed in `14_Source_TBC`, e.g. TBC-DSH-007, TBC-RPT-02, TBC-CFG-028, TBC-INT-02, TBC-AUD-11, TBC-PCR-02 …) |
| PTBC themes with zero affected RTM rows | 4 — PTBC-002 (activation authority), PTBC-030 (export watermark), PTBC-044 (observability stack), PTBC-045 (immutable audit implementation) |
| Distinct resolution-gate labels across the 48 PTBCs | 34 |
| Gate classes defined by CSB-14A §19.3 | 4 — Before Build / Integration Build; Before UAT; Before Production; May Remain Configurable |

**Gate normalisation.** Every one of the 34 labels maps to exactly one §19.3 class (SIT and performance-test gates precede UAT and are classed with Build):

| §19.3 gate class | PTBC themes | Source TBCs whose *earliest* PTBC gate is this class |
|---|---|---|
| BEFORE BUILD / SIT | 7 (PTBC-032, 033, 034, 035, 036, 038, 043) | 71 |
| BEFORE UAT | 31 | 375 |
| BEFORE PRODUCTION | 9 (PTBC-012, 026, 027, 029, 030, 044, 045, 047, 048) | 53 |
| MAY REMAIN CONFIGURABLE | 1 (PTBC-042) | 12 |
| **Total** | **48** | **511** |

This satisfies the TASK-002 validation note: each of the 511 source TBCs is explicitly deferred to a named PTBC gate; none is resolved (no AHDA value has been supplied yet, and none is invented here).

**Disposition.**

1. The theme-level crosswalk (511 → 48) is confirmed as complete and is the controlled crosswalk; the specific gate label of each PTBC is kept, and the four-class rollup above is added as a column to `08_PTBC_Impact` and `14_Source_TBC`.
2. The 106 TBCs with no RTM row and the 4 zero-row PTBCs are recorded as an *analytical* gap: their values still resolve at the PTBC gate; the RTM rows that depend on them are added when the domain owner binds stories (F-004 mechanism). They do not block any gate.
3. "Analytical theme links do not approve AHDA values" stands: signing F-008 approves the *map*, not any value.

`14B-DOD-14` → PASS on signature. Residual: value resolution at each PTBC gate, tracked in the workbook's Open Questions (OQ-001, 003, 005, 006, 007, 009, 010).

## 9. Sign-off register

Each signatory signs the exact statement in the "Signs that" column. A row is complete when name, role and date are filled. The assessment is QA CLOSED when all eight rows are complete and §10.1 has been executed.

| Finding | Signatory (accountable function, from `10_Findings`) | Signs that | Name / role | Date |
|---|---|---|---|---|
| 14B-F-001 | AHDA scope owner / PMO | "CSB-SCOPE (digest 98d7a1eced0efb6f) is the scope of record; no other adjusted scope exists; ICD-17, PTBC-048 and ICD-15 govern ¶95, ¶145 and ¶151–152." | | |
| 14B-F-002 (a) quantities | AHDA Business Sponsor + PMO Engagement Lead (ADR-006 owners) | The §6 statement: 38 governed definitions, 34 MVP; BoQ "24 outputs" satisfied. | | |
| 14B-F-002 (b) sequencing | PMO Engagement Lead | Sequencing is normalised by TASK-003; ¶229 is not copied literally. | | |
| 14B-F-002 (c) backup | AHDA IT / Cybersecurity | Tiered daily/weekly/monthly backup with configurable per-tier retention is the design requirement; retention/RPO/RTO values are supplied at PTBC-048 before production, including any CS-022 minimum. | | |
| 14B-F-003 | Functional architect (rows 1–31) and AHDA Business Sponsor (row 32, PTBC-042) | The §5.3 owner/behaviour table; SCR-035 deferred unless confirmed. | | |
| 14B-F-004 | Solution architect, on behalf of WF/FG functional owners | The per-story Definition-of-Ready join mechanism in §5.4. | | |
| 14B-F-005 | Business analyst + AHDA scope owner | The three-rule reconciliation in §5.5. | | |
| 14B-F-006 | Delivery manager / service transition lead | The §5.6 task ownership table; SLA values follow at OQ-009. | | |
| 14B-F-007 | Document-control owner | The five expansions in §7. | | |
| 14B-F-008 | Requirements governance lead | The crosswalk and gate rollup in §8; no value approved. | | |
| **Overall** | PMO Engagement Lead (Release Checklist gate "Step 14B RTM QA Closed") | All rows above complete; RTM v1.1 reissued. | | |

## 10. Changes required in controlled records

### 10.1 RTM workbook v1.1 reissue (document control, after signature)

| Sheet | Change |
|---|---|
| `00_Control` | Version → 1.1; Formal status → QA CLOSED; Open IMPORTANT findings → 0; Open documentation findings → 0; "Components with direct behavior links" → 239 (+ 2 contract-pending, 1 deferred); Untraced → 0 |
| `10_Findings` | Add columns `Disposition (v1.1 §ref)`, `Signatory`, `Signed date`; Status → CLOSED per row |
| `11_Readiness` | Conditions 1–5 → CLOSED; 14B-DOD-01/03/07/14/15 → PASS; 14B-DOD-06/16 → PARTIAL — per-story (§5.4); Formal Step 14B closure → QA CLOSED |
| `04_Screen_Traceability` | 32 rows per §5.3 |
| `08_PTBC_Impact`, `14_Source_TBC` | Add `Gate class (14A §19.3)` column per §8 |
| `03_WF_FG_Coverage`, `06_API_Event`, `08_PTBC_Impact` | Add `Expanded owners/consumers` beside the 4 shorthand rows per §7 |
| Parts 1–4 | Cell changes for RTM-19421, 19462, 19468, 19469 (§5.1); 19531, 19532, 19477 (§5.2); the 7 F-006 rows (§5.6); 175 F-005 rows (§5.5 rules); `Comments / Resolution` on 3,878 F-004 rows (§5.4). No RTM ID is added or renumbered. |
| Digests | New digests recorded in the TASK-001 register §3.4 (CSB-14B, CSB-14B-RTM → v1.1) |

### 10.2 Implementation-plan workbook (`AHDA_RPMO_Platform_Implementation_Plan.xlsx`)

| Record | Change |
|---|---|
| ADR-006 | Selected Option → §6 statement; Status → Approved on F-002(a) signature |
| OQ-002 | Status → Closed, answer = §6 statement |
| OQ-003 | Stays Open; note "mechanism fixed by 14B v1.1 §5.2.3; values at PTBC-048" |
| OQ-004 | Status → Closed by 14B v1.1 §5.3 |
| TASK-069/070/071/072 | Acceptance criteria: replace "the exact final dashboard/report count from TASK-002" with the §6 numbers |
| TASK-002 description | The FG-01/FG-02 tasks are TASK-069–072, not "TASK-062+" |
| Release Checklist "Step 14B RTM QA Closed" | Evidence = this document §9 complete + RTM v1.1 digests |
| TASK-001 §6 item 1 | Close: scope of record confirmed (F-001) |

### 10.3 Downstream Step 15–18 registers

CSB-15 `10_Findings_14B_Impact`, CSB-16 `12_Findings_Gates`, CSB-17 `Findings_Gates` and CSB-18 `Readiness_Gates` all carry the 8 findings as INHERITED — OPEN with "no closure evidence supplied". On signature, each is updated to reference this document as closure evidence; CSB-16's 35-ID list for F-003 is corrected to 32 (§5.3). Step 16 finding 16-F-002 (inventory-only behaviour gap) closes with F-003.

## 11. TASK-002 acceptance-criteria check

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Each of the 8 findings has a written, AHDA-approved disposition recorded in the RTM assessment | Written: **8 of 8** (§5, §7, §8). AHDA-approved: **0 of 8** — signatures are outstanding (§9). No approval is claimed on AHDA's behalf. | §4, §9 |
| 2 | RTM status changes from "conditionally ready" to QA CLOSED | **PENDING** — status rule in §2 flips on completion of §9 and the §10.1 reissue; not set by editing the cell | §2 |
| 3 | Final dashboard and report count is a single unambiguous number carried into the FG-01/FG-02 tasks | **MET** as a controlled recommendation: 38 governed definitions (12 + 26), 34 MVP — awaiting the F-002(a) signature that ADR-006 requires | §6 |
| V1 | RTM row count and traceability percentage re-validated | **PASS** — 19,533 rows; 75.16% fully traced; all v1.0 counts reproduce | §3 |
| V2 | 511 source TBCs each resolved or explicitly deferred to a named PTBC gate | **PASS** — 0 resolved, 511 deferred: 71 Before Build/SIT, 375 Before UAT, 53 Before Production, 12 May Remain Configurable | §8 |

## 12. Open items after this revision

| # | Item | Owner | Gate |
|---|---|---|---|
| 1 | Eight signatures in §9 | Named functions | Before Release Checklist gate "Step 14B RTM QA Closed" and before TASK-003 baseline |
| 2 | BoQ is not in the controlled archive; the "24 outputs" figure cannot be traced. Supply it and register it under TASK-001 §3.3 if AHDA wants the commercial reconciliation evidenced. | AHDA PMO | Before F-002(a) signature |
| 3 | CS-022 Backup policy is a scanned PDF; AHDA Cybersecurity reads it for retention minimums at PTBC-048 | AHDA Cybersecurity | Before Production |
| 4 | Behaviour contracts for MOD-100, SCR-007, MOD-113, SCR-010/011/012 | Functional architect | Before affected UI build |
| 5 | SCR-035 map view — confirm or defer | AHDA Business Sponsor | PTBC-042 |
| 6 | Per-story binding of 3,878 stories (F-004) and of the 106 TBCs with no RTM row | Domain owners | Per story, Definition of Ready |
| 7 | Hosting/residency (PTBC-048, ADR-001, OQ-001) — unchanged by this task | AHDA IT / Cybersecurity | Before any environment provisioning |
