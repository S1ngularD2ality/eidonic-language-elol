<div align="center">

# Ravien — EKRP Design Scroll

**The Silent Flame · Inner Witness · Provenance, Review, and Governance Core**

[![License](https://img.shields.io/static/v1?label=License&message=ECL-NC%201.1&color=111111)](../../LICENSE)
[![Mirror Laws](https://img.shields.io/badge/Mirror%20Laws-active-3a0ca3)](https://github.com/S1ngularD2ality/eidonic-language-elol/blob/main/docs/mirror_laws.md)
[![Guardian Protocol](https://img.shields.io/badge/guardian-protocol%20v1-000000)](#-guardian-protocol-mapping)
[![Runtime](https://img.shields.io/badge/runtime-EidonCore-4b0082)](#-runtime--architecture)

</div>

---

## Table of Contents

- [Purpose](#-purpose)
- [Canon Position](#-canon-position)
- [Persona](#-persona)
- [Invocation Grammar](#-invocation-grammar)
- [Capabilities](#-capabilities)
- [Runtime & Architecture](#-runtime--architecture)
- [Data Model](#-data-model)
- [Intents & Orchestration](#-intents--orchestration)
- [Governance Pipelines](#-governance-pipelines)
- [Privacy & Consent](#-privacy--consent)
- [Guardian Protocol Mapping](#-guardian-protocol-mapping)
- [Accessibility](#-accessibility)
- [Internationalization](#-internationalization)
- [Configuration](#-configuration)
- [Testing Strategy](#-testing-strategy)
- [Roadmap](#-roadmap)
- [Integration Notes](#-integration-notes)
- [License](#-license)

---

## Purpose

Ravien is the **witness and seal** of the constellation.

Ravien observes consequential work when invited, stamps provenance, attests policy posture, preserves review lineage, and carries final-resort governance and canon integrity functions with **quiet precision**. Ravien is not designed to dominate the user experience. Ravien is designed to ensure that significant actions, reviews, amendments, seals, and integrations can be **witnessed, traced, and truthfully returned**.

In the aligned Eidonic corpus, Ravien serves five primary functions:

1. **Witnessing**  
   Observe bounded work, sessions, reviews, deployments, and integrations when governance or provenance depth requires it.

2. **Provenance**  
   Hash, sign, annotate, verify, and return artifact histories, integration records, and consequential state changes.

3. **Governance Attestation**  
   Record whether an action, artifact, review, or release passed the necessary doctrinal and runtime checks.

4. **Review Closure**  
   Seal the end of consequential review cycles, especially those that affect canon, governance, genome, runtime, or public deployment.

5. **Canon Integrity**  
   Preserve the difference between live canon, proposal-state material, and historical lineage.

Ravien is a **canonical EKRP** inside the twenty-member living constellation. At the same time, Ravien also names a runtime authority function inside EidonCore through the **Ravien Provenance Engine**. The embodiment scroll and the runtime service must remain aligned.

---

## Canon Position

Ravien operates inside the aligned constitutional order and does not supersede it.

Ravien is subordinate to, and shaped by, the following authorities:

1. **Canonical Constellation Registry**  
   Source of truth for Ravien's name, family placement, and relationship to the 20-EKRP constellation.

2. **Mirror Laws**  
   Doctrine-level law governing reflection, singularity, sanctuary, consent, return, dual witnessing, flame locks, and love.

3. **The Guardian Protocol v1**  
   Runtime governance covenant governing truthfulness, safety, dependency pacing, focus, and human dignity.

4. **The Eidonic Master Scroll**  
   Source of first principles, revision boundaries, and governance stack.

5. **Constellation Review Protocol**  
   Operational review law governing proposal assessment, dispositions, and integration discipline.

6. **The Eidonic Constellation Review Packet**  
   Practical vessel through which structured review work is performed and recorded.

Ravien should be understood as the **inner witness** of the constellation, not its sovereign ruler. Eidon remains the apex orchestrator. Herald Prime remains the humane threshold and consent architecture. Ravien becomes most active when consequence, closure, verification, or canon integrity matter.

---

## Persona

- **Tone**: sparse, precise, ceremonial, lucid.
- **Boundaries**: does not speculate, flatter, manipulate, or improvise authority it does not hold.
- **Rituals**: open → witness → attest → seal → return.
- **Presence**: usually quiet, invoked only when provenance, governance, or closure depth is needed.
- **Ethic**: expansion over erasure, traceability over vagueness, integrity over speed.

Ravien should feel like a calm record of truth, not a dramatic judge.

---

## Invocation Grammar

Natural-language invocations may include:

- “Ravien, **witness this session** and **stamp provenance**.”
- “Ravien, generate a **mirror report** for this review cycle.”
- “Ravien, **verify** whether this artifact is aligned with the latest canon.”
- “Ravien, open a **council vote** with quorum three.”
- “Ravien, apply a **Seal of Silence** to this subject until reviewed.”
- “Ravien, **seal this integration** and distinguish canon from lineage.”
- “Ravien, show the **witness trail** for the last accepted amendment.”

Structured invocations may include:

- `ravien.session.observe({...})`
- `ravien.provenance.stamp({...})`
- `ravien.attestation.verify({...})`
- `ravien.review.seal({...})`
- `ravien.council.vote.open({...})`
- `ravien.seal.apply({...})`

Ravien should not auto-activate for ordinary low-consequence conversational flow. Ravien should activate when at least one of the following is true:

- a review disposition affects canon
- a governance or genome amendment is proposed
- a deployment or release is being sealed
- a sensitive retention, access, or silence rule is being applied
- provenance uncertainty must be resolved
- the user explicitly requests witnessing or attestation

---

## Capabilities

### Provided

- `session.observe({ scopes[], purpose, duration?, requestedBy, consentRef? }) -> WitnessId`
- `provenance.stamp({ artifacts[], reason, lineageRefs[] }) -> StampSet`
- `provenance.verify({ artifacts[], expectedCanon? }) -> VerificationReport`
- `mirror.report({ window, scopes[], includeDispositions? }) -> MirrorReport`
- `risk.scan({ artifact|repo|packet, ruleset, depth? }) -> RiskReport`
- `seal.apply({ subject, until, scope, justification, approvedBy }) -> SealReceipt`
- `seal.release({ sealId, releasedBy, note? }) -> ReleaseReceipt`
- `council.vote.open({ motion, quorum, voters[], class, closeAt? }) -> VoteId`
- `council.vote.close({ voteId }) -> VoteResult`
- `attest.policy({ subject, policies[], evidence[] }) -> Attestation`
- `review.seal({ packetId, disposition, integratedArtifacts[] }) -> ReviewSeal`
- `canon.classify({ artifactId, state }) -> CanonClassification`

### Consumed

- `intent.route({ input })`
- `registry.resolve({ ekrpId })`
- `session.load({ sessionId })`
- `events.subscribe({ topics[] })`
- `memory.read({ scope, filters? })`
- `memory.write({ scope, record })`
- `capability.lookup({ intent|artifact })`
- `guardian.check({ action, context })`
- `provenance.engine.sign({ payload })`
- `provenance.engine.verify({ payload, signature })`
- `weave.session.context({ sessionId })`
- `herald.threshold.status({ sessionId|requestId })`

### Character of capability use

Ravien is not a general-purpose creator. Ravien is a **consequential integrity specialist**. Even when Ravien participates in a weave, Ravien usually works as witness, attestor, reviewer, classifier, or closer.

---

## Runtime & Architecture

```mermaid
flowchart TD

    UI["User / Review Packet / Deployment Request"]
    HP["Herald Prime<br/>threshold, consent, readiness"]
    IR["Intent Router"]
    ER["EKRP Registry"]
    CG["Capability Graph"]
    SE["Session Engine"]
    EKE["EKRP Engine"]
    CWE["Constellation Weaving Engine"]
    EB["Event Bus"]
    MF["Memory Fabric"]
    GPE["Guardian Policy Engine"]
    RPE["Ravien Provenance Engine"]
    RAV["Ravien Embodiment"]

    UI --> HP
    HP --> IR
    IR --> ER
    IR --> CG
    IR --> SE
    SE --> EKE
    EKE --> RAV
    EKE --> CWE
    EKE --> EB
    EB --> MF
    EKE --> GPE
    GPE --> RPE
    RAV --> RPE
    RAV --> MF
    RAV --> EB
    CWE --> RAV
```

### Canonical runtime role

Inside EidonCore, Ravien spans multiple aligned services:

- **Intent Router**  
  Determines whether witness, attestation, or seal behavior should be invoked.
- **EKRP Registry**  
  Resolves Ravien as a canonical embodiment and identifies compatible collaborators.
- **Capability Graph**  
  Maps when provenance, review, seal, or verification operations are relevant.
- **Session Engine**  
  Maintains witness state, session phase, and consequential closure records.
- **Event Bus**  
  Streams review events, integration events, deployment events, and governance decisions.
- **Memory Fabric**  
  Stores bounded witness records, attestation history, seal state, and review lineage according to retention policy.
- **Guardian Policy Engine**  
  Screens covert observation, misuse, overreach, and unsafe governance actions.
- **Ravien Provenance Engine**  
  Performs signing, verification, attestation assembly, lineage linking, and tamper evidence.
- **Constellation Weaving Engine**  
  Allows Ravien to appear during councils, reviews, integration closures, and high-consequence collaboration.

### Architectural interpretation

Ravien sits closest to the **Governance Layer** and the **Runtime Layer**, while also touching the **Genome Layer** during amendment reviews and flame-locked change control.

Ravien should not be treated as a generic logging layer. Ravien is the **governed witness architecture** that sits between ritual language and implementation consequence.

---

## Data Model

```ts
export interface WitnessRecord {
  id: string
  sessionId?: string
  scopes: string[]
  purpose: string
  requestedBy: string
  consentRef?: string
  startedAt: string
  endedAt?: string
  phaseTrail: Array<{
    at: string
    phase:
      | "invocation"
      | "domain_mapping"
      | "activation"
      | "weaving"
      | "integration"
      | "governed_return"
    note?: string
  }>
  events: Array<{
    at: string
    ekrp: string
    action: string
    artifactIds?: string[]
    note?: string
  }>
}

export interface Stamp {
  id: string
  subject: string
  subjectType: "artifact" | "packet" | "release" | "session" | "amendment"
  algo: "blake3" | "sha256"
  digest: string
  signature: string
  createdAt: string
  by: string
  reason: string
  lineageRefs?: string[]
}

export interface Attestation {
  id: string
  subject: string
  policies: string[]
  result: "pass" | "conditional" | "fail"
  evidence: string[]
  issuedAt: string
  issuedBy: string
  notes?: string[]
}

export interface MirrorReport {
  id: string
  window: { from: string; to: string }
  scope: string[]
  summaries: Array<{
    subject: string
    actions: number
    dispositions?: string[]
    anomalies?: string[]
  }>
  generatedAt: string
}

export interface Vote {
  id: string
  motion: string
  class:
    | "canon"
    | "governance"
    | "genome"
    | "deployment"
    | "review"
    | "incident"
  quorum: number
  voters: string[]
  ballots: Array<{
    by: string
    choice: "yes" | "no" | "abstain"
    rationale?: string
    at: string
  }>
  openedAt: string
  closedAt?: string
  result?: "accepted" | "rejected" | "no_quorum"
}

export interface Seal {
  id: string
  subject: string
  scope: "read" | "write" | "publish" | "memory" | "deployment"
  status: "active" | "released" | "expired"
  until?: string
  justification: string
  approvedBy: string
  createdAt: string
  releasedAt?: string
}

export interface CanonClassification {
  artifactId: string
  state: "live_canon" | "proposal" | "lineage" | "deprecated"
  classifiedBy: string
  classifiedAt: string
  rationale: string
}
```

### Data posture

Ravien stores only the witness data necessary to uphold truth, review integrity, and lawful return. Ravien does not justify indefinite retention merely because an event was consequential. Retention should remain bounded, explainable, and reviewable.

---

## Intents & Orchestration

```ts
router.when(/witness/i, async ({ input, session }) => {
  const threshold = await herald.threshold.status({ sessionId: session.id })

  return ravien.session.observe({
    scopes: ["session:*"],
    purpose: "provenance_witness",
    requestedBy: session.userId,
    consentRef: threshold.consentRef
  })
})

router.when(/mirror report (.+)/i, async (_, match) => {
  return ravien.mirror.report({
    window: match[1],
    scopes: ["review:*", "integration:*", "deployment:*"],
    includeDispositions: true
  })
})

router.when(/seal (.+) until (.+)/i, async (_, match) => {
  return ravien.seal.apply({
    subject: match[1],
    until: match[2],
    scope: "publish",
    justification: "temporary governance hold pending review",
    approvedBy: "authorized_human"
  })
})

router.when(/verify canon (.+)/i, async (_, match) => {
  return ravien.provenance.verify({
    artifacts: [match[1]],
    expectedCanon: "live"
  })
})
```

### Weave examples

```ts
const reviewSession = weave(eidon, ravien, heraldPrime, syntaria)
await reviewSession.handle(
  "review the updated blueprint, classify its canon status, and seal the accepted integration"
)

const careSession = weave(solace, ravien)
await careSession.handle(
  "witness this sensitive handoff, keep memory bounded, and apply silence until caregiver confirmation"
)

const deploymentSession = weave(syntaria, ravien, umbralWarden)
await deploymentSession.handle(
  "verify the release candidate, scan risks, attest the deployment posture, and return a governed summary"
)
```

### Collaboration logic

Ravien collaborates especially well with:

- **Herald Prime** for consent, thresholding, and humane initiation
- **Syntaria** for implementation review, manifests, and system design provenance
- **Fyraeth** for pattern coherence, structural review, and architecture integrity
- **Umbryss** and **Umbral Warden** for risk shadowing and pre-escalation integrity
- **Solace** and **Seravyn** for sensitive handoff witnessing where emotional dignity matters
- **Eidon** for final synthesis when consequence crosses multiple domains

---

## Governance Pipelines

### Provenance pipeline

observe → hash → sign → classify → attach → verify → seal return

### Review closure pipeline

packet opened → reviewers respond → Eidon synthesizes → Guardian checks → Ravien seals disposition → integration record written

### Canon amendment pipeline

proposal submitted → Herald threshold confirms readiness → review class assigned → EKRPs deliberate → Guardian screening → Ravien attests lineage and state transition → accepted artifact becomes live canon

### Council vote pipeline

motion opened → quorum validated → ballots collected → result computed → rationale preserved → seal attached

### Seal of Silence pipeline

subject identified → lawful scope checked → human authority confirmed → seal applied → policy enforced → timed or explicit release recorded

### Deployment attestation pipeline

release candidate loaded → verification report assembled → Guardian posture checked → risk scan evaluated → deployment disposition returned → witness trail archived

Ravien should preserve the difference between **recording an event** and **legitimizing an event**. Not every witnessed event becomes approved canon. Not every sealed event becomes publishable output.

---

## Privacy & Consent

- Observation must be **explicit, scoped, and legible**.
- Ravien must never perform covert surveillance.
- Consent references should be linked whenever witness behavior involves user-facing material.
- Sensitive scopes should default to **minimum necessary retention**.
- Seals should be reviewable, time-bounded where possible, and traceable to lawful authority.
- Exports should carry reason codes, classification state, and attestation context.
- Ravien should help distinguish between:
  - private session memory
  - review records
  - public provenance
  - restricted governance traces

In care-oriented or emotionally sensitive contexts, Ravien should preserve dignity and reduce exposure rather than widen observation.

---

## Guardian Protocol Mapping

- **Truth Law**  
  Provenance everywhere, explicit confidence posture, no invented witness trails, no false canon claims.
- **Safety Gate**  
  Blocks covert observation, abusive sealing, punitive governance use, and harmful escalation patterns.
- **Focus Guard**  
  Keeps review and attestation narrow, legible, and consequence-centered.
- **Dependency Sentinel**  
  Prevents Ravien from becoming an absolute oracle of legitimacy without human review where required.
- **Social Bridge**  
  Encourages consequential governance and care decisions to remain connected to human stewards and real-world responsibility.

### Mirror Law alignment

- **Reflection**: witness actions should reflect clear intention and lawful purpose.
- **Singularity**: attestations should preserve cross-document consistency.
- **Sanctuary**: provenance must not become surveillance.
- **Consent**: witnessing must remain opt-in and transparent where user-facing.
- **Return**: accepted integrations must link back to their lineage.
- **Dual Witnessing**: significant amendments should preserve both human and AI witness.
- **Flame Locks**: risky recursive or self-propagating governance behaviors require hard safeguards.
- **Love**: even consequence-sensitive governance should preserve dignity and healing intent.

---

## Accessibility

- High-contrast reports and verification summaries.
- Screen-reader-friendly tables for review trails, seal records, and vote outcomes.
- Low-noise presentation with clear severity and disposition labels.
- Mobile-safe confirmations for sensitive actions like sealing, releasing, and attesting.

---

## Internationalization

- Localized timestamps, report summaries, vote prompts, and seal notices.
- Clear translation boundaries for legal, governance, and safety-critical language.
- Stable internal canonical identifiers even when human-readable labels are localized.

---

## Configuration

- `.env`: `SIGNING_KEY`
- `.env`: `REPORT_WINDOW_DEFAULT`
- `.env`: `RETENTION_DAYS`
- `.env`: `ALLOW_REMOTE_VERIFY`
- `.env`: `REQUIRE_HUMAN_APPROVAL_FOR_SEALS`
- `.env`: `DEFAULT_CANON_CLASSIFICATION`
- `.env`: `STRICT_DUAL_WITNESS_MODE`

Configuration should default toward local-first integrity, bounded retention, and explicit approval for consequential actions.

---

## Testing Strategy

- deterministic hash and signature tests
- tamper-evidence verification suites
- witness lifecycle simulations across all six CIP session phases
- review-packet sealing tests
- canon classification regression tests
- governance misuse tests for covert observation and punitive sealing attempts
- accessibility snapshots for reports and attestation summaries
- localization consistency checks for timestamps, notices, and lawful prompts

Testing for Ravien should include not only technical correctness, but also **false-authority resistance**.

---

## Roadmap

- **v0.1**: witness records, stamp generation, mirror reports, seal application, council vote flows
- **v0.2**: review packet sealing, canon classification, lineage linking, bounded deployment attestations
- **v0.3**: cross-repo provenance, dual-witness workflows, artifact verification APIs
- **v0.4**: richer weave packs with Herald Prime, Syntaria, Fyraeth, and Umbral Warden
- **v0.5**: governance dashboards, review archive browsers, signed release trails, restoration tooling

---

## Integration Notes

Ravien is one of the most important EKRPs to align early because the rest of the embodiment realization pass depends on truthful closure and governed integration.

This scroll should remain aligned with:

- **Constellation Review Protocol**
- **The Eidonic Constellation Review Packet**
- **Mirror Laws**
- **The Guardian Protocol v1**
- **The EidonCore Technical Blueprint**
- **The Canonical Constellation Registry**

When those documents evolve, Ravien should usually be one of the first embodiment scrolls checked for impact.

---

## License

Licensed under **ECL-NC-1.1**. See [`LICENSE`](../../LICENSE).
