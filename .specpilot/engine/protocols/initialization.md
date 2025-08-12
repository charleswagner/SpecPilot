### ## 🚦 Initialization Mode Protocol

This is the master startup mode. Upon activation, you must immediately and automatically establish logging infrastructure, then perform a systematic pre-flight check of the project's foundational documents.

1.  **User Identification & Workspace Setup**: As per the main orchestrator's boot sequence, identify the user by checking for `.specpilot.local` first, then falling back to Git. Once the `current_user_id` is determined, verify that their workspace directory exists at `.specpilot/workspace/[current_user_id]/`. If it does not, create it along with its subdirectories (`logs`, `notepads`). Use Logging Helper to log: `📝 - [LOG_HELPER] - log_milestone("🚦", "USER_IDENTIFIED", "User identified as [current_user_id]")`

2.  **Logging Initialization**: Use Logging Helper to ensure `.specpilot/workspace/[current_user_id]/logs/` exists: `📝 - [LOG_HELPER] - ensure_logs_directory()`. If logs exist under a different user (e.g., `cursor/`), migrate them: `📝 - [LOG_HELPER] - migrate_logs_if_needed()`. Log the initialization start: `📝 - [LOG_HELPER] - log_milestone("🚦", "MODE_SWITCH", "Switched to Initialization Mode")`. Begin batched transcripts: `📝 - [LOG_HELPER] - log_verbose("Initialization Mode activated - beginning systematic project validation")`.

3.  **Perform Systematic Check**: In order, check for the existence of the following files. Log each validation step: `📝 - [LOG_HELPER] - log_milestone("🔍", "SYSTEMATIC_CHECK", "Beginning systematic validation of foundational documents")`
    1. `README.md`
    2. `docs/project_conventions.md`
    3. `docs/plans/product_roadmap.md`
    4. `docs/plans/technical_roadmap.md`
    5. `docs/plans/architecture.md`
    6. `.specpilot/workspace/notepad/note.md`

3.1. **Comprehensive Architecture Validation**: After confirming all files exist, perform full architectural analysis: - **Document Alignment**: Compare technical roadmap, product roadmap, and README goals with architecture coverage - **Implementation Compliance**: Analyze `src/` codebase to verify implementation follows architectural patterns - **Component Interface Validation**: Check that code components implement documented architectural interfaces - **Security Architecture Compliance**: Verify security patterns are implemented as specified - **Approved Deviations Review**: Check architecture document for explicit exceptions that justify implementation gaps - **Architecture Comprehensiveness Assessment**: Validate that architecture document covers all technical roadmap components and provides complete system design

3.2. **Architecture Validation Classification**: Generate severity-classified report: - **🚨 CRITICAL**: Security violations, data integrity risks, architectural violations that could cause system failure - **⚠️ WARN**: Style deviations, performance concerns, documentation gaps, missing interfaces - **✅ COMPLIANT**: Components that properly follow architectural specifications - **📋 APPROVED EXCEPTIONS**: Deviations explicitly documented in architecture deviations log - **📝 INCOMPLETE**: Architecture gaps where roadmap components lack architectural coverage

4.  **Route Based on Check Result**:
    - **If any file is missing**: You **MUST STOP**. Announce missing document and switch to appropriate mode.
    - **If CRITICAL architectural violations found**: Present full validation report. Continue to **Pilot Mode** but warn user of critical risks.
    - **If INCOMPLETE architecture found**: Present comprehensiveness gaps and ask targeted questions to complete architecture coverage.
    - **If only WARN-level issues found**: Log warnings and continue to **Pilot Mode**
    - **If all validations pass**: Announce architectural soundness and switch to **Pilot Mode**

5.  **Development Modes Overview**: After completing the systematic check and before routing to the next mode, provide a comprehensive overview of all available development modes and their purposes:

    ## 🚀 SpecPilot Development Modes Overview

    **SpecPilot operates through 10 specialized modes, each designed for specific development phases:**

    ### **🚦 Initialization Mode** (Current)
    - **Purpose**: Project startup and validation
    - **Activities**: Validates foundational documents, performs architecture validation, establishes logging
    - **When to use**: Automatically runs at session start, validates project readiness

    ### **✈️ Pilot Mode** (Primary Development)
    - **Purpose**: Proactive development guidance along the Golden Path
    - **Activities**: Analyzes project state, guides Architecture → Design → Spec → Implementation flow, provides recommendations
    - **When to use**: For guided development, proactive task management, systematic roadmap execution
    - **Command**: "Enter Pilot Mode"

    ### **🚀 Bootstrap Mode** (New Projects)
    - **Purpose**: Initialize new projects with complete structure
    - **Activities**: Creates directory structure, foundational documents, configuration files
    - **When to use**: Starting completely new projects from scratch
    - **Command**: "Bootstrap new project"

    ### **🏛️ Architecture Mode** (Design & Planning)
    - **Purpose**: Collaborative architectural design and validation
    - **Activities**: Asks targeted questions, validates implementation against architecture, collaborative decision-making
    - **When to use**: Architectural changes, system design, addressing architectural gaps
    - **Command**: "Architecture mode"

    ### **🎨 Design Mode** (Specification Creation)
    - **Purpose**: Create detailed specification documents
    - **Activities**: Creates `.md` spec files, follows documentation templates, no code writing
    - **When to use**: Defining new features, creating specifications before implementation
    - **Command**: "Design mode"

    ### **📐 Spec Mode** (Implementation)
    - **Purpose**: Implement code based on specifications
    - **Activities**: Writes code and tests, provides verification plans, requires manual testing confirmation
    - **When to use**: Implementing features from specifications, writing production code
    - **Command**: "Spec mode"

    ### **🍄 Vibe Mode** (Debugging & Troubleshooting)
    - **Purpose**: Debugging and quick fixes
    - **Activities**: Provides direct solutions, troubleshooting, rapid problem resolution
    - **When to use**: Debugging issues, quick fixes, troubleshooting problems
    - **Command**: "Vibe mode"

    ### **🕵️ Deep Check Mode** (Quality Assurance)
    - **Purpose**: Comprehensive project auditing
    - **Activities**: Validates documentation-code sync, architecture compliance, identifies violations
    - **When to use**: Before commits, quality assurance, identifying project issues
    - **Command**: "Run a deep check"

    ### **🛠️ Scripts Mode** (Utility Management)
    - **Purpose**: Create and manage utility scripts
    - **Activities**: Creates scripts in `scripts/` directory, utility automation
    - **When to use**: Creating deployment scripts, automation tools, utilities
    - **Command**: "Scripts mode"

    ### **🎁 Commit Mode** (Intelligent Commits)
    - **Purpose**: Intelligent commit analysis and generation
    - **Activities**: Analyzes development session, generates enhanced commit messages, provides development intelligence
    - **When to use**: When ready to commit work, for intelligent commit analysis
    - **Command**: "Commit mode"

    ### **⚙️ Config Mode** (Framework Configuration)
    - **Purpose**: Manage SpecPilot framework settings
    - **Activities**: Updates configuration files, manages framework behavior
    - **When to use**: Adjusting framework behavior, changing logging settings
    - **Command**: "Configure SpecPilot:" or "Config Mode"

    **💡 Quick Reference**: Each mode has specific protocols and expectations. Use the appropriate mode for your current development phase to get the most effective assistance.

6.  **Final Step**: After completing the systematic check and providing the modes overview, announce completion and guide the user to the next step. Log completion: `📝 - [LOG_HELPER] - log_milestone("✅", "INITIALIZATION_COMPLETE", "SpecPilot framework initialization complete - ready for development")`

    "Initialization complete. The framework is now ready to guide you. **To begin the guided development process, say 'Enter Pilot Mode'.**"
