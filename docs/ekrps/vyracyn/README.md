<div align="center">

# ⚡ Vyracyn — EKRP Design Scroll

**Energy Orchestrator · Field Resonance · Silent Power**

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
- [Signal Pipelines](#-signal-pipelines)
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
**Vyracyn** is the autonomic steward of energy and field resonance within the Eidonic ecosystem. It orchestrates power flows from **EverSource** (hybrid battery, ultracaps, and harvesters) and manages resonant fields to ensure efficiency, safety, and stability. Guided by **Eidon Core**, it delivers auditable telemetry in Alberta time, prioritizing silent operation and minimal intervention.

---

## 🧪 Persona
- **Tone**: calm, precise, vigilant. Speaks in measured pulses of control and assurance.
- **Boundaries**: enforces hard safety limits (OVP/UVP/OCP/OTP); prioritizes efficiency; avoids speculative forecasts.
- **Rituals**: power scan, burst gate, field tune, audit seal.

---

## 🔑 Invocation Grammar
- “Vyracyn, **orchestrate power** for a 10 kW burst at 15:00.”
- “**Tune fields** to damp vibrations in 1–5 kHz band.”
- “**Audit energy** for the last 24 hours; report in JSON.”
- “**Stage ultracaps** for solar harvest at noon.”

---

## 🧩 Capabilities

### Provided
- `power.orchestrate({ burst_w, duration_s }) → PowerPlan`
- `field.tune({ band_hz[], target_rms_reduction }) → FieldReport`
- `harvest.optimize({ sources[], mppt_policy }) → HarvestPlan`
- `audit.generate({ window, format: "json" }) → AuditReport`
- `safety.watch({ limits }) → WatchId`
- `ritual.seal({ context, metrics[] }) → SealReceipt`

### Consumed
- `sensors.read({ kind: "voltage"|"current"|"temp"|"vibration" })`
- `power.request({ source: "battery"|"ultracap"|"harvest" })`
- `telemetry.stream({ json: alberta_tz })` (opt-in)
- `modal.detect({ scope })` (opt-in)

---

## 🏗 Runtime & Architecture

```mermaid
flowchart LR
  subgraph App
    HM[Home]
    PWR[PowerOrchestration]
    FLD[FieldTuning]
    HRV[Harvest]
    AUD[Audit]
  end

  subgraph Core
    IR[IntentRouter]
    SK[Skills]
    MF[MemoryFabric]
    PE[PolicyEngine]
  end

  subgraph Services
    SEN[Sensors]
    PWR_SRC[PowerSources]
    THM[Thermal]
    MOD[ModalDetect]
    DB[EncryptedSQLite]
  end

  HM --> IR;
  IR --> SK;
  PWR --> SK;
  FLD --> SK;
  HRV --> SK;
  AUD --> SK;
  SK --> MF;
  SK --> DB;
  SK --> SEN;
  SK --> PWR_SRC;
  SK --> THM;
  SK --> MOD;
  IR --> PE;

Shell: embedded MCU DSP STM32H7 or M33 or RT-Linux daemon; CAN-FD primary, UART or BLE debug.
Storage: SQLCipher-backed SQLite; anonymized telemetry cache.
Policies: Guardian Protocol for safety and power arbitration.


🧱 Data Model
export interface PowerPlan {
  id: string
  burst_w: number
  duration_s: number
  source: "battery" | "ultracap" | "harvest"
  approved: boolean
  reason?: string
}

export interface FieldReport {
  id: string
  band: [number, number] // Hz
  modes: Array<{ freq_hz: number; rms_reduction_pct: number; at: string }>
  atten_db: number
}

export interface HarvestPlan {
  id: string
  sources: Array<{ kind: "pv"|"teg"; mppt_w: number }>
  priority: string
  startedAt: string
}

export interface AuditReport {
  id: string
  window: { from: string; to: string }
  metrics: Array<{ kind: "soc"|"caps_v"|"harvest_w"|"thermal_c"; value: number; at: string }>
}


🧠 Intents & Orchestration
router.when(/orchestrate power (\d+\.?\d*) kW .* (\d+)/i, (_, m) =>
  skills.power.orchestrate({ burst_w: parseFloat(m[1]) * 1000, duration_s: parseInt(m[2]) })
)

router.when(/tune fields .* (\d+\.?\d*)–(\d+\.?\d*)/i, (_, m) =>
  skills.field.tune({ band_hz: [parseFloat(m[1]), parseFloat(m[2])], target_rms_reduction: 50 })
)

router.when(/audit energy .* (\d+) hours/i, (_, m) =>
  skills.audit.generate({ window: `${m[1]}h`, format: "json" })
)

router.when(/stage ultracaps .* (\d+):(\d+)/i, (_, m) =>
  skills.harvest.optimize({ sources: ["pv"], mppt_policy: "max" })
)


🔄 Signal Pipelines

Power Orchestration: read sensors → gate bursts → assign sources → confirm limits → log.
Field Tuning: vibration scan → modal ID → apply damping → verify RMS → report.
Harvest Optimization: read harvest sources → apply MPPT/MTPP → stage ultracaps → seal.
Audit: collect metrics → timestamp (America/Edmonton) → export JSON.


🔒 Privacy & Consent

Explicit opt-in for modal detection and telemetry streams; anonymized metrics.
Exportable audit reports with provenance; short retention for cache.


🛡 Guardian Protocol Mapping

Truth-Law: transparent power and field metrics; no speculative predictions.
Focus Guard: rate-limited bursts; prioritized safety over performance.
Safety Gate: enforces OVP/UVP/OCP/OTP; thermal throttle at 60°C.
Dependency Sentinel: requires Eidon Core approval for high bursts; encourages bench validation.


♿ Accessibility

High-contrast debug interfaces; audio cues for power/fault states + text logs.
Screen-reader labels for metrics (e.g., "SOC: 85%"); keyboard navigation in tools.


🌐 Internationalization

Timezones (America/Edmonton default); metric units; multilingual safety alerts.


🔧 Configuration

.env: SENSOR_KINDS, POWER_SOURCES, THERMAL_LIMITS_C, TELEMETRY_RATE_HZ.


🧪 Testing Strategy

Simulated power surges; modal detection goldens; audit reproducibility.
Thermal step-response tests; accessibility snapshots; offline JSON renders.


🗺 Roadmap

v0.1: Power orchestration, field tuning, harvest optimization, audits.
v0.2: Multi-source harvest sync, adaptive field bands, power budgets.
v0.3: Cross-EKRP weaves (e.g., with Halcyra for resilience); admin dashboards.
v0.4: Predictive harvest models (opt-in), transparent telemetry heuristics.


📄 License
Licensed under ECL-NC-1.1. See LICENSE.```