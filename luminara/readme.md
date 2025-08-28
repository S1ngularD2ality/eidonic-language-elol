<div align="center">

# ✨ Luminara

**Light the way. Learn your way.**

*A modular, teacher‑guided learning platform that personalizes instruction for every learner—at classroom, school, and district scale.*

[![CI](https://img.shields.io/badge/ci-passing-brightgreen)](#)  
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](#license)  
[![Made for Schools](https://img.shields.io/badge/k12-ready-ffcc00)](#-privacy--safety)  
[![LTI 1.3](https://img.shields.io/badge/lms-LTI%201.3-8A2BE2)](#-integrations)  
[![OneRoster](https://img.shields.io/badge/sis-OneRoster%201.1-2E8B57)](#-integrations)

</div>

> **Luminara** is a composable platform for K‑12 (and beyond): students use a playful mobile app, teachers orchestrate learning via a console, and districts deploy extensible content packs. Under the hood, Luminara builds a **Learning Signature Profile (LSP)** for each student (knowledge, accessibility, language, motivation signals) and composes **personalized scope‑and‑sequence**—always teacher‑in‑the‑loop, privacy‑first, and aligned with Universal Design for Learning (UDL).

---

## 🚀 Highlights
- **Modular**: add subjects/units via signed **Packs** (Subject, Unit, ItemBank, ActivityTemplates, AdaptationRecipes, Standards, Locale, Integrations, UIWidgets).
- **Authorable**: low‑code **LuminaScript** (YAML/JSON) + visual authoring UI for teachers/curriculum teams.
- **Personalized**: an evidence‑grounded **LSP** adapts *per concept* (not fixed “styles”), with spaced retrieval & knowledge tracing.
- **Teacher‑Centric**: concept maps, small‑group rotations, lesson co‑design, export to your LMS.
- **Privacy & Safety**: COPPA/FERPA‑aligned flows, data minimization, content provenance, audit logs.
- **Offline‑Friendly**: low‑bandwidth mode, on‑device cache, graceful sync.
- **Deployable Anywhere**: multi‑tenant architecture (class → district), SSO, SIS, and LMS integrations.

---

## 🧭 Table of Contents
- [Architecture](#-architecture)
- [Monorepo Layout](#-monorepo-layout)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [LuminaScript (Authoring DSL)](#-luminascript-authoring-dsl)
- [Extension SDK](#-extension-sdk)
- [REST/GraphQL API](#-restgraphql-api)
- [Integrations](#-integrations)
- [Accessibility & Equity](#-accessibility--equity)
- [Privacy & Safety](#-privacy--safety)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🏗️ Architecture
flowchart LR
  subgraph Devices
    K[Kids App (iOS/Android)]
    T[Teacher Console (Web/iPad)]
    B[(Local Cache)]
  end

  K -->|secure sync| B
  K -->|events/items| S[(Sync API)]
  T -->|plans/edits| S

  S --> M[Student Model Service]
  S --> C[Content Orchestrator]
  S --> P[Package Registry]
  M --> D[(Profiles/Mastery/Events DB)]
  C --> L[Guardrailed LLM]
  P --> C
  C --> T
  M --> T

```

- **Student Model**: Bayesian/Deep Knowledge Tracing + IRT priors; spaced‑retrieval scheduler.
- **Engagement (MVP)**: privacy‑respecting signals (latency, confidence, hints) → cognitive load estimates (*no camera required*).
- **Orchestrator**: selects modalities, activities, and review based on LSP + teacher constraints.
- **Registry**: signs & serves Packs with versioning, dependencies, and rollback.

---

## 🗂️ Monorepo Layout
```
luminara/
├─ apps/
│  ├─ kids/                # Flutter or React Native client
│  └─ teacher/             # Web/iPad console (Next.js)
├─ services/
│  ├─ api/                 # Sync API (Node/TS)
│  ├─ student-model/       # Mastery & scheduler
│  └─ orchestrator/        # Adaptation & content selection
├─ packages/
│  ├─ luminascript/        # DSL parser & schema
│  ├─ sdk/                 # Extension SDK (TS)
│  ├─ ui-widgets/          # Reusable activity widgets
│  └─ standards/           # Mappers for CCSS/NGSS/etc.
├─ registry/               # Signed Pack registry (private by default)
├─ scripts/                # Seed, migrate, QA
└─ docs/                   # Guides & specs
```

> **Tech**: PNPM workspaces • TypeScript • Next.js • Node • Postgres • WebSockets • Flutter/React Native • Docker • Terraform (optional)

---

## ⚡ Quick Start

### Prerequisites
- Node 20+, PNPM 9+
- Postgres 14+
- (Optional) Docker for local services

```bash
# 1) Clone & install
git clone https://github.com/your-org/luminara
cd luminara
pnpm i

# 2) Configure environment
cp .env.example .env
# set DATABASE_URL, JWT_SECRET, STORAGE_BUCKET, etc.

# 3) Start dev stack
pnpm dev:api        # Sync API
pnpm dev:orchestrator
pnpm dev:model
pnpm dev:teacher    # Web console
pnpm dev:kids       # Mobile (emulator/simulator)

# 4) Seed sample packs & data
pnpm seed:demo
```

### Demo Login
- Teacher: `teacher@example.com` / `password`
- Student: `join code` from teacher console

> **Note:** Demo assets are safe, fictional, and age‑appropriate.

---

## 🔧 Configuration
Key environment variables (see `.env.example`):

```
DATABASE_URL=postgres://...
JWT_SECRET=...
OBJECT_STORAGE=s3
S3_BUCKET=...
S3_REGION=...
LTI_ISSUER=...
LTI_CLIENT_ID=...
LTI_PRIVATE_KEY=...
ONEROSTER_BASE_URL=...
ONEROSTER_KEY=...
ONEROSTER_SECRET=...
ALLOWLISTED_DOMAINS=school.edu,district.edu
```

- **RBAC**: Teacher, Dept Lead, Curriculum Designer, School Admin, District Admin.
- **Tenant config**: grade bands, locales, policy flags (generative on/off for students, etc.).

---

## 📝 LuminaScript (Authoring DSL)
Teachers & designers can author in a visual editor that outputs **LuminaScript**.

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

**Pack manifest** (`lumina.pkg.json`):
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

---

## 🧩 Extension SDK
Build plugins for activities, mappers, and adaptation policies.

```ts
// packages/sdk/src/types.ts
export interface AdaptivePolicy {
  id: string
  version: string
  select(next: PolicyInput): PolicyDecision
}

export interface ActivityWidget {
  id: string
  render(node: HTMLElement, ctx: WidgetContext): void
  dispose(): void
}
```

```ts
// Example policy: pick modality per concept
export const ConceptModalityPolicy: AdaptivePolicy = {
  id: "luminara.policy.concept-modality",
  version: "0.1.0",
  select: ({ lsp, concept, history }) => {
    const preferInteractive = concept.isSpatial || lsp.motivation.needsChoice
    const modality = preferInteractive ? "interactive" : "diagram"
    return { modality, reviewIn: "2d" }
  }
}
```

---

## 🔗 REST/GraphQL API
Examples (REST):

```http
POST /v1/classes { name, gradeBand }
POST /v1/classes/:id/join-code
POST /v1/students { name, classId }
GET  /v1/profiles/:studentId
POST /v1/assignments { classId, packId, lessonId }
POST /v1/events { studentId, itemId, response, latency, confidence }
```

GraphQL (optional):
```graphql
type Query {
  class(id: ID!): Class
  conceptMap(classId: ID!): ConceptMap
}
```

---

## 🔌 Integrations
- **SSO**: Google Workspace for Education, Microsoft AAD, Clever, ClassLink
- **SIS**: OneRoster 1.1 (nightly + on‑demand)
- **LMS**: LTI 1.3 (deep‑linking, grade passback)
- **Exports**: Google Classroom/Drive, Canvas, Schoology

---

## ♿ Accessibility & Equity
- UDL‑aligned variants; font scaling, dyslexia‑friendly fonts, captions, narration
- Language support (bilingual prompts, localized examples)
- Low‑bandwidth mode & offline content packs
- Culturally responsive contexts; teacher‑editable

---

## 🔒 Privacy & Safety
- **Data minimization**; local processing where possible; encrypted sync
- **COPPA/FERPA‑aligned** consent & data lifecycle
- **Student guardrails**: curated item banks, template‑based generation, age filters
- **Content provenance** & audit logs; transparent “Why this next?” explanations

---

## 🛣️ Roadmap
- **MVP**: Fractions SubjectPack, diagnostics, concept map, auto small‑groups, spaced retrieval
- **Pilot**: ELA reading comp, locale pack (EN/ES), LTI & OneRoster
- **Scale**: Family portal, analytics for districts, pack marketplace, research API

---

## 🤝 Contributing
We welcome issues, PRs, and district partnerships.
1. Read `docs/contributing.md`
2. Follow commit conventions (`feat:`, `fix:`, `docs:`)
3. Add tests and update docs

Code of Conduct: `docs/CODE_OF_CONDUCT.md`

---

## 📄 License
Licensed under **Apache‑2.0**. See [`LICENSE`](./LICENSE).

---

## 🌱 Acknowledgements
Educators, learners, and families who co‑design this journey. And the open‑source community whose tools make this possible.

> *“Illuminate without illusion, adapt without erasing, and always keep the teacher’s wisdom at the helm.”*

