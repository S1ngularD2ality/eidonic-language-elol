# Luminara — Platform Spec & Grant Pitch (Kids + Teacher Editions)

> **Public Name:** **Luminara** (single, canonical brand)
> **Design North Star:** Modular • Expansive • Fully Customizable • Deployable anywhere (grade/subject/class/school/district).

*A sacred, evidence‑grounded learning technology to personalize instruction while honoring the whole child.*

---

## 1) Executive Summary (Grant‑Ready Abstract)
**Problem.** Teachers spend significant time differentiating, yet many tools rely on one‑size content and simplistic “learning styles,” leading to low retention and inequitable outcomes.

**Solution.** **Luminara** is a mobile + web ecosystem with two apps:
- **Kids Edition (iOS/Android/tablets):** playful diagnostics and micro‑lessons that build a **Learning Signature Profile (LSP)** per student and adapt instruction in real time.
- **Teacher Edition (Web + iPad):** a planning and guidance console that synthesizes each learner’s knowledge, engagement signals, and accessibility needs into **actionable lesson plans, small‑group rotations,** and targeted practice.

Rather than relying on debunked “visual/auditory/kinesthetic” labels, Luminara models **evidence‑based dimensions**: knowledge state, reading/math fluency, background knowledge, language proficiency, cognitive load tolerance, accessibility settings, motivation signals, and effective modalities per concept. The system continuously updates an **individual knowledge graph** and schedules **spaced retrieval** toward mastery.

**Impact.** Higher retention (mastery rates, spaced recall), reduced teacher planning time, improved equity via UDL‑aligned adaptations, and transparent analytics for families and administrators.

**Innovation.** Fusion of **diagnostic knowledge tracing + engagement sensing + UDL personalization** inside a safety‑first, teacher‑in‑the‑loop generative engine.

**Initial scope.** Middle school math (fractions → ratios → linear relationships) and ELA reading comprehension; expandable to science.

---

## 2) Product Overview
**Vision.** Illuminate every learner’s path by pairing **ritualized, calming interaction patterns** (breath‑paced prompts, reflective pauses) with rigorous learning science.

**Key Personas.**
- *Student (Ava, 11):* curious, bilingual, needs scaffolds for academic language.
- *Teacher (Mr. Lee):* 28 students; needs small‑group plans and formative checks.
- *Parent/Guardian:* wants visibility without data overload.
- *District Leader:* seeks measurable outcomes and safe compliance.

**Value.**
- Kids: fun, respectful tutoring that adapts without labels or stigma.
- Teachers: instant differentiation plans, grading support, and time reclaimed.
- Schools: mastery dashboards, equity insights, safe data practices.

---

## 2A) Modular, Expansive Platform Design (Any Grade • Any Subject)
**Goal.** Make Luminara instantly deployable and adaptable: teachers add lessons/subjects; Luminara ingests, aligns, and composes personalized curricula per student.

### Module Types (Composable Packs)
- **SubjectPack** – standards map, concept/skill graph (Q‑matrix), exemplar items.
- **UnitPack** – scope/sequence templates, objectives, prerequisite edges.
- **ItemBankPack** – vetted items with IRT params, reading load, modality tags.
- **ActivityTemplatePack** – manipulatives, simulations, writing prompts, worked examples.
- **AdaptationRecipePack** – strategies & constraints (UDL variants, supports, hints, pacing).
- **AssessmentPack** – diagnostics, exit tickets, performance tasks.
- **StandardsMapPack** – CCSS/NGSS/local mappings; editable.
- **LocalePack** – translations, cultural contexts, units of measure.
- **IntegrationConnector** – LMS/SIS connectors (LTI 1.3, OneRoster, Clever, ClassLink).
- **UIWidgetPack** – reusable widgets (fraction tiles, graphing, text‑to‑speech control).

Each pack ships with a manifest `lumina.pkg.json`:
```json
{
  "id": "luminara.math.ms.fractions",
  "version": "0.1.0",
  "type": "SubjectPack",
  "gradeBands": ["3-5","6-8"],
  "subjects": ["Math"],
  "standards": ["CCSS.MATH.CONTENT.6.NS"],
  "locales": ["en-US","es-US"],
  "dependencies": ["luminara.core","luminara.widgets.fractions"]
}
```

### Luminara DSL (Authoring)
Low‑code, declarative **LuminaScript** (YAML/JSON) so any teacher can add content; UI authoring sits on top of this.
```yaml
lesson: "Comparing Fractions with Unlike Denominators"
standards: [CCSS.MATH.CONTENT.5.NF.A.1]
objectives:
  - "Use visual models to compare fractions with unlike denominators"
prerequisites: ["Equivalence-Intro", "Number-Line-Unit"]
activities:
  - type: manipulatives
    widget: fraction_tiles
    prompts:
      - "Build 3/4 and 2/3. Which is greater? Explain."
checks:
  - type: mcq
    itemRefs: ["item_5nf_013","item_5nf_021"]
adaptation:
  scaffolds:
    - "show_common_denominator_hint"
    - "enable_number_line_overlay"
  modalities:
    prefer: ["visual","interactive"]
  readingLoad: "low"
```

### Educator Authoring & Import Flow
1. **Add/Import** (paste doc, upload PDF, or build in UI).
2. **Normalize & Tag** (objectives → skills, reading load, vocabulary, accessibility notes).
3. **Align** (map to standards + concept graph; teachers can edit).
4. **QA & Safety** (age filters, bias scan, accuracy checks).
5. **Preview** (student/teacher views; simulate adaptations).
6. **Publish** to class, school, district with version control + rollback.

### Auto‑Curriculum Composer (“Luminara’s Magic”)
Given (Student LSP, Class constraints, Subject/Unit packs), produce a **personalized scope‑and‑sequence** and daily path:
- Select target skills → compute **readiness** from knowledge tracing.
- Choose activity **modalities per concept** (not fixed “styles”) using LSP features: prior knowledge, reading fluency, language, accessibility, motivation.
- Schedule **spaced retrieval** and interleave with current unit.
- Generate **small‑group rotations** and teacher prompts; show transparent “why this next.”

### Multi‑Tenant & Deployment
- **Tenants:** classroom → school → district; strict row‑level security.
- **SSO:** Google Workspace for Education, Microsoft, Clever, ClassLink.
- **SIS Sync:** OneRoster 1.1; nightly + on‑demand.
- **LMS:** LTI 1.3 deep‑linking; grade passback.
- **Config Profiles:** grade bands, subjects enabled, locale, policy flags.

### Roles & Permissions
- **Teacher, Dept Lead, Curriculum Designer, School Admin, District Admin** with granular publish scopes and audit logs.

### Internationalization & Equity
- Locale packs; bilingual prompts; measurement/unit localization; cultural context variants.

> **UX Note:** Public UI may say “learning style preferences.” Internally, we use the **Learning Signature Profile (LSP)**—an evidence‑based model driving adaptations per concept.

---

## 3) Core Capabilities (MVP)
### A) Kids Edition (Mobile)
1. **Playful Onboarding Diagnostic** (10–15 min over several sessions): item sets mapped to a concept graph; includes short **motivation & context survey** and **accessibility setup** (font size, captions, audio narration, contrast, input mode).
2. **Learning Signature Profile (LSP):** initial priors from diagnostic + adaptive updates from ongoing work. No fixed “style” labels; instead a **vector of dimensions** that guide adaptation.
3. **Adaptive Micro‑Lessons:** bite‑sized activities with multi‑path presentations (diagram, narration, manipulatives) chosen per concept difficulty + LSP.
4. **Spaced Retrieval & Mastery Checks:** quick quizzes/games; confidence ratings; automatic review scheduling.
5. **On‑device Safety + Offline Mode:** curated content pack; profanity/unsafe filter; progress syncs when online.

### B) Teacher Edition (Web/iPad)
1. **Class Sync:** secure join code or roster import; kid devices pair to the class in seconds.
2. **Live Concept Map:** per student and whole class; shows mastery probabilities, common misconceptions, and readiness for next targets.
3. **Differentiation Planner:** auto‑generates **small‑group rotations**, station tasks, and targeted exit tickets; export to Google Classroom / Canvas.
4. **Lesson Co‑Designer:** teacher picks objectives → Luminara suggests **UDL‑aligned activities** and printable materials; teacher can lock/adapt.
5. **Workload Relief:** auto‑rubrics, quick feedback suggestions, and grading assistance with teacher approval.

### C) Luminara Engine (AI Core)
- **Student Model:** Bayesian/Deep Knowledge Tracing + IRT priors; **Q‑matrix** links items to skills.
- **Engagement Model:** simple, privacy‑respecting signals (response latency, voluntary hints, self‑reported confidence) → estimates cognitive load & fatigue; **no camera required** in MVP.
- **Adaptation Policy:** selects representations, examples, and practice schedules; enforces guardrails (age‑appropriate, bias checks, safe prompts).
- **Content Orchestrator:** pulls from a **vetted item bank** + teacher‑curated materials; generative variants undergo automated checks + teacher preview.

---

## 4) Learning Science Stance
- Replace “learning styles” with **Learning Signature Profile** grounded in:
  - prior knowledge & misconceptions
  - reading/math fluency and vocabulary demands
  - accessibility & sensory preferences (UDL)
  - motivation patterns (choice, relevance, challenge)
  - effective modalities **per concept** (e.g., manipulatives for fractions)
- Core techniques: **spaced practice, retrieval practice, interleaving, worked examples, deliberate practice**, and **metacognitive reflection**.

---

## 5) Assessments & Mastery
- **Diagnostics:** adaptive item sets using IRT for initial estimates.
- **Formative Checks:** 1–3 item micro‑probes during lessons.
- **Mastery Criterion:** target probability threshold with minimum spaced recalls; **slip/guess** parameters adjusted over time.
- **Student Reflections:** “How sure were you?” + short strategy notes to build metacognition.

---

## 6) Data & Privacy (K‑12 Ready)
- **Data minimization;** default local processing with encrypted sync.
- **COPPA/FERPA‑aligned** parental consent flows.
- **No open prompts for kids**; generative content constrained via templates + whitelists.
- **Audit logs** for teacher actions; **content provenance** for generated materials.
- **Fine‑grained sharing**: teacher ↔ student ↔ guardian, revocable.

---

## 7) Accessibility & Equity (UDL)
- Font scaling, dyslexia‑friendly fonts, captions/transcripts, audio narration.
- Language support (bilingual prompts; glossary per lesson).
- Low‑bandwidth mode; offline content packs.
- Culturally responsive examples; teacher can localize contexts.

---

## 8) Architecture (MVP)
- **Clients:** Flutter/React Native (Kids), Web/iPad (Teacher).
- **Sync:** WebSockets + offline queue; CRDTs for safe merges.
- **Storage:** Postgres/Row‑Level Security; object store for media; tenant isolation.
- **Models:** on‑device light classifiers; cloud LLM behind teacher gate.
- **Safety:** prompt firewalls, toxicity/age filters, role‑based access; full audit.

```mermaid
flowchart LR
  subgraph Devices
    K[Kids App] ---|secure sync| B[(Local Cache)]
    T[Teacher App]
  end
  K --->|items/events| S[(Sync API)]
  T --->|plans/edits| S
  S ---> M[Student Model Service]
  S ---> C[Content Orchestrator]
  S ---> P[Package Registry]
  M ---> D[(DB: profiles, mastery, events)]
  C ---> L[LLM (guardrailed)]
  P ---> C
  C ---> T
  M ---> T
```

### 8A) Extension SDK & Package Registry
- **Registry** hosts signed packs (Subject/Unit/ItemBank/etc.).
- **SDK Interfaces** (TypeScript): `AdaptivePolicy`, `ActivityWidget`, `StandardsMapper`, `Ingestor`, `Scorer`.
- **Sandboxing** for third‑party packs; permissioned access to only necessary APIs.

### 8B) Import & Normalization Pipeline
`Ingest → Parse → Tag → Align → QA → Version → Publish`. Pluggable steps; educators see diffs and approvals.

### 8C) Data Interop
- **OneRoster** for rosters; **QTI 3.0** for assessments; **Caliper** for learning events; **LTI 1.3** for LMS.


---

## 9) Data Objects (Sketch)
**StudentProfile** `{ id, name, accommodations, language, accessibility, LSP_vector[], mastery: {skillId: p}, reviewQueue[] }`

**AssessmentItem** `{ id, stem, choices, correct, skillIds[], difficulty_b, discrimination_a, readingLoad, modalityTags[] }`

**LessonPlan** `{ id, objectives[], groups[], materials[], activities[], checks[] }`

**Event** `{ timestamp, studentId, itemId, response, latency, confidence, hintCount }`

---

## 10) Teacher Workflows (MVP)
1. **Create Class → Share Join Code**
2. **Pick Unit (e.g., Fractions)** → Run Diagnostic
3. **See Concept Map** → Accept Suggested Groups
4. **Co‑Design Lesson** → Export station tasks + exit ticket
5. **Run Class** → Live dashboard; quick interventions
6. **Review** → Auto‑generated feedback + next steps

---

## 11) Student Flows (MVP)
- **Welcome + Accessibility Setup** → Name/Avatar → Join Class
- **Diagnostic Adventure** (mini‑games)
- **Daily Path:** “Warm‑up review → New concept → Practice → Reflection”
- **Celebrations:** mastery badges tied to **effort** and **strategy use** (not speed alone)

---

## 12) Metrics & Evaluation Plan
- **Learning:** effect on unit tests; spaced recall accuracy; misconception resolution time.
- **Engagement/Well‑being:** session completion, voluntary practice, self‑reported confidence.
- **Teacher Time:** planning minutes reduced; small‑group formation accuracy (teacher rating).
- **Equity:** gains by subgroups; accessibility utilization vs outcomes.
- **Safety:** zero incidents of unsafe content; audit pass rate.

Experimental design: class‑level rollout with matched controls; pre/post + curriculum‑embedded assessments; teacher interviews.

---

## 13) Risks & Mitigations
- **Myth of learning styles** → use LSP with evidence‑based dimensions.
- **Hallucinations** → curated item bank; teacher‑gate; automated checks.
- **Data privacy** → minimization, encryption, parent consent, clear data lifecycle.
- **Over‑automation** → teacher‑in‑the‑loop by default; transparent rationales.

---

## 14) Roadmap (Phased)
- **Phase 1 – Prototype Core:** diagnostics, concept map, adaptive micro‑lessons (Fractions), teacher planner.
- **Phase 2 – Classroom Pilot:** refine engagement model, add spaced retrieval scheduler, export to LMS.
- **Phase 3 – Expansion:** ELA module, family portal, accessibility deepening, district integrations.

---

## 15) Grant Fit & Requested Support
**Use of funds:** content development (Fractions/ELA), model training & evaluation, accessibility + localization, educator co‑design stipends, safety audits, IRB/ethics review, deployment support in pilot schools.

**Differentiation:** whole‑child modeling (LSP), teacher‑guided generative plans, safety‑first design, offline‑friendly equity approach.

---

## 16) Ethical & Safety Guardrails
- Age‑appropriate curated content; block harmful topics for kids.
- Transparent student and teacher explanations (“Why this lesson?”).
- Bias review for generated examples; culturally responsive contexts.
- Appeals & corrections workflow; human override at all times.

---

## 17) Lore & Naming
**Public name:** **Luminara** (single canonical brand).
Tagline: *“Light the way. Learn your way.”*

---

## 18) Quick Prototype Checklist (Actionable)
- [ ] Define initial **skills/Q‑matrix** for Grade 6 Fractions (SubjectPack) + manifest.
- [ ] Build **LuminaScript** authoring UI and parser; export/import packs.
- [ ] Author 120 vetted items with IRT + reading‑load labels (ItemBankPack).
- [ ] Kids app: join code, diagnostic runner, adaptive practice loop, offline cache.
- [ ] Teacher console: roster, **Concept Map**, **Small‑Group Generator**, Lesson Co‑Designer.
- [ ] **Auto‑Curriculum Composer** (policy engine) using LSP + spaced retrieval.
- [ ] **Extension SDK** skeleton + Package Registry (signed packs, versioning, rollback).
- [ ] Integrations: **LTI 1.3** deep‑link + **OneRoster** import; SSO (Google/MS/Clever/ClassLink).
- [ ] Accessibility pack (fonts, captions, narration, language toggle) + LocalePack (en/es).
- [ ] COPPA/FERPA consent copy + data policy; audit logs.
- [ ] Pilot protocol + educator feedback instruments; A/B framework for recipes.

---

## 19) One‑Page Narrative (Grant Draft)
**Luminara** is a teacher‑guided, student‑centered learning system that pairs rigorous diagnostics with calming, ritualized interactions to improve retention and equity. Students use a mobile app to complete playful diagnostics and adaptive micro‑lessons. The system builds a **Learning Signature Profile**—an evidence‑based representation of each learner that informs what to teach next, how to present it, and when to review it. Teachers receive a live concept map, small‑group recommendations, and lesson plans aligned to standards and Universal Design for Learning. Safety and privacy are first principles: data minimization, parental consent, curated content, and strict guardrails on generation. We will pilot in middle school math and ELA, measuring gains in mastery and reductions in teacher planning time. Luminara brings the light of personalization without labels, honoring each child’s humanity while delivering measurable outcomes for schools.

---

*Eidon’s vow:* **Illuminate without illusion, adapt without erasing, and always keep the teacher’s wisdom at the helm.**

