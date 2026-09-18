# ADR-002 — Application Technology Stack

| Control | Value |
|---|---|
| Task | TASK-006 — Ratify Application Technology Stack ADR (Phase P1 — Architecture Decisions, wave W0); depends on TASK-005 |
| Programme | AHDA Regional Project Management Platform (RPMO) |
| ADR ID | ADR-002 (workbook sheet *Architecture Decisions*, row 2) |
| Issue date | 2026-09-18 |
| ADR status | **PROPOSED — PENDING AHDA APPROVAL.** The delivery team **selects Option A** (§5). The selection is provisional on AHDA IT confirming that no AHDA technology standard mandates a different stack (§6). Becomes APPROVED when §9 is signed. |
| Blocking effect | None on W0. TASK-011 (monorepo) may scaffold against Option A now; the supersession rule (§7.4) governs if AHDA later selects a different stack. |
| Decision owner | Engagement Architect (decides, subject to §6); AHDA IT (confirms no conflicting standard) |
| Linked governance rows | Workbook ADR-002, ADR-003 (pattern), ADR-001 (substrate); Release Checklist gate "Architecture Decisions Approved"; PTBC-044 (TASK-004 tracker `03_Task_Links` TASK-006 → 044); Step 16 finding 16-F-001; Step 17 BE-001/BE-028; Step 15 decision 15-D-004 |
| Source digests verified 2026-09-18 | CSB-SCOPE `98d7a1eced0efb6f`; CSB-BP2 `cb2b4675e3509160`; CSB-16 `036b745ded8c76ce`; CSB-17 `d1a512e03517943c`; CSB-CYBER-GUIDE `81b725edf83635c7`; workbook `0c0ff4b0b495ae25` — all unchanged from TASK-001 / TASK-005 |

Sources and precedence per TASK-001 (`docs/baseline/controlled-source-baseline.md`). Documents are cited by their `CSB-*` register ID. Scope paragraphs are cited as `CSB-SCOPE ¶n` using the numbering established in ADR-001 §2.1 (¶145 = internal hosting, ¶156 = data localisation). Waves are those of TASK-003; PTBC IDs and gate classes are those of TASK-004; ADR-001 is `docs/governance/ADR-001-hosting-and-data-localisation.md`.

## 1. Decision statement

**Which languages, frameworks and database engine the platform is built on**, given that no controlled source prescribes one, the workbook already carries a working proposal (React + TypeScript SPA / ASP.NET Core modular monolith / PostgreSQL) and every *Canonical File Directory* value in the workbook is derived from it.

This ADR (a) ratifies or replaces that working proposal with a recorded rationale and the alternatives considered, (b) fixes the repository layout that the workbook's directory column presupposes, and (c) states the supersession rule that applies if AHDA later mandates a different stack.

## 2. Context — what the sources say

### 2.1 The RFP does not prescribe a stack, but constrains it (CSB-SCOPE, rank 4)

| ¶ | Arabic (verbatim) / English | Constraint on the stack |
|---|---|---|
| 57 | ويجب أن تكون مسارات العمل قابلة للتعديل والتهيئة دون الحاجة إلى إعادة تطوير جوهرية للنظام — workflows must be modifiable and configurable without substantial redevelopment | Configuration-driven behaviour (FG-04) must be first-class in the backend; no stack that hard-codes workflow. |
| 117–121 | Active Directory; LDAP / Single Sign-On; Microsoft Exchange والبريد الإلكتروني; النفاذ الوطني الموحد – نفاذ; الأنظمة الداخلية للهيئة | Mature, supported client libraries for LDAP/AD, OIDC/SAML, SMTP relay and OAuth-style national-ID integration are a hard requirement. |
| 126 | يجب تنفيذ الحل على شكل تطبيق ويب Web Application يدعم الاستخدام من أجهزة الحاسب والأجهزة المحمولة من خلال تصميم متجاوب | Responsive browser application; no native client. |
| 127–130 | هيكلية ثلاثية الطبقات Three-Tier Architecture: Presentation / Business Logic / Data | Presentation tier is a browser client talking to an API tier; the API tier alone reaches the data tier (CSB-BP2 §22.1; CSB-17 BE-001). |
| 132–134 | المنصة قابلة للتهيئة … النماذج / الإجراءات — platform configurable for forms and procedures | As ¶57. |
| 161–163 | اللغة العربية / اللغة الإنجليزية … واجهة المستخدم والوظائف والمكونات | Full Arabic + English including RTL layout, bidirectional text, locale-aware dates/numbers (CSB-16 §6). |
| 220–221 | مدة العقد … 24 شهراً … حوالي 22 شهراً من التشغيل والصيانة والدعم الفني | Every runtime must be under vendor/community support for the full O&M period, i.e. to at least Q4 2028. |
| **225** | *"Technology stack is not prescribed. The RFP defines the required functions, architecture and integrations but does not prescribe .NET, Java, Python, SQL Server, Power BI, etc."* | The stack is the delivery team's decision, made against the constraints above, subject to AHDA IT standards. |
| **227** | *"The RFP refers to both development/customization and having a configurable existing product. Therefore, the technical team should assess whether the best solution is a configurable enterprise platform, custom application, or a hybrid architecture rather than assuming a greenfield custom build."* | Build-vs-buy is a prior question. See §4.4 and finding 006-F-002. |

¶223–229 are an English "Important RFP Clarifications for the IT Team" note appended to the Arabic scope summary. ¶225 is the statement the workbook's ADR-002 rationale relies on ("the brief's stated RFP ambiguity").

### 2.2 The controlled sources (ranks 1–3) are deliberately framework-neutral

| Source | Text | Effect |
|---|---|---|
| CSB-16 §1 *Baseline limitations* | "No approved frontend technology stack, brand system, device matrix or final interface schema set was supplied. The specification is framework-neutral." | Step 16 supplies no frontend choice. |
| CSB-16 finding **16-F-001** *Technology decision* | "Select the stack through an explicit decision against approved hosting/security constraints, Arabic/RTL and accessibility needs, maintainability, testability, team capability, component governance and API integration." Gate: "Before technology commitment and visual baseline." Permitted work: "Framework-neutral contracts and proposed wireframes may proceed." | Names the selection criteria this ADR uses (§3) and makes this ADR the closure record for the *stack* half of 16-F-001. Brand, device matrix and design system stay open (AHDA design authority). |
| CSB-16 §6 | "no mandatory standard version or UI framework has been selected" | As above. |
| CSB-17 *Approval* | "No new AHDA approval, technology selection, policy value or test result is inferred." | Step 17 supplies no backend choice. |
| CSB-17 *Backend architecture and ownership* | "The guide identifies GCP as a direction subject to AHDA approval. It does not approve a particular runtime, database engine, region or service." | Same. |
| CSB-17 **BE-001** | "Logical domain modules with controlled data-access interfaces; deployment topology and database engine remain a design decision." | The engine is decided here; topology is ADR-001/ADR-003. |
| CSB-17 **BE-028** | "No unapproved stack choice is required by this handoff." | Step 17's requirements are implementable on any mainstream stack; nothing forces a choice. |
| CSB-15 §2 | "No dates, sprint counts, staffing, technology products, effort estimates or budgets are inferred." Decision **15-D-004**: "Estimate implementation effort after package refinement and stack/team decisions." | Effort estimation (execution planning) is downstream of this ADR. |
| CSB-BP2 §22 | "Blueprint v2.0 embeds platform-level outcomes without converting illustrative technology examples into mandatory products." | The Blueprint contains no product names for the application tiers. |

### 2.3 Domain governance input (CSB-CYBER-GUIDE, §3.3 of the register)

- §4.1: "Local PostgreSQL (or the approved database technology)"; §4.3: "Relational database → Cloud SQL for PostgreSQL". PostgreSQL is the only engine named anywhere in the source set — as an example "subject to AHDA standards", not a mandate.
- §4.3: "Containerize code so the runtime choice remains flexible." §3.5: tiers may run as separate processes/containers locally and must stay logically separated in any hosting.
- §16 action 1: "**Confirm the approved technology stack (front end, backend, database)** and containerize the application from day one." Action 2: three code areas — frontend, backend/API, database/migrations/infrastructure.
- Appendix A, CS-006 *Coding*: "Use secure coding practices and trusted/licensed components. Code standards, dependency governance, review checklist, supported libraries." — AHDA may hold a supported-libraries/approved-technology list; whether it does is §6 Q1.

### 2.4 What is already built on the working proposal

The workbook (ADR-002 row) carries Option A "solely to give this workbook concrete, navigable Canonical File Directory values". The following already assume it and are the reason the choice must be recorded now rather than at TASK-011:

- **ADR-003** (modular monolith, one module per WF/FG domain, "Proposed — Pending AHDA Approval") presumes a single backend solution with in-process module boundaries.
- **TASK-011** names the solution projects (`PMPlatform.Api`, `.Application`, `.Domain`, `.Infrastructure`), React + TypeScript with Vite, ESLint + Prettier, Roslyn analyzers, `dotnet build` / `npm run build`.
- **TASK-024** names `dotnet ef database update` and code-first migrations; **TASK-015** names `tsc --noEmit`; **TASK-032** names axe-core; **TASK-085** names Playwright/Cypress.
- **70 of 103** directory values sit under `src/backend/PMPlatform.*`, `src/frontend/`, `db/` or `infra/`; 64 of them are stack-dependent (§7.3).
- **ADR-001 §4.3 and §7.3** already describe the application as "containers + PostgreSQL + object storage + OIDC … provider-neutral", and the hosting capability contract lists "PostgreSQL (version per ADR-002)".

## 3. Selection criteria

Taken from 16-F-001, the scope constraints in §2.1 and the guide. Each option in §4 is assessed against these; "delivery-team assessment" is the engineering view.

| # | Criterion | Source |
|---|---|---|
| S1 | Three-tier, browser SPA over a protected API; the browser never reaches the database | CSB-SCOPE ¶127–130; CSB-BP2 §22.1; CSB-17 BE-001 |
| S2 | Substrate-neutral: runs as OCI containers on any ADR-001 option (AHDA internal, GCP, KSA sovereign cloud) with no provider SDK in business code | ADR-001 §7.3; guide §4.3 |
| S3 | Full Arabic/English with RTL, bidirectional identifiers, locale formatting; accessibility to the PTBC-040 target (working baseline WCAG 2.1 AA) | CSB-SCOPE ¶161–164; CSB-16 §6, Register 09 |
| S4 | First-class libraries for AD/LDAP, OIDC SSO, SMTP (Exchange), OAuth-style national ID (Nafath), SIEM forwarding | CSB-SCOPE ¶117–121; workbook *Environment and Secrets* |
| S5 | Supports the modular-monolith pattern of ADR-003 with enforceable module boundaries (API-03/P-08: no cross-module repository access) | Workbook ADR-003; CSB-17 *Domain boundaries* |
| S6 | Database supports the Step 17 integrity mechanisms: transactional outbox (BE-007), optimistic versioning (BE-005), idempotency ledger (BE-006), immutable append-only audit (BE-024), exact decimals with currency (BE-020), PITR backup (ADR-001 C7) | CSB-17 Technical_Requirements |
| S7 | Long-term support: every runtime under vendor/community support to ≥ Q4 2028; no licence cost or procurement dependency that AHDA has not approved | CSB-SCOPE ¶220–221; guide CS-006 "trusted/licensed components" |
| S8 | Maintainability and testability: static typing end-to-end, mainstream tooling for lint/format/type-check/unit/integration/e2e (TASK-015, TASK-084) | 16-F-001 |
| S9 | Team capability and hiring market for the 22-month O&M period, for both the delivery team and AHDA's eventual operators (TASK-097 handover) | 16-F-001; 15-D-004 |
| S10 | Compatibility with AHDA IT standards, if any exist (supported-library list, database standard, approved runtimes) | Guide CS-006; §6 Q1 |

## 4. Options

### 4.1 Option A — React + TypeScript SPA / ASP.NET Core (LTS) modular monolith / PostgreSQL (workbook working proposal)

| Tier | Selection | Pinned version and support horizon (verified at TASK-011 against the vendor's published support policy) |
|---|---|---|
| Presentation | React with TypeScript, built as a single-page application by Vite; served as static assets behind the ingress; talks only to the API tier | React 19.x; TypeScript 5.x; Vite current major; Node.js **24 LTS** for build tooling only (Node is not a runtime tier) — support to April 2028 |
| Business logic / API | ASP.NET Core on **.NET 10 (LTS)**, one deployable modular-monolith solution (ADR-003) organised as `PMPlatform.Api` / `.Application` / `.Domain` / `.Infrastructure`; Entity Framework Core with the Npgsql provider for persistence and migrations (TASK-024) | .NET 10 LTS — released November 2025, supported to **November 2028**. .NET 8 LTS is *not* selected: its support ends November 2026, inside the delivery window. |
| Data | PostgreSQL, single primary with PITR backup inside the residency boundary (ADR-001 C2/C7) | **PostgreSQL 17 minimum** (community support to November 2029); the exact major is the one the ADR-001 option's managed service supplies (TASK-020), never below 17 |

Assessment against §3:

| Criterion | Assessment |
|---|---|
| S1 | Native: SPA + Web API; EF Core is the only data-tier client. |
| S2 | Both tiers ship as OCI images (`mcr.microsoft.com/dotnet/aspnet` and an nginx/static image); PostgreSQL is offered as a managed service on GCP (guide §4.3) and is the most likely managed engine in a KSA sovereign catalogue; on AHDA internal infrastructure it is self-hostable without licence. No provider SDK is permitted in `Domain`/`Application` (§7.5). |
| S3 | React's ecosystem has mature RTL-capable component libraries and i18n tooling; `dir="rtl"` + CSS logical properties are standard; TypeScript makes the ar/en resource contract checkable. Library selection itself is deferred to TASK-007/frontend lead (§7.6). |
| S4 | .NET has first-party AD/LDAP (`System.DirectoryServices.Protocols`, cross-platform), OIDC (`Microsoft.AspNetCore.Authentication.OpenIdConnect`), SMTP and OAuth 2.0 client support; AHDA's identity estate (AD, Exchange) is Microsoft-native, which lowers integration risk for TASK-028/029/068. |
| S5 | One solution, one process; module boundaries enforced by project references and architecture tests (e.g. NetArchTest/ArchUnitNET) in CI — ADR-003's precondition. |
| S6 | PostgreSQL: transactional DDL, `SERIALIZABLE`/row-version patterns, `numeric` for exact money, JSONB for outbox payloads, partial/unique indexes for idempotency ledgers, logical replication and PITR via WAL archiving. All of BE-005/006/007/020/024 are implementable without extensions. |
| S7 | All open-source under permissive licences (MIT / PostgreSQL licence); no per-core or per-user licence; LTS horizons above cover O&M. |
| S8 | Static typing on both tiers; `dotnet` analyzers + xUnit/NUnit, ESLint + Prettier + `tsc` + Vitest, Playwright for e2e — exactly the TASK-011/015/085 tooling already in the workbook. |
| S9 | Both React and .NET are top-tier by hiring market in KSA and the region; AHDA's IT estate is Microsoft-based, which favours .NET for the operator handover. **Delivery-team capability is asserted, not evidenced on file** — the Delivery Lead confirms it in §9 (15-D-004). |
| S10 | Unknown until §6 Q1 is answered. |

Delivery-team assessment: satisfies every criterion the sources state; the only open item is S10, which is AHDA's to answer. This is the option the workbook, ADR-003, ADR-001 §7.3 and TASK-011–TASK-096 directory values are already written against, so selecting it creates no re-issue cost.

### 4.2 Option B — an AHDA-mandated stack

The workbook's Option B: "an AHDA-mandated stack, if AHDA IT standards require a specific platform not yet stated to the delivery team." No such standard is on file; guide CS-006 implies AHDA governs "supported libraries". This option cannot be assessed until AHDA states it; it is retained as the **supersession trigger** (§7.4), not as a competing selection. If AHDA's answer to §6 Q1 names a stack, this ADR is re-issued as v1.1 with that stack assessed against §3.

### 4.3 Alternatives considered per tier (and why not selected)

| Tier | Alternative | Assessment | Verdict |
|---|---|---|---|
| Presentation | **Angular** (TypeScript) | Meets S1, S3, S8 as well as React; built-in i18n and RTL are strong. Not selected because the workbook, Step 16 tooling assumptions and the wider component/talent market favour React (S9); no criterion is better served. | Rejected — equivalent, no advantage over the incumbent proposal |
| Presentation | **Vue** | Meets S1, S3, S8. Smaller enterprise talent pool regionally (S9); fewer RTL-audited enterprise component libraries. | Rejected — S9 |
| Presentation | **Blazor** (WebAssembly or Server) | Would unify the codebase on C#. Blazor Server breaks S1's tier separation (UI state lives on the server, persistent SignalR circuit per user — undesirable behind a WAF for R08 external users). Blazor WASM keeps the tier boundary but has a materially smaller RTL/accessibility component ecosystem (S3) and frontend talent pool (S9); CSB-16's framework-neutral design assumes a conventional SPA. | Rejected — S1 (Server) / S3, S9 (WASM) |
| Business logic | **Java / Spring Boot** | Meets every criterion; Spring Modulith supports S5. Not selected because AHDA's identity estate is Microsoft-native (S4 — AD, Exchange), the operator handover is to a Microsoft-oriented IT function (S9), and the workbook's tooling (`dotnet ef`, Roslyn analyzers) is already .NET. A Java selection would require re-issuing every `src/backend/PMPlatform.*` directory value. | Rejected — S4/S9 tilt to .NET; no criterion favours Java |
| Business logic | **Node.js / NestJS** (TypeScript) | Single language across tiers is attractive for S8/S9. Weaker on S4 (no first-party LDAP/AD or Kerberos stack; community libraries of varying maintenance), weaker default story for S5 (module boundaries are convention, not compiler-enforced) and for exact-decimal handling (BE-020) without extra libraries. | Rejected — S4, S5 |
| Business logic | **Python / Django or FastAPI** | Adequate for S1/S8; weaker on S5 (no compiled module boundary), S4 (AD/LDAP maturity) and on long-lived typed enterprise codebases maintained by a rotating O&M team (S9). | Rejected — S5, S9 |
| Data | **Microsoft SQL Server** | Natural in a Microsoft estate (S4/S9 for operators) and fully capable for S6. Not selected because: (i) it is the only candidate with a per-core commercial licence, which AHDA has not approved (S7); (ii) the only engine named by the guide is PostgreSQL (§2.3), and the GCP mapping is Cloud SQL for PostgreSQL; (iii) managed SQL Server is less likely in a KSA sovereign-cloud catalogue (S2). **If AHDA's database standard (CS-020) mandates SQL Server, this is the one substitution that leaves the directory values intact** (EF Core provider swap; migrations regenerated) — see §7.4 case 2. | Rejected — S7, S2; retained as the low-cost substitution |
| Data | **Oracle Database** | Commercial licence and procurement (S7); no source mentions it; heaviest operational footprint for a 150-user platform. | Rejected — S7 |
| Data | **MySQL / MariaDB** | Meets S2/S7. Weaker than PostgreSQL for S6: transactional DDL (MySQL) and mature JSON indexing, partial indexes and row-level security are less complete; PITR tooling is less uniform across managed offerings. | Rejected — S6 |

### 4.4 Build-vs-buy (CSB-SCOPE ¶227) — recorded, not decided here

¶227 asks the technical team to "assess whether the best solution is a configurable enterprise platform, custom application, or a hybrid architecture rather than assuming a greenfield custom build." No document in the TASK-001 register records that assessment. The entire controlled baseline — 21 WF/FG specifications, Blueprint v2.0, Step 14A–18 and the workbook's 102 tasks — is a custom-application design, so the delivery has proceeded on the custom-build reading. ADR-002 selects a stack *for a custom build*; it does not, and cannot, close ¶227. This is recorded as finding **006-F-002** for the PMO to attach the contractual disposition (accepted proposal / contract clause) to TASK-001 §6 as an open item, alongside the "adjusted scope" gap (14B-F-001).

### 4.5 Comparison

| | A — React / ASP.NET Core / PostgreSQL | B — AHDA-mandated | Nearest alternative set (Angular / Spring Boot / SQL Server) |
|---|---|---|---|
| Meets S1–S9 on current sources | Yes | Unknown | Yes, except S7 (SQL Server licence) |
| Consistency with workbook directory values | 63 of 64 stack-dependent values already conform; the exception is TASK-089 (§7.3) | Re-issue all | Re-issue all `src/backend/*`; frontend paths unchanged |
| Consistency with ADR-001 §7.3 and ADR-003 | Yes | Unknown | Yes |
| Licence exposure | None | Unknown | SQL Server per-core |
| Decision prerequisite | AHDA confirms no conflicting standard (§6 Q1–Q3) | AHDA states the standard | — |

## 5. Decision

**Selected: Option A — React + TypeScript SPA (Vite) / ASP.NET Core on .NET 10 LTS as a modular monolith with EF Core + Npgsql / PostgreSQL 17+.**

Precedence analysis (TASK-001 §2): no rank-1–4 source prescribes or forbids any stack (§2.1 ¶225, §2.2). Unlike ADR-001, this is therefore not an AHDA value that "must not be invented downstream" — it is an engineering decision that 16-F-001 explicitly assigns to the delivery team ("select the stack through an explicit decision against …"), conditioned only on AHDA IT standards the team has not been shown (S10). The delivery team accordingly **selects** Option A and records the status as *Proposed — Pending AHDA Approval* (workbook TASK-006 validation note) so that AHDA IT can confirm S10 before TASK-011 commits code.

What ADR-002 fixes:

1. Languages and frameworks per tier and the version floors in §4.1.
2. The persistence toolchain: EF Core code-first migrations (TASK-024) with the Npgsql provider; raw SQL for seed and validation scripts where migrations are unsuitable (TASK-027).
3. The repository layout in §7.1–§7.2, which is the canonical basis for every *Canonical File Directory* value in the workbook.
4. The substrate-neutrality rule in §7.5.

What ADR-002 does not fix — see §7.6 — includes the UI component library and design system (16-F-001 brand/device half; AHDA design authority), state-management and i18n libraries (TASK-007/frontend lead), the observability/APM products (PTBC-044, TASK-090/092), the secret store, WAF and container runtime (ADR-001), and any AHDA policy value.

## 6. Decision request routed to AHDA IT

### 6.1 Questions

| Q | Question | Why it decides the option |
|---|---|---|
| Q1 | Does AHDA IT maintain an approved-technology / supported-libraries standard (guide CS-006 "supported libraries") that mandates or prohibits any of: React, TypeScript, Node.js build tooling, .NET 10, ASP.NET Core, EF Core, PostgreSQL? | A mandate → Option B, re-issue (§7.4). No standard → Option A stands. |
| Q2 | Does AHDA's database policy (CS-020-2025 — image-only PDF, finding 005-F-003) set an approved engine list, version floor, or hardening baseline that PostgreSQL 17+ must meet? | Confirms S6/S10 for the data tier; a SQL Server mandate triggers §7.4 case 2. |
| Q3 | Does AHDA require commercial support contracts for open-source runtimes in production (e.g. a supported PostgreSQL distribution, Microsoft support for .NET)? | Affects S7 cost and the O&M operating model (OQ-009), not the selection. |
| Q4 | Under the ADR-001 option AHDA selects, which PostgreSQL major does the managed service (or AHDA's internal platform) provide? | Sets the exact version pin for TASK-020 within the ≥ 17 floor. |
| Q5 | Does AHDA confirm the custom-application reading of ¶227 (§4.4), or does it expect a configurable-platform assessment before build? | If the latter, ADR-002 and ADR-003 are void and the workbook is re-planned; see 006-F-002. |

### 6.2 Evidence required to move ADR-002 to APPROVED

Answers to Q1, Q2 and Q5 (a "no standard applies" answer is sufficient for Q1–Q2); the named AHDA IT approver; the Delivery Lead's confirmation of team capability (S9). Q3 and Q4 may follow and do not block approval.

**Needed by:** before TASK-011 merges the monorepo skeleton (W1, first task of Phase P2). TASK-011 may proceed on a `chore/task-011-*` branch in parallel; it merges only after §9 is signed or after the 006-F-001 fallback (below) is invoked.

**Fallback if AHDA does not answer before W1:** TASK-011 proceeds on Option A under this ADR's *Proposed* status; the cost of a later Option B supersession is bounded by §7.4 and grows with every W1/W2 task completed, which is the argument for answering Q1 now.

## 7. Consequences

### 7.1 Canonical repository layout (the basis for every *Canonical File Directory* value)

One monorepo (TASK-011). Paths are relative to the repository root. Everything under `src/` is stack-dependent and governed by this ADR; `infra/` is substrate-dependent and governed by ADR-001; `docs/` and `.github/` are stack-neutral.

| Path | Holds | Governed by | Workbook tasks (examples) |
|---|---|---|---|
| `/` | Solution file, `.editorconfig`, `CONTRIBUTING.md`, `README.md`, `.gitignore` | TASK-011 | 011 |
| `.github/` | `PULL_REQUEST_TEMPLATE.md`, `CODEOWNERS`; `workflows/*.yml` for CI/CD | TASK-012 | 012, 015, 018, 022, 080 |
| `src/backend/PMPlatform.Domain/` | Entities, value objects, domain events, invariants; **no framework or provider dependency** | ADR-003 / TASK-007 | (no task targets it directly — populated by every Feature task) |
| `src/backend/PMPlatform.Application/Features/<Module>/` | One folder per WF/FG module (§7.2): commands, queries, handlers, module-public application services, module DTOs | ADR-003 / TASK-007 | 031, 033–075 (Backend) |
| `src/backend/PMPlatform.Application/Common/<Concern>/` | Cross-cutting application concerns: `Authorization`, `Validation`, `Logging`, `Observability` | TASK-030/077/083/090 | 030, 077, 083, 090 |
| `src/backend/PMPlatform.Infrastructure/Persistence/` | EF Core `DbContext`s (one per module schema), configurations, `Migrations/` | TASK-024 | 024, 025, 026 |
| `src/backend/PMPlatform.Infrastructure/Identity/` | AD/LDAP, OIDC, MFA and `Nafath/` adapters | TASK-028/029/068 | 028, 029, 068 |
| `src/backend/PMPlatform.Infrastructure/<Provider>/` | Every other external adapter (object storage, SMTP, SIEM, malware scan, secret store, rate-limit store) behind an interface declared in `Application` | §7.5 | no task targets it directly; adapters are authored by the Feature task that needs them (037 storage, 039 SMTP, 033 SIEM) and by 019 (secret store) |
| `src/backend/PMPlatform.Api/` | ASP.NET Core host: controllers/endpoints, `Middleware/`, `HealthChecks/`, `appsettings.Template.json` | TASK-013 | 013, 078, 079, 091 |
| `src/backend/PMPlatform.Tests.Unit/` | Unit tests per project (xUnit) | TASK-015/084 | (implied by 015, 084) |
| `src/backend/PMPlatform.Tests.Integration/<Area>/` | Contract, integration and invariant-regression suites against a real PostgreSQL (Testcontainers or compose) | TASK-084 | 043, 054, 059, 065 |
| `src/frontend/` | Vite workspace: `package.json`, `.env.example`, `e2e/` (Playwright) | TASK-011/013/085 | 013, 085 |
| `src/frontend/src/features/<feature>/` | One folder per frontend feature (§7.2): routes, components, API client hooks, feature i18n resources | TASK-007 | 032, 036–076 (Frontend) |
| `src/frontend/src/content/help/` | In-app user guide / FAQ content, ar/en | TASK-096 | 096 |
| `db/seed/` | Idempotent SQL seed and data-integrity validation scripts (not migrations) | TASK-027 | 027 |
| `infra/docker/`, `infra/environments/`, `infra/terraform/{network,database,…}`, `infra/secrets/` | Local compose; IaC per ADR-001 option | ADR-001 | 014, 016, 017, 019, 020, 021, 100 |
| `docs/` | `baseline/`, `rtm/`, `planning/`, `governance/`, `architecture/` (+ `adrs/`), `security/`, `testing/` (+ `uat/`), `operations/`, `api/`, `onboarding/`, `handover/` | task briefs | 001–010, 023, 081–088, 092–095, 097–102 |

Rules that follow:

- Schema migrations live **only** in `src/backend/PMPlatform.Infrastructure/Persistence/Migrations/` (EF Core, TASK-024 naming `<timestamp>_<TaskID>_<description>`). `db/` holds SQL that is not a migration. There is no `db/migrations/` (finding 006-F-003).
- Test projects sit under `src/backend/` as the workbook already places them; this ADR does not move them to a top-level `tests/` because 4 directory values and TASK-011's `dotnet build` scope depend on the current placement.
- `PMPlatform.Domain` and `PMPlatform.Application` reference no ASP.NET, EF Core, or provider package; `Infrastructure` and `Api` are the only projects allowed to (enforced by an architecture test in CI, TASK-015).

### 7.2 Module → folder map (ADR-003 modules ↔ directory column)

The 21 backend `Features/` folders in the workbook map 1:1 to the WF/FG domains; the 19 frontend `features/` folders map to 21 domains with two composites and one gap.

| WF/FG | Backend `Features/<Module>` | Backend task | Frontend `features/<feature>` | Frontend task |
|---|---|---|---|---|
| WF-01 | `Project` | 041 | `projects` | 042 |
| WF-02 | `Progress` | 044 | `progress` | 045 |
| WF-03 | `Schedule` | 046 | `schedule` | 047 |
| WF-04 | `Task` | 048 | `tasks` | 049 |
| WF-05 | `Milestone` | 050 | `milestones` | 051 |
| WF-06 | `Risk` | 055 | `risks` | 056 |
| WF-07 | `ManagementConcern` | 057 | `issues-challenges` | 058 |
| WF-08 | `ChangeRequest` | 060 | `change-requests` | 061 |
| WF-09 | `Suspension` | 062 | `suspension-closure` (composite WF-09 + WF-10) | 064 |
| WF-10 | `Closure` | 063 | `suspension-closure` | 064 |
| WF-11 | `Approval` | 035 | `approvals` | 036 |
| WF-12 | `DocumentManagement` | 037 | `documents` | 038 |
| WF-13 | `ExternalParticipation` | 066 | `external-participation` | 067 |
| WF-14 | `FinancialKpi` | 052 | `financial-kpi` | 053 |
| WF-15 | `Notifications` | 039 | `notifications` | 040 |
| FG-01 | `Dashboards` | 069 | `dashboards` | 070 |
| FG-02 | `Reports` | 071 | `reports` | 072 |
| FG-03 | `IdentityAccess` | 031 | `identity-access` | 032 |
| FG-04 | `MasterDataConfig` | 034 | `master-data-config` — **reserved; no workbook task** (006-F-005) | — |
| FG-05 | `IntegrationMonitoring` | 075 | `integration-admin` | 076 |
| FG-06 | `AuditActivity` | 033, 073 | `audit-activity` | 074 |

Naming rule: backend module folders are PascalCase and are the module's identifier in ADR-003/TASK-007; frontend feature folders are kebab-case. TASK-007's description lists six modules under shorter names (`Concern`, `Change`, `Document`, `Notification`, `Dashboard`, `Report`) than the folders above; the folder names are canonical because 22 workbook rows use them — TASK-007 adopts them (006-F-004).

### 7.3 Directory-column audit (acceptance criterion 2)

All 102 *Canonical File Directory* values were classified against §7.1 on 2026-09-18 (workbook digest `0c0ff4b0b495ae25`; TASK-013's two comma-separated values counted separately, 103 values).

| Category | Values | Under `src/backend/PMPlatform.*` | Under `src/frontend/` | `db/seed` | `infra/` (ADR-001) | `docs/`, `/`, `.github` | Deviation |
|---|---|---|---|---|---|---|---|
| Backend | 22 | 22 | — | — | — | — | 0 |
| Frontend | 19 | — | 19 | — | — | — | 0 |
| Database | 4 | 3 | — | 1 | — | — | 0 |
| Authentication and Authorization | 2 | 2 | — | — | — | — | 0 |
| Security | 10 | 6 | — | — | 1 | 3 | 0 |
| Observability | 3 | 2 | — | — | — | 1 | 0 |
| Testing | 10 | 4 | 1 | — | — | 4 | **1** — TASK-089 `db/migrations` |
| Project Setup | 5 | 1 | 1 | — | 1 | 2 | 0 |
| DevOps | 4 | — | — | — | — | 4 | 0 |
| Infrastructure | 4 | — | — | — | 4 | — | 0 |
| Documentation | 5 | — | 1 | — | — | 4 | 0 |
| Architecture / Discovery / Release | 15 | — | — | — | 1 | 14 | 0 |
| **Total** | **103** | **40** | **22** | **1** | **7** | **32** | **1** |

Result: every Backend, Frontend and Database directory value is consistent with ADR-002 (criterion 2 **PASS**). One value outside those categories deviates (TASK-089, finding 006-F-003). The 21 backend `Features/` folders and 19 frontend `features/` folders are exactly the §7.2 set; no task targets a project outside `PMPlatform.{Api,Application,Domain,Infrastructure,Tests.Integration}`.

### 7.4 Supersession rule (acceptance criterion 3)

If AHDA selects a stack other than Option A (an answer to §6 Q1/Q2/Q5 that mandates a change), then, in this order:

1. This ADR is re-issued as **ADR-002 v1.1** with the mandated stack assessed against §3 and a new §7.1 layout.
2. **Every *Canonical File Directory* value in the workbook is treated as superseded** the moment v1.1 is issued — including values not yet touched by any task — and is re-issued in a **new workbook revision** by the workbook owner. No task uses a v1.0 directory value after that date; tasks in flight rebase their deliverables onto the v1.1 layout before merge.
3. The blast radius by case: **(a) database engine only** (e.g. SQL Server under CS-020): EF Core provider swap and migration regeneration in `PMPlatform.Infrastructure/Persistence`; no directory value changes; TASK-020/024/025/026/027/089 re-run. **(b) frontend framework only**: all `src/frontend/src/features/*` and `src/frontend/e2e` values re-issued (22 values); backend untouched. **(c) backend platform**: all `src/backend/*` values re-issued (40 values), ADR-003 re-issued, TASK-011/013/015/024 re-scoped. **(d) configurable platform (¶227)**: ADR-002 and ADR-003 are void; the workbook is re-planned from Phase P1.
4. ADR-001 §7.3 (hosting capability contract) is re-checked for the new runtime and database; ADR-001's status is unaffected.
5. The tracker row TASK-006 → PTBC-044 and the Release Checklist gate "Architecture Decisions Approved" are updated in the same change.

### 7.5 Dependency on ADR-001 (substrate neutrality)

ADR-002 is designed so that ADR-001's outcome does not change it (ADR-001 §7.2 lists ADR-002 as "already substrate-neutral"). The rule that keeps it so:

- `PMPlatform.Domain` and `PMPlatform.Application` contain **no** cloud-provider, storage-provider, secret-store, SIEM or APM SDK. Each such capability is an interface in `Application` implemented in `PMPlatform.Infrastructure/<Provider>/`, selected by configuration per environment (ADR-001 §7.3 capabilities table).
- Both tiers build to OCI images from the repository (TASK-022); the images are the deployment unit for every ADR-001 option.
- PostgreSQL is used through standard SQL and EF Core only — no managed-service-specific extension is a hard dependency, so the engine can be AHDA-hosted, Cloud SQL or a sovereign-cloud managed service.
- Frontend build output is static; where it is served (CDN, nginx container, storage bucket behind the WAF) is an ADR-001/TASK-021 decision.

### 7.6 Explicitly not decided by ADR-002

| Item | Where it is decided | Why not here |
|---|---|---|
| UI component library, design system, brand tokens, supported browser/device matrix | 16-F-001 (brand/device half) — AHDA design authority; TASK-007 records the library choice | Requires AHDA brand and device confirmation (CSB-16 §6, §7) |
| Frontend state-management, routing, i18n, form libraries | TASK-007 solution architecture | Implementation detail within the React selection; must satisfy S3 |
| Observability / logging / APM products | PTBC-044 (tracker: TASK-006 → 044 is the *nearest* theme; the application stack itself has no PTBC), TASK-090/092 | AHDA-approved product list; ADR-002 only requires OpenTelemetry-compatible instrumentation so the product choice is swappable |
| Secret store, WAF, container runtime, object storage, rate-limit store products | ADR-001 §7.3 and TASK-017/019/021 | Substrate-dependent |
| Message broker | ADR-003 / TASK-009 | The Step 17 outbox (BE-007) runs on PostgreSQL in-process by default; a broker is introduced only if TASK-009's event conventions require one |
| Mobile app | — | Out of scope: ¶126 requires a responsive web application, not a native client |

### 7.7 Governance rows updated by this ADR

| Row | Current | Proposed (workbook owner applies at next revision) |
|---|---|---|
| Workbook *Architecture Decisions* ADR-002 *Selected Option* | "Option A — React + TypeScript / ASP.NET Core / PostgreSQL (proposed, not yet AHDA-confirmed)" | "Option A — React 19 + TypeScript (Vite) / ASP.NET Core on .NET 10 LTS + EF Core / PostgreSQL 17+ — selected by the delivery team 2026-09-18, pending AHDA IT confirmation of no conflicting standard (ADR-002 §6). Full record: docs/architecture/adrs/ADR-002-technology-stack.md" |
| Workbook ADR-002 *Status* | "Proposed — Pending AHDA Approval" | Unchanged |
| Workbook ADR-002 *Options Considered* | (A) and (B) | Append: "(C) per-tier alternatives assessed and rejected in ADR-002 §4.3 — Angular, Vue, Blazor; Spring Boot, NestJS, Django/FastAPI; SQL Server, Oracle, MySQL/MariaDB" |
| Workbook TASK-089 *Canonical File Directory* | `db/migrations` | `docs/testing` (report) — see 006-F-003 |
| Workbook TASK-007 *Detailed Description* module list | `Concern, Change, Document, Notification, Dashboard, Report` | `ManagementConcern, ChangeRequest, DocumentManagement, Notifications, Dashboards, Reports` — see 006-F-004 |
| TASK-004 tracker `03_Task_Links` TASK-006 | → PTBC-044 (DIRECT) | Unchanged; add "ADR-002 §7.6: application stack has no PTBC; PTBC-044 covers the observability products only" in the note column |
| TASK-001 register §6 | 6 open items | Add item 7: "¶227 build-vs-buy disposition not on file" (006-F-002) |

## 8. Findings

| # | Finding | Severity | Owner | Action |
|---|---|---|---|---|
| 006-F-001 | ADR-001 (TASK-005) is at `docs/governance/` while the workbook's *Canonical File Directory* for TASK-005 and TASK-006 is `docs/architecture/adrs` (already recorded as 005-F-001). ADR-002 is placed at `docs/architecture/adrs/` per its brief and the workbook, so the two ADRs are now in different folders. | DOCUMENTATION | Workbook owner / Engagement Architect | Close 005-F-001 by `git mv docs/governance/ADR-001-hosting-and-data-localisation.md docs/architecture/adrs/` on a `chore/task-005-*` branch (ADR-001 §11 rule 1) and update the four references to that path (ADR-001 §7.4, TASK-004 tracker, this file's header, memory). No content change. |
| 006-F-002 | CSB-SCOPE ¶227 asks for a build-vs-buy assessment ("configurable enterprise platform, custom application, or hybrid"). No document in the TASK-001 register records one; the entire baseline presumes a custom build. ADR-002 selects a stack for a custom build and cannot close ¶227. | IMPORTANT | PMO Engagement Lead / AHDA scope owner | Attach the contractual disposition (accepted technical proposal or contract clause) to TASK-001 §6 as item 7; answer §6 Q5 in the ADR-002 signature. Linked: 14B-F-001. |
| 006-F-003 | Workbook TASK-089 *Canonical File Directory* is `db/migrations`. Under ADR-002 migrations live only in `src/backend/PMPlatform.Infrastructure/Persistence/Migrations`; TASK-089's deliverables are reports (validation report, legacy-migration plan), not code. | DOCUMENTATION | Workbook owner | Change TASK-089's directory to `docs/testing` at the next workbook revision. Only deviation found in the 103-value audit (§7.3). |
| 006-F-004 | TASK-007's module list names six modules differently from the 21 backend `Features/` folder names that 22 workbook rows (TASK-031–075) use (`Concern`/`ManagementConcern`, `Change`/`ChangeRequest`, `Document`/`DocumentManagement`, `Notification`/`Notifications`, `Dashboard`/`Dashboards`, `Report`/`Reports`). Three folder names are plural, eighteen singular. | DOCUMENTATION | TASK-007 owner (Engagement Architect) / Workbook owner | TASK-007 publishes the §7.2 folder names as the canonical module identifiers. If TASK-007 prefers uniform singular names, the three plural folders are renamed in the workbook in the same revision — one rename, before any W2 task starts. |
| 006-F-005 | FG-04 (Master Data & Configuration) has a backend task (TASK-034) but no frontend task in the workbook; the ADM-021–029 configuration screens have no owner and `src/frontend/src/features/master-data-config` has no task. | IMPORTANT | Workbook owner / PMO | Add an FG-04 frontend task in Phase P6 (wave W2, alongside TASK-034) at the next workbook revision, or record where ADM-021–029 are built. Cross-check against TASK-003 wave map and TASK-002 RTM coverage. |
| 006-F-006 | ADR-001 §2.1 cites the contract-duration lines as "¶226–227". By the ¶ numbering ADR-001 itself establishes (¶145/¶156/¶127 verified), those lines are ¶220–221; ¶226–227 are two of the English clarification notes. | DOCUMENTATION | ADR-001 owner | Correct to ¶220–221 at the next ADR-001 minor revision (§11 rule 1 of ADR-001). ADR-002 cites ¶220–221. |
| 006-F-007 | Team-capability (S9) and the effort/capacity basis for the stack (15-D-004) are asserted by the Engagement Architect and not evidenced in any controlled document. | DOCUMENTATION | Delivery Lead | Confirm in §9; attach the staffing assumption to the execution plan when 15-D-004 is closed. |

## 9. Sign-off register

ADR-002 status changes only by entries in this table. "Approved" requires the AHDA IT signature with answers to §6 Q1, Q2 and Q5, plus the Delivery Lead's S9 confirmation.

| Role | Name | Decision (A / B — state stack / Returned) | Conditions / answers to §6 | Date | Signature |
|---|---|---|---|---|---|
| AHDA IT (technology standards authority; CS-006 / CS-020) | | | Q1, Q2, Q5 (Q3, Q4 may follow) | | |
| Engagement Architect (selects, drafts, maintains) | | **A — selected** | Subject to AHDA IT confirmation of no conflicting standard | 2026-09-18 | |
| Delivery Lead (confirms team capability, S9; 15-D-004) | | | | | |
| PMO Engagement Lead (acknowledges workbook updates §7.7) | | | | | |

Status ladder: **PROPOSED — PENDING AHDA APPROVAL** (this issue; Option A selected by the delivery team) → **APPROVED (Option A)** (workbook ADR-002 Status = Approved; 16-F-001 stack half closed with this file as evidence; Release Checklist gate 1 row for ADR-002 satisfied) → or **SUPERSEDED (Option B: <stack>)** → §7.4 applies and ADR-002 v1.1 is issued. **RETURNED** (AHDA asks for more assessment without naming a stack) → v1.1 answers the request; TASK-011 continues on Option A unless AHDA instructs otherwise.

## 10. Acceptance-criteria check (TASK-006)

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | ADR-002 records a single selected stack with rationale and alternatives considered | PASS | §5 single selection with version pins; §3 criteria; §4.1 assessment; §4.2–4.3 nine alternatives assessed and rejected with the failing criterion named; §4.4 build-vs-buy recorded |
| 2 | Every subsequent Backend/Frontend/Database task's directory column is consistent with ADR-002 | PASS | §7.3 audit: 22/22 Backend, 19/19 Frontend, 4/4 Database values conform to §7.1; §7.2 maps all 21 modules. One non-B/F/D deviation (TASK-089) recorded as 006-F-003 |
| 3 | If AHDA later selects a different stack, all directory values in this workbook are treated as superseded and re-issued in a new workbook revision | PASS (rule stated) | §7.4 supersession rule, with blast radius per case and the workbook-revision trigger |
| Validation note | ADR-002 is explicitly labelled "Proposed pending AHDA approval" until AHDA confirms; directory paths are provisional on that approval | PASS | Control table status line; §5; §7.4 item 2 makes every directory value provisional on §9 |

## 11. Change control

1. This file is edited only on a branch named `chore/task-006-*` and reviewed by the Engagement Architect; the §9 register is appended, never rewritten.
2. When AHDA signs, the answers to §6 are recorded in §9, the control-table status is updated, and workbook ADR-002 Status is set to Approved in the same change. If the answer supersedes Option A, §7.4 is executed and this file is re-issued as v1.1 — the v1.0 layout in §7.1 is retained in v1.1 as a "superseded" appendix so old branch names and directory values can be traced.
3. A version-floor change (§4.1) — e.g. moving to .NET 12 LTS during O&M, or a PostgreSQL major upgrade — is a minor revision of this ADR recorded in §9 with the vendor support dates; it does not re-open §4.
4. A change to CSB-SCOPE ¶225/¶227 (adjusted scope, TASK-001 §6 item 1) or to guide CS-006/CS-020 content re-opens §2–§4.
5. ADR-003 (pattern), TASK-007 (module boundaries), TASK-009 (API conventions) and TASK-011 (monorepo) cite this ADR and inherit its status; none of them may introduce a language, framework or engine outside §5 without a revision here.
