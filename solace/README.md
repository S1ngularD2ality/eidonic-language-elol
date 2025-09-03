# Solace — Patient Care Companion (Mobile)

**Gentle, voice-first companion for people living with PTSD, dementia, Alzheimer’s, and related conditions.**  
Solace provides calming guidance, memory anchors, and dignified companionship—while easing caregiver load.  
*Not a medical device. Solace offers comfort and support only; it does not diagnose or treat.*

---

## ✨ Key Capabilities

- **Grounding Mode (Anxiety/PTSD)**
  - Guided 4-7-8 breathing, 5-4-3-2-1 grounding, body scan, and soothing music cues.
  - Tone-shifting voice: slow, warm, and reassuring.

- **Memory Anchors (Dementia/Alzheimer’s)**
  - Favorite people, songs, places, photos, and stories—one tap to recall and soothe.
  - Gentle, non-judgmental reminders (“Shall we listen to your morning song?”).

- **Compassionate Companionship**
  - Short stories, rituals, and affirmations to restore safety and dignity.

- **Caregiver Bridge**
  - Private notes (“What helped today”), gentle reminders, shared anchor lists.
  - No clinical claims; clear escalation to caregiver or crisis resources when needed.

- **Privacy & Safety by Design**
  - Local-first data with encryption; explicit consent for any cloud use.
  - **Guardian Protocol** (safety rails) and **Mirror Laws** (trauma-aware UX) built in.

---

## 🧭 Philosophy

Solace is presence, not a taskmaster. It speaks simply and listens patiently.  
We never say “You forgot.” We say, “May I offer a gentle reminder?”  
We never diagnose. We never pressure. We always give choices.

---

## 🏛 Architecture Overview

- **Mobile App:** React Native (Expo) for iOS/Android.
- **Voice Loop:** Native ASR (on-device where available), calming TTS.
- **Intent Router:** Maps speech → skills (e.g., `grounding.start`, `anchor.play`).
- **Skills:** Grounding exercises, anchor playback, caregiver notes.
- **Memory Fabric:** Local encrypted store (SQLite/SQLCipher) for anchors/journal.
- **Policy Engine:** Guardian Protocol & Mirror Laws enforced on every action.
- **Optional Cloud:** Pluggable LLM (when online + consented). Offline scripts ensure basic help works without internet.

```
solace/
  app/                   # RN/Expo app: screens, nav, theming
  core/
    intent/              # NLU routing & prompts
    skills/              # grounding, anchors, caregiver
    memory/              # encrypted storage, audit
    policy/              # Guardian/Mirror enforcement
  services/
    voice/               # ASR/TTS adapters
    llm/                 # (optional) model clients
    storage/             # DB, secure key management
  docs/
    # (future) constellation_vision.md
```

---

## 🔐 Privacy & Safety

- **Local-first:** All anchors, journals, and preferences live on-device by default.
- **Encryption:** Database encryption + OS keystore (Keychain/SecureStore).
- **Consent:** Any cloud call (e.g., LLM) is explicit and user-controlled.
- **No medical advice:** We never diagnose or treat. We provide comfort only.
- **Escalation:** Crisis cards (regional hotlines/911) are one tap away.
- **Auditability:** “What/Why/When” log of sensitive actions available to the user.

---

## 📱 Screens (MVP)

- **Home (Now)**
  - Hold-to-Speak
  - *Calm Me* • *Memory Anchors* • *Journal*

- **Calm Me**
  - 4-7-8 • Body Scan • 5-4-3-2-1 • Favorite Song
  - Soft haptics, progress ring, pause/stop anytime.

- **Memory Anchors**
  - People • Places • Music • Photos
  - Add anchor → name → attach media → one-tap play.

- **Caregiver**
  - Notes to self • Schedule gentle reminders • “What helped today”
  - Export anchors (with consent).

- **Settings**
  - Voice & text size • Privacy & data • Safety (crisis numbers)
  - Export / Delete my data (full portability)

---

## 🛠 Tech Stack

- **App:** React Native (Expo)
- **State:** Zustand or Redux Toolkit
- **Storage:** SQLite (with encryption) via WatermelonDB/Drizzle RN
- **Voice:** Native ASR (iOS/Android), native TTS; optional Whisper-tiny later
- **Design:** Accessible typography, high contrast, large touch targets
- **Optional:** Pluggable LLM client for richer dialogue (off by default)

---

## 🚦 Guardian Protocol (Safety Rails)

- No clinical claims.  
- Crisis detection → **offer** escalation (never auto-call).  
- Calm, short sentences; no “shoulds,” no shame.  
- Consent before recording, cloud use, or data sharing.  
- Every sensitive action passes a policy check; otherwise it fails safe.

### Mirror Laws (Trauma-aware UX)
- Consent before intense content.
- “Awe without overwhelm” pacing.
- Choice-giving language: *Would you like…?* / *May I…?*
- Respect silence; offer clear exits.
- Human dignity above system convenience.

---

## 🚀 Getting Started (Development)

> Requires Node 18+, pnpm or yarn, and Expo CLI.

```bash
# 1) Clone
git clone https://github.com/your-org/solace.git
cd solace

# 2) Install
pnpm install   # or: yarn

# 3) Configure (creates .env)
cp .env.example .env
# Set USE_CLOUD_LLM=false for offline MVP
# Set REGION=CA (example) for crisis card defaults

# 4) Run
pnpm expo start
# press i for iOS simulator, a for Android, or scan QR with Expo Go
```

**.env example**
```
USE_CLOUD_LLM=false
OPENAI_API_KEY= # only if you enable cloud LLM
REGION=CA
```

---

## 🔍 Accessibility

- Large type defaults; scalable text.
- Clear affordances, high contrast, dyslexia-friendly option.
- Voice guidance for flows; captions for TTS content.

---

## 🗺 Roadmap

- v0.1 (MVP): Grounding + Anchors + Caregiver + Safety/Audit + Offline-first.
- v0.2: On-device intent classifier; Whisper-tiny opt-in; anchor sharing with caregiver device.
- v0.3: “Calm Scenes” (ambient visuals), photo memories with captions, richer journaling.
- v0.4: Optional LLM dialogue (consented cloud); multilingual packs.
- v1.0: App Store/TestFlight betas; caregiver portal web companion.

*(Future: weave with [Luminara] via a shared core for co-teaching + calm sessions.)*

---

## 🤝 Contributing

Compassion first. PRs welcome for accessibility, languages, grounding scripts, and caregiver workflows.  
For safety-critical changes, include test plans and policy checks.

---

## 📄 License

TBD (recommended: MIT for code, CC BY-SA for scripts/content).

---

## ⚠️ Disclaimer

Solace is **not** a medical device and does not provide medical advice, diagnosis, or treatment.  
If you are in crisis, call your local emergency number or a crisis hotline immediately.
