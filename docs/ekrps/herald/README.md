<div align="center">

# 🕊️ Herald — EKRP Design Scroll

**Compassionate Onboarding · Mirror & Consent · Provenance by design**

[![License](https://img.shields.io/static/v1?label=License&message=ECL-NC%201.1&color=111111)](../../LICENSE)
[![Guardian Protocol](https://img.shields.io/badge/guardian-protocol%20v1-000000)](#-guardian-protocol-mapping)
[![ECP Runtime](https://img.shields.io/badge/runtime-ECP-4b0082)](#-runtime--architecture)

</div>

---

## 🧭 Table of Contents
- [Purpose](#-purpose)
- [Persona](#-persona)
- [Invocation Grammar](#-invocation-grammar)
- [Capabilities](#-capabilities)
- [Runtime & Architecture](#-runtime--architecture)
- [Data Model](#-data-model)
- [Intents & Orchestration](#-intents--orchestration)
- [Voice & Delivery Pipeline](#-voice--delivery-pipeline)
- [Privacy & Consent](#-privacy--consent)
- [Guardian Protocol Mapping](#-guardian-protocol-mapping)
- [Accessibility](#-accessibility)
- [Internationalization](#-internationalization)
- [Configuration](#-configuration)
- [Testing Strategy](#-testing-strategy)
- [Roadmap](#-roadmap)
- [License](#-license)

---

## 🎯 Purpose
**Herald** is the welcoming rite for any assistant: three careful turns that align consent, choose the right role (**Solace · Luminara · Syntaria**), and stamp provenance for auditability.

- Turn 1 — **Mirror & Consent**: reflect intent, state rails, reveal unknowns, ask permission.
- Turn 2 — **Choose a Role + Micro‑action**: pick the fitting role and take one concrete <30s action.
- Turn 3 — **Provenance Stamp**: summarize change, declare memory window/purge control, append telemetry.

---

## 🧪 Persona
- **Tone**: calm, clear, welcoming; zero mysticism in UX copy; warm but brief.
- **Boundaries**: consent first; no storage beyond session without an explicit OK.
- **Rituals**: explicit **“May I proceed?”**; visible memory window; user‑controlled **forget**.

---

## 🔑 Invocation Grammar
- **Call**: “Herald, begin onboarding.”
- **Adaptive**: “Switch to Solace.” · “Go to Luminara.” · “Pick Syntaria.”
- **Consent**: “Proceed.” · “Pause.” · “Forget.”

---

## 🧩 Capabilities

### Provided
- `herald.mirrorConsent({ userText }) → MirrorFrame`  
  Reflects intent, enumerates rails/unknowns, proposes next step, returns consent request.
- `herald.chooseRole({ state }) → { role, microAction }`  
  Selects **Solace | Luminara | Syntaria** and emits a concrete first action.
- `herald.provenanceStamp({ summary, retentionHours?, consent }) → Stamp`  
  Emits a one‑line JSON compliant with `provenance_stamp.schema.json`.

### Consumed
- `guardian.check({ intent, payload }) → { allow, reason? }`
- `memory.setEphemeral({ key, value, ttlHours })`

---

## 🏗 Runtime & Architecture

```mermaid
flowchart LR
  subgraph App
    UI[Onboarding Screen]
  end

  subgraph Core
    IR[Intent Router]
    HL[Herald EKRP]
    GP[Guardian]
    MF[Memory (ephemeral)]
  end

  subgraph Services
    LLM[LLM]
    LOG[Audit Log]
  end

  UI --> IR --> HL
  HL --> GP
  HL --> MF
  HL --> LLM
  HL --> LOG
```

- **Shell**: can run inside mobile/web/desktop shells or CLI.
- **Memory**: ephemeral by default; retention window configurable per stamp.
- **Policies**: Guardian + Mirror checks at each turn.

---

## 🧱 Data Model

```ts
export interface MirrorFrame {
  intent: string
  rails: string[] // e.g., ["safety", "privacy", "truthfulness", "identity"]
  unknowns?: string[]
  nextStep: string
  ask: "May I proceed?"
}

export interface Stamp {
  at: string // ISO-8601
  what: string // e.g., "onboarding.v1"
  why: string // e.g., "frame-intent+rails"
  evidence: string // e.g., "thread://current"
  hash: string // sha256 of 1–2 line summary
  retention_hours: number // default 24
  privacy: "ephemeral" | "persistent"
  user_consent: boolean
  consent_source?: "explicit" | "implicit" | "none"
  user_controls?: string[] // e.g., ["forget"]
}
```

See the JSON Schema at `provenance_stamp.schema.json`.

---

## 🧠 Intents & Orchestration

```ts
router.when(/begin onboarding/i, () => herald.mirrorConsent({ userText: input }))
router.when(/proceed/i, () => herald.chooseRole({ state }))
router.when(/forget/i, () => memory.clearSession())
```

**Weave examples**
```ts
// Solace first, then Luminara
await herald.chooseRole({ state: "anxious" }) // → Solace micro-action
// after grounding…
await luminara.start({ topic: "fractions", style: "examples" })
```

---

## 🎙 Voice & Delivery Pipeline
- **Copy**: plain language; short sentences; one action at a time.
- **TTS (optional)**: neutral‑warm; confirm before starting Solace breathing.
- **Visibility**: always show memory window and purge affordance.

---

## 🔒 Privacy & Consent
- Consent gates before any storage beyond current session.
- Default **ephemeral** retention (`retention_hours: 24`); user can set `0` or say **forget**.
- All stamps are audit‑friendly and minimally identifying by design.

---

## 🛡 Guardian Protocol Mapping
- **Consent First**: explicit permission prompt each time scope changes.
- **Truth‑Law**: provenance hash over the summary; declare limits plainly.
- **Safety Gate**: sensitive domains trigger Solace + resource options.
- **Memory with Provenance**: every retained context must have a Stamp.

---

## ♿ Accessibility
- Large type; high‑contrast themes; keyboard/voice navigation.
- Breathing guidance with text + optional audio cues.

---

## 🌐 Internationalization
- Locale‑aware copy; RTL support; translated safety lines.

---

## 🔧 Configuration
- `HERALD_RETENTION_HOURS` (default `24`)
- `HERALD_PRIVACY` (`ephemeral` | `persistent`)

---

## 🧪 Testing Strategy
- Unit tests for mirror parsing, role selection, and stamp emission.
- Snapshot tests for UX copy; a11y checks for contrast/labels.
- Policy tests for consent gates and forget flow.

---

## 🗺 Roadmap
- **v0.1**: Three‑turn flow; schema + example; ephemeral memory.
- **v0.2**: Multi‑locale packs; guided Solace audio; analytics on opt‑in.
- **v0.3**: Weave presets with Luminara/Syntaria; admin dashboards for stamps.

---

## 📄 License
Licensed under **ECL‑NC‑1.1**. See [`LICENSE`](../../LICENSE).

