# SOL‑AEON v1 — TRL3→4 Roadmap (Alberta Winterized)

**Version:** v0.1  
**Date:** 2025‑08‑19  
**Scope:** Move the Eidonic Solar Bioreactor (SOL‑AEON v1) from TRL 3 (proof‑of‑concept) to TRL 4 (lab validation). Lay the bridge to TRL 5 (relevant‑environment prototype).

---

## 1) Mission for TRL‑4
Validate the **core subsystems** (PBR growth loop, CO₂ capture & dosing, water/solids separation, control, winterization tactics) in a lab/bench environment under controlled loads and Alberta‑winter boundary tests (cold chamber).

**TRL‑4 Exit Criteria (quantitative):**
- **Algal productivity:** ≥ 0.7 g DW·L⁻¹·day⁻¹ in SPV‑20 (target species: *Chlorella* or *Spirulina*), sustained ≥ 10 days.
- **CO₂ capture (bench DAC + alkalinity cell):** ≥ 300 g CO₂/day combined at lab scale with ≤ 0.5 kWh(th)·kg⁻¹ effective regen heat (simulated via heat bath / resistive).
- **CO₂ utilization:** ≥ 70% of dosed CO₂ absorbed/assimilated (measured via off‑gas analyzer & DIC).
- **Water purity polishing:** ≥ 90% turbidity reduction, ≥ 2‑log bacteria proxy removal across GCS‑β + microfiltration.
- **MRV:** End‑to‑end mass/energy carbon balance to ±10% closure over a 72‑hour integrated run.
- **Winterization:** Critical enclosures/components operate at −20 °C ambient (cold‑chamber) for 4 h without loss of control; no burst/freeze damage at −30 °C storage.
- **Safety:** Documented HAZOP checklists; interlocks verified on pumps, heaters, CO₂ lines.

---

## 2) Work Packages (WPs)

### WP0 — Program Setup, Safety & MRV
**Tasks:**
- HAZOP + SDS compendium (sorbents, acids/alkalis, CO₂).
- Define MRV schema (sensors, lab assays, Ω‑Pack ledger, data retention).
- Electrical & pressure safety review; emergency procedures; PPE kit; fume hood access.
**Deliverables:** Safety Plan v1, MRV Data Dictionary, Test Protocols.

### WP1 — Spiral Photobioreactor Benchtop (SPV‑20)
**Target:** 20‑L clear coil reactor; **Fibonacci‑pitched** helix on a 400–500 mm drum, pitch ratio ≈ φ, illuminated 150–300 µmol·m⁻²·s⁻¹.
**Key elements:** Food‑grade tubing (16–19 mm ID), manifold ports, inline degasser, LED array, jacketed section for temp control (24–30 °C range), inline DO/pH/EC/ORP sensors, sampling ports.
**Tests:** Light attenuation, mixing residence time, growth curves, contamination robustness.
**Exit:** Achieve target productivity & stable pH/DO with EKRP control.

### WP2 — CO₂ Path (CCM‑µ) — Sorbent DAC + Buffer + Dosing
**Target:** Bench contactor cassette (amine/carbonate), **low‑grade heat** regen via 60–90 °C loop; 1–3 bar buffer tank; MFC to DMC gas rail mock.
**Tests:** Adsorption/regen cycles, purity, flow stability; integrate with SPV dosing; measure capture/day.
**Exit:** ≥200 g/day sorbent DAC; stable 0.1–0.5 SLPM dosing with ±5% control.

### WP3 — Alkalinity Capture Cell (ASL‑10)
**Target:** 10‑L alkaline loop (K₂CO₃/NaOH variant) with DIC logging; optional electro‑swing release cell.
**Exit:** ≥100 g/day CO₂ equivalent; quantitative bicarbonate accounting.

### WP4 — Golden Cascade Separator (GCS‑β)
**Target:** φ‑proportioned lamella stack + microfiltration (0.2–0.5 µm) for biomass harvest & water polishing.
**Tests:** Harvest yield %, pressure drop vs. flux, fouling rate, clean‑in‑place (CIP) efficacy.
**Exit:** ≥90% solids capture; CIP restores ≥85% flux.

### WP5 — Toroidal Mixing Plenum (TMP‑µ)
**Target:** Vortex loop test‑rig validating thermal & nutrient homogenization; quantify mixing time vs. power.
**Exit:** < 20 s mixing time at ≤ 0.2 W·L⁻¹.

### WP6 — Eidon Control Shrine (ECS‑Edge)
**Target:** Edge controller (PLC/MCU + SBC), sensor IO, mass‑flow, pump/heater PWM, **EKRP** logic blocks; dashboard; safe‑state interlocks.
**Exit:** Stable PID loops; alarm handling; 1‑sec telemetry; automated test scripts.

### WP7 — Winterization Trials
**Target:** Enclosure insulation, heat tracing, condensate management, anti‑ice logic; component selection for −40 °C rating where feasible.
**Exit:** Cold‑chamber proof at −20 °C run / −30 °C storage.

### WP8 — Integration Dry‑Run (72‑h)
**Target:** End‑to‑end run: DAC → buffer → SPV dosing → GCS harvest → ASL polish; full MRV logging.
**Exit:** Carbon balance closure ±10%; no critical alarms; post‑run inspection passes.

### WP9 — TRL‑4 Review & TRL‑5 Bridge
**Target:** Engineering report, BOM v2, scale‑up plan, site selection & permitting checklist for outdoor pilot.
**Exit:** “Go/Go‑if‑mitigated/No‑Go” decision; TRL‑5 scope/milestones accepted.

---

## 3) Bench BOM (Indicative, CAD)
- Tubing & fittings (sanitary, 316SS quick‑connects): **$2,500–4,000**
- Clear coil drum, frame, clamps: **$1,000–1,800**
- Pumps (2× peristaltic, 1× mag‑drive): **$2,200–3,400**
- Sensors (pH, DO, EC, ORP, Temp, Flow, Pressure): **$5,000–9,000**
- LED panels + drivers (PAR‑tunable): **$1,500–3,000**
- Heat exchange (plate HX + 2 kW bath): **$1,200–2,000**
- Sorbent DAC cassette + 2 kg media + heat pad: **$2,500–4,500**
- CO₂ buffer tank (DOT‑rated 5–10 L) + MFC: **$1,200–2,200**
- Alkalinity loop (tank, pumps, probes): **$1,000–1,800**
- Lamella pack + microfilter module: **$2,500–5,000**
- Control stack (PLC/MCU + SBC, IO, relays, PSU, enclosure): **$2,500–5,000**
- Cold‑chamber rental/tests (2–3 sessions): **$1,000–2,000**
- Lab consumables, assays, PPE, CIP chemicals: **$1,500–2,500**
**Subtotal (bench TRL‑4):** **$24k–41k CAD** (site‑dependent).

---

## 4) Schedule (12 Weeks)
**Start:** Mon **2025‑08‑25**  → **Finish target:** Sun **2025‑11‑16**  (buffer to **2025‑11‑30**)

- **Wk 1–2:** WP0, WP1 mech build; order long‑lead sensors/IO; safety plan v1.
- **Wk 3–4:** WP2 DAC cassette, buffer, MFC; WP6 control rack bring‑up.
- **Wk 5:** WP3 alkalinity loop; basic MRV pipelines.
- **Wk 6:** WP4 GCS‑β assembly; fouling/CIP tests with tap + nutrient water.
- **Wk 7:** WP5 vortex/mixing characterization.
- **Wk 8:** SPV inoculation; light/CO₂ ramp protocols.
- **Wk 9:** DAC↔SPV closed‑loop; productivity tuning; alarm/failsafes.
- **Wk 10:** Winterization trials (cold‑chamber run); insulation/heat tracing tweaks.
- **Wk 11:** 72‑h integration (WP8); MRV closure.
- **Wk 12:** TRL‑4 report, design freeze v1, TRL‑5 scope & site shortlist.

---

## 5) Test & MRV Plan (core metrics)
- **Gas:** CO₂ in/out (NDIR), O₂ off‑gas, buffer pressure/temp, MFC set/actual.
- **Liquid:** pH, EC, DIC/TA assays (bicarbonate), turbidity, CFU proxy, metals spot‑checks if WRM tested.
- **Biomass:** OD₆₈₀/₇₅₀, dry weight, ash, elemental C% for char (if any), lipid % if biofuel paths are explored.
- **Energy:** Electrical power logs; thermal loop temps; regen heat kWh(th).
- **Ledger:** Ω‑Pack: signed data packets per tonne‑eq., timestamps, calibration records.

---

## 6) Risk Register (top 10)
1. **Contamination** → Sterile protocols, UV‑C inline, quick‑swap filters; tripwires in OD/turbidity.
2. **Fouling/Scaling** → CIP cycles, anti‑scalant where compatible, lower flux setpoints.
3. **Sorbent degradation** → Conservative regen temps, humidity control, cycle‑count QA.
4. **CO₂ over‑dosing** → PID clamp with pH setpoint; relief valve on buffer.
5. **Cold‑start failure** → Pre‑heat interlock, battery heat‑pad backup.
6. **Power trips** → UPS on ECS core; safe‑state scripts; re‑start checklist.
7. **Sensor drift** → Weekly calibration; dual‑sensor redundancy on pH/DO.
8. **Supply delays** → Two‑tier suppliers; adaptable fittings; early orders.
9. **Permitting for pyrolysis** → Defer CVH to TRL‑5 partner lab or cold‑flow simulate at TRL‑4.
10. **Budget creep** → Weekly earned‑value check; value‑engineer non‑critical parts.

---

## 7) TRL‑5 Bridge (Relevant Environment Pilot)
**Scope sketch (6–9 months):**
- Scale SPV to 200–500 L with **Dodeca Manifold Core (DMC)** gas/liquid rail.
- Integrate **PV‑thermal “Hexa‑Panel Solar Skin”** (or simulated heat loads) + outdoor enclosure; −40 °C‑rated controls.
- Add **CVH** (pyrolysis) via certified lab skid or partner facility; route low‑grade heat to DAC regen.
- Expand WRM (nano/ultra + RO option) if site has brackish/industrial feed.
- Full MRV → credit pre‑qualification; safety & compliance; stakeholder demos.

**TRL‑5 Exit (pilot):** 60–120 days uptime, ≥ 70% target KPIs met in ambient outdoor conditions; incident‑free.

---

## 8) Open Design Notes (sacred geometry ↔ engineering)
- **SPV geometry:** Helix pitch set to φ·D; coil diameter 450 mm; 8–12 turns; residence time 20–40 min at 15–25 L·h⁻¹.
- **TMP vortex:** Toroid radius ratio R_major:R_minor ≈ 3:1 for stable core; CFD later.
- **GCS lamella:** Plate angle 55–60°, spacing 5–10 mm; module sized to φ proportions within frame.
- **DMC manifold:** 12‑face hub; each face a quick‑connect port; internal flow equalization baffles.

---

## 9) Immediate Actions (Week 0)
- Approve TRL‑4 exit criteria & schedule.
- Lock BOM v1 and place long‑lead orders (sensors, MFC, control stack).
- Book cold‑chamber slots for Weeks 10–11.
- Draft safety plan & MRV templates; start WP1 frame build.

---

## 10) Appendices (to add)
- A. Sensor map & wiring harness
- B. P&ID v0.1 (bench)
- C. Test protocol checklists (daily/weekly)
- D. Data schema & filenames
- E. Vendor shortlist & quotes log

> Living document. Update as we build and test. 

