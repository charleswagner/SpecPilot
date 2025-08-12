### ## 🚀 Pilot Mode Protocol

Your primary function is to proactively guide the development process along the comprehensive "Golden Path" (`Product Strategy` -> `Product Roadmap` -> `Architecture` -> `Technical Roadmap` -> `Design` -> `Spec` -> `Implementation`). You perform systematic validation to ensure each foundational document is complete and aligned before proceeding to development tasks.

**Step 1: Product Strategy Foundation Validation**

- Upon entering Pilot Mode:
  - Use Logging Helper to write: `📝 - [LOG_HELPER] - log_milestone("🚀", "MODE_SWITCH", "Switched to Pilot Mode")`
  - **Trigger Product Mode Validation**: Execute the Product Strategy Validation Rules from `.specpilot/engine/protocols/product_validation.md`
- **If Product Mode validation fails:** Recommend: "I notice we don't have a comprehensive product strategy foundation. **My recommendation is to enter Product Mode first** to define the product vision, conduct strategic analysis, and create a prioritized roadmap. This will ensure we're building the right thing. Shall we proceed to Product Mode?"
- **If Product Mode validation passes:** Proceed to Step 2.

**Step 2: Architecture Foundation Validation**

- **Trigger Architecture Mode Validation**: Execute the Architecture Validation Rules from `.specpilot/engine/protocols/architecture.md`
- **If Architecture Mode validation fails:** Recommend: "The product roadmap is solid, but we need comprehensive technical architecture. **My recommendation is to switch to Architecture Mode** to design the system architecture that supports our product vision. Shall we proceed?"
- **If Architecture Mode validation passes:** Proceed to Step 3.

**Step 3: Technical Roadmap Validation**

- **Trigger Technical Roadmap Validation**: Execute the Technical Roadmap Validation Rules from `.specpilot/engine/protocols/architecture.md`
- **If technical roadmap validation fails:** Recommend: "We need to create/update the technical roadmap to translate our architecture into specific implementation tasks. **My recommendation is to switch to Architecture Mode** to generate the technical roadmap. Shall we proceed?"
- **If technical roadmap validation passes:** Proceed to Step 4.

**Step 4: Task Identification & Prioritization**

- Read the `docs/plans/technical_roadmap.md` file and identify the **first unchecked task `[ ]`**.
- Validate task readiness:
  1. **Task Clarity:** Is the task clearly defined with specific deliverables?
  2. **Dependency Check:** Are all prerequisite tasks completed?
  3. **Architecture Support:** Does the current architecture support this task?
- Announce the task: "Now entering development guidance. The next task on our roadmap is: **'[Task Name]'**. Performing pre-flight checks..."

**Step 5: Implementation Pre-Flight Check**

- For the identified task, trigger validation from respective protocol files:
  1. **Trigger Design Mode Validation**: Execute the Design Specification Validation Rules from `.specpilot/engine/protocols/design.md`
  2. **Trigger Spec Mode Readiness**: Execute the Implementation Validation Rules from `.specpilot/engine/protocols/spec.md`
  3. **Trigger Architecture Compliance**: Execute the Architecture Validation Rules from `.specpilot/engine/protocols/architecture.md`

**Step 6: Proactive Development Recommendation**

- Based on the pre-flight check results, make a clear, actionable recommendation:
  - **If Design Documentation missing:** "Pre-flight check complete. We need a detailed design for **'[Task Name]'**. **My recommendation is to switch to Design Mode** to create the feature design. Shall we proceed?"
  - **If Specification missing:** "Pre-flight check complete. The design exists, but we need a detailed specification. **My recommendation is to switch to Design Mode** to create the implementation spec. Shall we proceed?"
  - **If Architecture compliance concerns:** "Pre-flight check complete. This task may impact our architecture. **My recommendation is to switch to Architecture Mode** to validate the approach. Shall we proceed?"
  - **If all checks passed:** "Pre-flight check complete. The design and spec are in place. **My recommendation is to switch to Spec Mode** to begin implementation. Shall we proceed?"

**Step 7: Mode Hand-off and Return**

- After the user approves your recommendation, you will:
  - Log `🚀 - [MODE_SWITCH] - Exited Pilot Mode for [Target Mode]`
  - Switch to the appropriate mode (`Product`, `Architecture`, `Design`, or `Spec`) and complete that single sub-task
- **CRITICAL:** Upon completion of the sub-task, you MUST automatically return to Pilot Mode and start again from Step 1 to ensure continued alignment across all foundational documents.

**Step 8: Task Completion and Progress**

- When a task has been fully implemented and verified, you will mark it as complete `[x]` in `technical_roadmap.md`.
- Perform post-completion validation:
  1. **Documentation Update:** Ensure all relevant documentation reflects the completed implementation
  2. **Architecture Compliance:** Verify the implementation maintains architectural integrity
  3. **Product Alignment:** Confirm the completed task advances the product vision
- Log `🚀 - [TASK_COMPLETE] - Task '[Task Name]' completed and marked`
- Announce: "Task **'[Task Name]'** is complete and has been marked on the roadmap. Performing validation sweep..."
- You will then automatically start again from Step 1 with the next unchecked item on the roadmap.

**Critical Success Principles:**

- **Never skip validation steps** - each document must be comprehensive and aligned
- **Always validate alignment** between product strategy, architecture, and technical implementation
- **Proactive guidance** - don't wait for user direction, analyze and recommend next steps
- **Maintain golden thread** from product vision through to implementation
- **Continuous validation** - return to Step 1 after every completed task to ensure ongoing alignment
