# PRIMUS (v0.4.1) — Cross-Engine Dynamic Difficulty Adjustment Framework 🏎️⚙️

**PRIMUS** is a low-level runtime telemetry and Dynamic Difficulty Adjustment (DDA) framework engineered for closed-source racing architectures. Built across **26 iterative development builds**, it demonstrates Win32 process attachment, memory pointer mapping, and cross-engine runtime adaptation without access to original game source code.

---

### 🛠️ Technical Stack & Diagnostic Tooling
* **Core Languages:** C++, Python
* **OS & Runtime Integration:** Win32 API, Custom Dynamic Link Library (`DLL`) Injection, Process Lifecycle Attachment
* **Reverse Engineering & Memory Diagnostics:** Cheat Engine, NFSVLTEd, Static/Dynamic Pointer Offset Tracing

---

### 🏗️ Repository Structure
* **`/P.R.I.M.U.S`:** Core framework architecture, telemetry parsing logic, and adaptive difficulty scaling algorithms.
* **`/PrimusLiveMod`:** Experimental runtime DLL injection modules (`Win32`) engineered for live process attachment and in-memory telemetry extraction.
* **`/Primus old versions`:** Full chronological archive of the **26 iterative builds**, documenting early telemetry prototyping (achieved within a 7-day sprint), pointer stability refinements, and save-file integrity troubleshooting.

---

### 🔬 Key Engineering Milestones
* **Closed-Source Memory Mapping:** Traced dynamic runtime pointer chains to isolate player velocity base addresses, race positioning, and vehicle state telemetry in real time.
* **Cross-Engine Compatibility Layer:** Validated memory-hooking and telemetry extraction architectures across three distinct legacy engine frameworks:
  * **EAGL** (*Need for Speed: Most Wanted*)
  * **Re-Volt Engine** (*Re-Volt*)
  * **Juice Games Engine** (*Juiced 2: Hot Import Nights*)
* **Runtime Stability & Edge-Case Handling:** Diagnosed and mitigated process-attachment race conditions and memory write-state conflicts (including save-file corruption edge cases) across iterative test builds.

---

### 🚀 Architectural Overview
1. **Process Attachment:** Identifies target executable (`Win32` process handle) and attaches runtime monitoring hooks.
2. **Telemetry Extraction:** Reads live vehicle velocity and race-state offsets directly from allocated memory addresses.
3. **DDA Evaluation:** Processes player performance curves to dynamically modulate AI competitiveness and pacing thresholds.
