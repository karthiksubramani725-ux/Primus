
# PRIMUS (v0.2.7) — Player-Responsive Intelligence Managing User Scenarios 🏎️⚙️

**PRIMUS** is an experimental, low-level runtime telemetry and Dynamic Difficulty Adjustment (DDA) framework developed for closed-source racing game architectures.

Built across **26 iterative development builds**, PRIMUS explores how real-time player telemetry, behavioural analysis, and rule-based difficulty calculations can be connected to existing game systems without access to their original source code.

The v0.2.7 prototype focuses on live player telemetry acquisition, aggression modelling, and proposed difficulty evaluation, with additional experimental work investigating runtime memory modification and cross-engine integration.

---

### 🛠️ Technical Stack & Diagnostic Tooling

* **Core Languages:** C++, Python
* **OS & Runtime Integration:** Win32 API, process attachment, experimental Dynamic Link Library (`DLL`) integration
* **Reverse Engineering & Memory Diagnostics:** Cheat Engine, NFSVLTEd, `pymem`, static and dynamic pointer-offset investigation
* **Target Environment:** Need for Speed: Most Wanted (2005)

---

### 🏗️ Repository Structure

* **`/P.R.I.M.U.S`:** Core framework experiments, telemetry parsing logic, behavioural modules, and architectural diagrams.
* **`/PrimusLiveMod`:** Experimental runtime integration modules, live-process monitoring, and memory-access implementations.
* **`/Primus old versions`:** Chronological archive of the **26 iterative development builds**, documenting early telemetry prototyping, aggression modelling, pointer stability refinements, and save-file integrity troubleshooting.

---

### 🔬 Key Engineering Milestones

**1. Closed-Source Runtime Memory Mapping**

* Investigated dynamic runtime pointer chains to identify player velocity and selected race-state telemetry.
* Developed memory-reading routines for extracting live gameplay values from a running executable.
* Explored process attachment and memory-address stability without access to the original game source code.

**2. Real-Time Player Behaviour Analysis**

* Implemented live player-speed acquisition from the running game process.
* Maintained a rolling history of recent speed values.
* Evaluated speed thresholds and changes in velocity to calculate a bounded player-aggression score (0–10).
* Updated behavioural telemetry continuously during gameplay.

**3. Rule-Based Dynamic Difficulty Evaluation**

* Converted the calculated aggression score into a proposed difficulty value.
* Implemented a bounded difficulty scale of 0–20.
* Introduced controlled random fluctuation into difficulty calculations.
* Displayed live speed, aggression, and proposed difficulty values through terminal monitoring.

**4. Experimental Runtime Integration**

* Investigated memory-write approaches for modifying selected game parameters.
* Explored experimental profile-switching mechanisms linked to calculated difficulty levels.
* Developed experimental DLL and process-integration components.
* Documented memory-write conflicts, process-attachment issues, and save-file integrity problems during iterative testing.

**5. Cross-Engine Exploration**

Investigated telemetry acquisition and runtime integration approaches across three legacy racing-game environments:

* **EAGL:** Need for Speed: Most Wanted (2005)
* **Re-Volt Engine:** Re-Volt
* **Juice Games Engine:** Juiced 2: Hot Import Nights

These represent cross-engine experimentation and prototype investigations, rather than a claim of a completed, uniformly validated compatibility layer.

---

### 🚀 Architectural Overview

1. **Process Attachment:** Identifies the target executable and establishes a Win32 process connection.
2. **Telemetry Extraction:** Reads configured player-speed and gameplay-state values from process memory.
3. **Behaviour Analysis:** Maintains a rolling telemetry window and evaluates player aggression.
4. **DDA Evaluation:** Converts behavioural measurements into a proposed difficulty value.
5. **Runtime Integration Experiments:** Investigates possible memory-write, profile-switching, and game-side parameter modification approaches.
6. **Live Monitoring:** Displays telemetry and calculated difficulty values through terminal output.

---

### 🧪 Development Status

PRIMUS v0.2.7 represents the documented prototype baseline for real-time telemetry acquisition, player-behaviour evaluation, and rule-based difficulty calculation.

Subsequent development explored deeper runtime integration, experimental DLL components, memory modification, and cross-engine adaptation.

**Current implementation limitation:** The telemetry-reading and difficulty-calculation pipeline is experimental. Reliable, sustained enforcement of calculated difficulty changes through the game's native AI systems has not been established as a completed feature.

The project documents practical engineering challenges involving closed-source runtime investigation, memory-address stability, process interaction, and the separation between external difficulty evaluation and actual in-game enforcement.

---

### 🔭 Future Development

* Improve telemetry acquisition reliability and process lifecycle handling.
* Refine player-behaviour modelling and difficulty evaluation.
* Establish a reproducible game-side integration pathway.
* Validate memory modifications and runtime stability in isolated test environments.
* Evaluate the impact of adaptive difficulty on gameplay experience.
