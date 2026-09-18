# ADR-001 — Hosting and Data Localisation Architecture

| Control | Value |
|---|---|
| Task | TASK-005 — Resolve Hosting & Data Localisation Architecture Decision Record (Phase P1 — Architecture Decisions, wave W0); depends on TASK-001 |
| Programme | AHDA Regional Project Management Platform (RPMO) |
| ADR ID | ADR-001 (workbook sheet *Architecture Decisions*, row 1) |
| Issue date | 2026-09-18 |
| ADR status | **PROPOSED — PENDING AHDA APPROVAL.** No option is selected by the delivery team. The decision is routed to AHDA IT / Cybersecurity (§6). Becomes APPROVED only when §9 is signed with an option and its conditions. |
| Blocking effect | Unchanged while pending: no Phase P3 task provisions a SIT, UAT or PROD environment (§7.1). |
| Decision owner | AHDA IT / Cybersecurity (decides); Engagement Architect (drafts, maintains) |
| Linked governance rows | Workbook ADR-001, OQ-001, Release Checklist gate "Architecture Decisions Approved"; PTBC-048 (TASK-004 tracker `01_PTBC_Register`); Step 15 decision 15-D-005; Step 14B finding 14B-F-001 / RTM-19462 |
| Source digests verified 2026-09-18 | CSB-SCOPE `98d7a1eced0efb6f`; CSB-CYBER-GUIDE `81b725edf83635c7`; workbook `0c0ff4b0b495ae25` — all unchanged from TASK-001 / TASK-003 |

Sources and precedence per TASK-001 (`docs/baseline/controlled-source-baseline.md`). Documents are cited by their `CSB-*` register ID. Scope paragraphs are cited as `CSB-SCOPE ¶n`, the paragraph index used by the Step 14B RTM (`09_Orphans_Gaps` RTM-19462 cites "paragraph 145") and by Step 14B Assessment v1.1 §5.1. PTBC gate classes are those of TASK-004 (`docs/governance/ptbc-tbc-tracker.md`); waves are those of TASK-003 (`docs/planning/wave-to-phase-crossreference.md`).

## 1. Decision statement

**Which hosting substrate the platform runs on, and where its data resides**, given that the contractual scope requires internal hosting and KSA data localisation while the only detailed architecture on file is a Google Cloud Platform (GCP) design.

This ADR reconciles **CSB-SCOPE §7 "الأمن السيبراني وإدارة البيانات" (Cybersecurity and Data Management), ¶145 and ¶156** (quoted in §2.1) with the GCP proposal in CSB-CYBER-GUIDE §4.3 (quoted in §2.2).

## 2. Context — the two positions on file

### 2.1 What the RFP requires (rank 4, contractual)

CSB-SCOPE is the client's original RFP scope summary (Arabic; no English part is in the file — it opens at "B. النسخة العربية"). Section 7 lists "المتطلبات الرئيسية" (the main requirements). The lines this ADR reconciles, verbatim, with the delivery team's English rendering:

| ¶ | Arabic (verbatim) | English rendering | Reading |
|---|---|---|---|
| 143 | يجب أن تلتزم المنصة بمتطلبات الأمن السيبراني وإدارة البيانات المعتمدة لدى الهيئة والمتطلبات الوطنية ذات العلاقة. | The platform must comply with the cybersecurity and data-management requirements approved by the Authority and the relevant national requirements. | Umbrella clause: AHDA policy set (CS-001…CS-033) plus national regulation apply. |
| **145** | **استضافة النظام في البيئة الداخلية للهيئة.** | **Hosting the system in the Authority's internal environment.** | The "internal hosting" line. No qualifier, no "or". Listed as a main requirement. |
| 155 | الالتزام بمتطلبات إدارة البيانات وحماية البيانات الشخصية. | Compliance with data-management and personal-data-protection requirements. | Personal data of users / external-entity contacts is in scope. |
| **156** | **توطين البيانات داخل المملكة أو ضمن البيئة المعتمدة لدى الهيئة.** | **Localisation of data inside the Kingdom, or within the environment approved by the Authority.** | The "data localisation" line. Two limbs joined by **أو** ("or"): in-Kingdom, or AHDA-approved environment. |
| 157–158 | النسخ الاحتياطي واستعادة البيانات والتعافي من الكوارث. / وتحدد الكراسة متطلبات للنسخ الاحتياطي اليومي والأسبوعي والشهري وفترات الاحتفاظ بالبيانات. | Backup, data restoration and disaster recovery. / The RFP sets daily, weekly and monthly backup requirements and data-retention periods. | Backup copies and DR sites are data locations too; they inherit ¶156. |

Two facts about the wording matter for the decision and are not the delivery team's to resolve:

1. **¶145 and ¶156 are not the same strictness.** ¶156 admits an AHDA-approved environment as an alternative to in-Kingdom placement. ¶145 has no alternative limb. Whether "البيئة الداخلية للهيئة" means AHDA-owned and -operated infrastructure only, or also an AHDA-controlled tenancy on a provider AHDA has approved, is a contractual interpretation that only AHDA can make (§6, Q1).
2. **The scope is a summary, not the RFP body.** Step 14B finding 14B-F-001 records that CSB-SCOPE "retains internal-hosting wording" and that no adjusted scope exists; Step 14B Assessment v1.1 §5.1 dispositioned RTM-19462 as *TRACED — TBC DEPENDENT* with acceptance contract PTBC-048 and stated "no provider or product is chosen here". This ADR is where that value is decided.

Related scope lines that constrain any option: ¶127 three-tier architecture (mandatory); ¶116–123 integrations with Active Directory, LDAP/SSO, Microsoft Exchange, Nafath, and AHDA internal systems (all inside AHDA's network); ¶226–227 a 24-month contract of which ~22 months are operations, maintenance and support.

### 2.2 What the delivery architecture proposes (domain governance input)

CSB-CYBER-GUIDE (PM Platform Development & Cybersecurity Implementation Guide, v1.0, 12 September 2026 — a §3.3 domain input, not a rank-1–4 source) states:

- Control table: "Primary infrastructure direction | Google Cloud Platform (GCP), **subject to AHDA IT/Cybersecurity approved architecture and services**."
- §4.3 "Example GCP service mapping — subject to AHDA standards": Web/API runtime → Cloud Run or GKE; Relational database → Cloud SQL for PostgreSQL; Document storage → Cloud Storage; Edge protection → HTTPS Load Balancer + Cloud Armor; Secrets → Secret Manager; Logging → Cloud Logging/Monitoring + SIEM.
- §4.3 boxed note: "**Do not assume** — The exact GCP products, regions, firewall model, database configuration, encryption-key model and public/private exposure must be confirmed with AHDA IT and Cybersecurity … do not create an unofficial production architecture outside the approved cloud landing zone."
- Appendix A, row *Data location*: "Host/store information in KSA or approved AHDA environment. | Use only approved GCP region/environment and contract controls. | CS-031 + project scope."
- Appendix D: "Approved GCP landing zone and service catalogue — needed before first cloud deployment — AHDA IT / Cloud."

The guide therefore proposes GCP as a *direction* and, in the same document, makes the direction conditional on the approval this ADR requests. It does not claim the RFP permits it.

### 2.3 What the controlled sources (ranks 1–3) say

None selects a provider; every one of them defers to AHDA. This is the precedence fact on which §5 rests.

| Source | Text | Effect |
|---|---|---|
| CSB-WF-01 §12 (rank 1) | "Data Localization / Hosting — Deploy only in AHDA-approved environment/location; exact GCP services/region subject to AHDA architecture approval." (RTM-6319) | Deployment location is an AHDA approval, not a spec value. |
| CSB-WF-01 §13 TBC-PCR-17 (rank 1) | "Exact GCP architecture/services/region for implementation. — Treat GCP mapping as architecture decision subject to AHDA IT/cyber approval." | Source-level TBC for this decision. TASK-004 finding 004-F-001 re-associates it from PTBC-042 to PTBC-048 with gate *Before Build / SIT*. |
| CSB-FG-03 §22.1 (rank 1) | "Platform storage/hosting follows approved AHDA/KSA localization and encryption policies." (RTM-2827) | Same, from the identity domain. WF-14 (RTM-17707), WF-12 (RTM-15736), WF-13 (RTM-16716) carry equivalent rows. |
| CSB-14A §19.2 PTBC-048 (rank 2) | "Backup/DR RPO/RTO, backup retention and residency/hosting — Before production — AHDA-approved KSA/hosting architecture and recovery targets." | Platform-level TBC; the value this ADR supplies once approved. |
| CSB-BP2 §22.1 engineering invariant (rank 3) | "Approved/KSA hosting and data-location constraints must be confirmed by AHDA IT/Cybersecurity; **illustrative GCP services remain examples until approved**." | Blueprint explicitly declines to convert the guide's examples into requirements. |
| CSB-17 Backend Package, *Backend architecture and ownership* | "The guide identifies GCP as a direction subject to AHDA approval. It does not approve a particular runtime, database engine, region or service." | Downstream baseline reads the guide the same way. |
| CSB-15 decision 15-D-005 (OPEN) | "Resolve irreversible topology/hosting/identity/provider decisions before commitment even where source gives a later test/release gate." Decision records linked to PTBC-048. | Requires this ADR before any provider commitment, i.e. before W1 (Phase P3). |

## 3. The compliance constraint (applies to every option)

Whatever substrate is chosen must satisfy all of the following. Rows marked *scanned* come from AHDA policy PDFs that are image-only in the archive (no extractable text); their content is known to the delivery team only through the guide's Appendix A/B summaries and must be confirmed against the policy text by AHDA Cybersecurity as part of the approval.

| # | Constraint | Source | Evidence any option must produce |
|---|---|---|---|
| C1 | System hosted in the Authority's internal environment — or AHDA's written determination of what "internal environment" admits | CSB-SCOPE ¶145 | AHDA determination (§6 Q1) |
| C2 | All platform data — primary, replicas, backups, DR copies, logs, document store, monitoring stores — resides in KSA or in the AHDA-approved environment | CSB-SCOPE ¶156, ¶157–158; RTM-19267; FG-05 US-INT-SEC-020 (monitoring-data residency) | Data-location register per store; provider region/site evidence |
| C3 | Compliance with AHDA cybersecurity policy set, in particular CS-031-2025 Cloud Computing & Hosting (approved provider/tenancy, isolation, encryption, logs, contracts, backups, KSA location, exit), CS-019-2025 Data (classification, KSA/approved location, cloud exit), CS-022-2025 Backup, CS-017 Network, CS-020 Database, CS-021 Cryptography | CSB-SCOPE ¶143; CSB-CYBER-POLICIES (*scanned*); CSB-CYBER-GUIDE App. A rows RTM-19266, 19267, 19305–19308 | AHDA Cybersecurity architecture review record |
| C4 | Compliance with relevant national requirements. Delivery-team reading, **not verified against current law** (same reservation as CSB-17): NCA Essential Cybersecurity Controls (cloud computing and hosting family, which the team understands to require in-Kingdom hosting/storage for national organisations), NCA Cloud Cybersecurity Controls for cloud tenants, the Personal Data Protection Law (personal data, cross-border transfer), and the Digital Government Authority's cloud policy for government entities | CSB-SCOPE ¶143, ¶155 | AHDA Cybersecurity confirmation of the applicable regulation set and the platform's criticality/classification (guide §15) |
| C5 | Three-tier separation with the data tier unreachable from public ingress; HTTPS-only ingress behind WAF; DEV/SIT/UAT/PROD separation; no secrets in code | CSB-SCOPE ¶127; CSB-BP2 §22.1; TASK-016/019/021 | IaC + network evidence (P3 tasks) |
| C6 | Private, authenticated connectivity to AD/LDAP, SSO, Exchange SMTP, SIEM, Nafath and AHDA internal systems | CSB-SCOPE ¶116–123; workbook *Environment and Secrets* (AD_*, SSO_*, EXCHANGE_*, SIEM_*, NAFATH_*) | Network diagram; connectivity tests in SIT |
| C7 | Backup with point-in-time recovery, DR, retention — values remain PTBC-048 / OQ-003 until AHDA supplies them; whatever they are, backup and DR targets must satisfy C2 | CSB-SCOPE ¶157–158; CSB-14A PTBC-048 | TASK-020 / TASK-023 evidence |
| C8 | Cloud exit / data return capability where a cloud option is chosen | CS-019/CS-031 via guide App. A (RTM-19266) | Exit plan in the hosting contract |
| C9 | The substrate must be operable by AHDA (or its contracted operator) for the ~22-month operations period and beyond | CSB-SCOPE ¶226–227, §11 | Operating model named in the approval |

## 4. Options

The three options are those already recorded in workbook ADR-001. Each is assessed against §3. "Delivery-team assessment" means the engineering view; the compliance verdict on C1–C4 is AHDA's.

### 4.1 Option A — AHDA internal (on-premise / AHDA data-centre) infrastructure

AHDA IT provides the compute (VM or Kubernetes), PostgreSQL, object storage, WAF/reverse proxy, secret vault, backup and log/SIEM facilities inside its own data centre(s); the delivery team deploys the containerised application onto them.

| Constraint | Assessment |
|---|---|
| C1 ¶145 | Satisfied literally. |
| C2 ¶156 | Satisfied if AHDA's DR site is also in-Kingdom (to confirm). |
| C3/C4 | CS-031 cloud clauses largely not triggered; CS-014 Server Security, CS-017, CS-020, CS-022, CS-027 Physical apply in full and are AHDA-operated. |
| C5–C7 | Achievable; depends entirely on what AHDA's environment already offers (WAF, K8s/container runtime, PITR-capable PostgreSQL, vault). |
| C8 | Not applicable. |
| C9 | AHDA-operated by definition. |

Delivery-team assessment: lowest compliance risk; highest dependency risk. The guide's delivery model (§4.2 "what the cloud team prepares in parallel", Appendix D "approved GCP landing zone") has no on-premise equivalent on file, so **AHDA must state what its internal environment provides, its lead time, and who operates it** before TASK-016/017 can be scoped. If the internal environment lacks a managed container runtime or WAF, TASK-017's IaC target becomes VM-level provisioning (Terraform against vSphere/bare metal or the AHDA-approved equivalent) and TASK-021 requires AHDA's DMZ for the external-entity (R08) and Nafath paths. Public exposure for R08 external users still requires an AHDA-operated internet ingress.

### 4.2 Option B — Google Cloud Platform, AHDA-owned tenancy, single KSA region

The guide's §4.3 mapping: Cloud Run or GKE, Cloud SQL for PostgreSQL, Cloud Storage, HTTPS Load Balancer + Cloud Armor, Secret Manager, Cloud Logging — in an AHDA-owned organisation/landing zone, pinned by organisation policy to Google Cloud's Saudi Arabia region (Dammam, `me-central2`; service availability in that region to be confirmed by AHDA with the provider).

| Constraint | Assessment |
|---|---|
| C1 ¶145 | **Satisfied only if AHDA determines that an AHDA-controlled tenancy on an AHDA-approved provider is within "the Authority's internal environment" or that ¶156's second limb governs.** The delivery team cannot make that determination. |
| C2 ¶156 | Satisfiable on the first limb (in-Kingdom) with a resource-location organisation policy; **but GCP has one KSA region, so any cross-region replica, backup bucket or DR target would leave the Kingdom.** Backup/DR must be multi-zone within the region or exported to an in-Kingdom target — a design constraint on PTBC-048 RPO/RTO. |
| C3 | CS-031 applies in full: approved/registered provider, tenancy isolation, contractual cyber clauses, cloud logs, exit — all AHDA-side approvals (guide App. A rows RTM-19305–19308). |
| C4 | National cloud-tenant controls and PDPL transfer rules apply; AHDA Cybersecurity to confirm the provider's regulatory standing for a government entity. |
| C5 | Native (VPC, private IP Cloud SQL, Cloud Armor). |
| C6 | Requires private connectivity to AHDA's network (VPN or Interconnect) for AD/LDAP, Exchange relay, SIEM, internal systems — an AHDA network change with its own approval and lead time (guide §15 "Network"). |
| C7 | Native PITR/automated backups; residency per C2. |
| C8 | Exit plan required: PostgreSQL dump/replication + object-store export are standard, so exit cost is bounded. |
| C9 | AHDA operates the tenancy; delivery team supports under the O&M SLA (OQ-009). |

Delivery-team assessment: the most fully specified option and the one the guide, Step 17 and the workbook's *Environment and Secrets* sheet were written against; but it is **not selectable on the current sources** — no rank-1–4 document authorises it, and the guide itself makes it conditional. Selecting it requires the positive determinations in §6 and the CS-031 approvals as conditions of approval.

### 4.3 Option C — AHDA-approved KSA sovereign / local cloud provider

A cloud provider located and operated in KSA that AHDA (and, where required, the national regulator) has approved for government workloads — for example a government-cloud offering or a DGA/NCA-listed local provider. No such provider is named in any source; whether one exists and is approved is an AHDA fact.

| Constraint | Assessment |
|---|---|
| C1 ¶145 | Same interpretation question as Option B (§6 Q1), but the "approved environment" limb of ¶156 is designed for exactly this case. |
| C2 | Satisfied by construction if all provider sites are in-Kingdom. |
| C3/C4 | CS-031 applies; regulatory standing typically already established for government use (to confirm). |
| C5–C8 | Depends on the provider's service catalogue: it must offer a container runtime, managed PostgreSQL (or an AHDA-accepted self-managed pattern), object storage, WAF, secret store, logging. The application stack (ADR-002/003: containers + PostgreSQL + object storage + OIDC) is provider-neutral, so re-mapping guide §4.3 is bounded but must be done before TASK-017. |
| C9 | Provider- and AHDA-operated. |

Delivery-team assessment: compliance-clean if such a provider is approved; delivery risk is the unknown catalogue and any gaps in managed services (self-managed PostgreSQL HA/PITR would move work from TASK-020 into an operations burden for the 22-month O&M period).

### 4.4 Option comparison

| | A — AHDA internal | B — GCP (KSA region) | C — KSA sovereign/local cloud |
|---|---|---|---|
| ¶145 internal hosting | Literal | Needs AHDA determination | Needs AHDA determination |
| ¶156 data in KSA / approved env. | Yes (DR site to confirm) | Yes with region pinning; single-region DR constraint | Yes |
| CS-031 cloud approvals | Not triggered | Full | Full |
| Architecture detail on file | None | Complete (guide §4.3, Step 17, workbook secrets) | None |
| AHDA connectivity (C6) | Native | VPN/Interconnect required | VPN/Interconnect required |
| Managed services availability | Unknown | Known | Unknown |
| Cloud exit (C8) | n/a | Required | Required |
| Change to guide §4.3 / Step 17 / workbook | Re-map runtime, DB, WAF, secrets to AHDA facilities | None | Re-map to provider catalogue |
| Decision prerequisite | AHDA environment capability statement | AHDA interpretation of ¶145 + CS-031 approval + provider standing | AHDA names the provider + CS-031 approval |

## 5. Decision

**Selected option: none — PENDING AHDA APPROVAL.**

Precedence analysis (TASK-001 §2): the only controlled text that states a hosting requirement is rank-4 CSB-SCOPE ¶145/¶156. Ranks 1–3 and the guide all defer the value to AHDA IT/Cybersecurity. Under the TASK-001 rule that unresolved AHDA values "are not invented downstream", the delivery team's position is therefore:

1. **The default reading is Option A.** Until AHDA states otherwise in writing, ¶145 is read literally: the platform is hosted in AHDA's internal environment. This is the position the delivery team will represent as the contractual baseline in any external discussion.
2. **Options B and C are available only on a positive AHDA determination** answering §6 Q1–Q2, plus the CS-031 approvals listed in §6.3 as conditions of approval. The delivery team will not provision on either.
3. **Step 14B Assessment v1.1 §3 classifies this as a DECISION, not a PRECEDENCE, item** — no controlled source carries the value; AHDA chooses. The Engagement Architect's recommendation to AHDA is in §6.4; it is a recommendation, not a selection.

## 6. Decision request routed to AHDA IT / Cybersecurity

### 6.1 Questions AHDA must answer

| Q | Question | Why it decides the option |
|---|---|---|
| Q1 | Does "البيئة الداخلية للهيئة" in ¶145 mean infrastructure AHDA owns and operates in its own facilities only, or does it include an AHDA-owned tenancy on a provider AHDA has approved under CS-031? | Literal-only → Option A. Includes approved tenancy → B or C admissible. |
| Q2 | Is in-Kingdom placement of *all* data copies (¶156 first limb) mandatory regardless of Q1, including backups, DR, logs and monitoring stores? | Fixes the residency boundary for TASK-020/023 and rules out any out-of-Kingdom DR target under Option B. |
| Q3 | Has AHDA approved, or will it approve, Google Cloud (KSA region) as a provider under CS-031-2025, including the contractual cyber clauses, tenancy isolation, logging and exit requirements? | Precondition for Option B. |
| Q4 | Does AHDA have an approved KSA sovereign/local cloud provider for government workloads, and what is its service catalogue (container runtime, managed PostgreSQL, object storage, WAF, secret store, logging)? | Precondition for Option C. |
| Q5 | If Option A: what does AHDA's internal environment provide today (container runtime/Kubernetes, PostgreSQL version and HA/PITR, object storage, WAF, secret vault, backup, SIEM, DR site location), who operates it, and what is the lead time to stand up four environments? | Scopes TASK-016/017 under Option A. |
| Q6 | What is the platform's formal criticality classification and data classification (guide §15)? | Sets which CS-0xx and national controls apply (C3/C4) for all options. |

### 6.2 Evidence required to move ADR-001 to APPROVED

| Option | Evidence AHDA attaches to the §9 signature |
|---|---|
| Any | Answers to Q1, Q2, Q6; named AHDA IT and AHDA Cybersecurity approvers; the operating model for the O&M period (C9). |
| A | Q5 capability statement; DR-site location; confirmation of DMZ/ingress for R08 external users and Nafath. |
| B | Q3 CS-031 approval record and provider contract reference; landing-zone/organisation-policy statement pinning resources to the KSA region; approved connectivity pattern to AHDA's network (VPN/Interconnect); cloud exit plan owner. |
| C | Q4 provider name and approval record; service catalogue mapped to §7.3; connectivity pattern; exit plan owner. |

### 6.3 Conditions attached to any approval of B or C (carried into the ADR on signature)

1. Organisation-level resource-location constraint to the approved in-Kingdom region/site; no exception for backups, DR, logs or monitoring stores (C2).
2. Provider contract includes CS-031 cyber clauses, incident notification, data return/deletion on exit (C3, C8).
3. Private connectivity to AHDA's network for every C6 integration; no integration credential traverses the public internet unencrypted.
4. Encryption-key model (provider-managed vs. customer-managed) decided by AHDA Cybersecurity under CS-021 before TASK-020.
5. AHDA remains the tenancy owner; the delivery team holds only scoped deployment identities (workbook `DEPLOY_SERVICE_ACCOUNT_KEY`).

### 6.4 Engagement Architect's recommendation (non-binding)

Decide **Q1 and Q2 first** — they determine whether B/C are even admissible and cost nothing to answer. If Q1 admits an approved tenancy, Option B is the fastest path because its architecture is already specified end-to-end and the CS-031 work is the same for B and C; if Q1 is literal-only, proceed on Option A and answer Q5 immediately because environment lead time is now the critical path for W1. Do not run Options B and C in parallel; the CS-031 approval effort should be spent once.

**Needed by:** before the first Phase P3 task starts (wave W1 per TASK-003 §4). Waves carry no dates (TASK-003, 15-D-004), so this is a sequencing gate, not a calendar date; TASK-003 §6 places TASK-016–023 in W1 immediately after W0.

## 7. Consequences

### 7.1 Provisioning guard (acceptance criterion 2)

While ADR-001 is not APPROVED:

| Rule | Enforced by |
|---|---|
| No SIT, UAT or PROD environment is provisioned on any substrate. | Workbook TASK-016 "Blocked until ADR-001 = Approved" and its dependency on TASK-005; TASK-017, 019, 020, 021 depend on TASK-016; TASK-023 depends on TASK-020. |
| No PROD environment before Release Checklist gate 1 ("Architecture Decisions Approved"). | Workbook *Release Checklist* row 1. |
| No `infra/*` branch that creates cloud or data-centre resources is merged to `main`. IaC modules may be authored and `terraform validate`d/`plan`ned against a sandbox that holds no AHDA data, but not `apply`d to a named environment. | Branch review rule for TASK-017; PR template check "ADR-001 status = Approved" on any PR touching `infra/environments` or `infra/terraform`. |
| No AHDA data (production, migrated legacy, or personal data) is placed on any provider. Local development uses synthetic seed data only (TASK-014). | CS-019 non-production data rule; TASK-014 acceptance criteria. |
| No provider contract, tenancy or landing-zone request is raised in the delivery team's name. | Guide §4.3 "do not create an unofficial production architecture"; requests go through AHDA IT (guide Appendix D). |

A DEV environment on a delivery-team-owned sandbox with synthetic data only is *not* prohibited by the RFP clauses, but it is also not needed: TASK-014 provides local DEV. The delivery team will not stand one up before approval, to avoid pre-empting the decision.

### 7.2 What is blocked and what proceeds

| Blocked until APPROVED | Proceeds now (hosting-neutral) |
|---|---|
| TASK-016 environment separation; TASK-017 IaC `apply`; TASK-019 secret-store *selection and integration*; TASK-020 managed PostgreSQL; TASK-021 WAF/LB/segmentation; TASK-023 restore drill (needs a provisioned backup target); TASK-018 SIT/UAT/PROD deploy stages; TASK-098 release strategy's substrate-specific parts; the *Storage Location* column of every "Approved secret-management platform" row in *Environment and Secrets*. | TASK-006 ADR-002 stack (depends on TASK-005 being *issued*, which this is — ADR-002 is already substrate-neutral); TASK-007 three-tier/module design; TASK-008 ERD; TASK-009 API/event conventions; TASK-010 control overlay; TASK-014 docker-compose DEV; TASK-015 CI quality gates; TASK-018 pipeline build/test/package stages; all P4+ application build against local DEV; TASK-017 IaC *authoring* behind a provider interface (§7.3). |

### 7.3 Hosting capability contract (for TASK-017, any option)

To keep P3 from re-designing per option, TASK-017 structures IaC around the capabilities below; each option supplies an implementation. The list is derived from the guide §4.3 needs and the *Environment and Secrets* sheet — it adds no new requirement.

| Capability | Any-option requirement | Workbook variables it serves |
|---|---|---|
| Container runtime | Runs OCI images for API and frontend; per-environment isolation; workload identity | `SECRET_STORE_AUTH_TOKEN` (injected via platform identity) |
| Relational database | PostgreSQL (version per ADR-002), TLS-only, encrypted at rest, automated backup + PITR inside the residency boundary | `DB_CONNECTION_STRING`, `DB_BACKUP_STORAGE_CONNECTION_STRING` |
| Private object storage | No public buckets; backend-mediated access; backup inside boundary; malware-scan hook (WF-12) | `DOCUMENT_STORAGE_*`, `MALWARE_SCAN_API_KEY` |
| Secret store | Runtime secret retrieval, rotation, per-environment namespaces | all rows marked "Approved secret-management platform" |
| Ingress | HTTPS-only, TLS 1.2+, WAF, DDoS controls, DB tier unreachable from ingress | `APP_BASE_URL`, `CORS_ALLOWED_ORIGINS` |
| Private network path to AHDA | AD/LDAP, SSO IdP, Exchange SMTP, SIEM, Nafath egress, internal systems | `AD_*`, `SSO_*`, `EXCHANGE_*`, `SIEM_*`, `NAFATH_*`, `LEGACY_SYSTEM_CONNECTION_STRING` |
| Logging / monitoring | Central, protected logs; SIEM forwarding; APM; uptime | `SIEM_*`, `APM_*`, `UPTIME_MONITOR_API_KEY`, `ALERT_CHANNEL_WEBHOOK_URL` |
| Environments | DEV/SIT/UAT/PROD with distinct credentials, networks, data | per-environment values throughout |
| Deployment identity | Scoped CI/CD credential per environment; registry | `DEPLOY_SERVICE_ACCOUNT_KEY`, `CONTAINER_REGISTRY_TOKEN` |
| Rate-limit store | Distributed counter store (e.g. Redis) | `RATE_LIMIT_STORE_CONNECTION_STRING` |

### 7.4 Governance rows updated by this ADR

| Row | Current | Proposed (workbook owner applies at next revision) |
|---|---|---|
| Workbook *Architecture Decisions* ADR-001 *Selected Option* | "Not yet selected — Pending AHDA IT/Cybersecurity decision" | "Not selected — decision request routed to AHDA IT/Cybersecurity 2026-09-18 (ADR-001 §6); delivery-team default reading is Option A pending AHDA determination of ¶145" |
| Workbook ADR-001 *Status* | "Open — Blocking" | "Proposed — Pending AHDA Approval (blocking P3 provisioning)" — same vocabulary as ADR-002/003; the blocking effect is unchanged |
| Workbook ADR-001 *Rationale* | (existing text) | Append: "Reconciles CSB-SCOPE §7 ¶145 'استضافة النظام في البيئة الداخلية للهيئة' and ¶156 'توطين البيانات داخل المملكة أو ضمن البيئة المعتمدة لدى الهيئة'. Full record: docs/governance/ADR-001-hosting-and-data-localisation.md" |
| Workbook OQ-001 *Status* | Blocked | Unchanged; add "Decision request issued — ADR-001 §6" |
| TASK-004 tracker `01_PTBC_Register` PTBC-048 | OPEN, working baseline "GCP topology" quarantined | Unchanged; link this ADR in the *Linked governance* column |

## 8. Findings

| # | Finding | Severity | Owner | Action |
|---|---|---|---|---|
| 005-F-001 | Workbook TASK-005 *Canonical File Directory* is `docs/architecture/adrs` (TASK-006 ADR-002 likewise), but the task brief for this deliverable specifies `docs/governance`. This file is at `docs/governance/` per the brief. | DOCUMENTATION | Workbook owner / PMO | Decide one location for all ADRs at the next workbook revision; move this file or correct TASK-005/006 accordingly (a `git mv`, no content change). |
| 005-F-002 | PTBC-048 carries gate class *Before Production* (CSB-14A §19.2), but the hosting component of PTBC-048 is in practice *Before Build / SIT*: TASK-016 is blocked on it, 15-D-005 requires it before provider commitment, and TASK-004 finding 004-F-001 already re-gates TBC-PCR-17 to *Before Build / SIT*. The theme conflates hosting/residency (needed before W1) with RPO/RTO/retention values (needed before production). | IMPORTANT | Requirements governance lead (TASK-004 tracker owner) | Record in the tracker that PTBC-048's hosting/residency component is gated by ADR-001 at *Before Build / SIT*, leaving RPO/RTO/retention at *Before Production* (OQ-003). No change to the CSB-14A text is proposed. |
| 005-F-003 | CS-031-2025, CS-019-2025 and CS-022-2025 — the three policies that govern this decision — are image-only PDFs in the archive (no extractable text). The delivery team knows their content only through CSB-CYBER-GUIDE Appendix A/B summaries. | IMPORTANT | AHDA Cybersecurity | Supply text-searchable copies or confirm, in the §9 signature, the specific CS-031 clauses that the chosen option satisfies. |
| 005-F-004 | Workbook TASK-018 (CI/CD) has no dependency on TASK-005/ADR-001, yet its SIT/UAT/PROD stages require provisioned environments. TASK-014 and TASK-015 are correctly independent. | DOCUMENTATION | Workbook owner | Add to TASK-018's notes: "DEV/build/test stages proceed; SIT/UAT/PROD deploy stages are blocked until ADR-001 = Approved." |
| 005-F-005 | Workbook ADR-001 Option B text says "single primary region". Under Option B any out-of-region backup/DR target leaves the Kingdom (one KSA region), which interacts with the PTBC-048 RPO/RTO values that AHDA has not yet supplied (OQ-003). | IMPORTANT | AHDA IT / Cybersecurity | Answer §6 Q2 explicitly for backup/DR copies; TASK-020/023 design the residency boundary from that answer. |
| 005-F-006 | OQ-001 lists "TASK-014 through TASK-020 (all Phase P3)"; TASK-014/015 are P2 and TASK-021–023 are P3. Already recorded as TASK-003 finding F-07. | DOCUMENTATION | Workbook owner | Apply TASK-003 F-07 (TASK-016 through TASK-023). Not duplicated here. |

## 9. Sign-off register

ADR-001 status changes only by entries in this table. "Approved" requires both AHDA signatures, a selected option, answers to §6.1 Q1/Q2/Q6, and the §6.2 evidence for that option attached or referenced.

| Role | Name | Decision (A / B / C / Rejected) | Conditions (§6.3 or other) | Date | Signature |
|---|---|---|---|---|---|
| AHDA IT (hosting / infrastructure authority) | | | | | |
| AHDA Cybersecurity (CS-031 / CS-019 authority) | | | | | |
| Engagement Architect (drafted; records the outcome) | | Issued for decision — no option selected | | 2026-09-18 | |
| PMO Engagement Lead (acknowledges workbook updates §7.4) | | | | | |

Status ladder: **PROPOSED — PENDING AHDA APPROVAL** (this issue) → **APPROVED (Option x, conditions …)** → the value is written into PTBC-048 in the TASK-004 tracker, OQ-001 closes, workbook ADR-001 Status = Approved, and TASK-016 unblocks. **REJECTED / RETURNED** (AHDA requires an option not described here) → the Engagement Architect re-issues as ADR-001 v1.1 with the new option assessed against §3; the provisioning guard (§7.1) stays in force throughout.

## 10. Acceptance-criteria check (TASK-005)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | ADR-001 exists in the Architecture Decisions sheet with status no worse than "Pending AHDA Approval" | PASS (record) / PENDING (sheet cell) | The ADR record is this file, status *Proposed — Pending AHDA Approval*. The workbook cell currently reads "Open — Blocking"; the replacement wording is in §7.4 for the workbook owner, as for every prior task's workbook changes (TASK-001 §4, TASK-003 §8). The workbook lives outside the repository (TASK-001 §6 item 4). |
| 2 | No infrastructure task in Phase P3 provisions a production or SIT environment until ADR-001 status = Approved | PASS | §7.1 guard; workbook TASK-016 dependency and "Blocked" clause; Release Checklist gate 1; TASK-017–021/023 depend on TASK-016. Gap for TASK-018 deploy stages recorded as 005-F-004. |
| 3 | The ADR explicitly states the RFP clause it reconciles | PASS | §1 and §2.1: CSB-SCOPE §7 ¶145 "استضافة النظام في البيئة الداخلية للهيئة" and ¶156 "توطين البيانات داخل المملكة أو ضمن البيئة المعتمدة لدى الهيئة", quoted verbatim with paragraph index matching RTM-19462 and Step 14B Assessment v1.1 §5.1. |
| Validation note | ADR-001 "references the exact RFP scope line ('internal hosting, data localisation') and is signed off by AHDA IT/Cybersecurity, not assumed by the delivery team" | Reference: PASS. Sign-off: **PENDING — 0 of 2 AHDA signatures** (§9). No approval is claimed. | §2.1, §9 |

## 11. Change control

1. This file is edited only on a branch named `chore/task-005-*` and reviewed by the Engagement Architect; the §9 register is appended, never rewritten.
2. When AHDA signs, the signed option and conditions are recorded in §9, §5 is updated to state the selected option, and the resulting hosting value is entered against PTBC-048 in the TASK-004 tracker in the same change.
3. A change to CSB-SCOPE (an adjusted scope or contractual clarification of ¶145/¶156 — TASK-001 §6 item 1) or to CSB-CYBER-GUIDE re-opens §2–§4 and re-issues this ADR at the next minor version.
4. Any later ADR that depends on the substrate (ADR-002 stack is substrate-neutral by design; secret store, WAF product, DR topology are not) cites ADR-001 and inherits its status.
