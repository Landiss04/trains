# PAAC North Shore Extension — Module Requirements Matrix

Source: `Final Project vF.pdf` (course slide deck, 81 slides).
**Scope note:** The Moving Block Overlay (MBO) module — both the MBO Controller and the MBO Scheduler — is **out of scope** for this implementation. Every requirement that originally depended on the MBO is called out below in [Section 4](#4-scope-gaps-created-by-dropping-mbo), since dropping it removes some requirements outright and silently transfers others onto remaining modules.

Legend: 🔴 **VITAL** = safety-critical per the deck's definition ("in the railroad and transit industry 'vital' means 'safety critical'"). 🟡 = tension/conflict flagged in Section 3.

---

## 1. Module Requirements Side by Side

| Aspect | Track Model | Train Model | Track Controller (SW + HW) 🔴 | Train Controller (SW + HW) 🔴 | CTC Office |
|---|---|---|---|---|---|
| **Primary role** | Simulated physical model of the track layout | Simulated physical model of a train's dynamics | 🔴 Vital wayside controller that governs a section of track | 🔴 Vital onboard controller that governs a train | Dispatcher-facing central control point for the whole system |
| **Vital?** | No (physical sim, not a controller) | No (physical sim, not a controller) | 🔴 **Yes** — explicitly stated | 🔴 **Yes** — explicitly stated | Not stated vital, but issues authority that vital controllers rely on |
| **Configuration / data model** | Configurable layout, ideally DB-backed; grade & elevation; allowable directions of travel; branching; speed limits; configurable block size | Length, height, width, mass, crew count, passenger count; may consist of multiple cars | Runs a **user-written PLC program**, specified separately from the controller implementation | (No config specifics given beyond vital architecture requirement) | Track model is "held in a database"; dispatcher assigned a portion of territory |
| **Inputs it receives** | Switch position commands, signal/light commands from Track Controller | Authority (distance) from Wayside Controller; setpoint speed; brake command; speed/accel/decel limits; route info; temp control; door open/close; transponder input; track circuit input; tunnel light control; passenger e-brake | Authority & speed limits from CTC Office | Track signal (decoded for speed limit + authority); setpoint command from Transit Operator/driver | Dispatcher inputs (schedule, routing, section open/close, authority) |
| **Outputs it produces** | Track circuit signal (occupancy), signal/switch state, presence detection to Track Controller | Physical train state (position, velocity) consumed by Track Model | Commanded speed, authority, switch positions, lights → Track Model; switching of track; crossing lights/cross-bar; state of track/crossing/signals/trains reported back to CTC | Regulated speed to train; door/light control; station announcements; fault handling | Suggested speed & authority to controllers; throughput metrics; system-wide state display |
| **Failure modes to model** | Broken rail, track circuit failure, power failure | Train engine failure, signal pickup failure, brake failure (wheel slippage/power consumption optional) | Must **detect** broken rails and report track/crossing/train/signal state | Must **monitor for faults and act safely** | (not specified) |
| **Detection responsibilities** | Track circuits for **presence detection** (physical shorting of the circuit) | — | **Detects presence of trains**, detects broken rails (consumes Track Model's physical signal) | Decodes track signal for speed limit/authority | Monitors trains system-wide |
| **Diverse/redundant implementation** | Not required | Not required | 🟡 **Required** — "implementation must be diverse" for the PLC program vs. controller | Not explicitly required, but same vital bar applies | Not required |
| **Extra domain features** | Railway crossings; stations for loading/unloading; power limitations; track heater | Terrain-aware Newtonian point-mass dynamics; light controller for tunnels | Controls railway crossing gates + lights | Announces stations, opens/closes doors, on/off lights on schedule | Schedule trains, route trains, open/close sections for maintenance |
| **UI (NFR, all modules)** | Required | Required | Required (separately for HW and SW instances — see §3.3) | Required (separately for HW and SW instances — see §3.3) | Required — must display current state of entire system |

---

## 2. Cross-Cutting / Non-Functional Requirements (apply to every module)

- Executable on Windows 11; whole system submittable as one runnable executable; each subsystem also independently installable.
- Automatic demo mode with preset scenarios.
- System must run **≥10× wall-clock speed** and be pausable.
- Must use ≥1 architectural/design pattern from the course, documented.
- Any COTS components used must be identified.
- Vital aspects of the system and their effect on architecture/design must be explicitly described.
- 🔴 Train Controller and Track Controller specifically **must have a vital architecture**.
- Communications between office ↔ wayside ↔ train are **non-vital in the US** architecture the project follows (vital only in the European convention, per slide 30) — see tension in §3.1.

---

## 3. Points of Tension / Conflicts

### 3.1 🟡 Vital controllers riding on a non-vital communication channel
The deck states US-style rail comms (office↔wayside↔train) are **non-vital**, yet the Train Controller and Track Controller *themselves* are required to have a **vital architecture**. This is a direct tension: a safety-critical decision (speed/authority enforcement) is being made from data that may arrive corrupted, delayed, or duplicated over a non-vital link. The requirements don't specify who is responsible for closing this gap.
- **Affected modules:** Track Controller, Train Controller (consumers), CTC Office / Track Model (producers of the data being trusted).
- **Recommendation:** Decide explicitly whether "vital" here means the *controller logic* must fail safe even when its inputs are untrustworthy (checksums, staleness timeouts, fail-to-restrictive defaults), since you cannot make the wire itself vital without contradicting the slide's own non-vital-comms framing.

### 3.2 🟡 Overlapping ownership of presence/switch state between Track Model and Track Controller
- Track Model: "Should have track circuits for presence detection" and "need to show signals and switch machines."
- Track Controller: "Detects the presence of trains," "controls the switching of the track."

Both modules are described as owning detection/switch state. Read charitably, Track Model is the physical simulation (it *generates* the raw track-circuit short/open signal and *displays* switch position) while Track Controller *interprets* that signal and *commands* switch changes — but the deck never draws this boundary explicitly, and it's exactly the kind of ambiguity that caused past teams' "track traversal methods worked for train movement but not easy Wayside access" integration failure (peer retrospective, slide ~78).
- **Recommendation:** Pin down the interface contract early: Track Model exposes a physical/electrical-level signal; Track Controller is the only module allowed to interpret it and issue commands back. Don't let both sides implement "detection" logic independently.

### 3.3 🟡 "Diverse implementation" vital requirement vs. per-subsystem UI requirement
The Track Controller requirement explicitly demands the PLC program be "specifiable separately from the implementation" and that "implementation must be diverse" (i.e., N-version-style redundancy is implied for a vital component). Separately, the NFRs require **every subsystem to have its own UI** and be independently installable. Taken together this means you need **two independently-built, diverse HW/SW controller implementations, each with its own UI**, that must still agree/vote on a single safe outcome for the track. That's a materially larger scope than "one Track Controller module" and isn't costed anywhere else in the requirements (no mention of a voting/arbitration layer).
- **Affected modules:** Track Controller (HW), Track Controller (SW).
- **Recommendation:** Explicitly scope how much diversity is required (e.g., diverse PLC logic implementations behind a common interface vs. full diverse hardware/software stacks with voting), and decide if the Train Controller needs the same treatment — the deck only states diversity for the Track Controller, but both are marked vital.

### 3.4 🟡 10× real-time speed requirement vs. control-law timing assumptions
The Train Controller's control law is derived as a discrete-time PI controller with an explicit sample period `T` (trapezoidal integration, `u_k = u_k-1 + T/2(e_k + e_k-1)`), and the Track Model has time-based elements (crossing gate timing, track heater, PLC scan timing). Running the whole system at ≥10× wall-clock speed changes the effective `T` seen by every timed component. If Train Model/Controller, Track Controller PLC logic, and CTC scheduling don't all scale `T` consistently under fast-forward, you risk instability in the control loop or desynchronized crossing/signal timing that wasn't caught until integration — precisely the failure mode called out in the retrospective slides ("integration takes MUCH longer than expected").
- **Affected modules:** Train Model, Train Controller, Track Model, Track Controller.
- **Recommendation:** Define one shared simulation clock/tick contract up front (owned by whichever module drives time), and derive each module's control constants from it rather than hardcoding assumptions about wall-clock `T`.

### 3.5 🟡 Producer/consumer failure-mode pairs need a defined fault-injection contract
Track Model owns simulating failures (broken rail, track circuit failure, power failure) that Track Controller must *detect*; Train Model owns simulating failures (engine, signal pickup, brake) that Train Controller must *monitor and act on*. The architecture diagram's "Murphy" actor injecting faults directly into Track Model/Train Model reinforces this split, but no interface is specified for how a simulated fault becomes an observable signal to the corresponding controller.
- **Recommendation:** Define the fault-injection/fault-reporting interface as its own contract between each Model/Controller pair before implementation starts.

---

## 4. Scope Gaps Created by Dropping MBO

Removing the MBO Controller and MBO Scheduler doesn't just delete two modules — it removes functionality the other modules' requirements were written assuming would exist elsewhere. These need explicit decisions, not silent omission:

1. **Train authority source changes.** The architecture diagram (slide 8) shows the *train side* getting "Suggested Speed, Authority" from MBO, while the Train Model requirement separately says train inputs include "authority (distance) from **Wayside Controller**." These two aren't actually contradictory (Wayside/Track Controller was always the fixed-block authority source) — but with MBO gone, **all** train authority must now come from the Track Controller via fixed block, not moving block. Moving-block-style continuous safe-stopping-distance authority is no longer possible. Confirm this fixed-block-only approach is acceptable for the demo, since it's a real capability reduction versus what the slides describe as the target architecture.
2. **Scheduling logic has no owner.** The CTC Office requirements only say "Schedule trains, Route trains" in one bullet each. All of the *detailed* scheduling logic — hourly throughput input, user-specified start time, schedule validated against vital requirements, yard startup dispatch mode, 8.5-hour operator shifts, mandatory 30-minute break after 4 hours of driving, trains returning to yard for shift change — lived entirely in the now-deleted **MBO Scheduler** slide. **This is the single largest silent scope gap.** Either CTC Office needs to absorb this whole scheduling feature set, or the group needs to formally decide it's out of scope and document that decision (recommended, given the added complexity is substantial and orthogonal to the vital control problem the course is actually testing).
3. **Train position reporting loses its consumer.** The diagram has trains sending vital position messages to MBO. Without MBO, decide whether trains still need to report position anywhere (e.g., to CTC Office for the "display current state of entire system" requirement) or whether track-circuit-based occupancy detection alone satisfies that display requirement.

---

## 5. Suggested Next Step

Before implementation, get explicit team sign-off on:
- The fixed-block-only authority model (item 4.1),
- Whether any scheduling requirements survive the MBO cut (item 4.2),
- The Track Model/Track Controller interface boundary (§3.2),
- What "diverse implementation" concretely means for the Track Controller (§3.3).

These four are the ones most likely to cause the "all at once integration failed" problem multiple past teams flagged in their retrospectives — they're all interface/ownership questions, not implementation questions, so they're cheap to resolve now and expensive to resolve after modules are half-built.
