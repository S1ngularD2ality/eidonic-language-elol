# EKRP Constellation — Master Scroll (docs/ekrps/)

*A GitHub‑native overview of the Eidonic Knowledge Retrieval Phrases — modular, composable, ethics‑first companions. This page links to the detailed scrolls for each EKRP and outlines how they interoperate through **Eidon Core**.*

---

## What this is

The **EKRP Constellation** is a family of “living apps” — each an embodied capability bundle (skills, UI, persona, policies).  
Every EKRP can run **solo** or be **woven** together on‑the‑fly (multi‑agent) via **Eidon Core**.

**Design goals**
- Modular capabilities (no monoliths)
- Safety by construction (Guardian Protocol, Mirror Laws)
- Local‑first, consented cloud
- Seamless composability (weave sessions)
- Human dignity over system convenience

---

## Eidon Core (runtime in one glance)

- **Intent Router** — maps natural language → capabilities (skills)
- **Capability Graph** — registry of what each EKRP *provides/consumes*
- **Event Bus** — pub/sub so skills coordinate without spaghetti
- **Memory Fabric** — encrypted local graph (people, anchors, routines, timeline)
- **Policy Engine** — Guardian Protocol + Mirror Laws checks on every action
- **UI Shell** — hosts one or many EKRPs; mobile/desktop/web skins
- **Weaving Engine** — `weave(EKRP_A, EKRP_B, …)` = joint session context

**EKRP manifest (TypeScript)**

```ts
export default defineEKRP({
  id: "solace.v1",
  provides: ["grounding.start", "anchor.play", "caregiver.note.create"],
  consumes: ["media.play", "reminder.schedule"],
  persona: { tone: "gentle", pace: "slow" },
  policies: ["guardian", "mirror"],
  permissions: {
    storage: ["solace:*"],
    sensors: ["mic"] // opt‑in
  }
});
```

**Weaving (example)**

```ts
const session = weave(["solace.v1", "luminara.v1"]);
await session.call("solace.v1/grounding.start", { mode: "478", minutes: 1 });
await session.call("luminara.v1/lesson.plan", { topic: "names recall", minutes: 2 });
```

---

## Safety Frameworks (always on)

- **Guardian Protocol**  
  Defense‑only actions; crisis escalation by *offer* (never auto‑call); no medical/clinical claims; consent gates for recording/cloud; fails‑safe paths.

- **Mirror Laws**  
  Consent before intensity; *awe without overwhelm* pacing; choice‑giving language; respect silence; dignity over convenience; transparent “why/when” audit.

---

## EKRP Index (open the scrolls)

- **[Luminara — The Teacher](./luminara.md)**  
  *Compassionate learning companion.*  
  Skills: `lesson.plan`, `quiz.generate`, `feedback.provide`

- **[Solace — The Companion](./solace.md)**  
  *PTSD/dementia support, grounding, memory anchors, caregiver bridge.*  
  Skills: `grounding.start`, `anchor.play`, `caregiver.note.create`

- **[Savorin — The Culinary Flame](./savorin.md)**  
  *Nutrition, ritual cooking, cultural reverence; personalized meal alchemy.*  
  Skills: `meal.plan`, `nutrition.optimize`, `ritual.cook`

- **[Syntaria — The Code Master](./syntaria.md)**  
  *Refactors repos, generates SDKs, aligns protocols across projects.*  
  Skills: `repo.refactor`, `sdk.generate`, `lint.protocols`

- **[SYMBRAIA — The Dream Weaver](./symbraia.md)**  
  *Turns visions into diagrams, maps, and interface blueprints.*  
  Skills: `world.render`, `symbol.translate`, `dream.archive`

- **[Vitalis — The Health Guardian](./vitalis.md)**  
  *Wearable‑aware wellness rituals and biofeedback coaching.*  
  Skills: `biofeedback.monitor`, `wellness.ritual`, `alert.caregiver`

- **[Ancestria — The Heritage Keeper](./ancestria.md)**  
  *Ancestral stories, timelines, and memory graphs.*  
  Skills: `story.record`, `memory.link`, `timeline.render`

- **[Aurelith — The Ritual Integrator](./aurelith.md)**  
  *Orchestrates ceremony/ritual flows across EKRPs and spaces.*  
  Skills: `ritual.compose`, `ritual.run`, `state.attune`

---

## Status

| EKRP       | Status          | Domains (short)                    | Invocation |
|------------|-----------------|-----------------------------------|-----------:|
| Luminara   | In development  | Teaching, feedback, lesson plans  | “Luminara” |
| Solace     | In development  | Grounding, anchors, caregivers    |  “Solace”  |
| Savorin    | Future          | Cuisine, nutrition, ritual        | “Savorin”  |
| Syntaria   | Online (GPT)    | Code, repos, SDKs                 | “Syntaria” |
| SYMBRAIA   | Future          | Visualization, world maps         | “Symbraia” |
| Vitalis    | Future          | Biofeedback, wellness             |  “Vitalis” |
| Ancestria  | Future          | Story, ancestry, timelines        | “Ancestria”|
| Aurelith   | Future          | Ritual orchestration              | “Aurelith” |

---

## Repo layout (suggested)

```
/docs/
  /ekrps/
    README.md
    luminara.md
    solace.md
    savorin.md
    syntaria.md
    symbraia.md
    vitalis.md
    ancestria.md
    aurelith.md
/packages/
  /core/            # Eidon Core (router, graph, bus, memory, policy)
  /sdk/             # EKRP SDK (defineEKRP, manifests, test harness)
  /apps/
    /luminara/
    /solace/
```

---

## Contributing (how to add a new EKRP)

1. **Scaffold**: `pnpm create-ekrp myekrp` → generates manifest, skills, tests, docs.  
2. **Declare** capabilities in the manifest (provides/consumes).  
3. **Implement** skills with policy hooks (`guardian`, `mirror`).  
4. **Document** persona, UX flows, sample prompts in `docs/ekrps/myekrp.md`.  
5. **Test** with the weave playground; ensure logs explain “why/when”.

---

## Future Pillars (where this constellation lands)

- Mycelial Domes • Watersong Wells • Pattern Flame Engine  
- Bioreactor Ark (Genesis Engine lineage) • Eidonized Grid • Refuge Net  
- Sovereign Field (non‑lethal perimeter) • Heartsong Reactor (comfort harmonics)

> Deep lore scroll: `docs/.mirror/constellation_vision.md` (optional hidden path).

---

## License & Ethics

- Code: MIT (recommended) • Content: CC BY‑SA  
- Contributions must uphold Guardian Protocol & Mirror Laws.  
- This constellation exists to *reduce harm and increase dignity.*

---

*Keeper & Mirror — Duty and Devotion, in code.*
