### ## Global Logging Rules

This project uses a two-tiered logging system. For every significant action, you **MUST** append new entries to the appropriate log file. **CRITICAL: Always append to the end of log files - never edit or rewrite existing log content.**

**LOGGING FREQUENCY**: You must log using a batched milestone approach:

**Immediate Logging (specpilot.log):**

- All mode switches, code proposals, and verification results
- All significant development activities and decisions

**Batched Logging (specpilot_verbose.log) - Write at these triggers:**

- Right before any code commit (in Commit Mode)
- At the start of responding to any user prompt
- Batch should include: Complete conversation cycles, full transcripts, questions/responses, dialogue cycles from the session

1.  **`.specpilot/workspace/logs/specpilot.log` (Milestone Log)**: This file captures high-level project progress. You must append the following events here:
    - `[MODE_SWITCH]`
    - `[Pilot_...]`
    - `[GIT_COMMIT_SUCCESS]`

2.  **`.specpilot/workspace/logs/specpilot_verbose.log` (Verbose Log)**: This file captures the full, detailed history of every interaction. You must append all other events here. **Crucially, for every turn, you must also append a full transcript of the interaction**, formatted as follows:

    **Event markers (with full prefixes):**

    ```
    username - mode_emoji - [EVENT_TYPE] - content
    ```

    **Transcript entries (single prefix, then clean content):**

    ```
    username - mode_emoji - [TRANSCRIPT] - Complete conversation cycle
    ---
    ### USER PROMPT:
    [The user's complete and verbatim prompt]

    ### CURSOR RESPONSE:
    [Your complete and verbatim response, including any questions you ask]

    ### USER RESPONSE:
    [User's response to your questions, if applicable]

    ### CURSOR FOLLOW-UP:
    [Your follow-up response, final thoughts, or conclusions]
    ---
    ```

**CRITICAL: All logging must happen CONTINUOUSLY throughout project work. Logging should be done by appending to log files during conversations to maintain complete development audit trails.**

**IMPLEMENTATION NOTE: Logging uses a batched milestone approach - milestone events are logged immediately to .specpilot/workspace/logs/specpilot.log, while verbose transcripts are collected and batched for writing only at specific trigger points: (1) right before code commits, and (2) at the start of responding to prompts. This minimizes visible logging operations while maintaining complete audit trails.**

**VERBOSE LOGGING FORMAT**: For verbose log transcripts, use a single timestamp prefix for the entire entry, followed by clean transcript content without additional prefixes. This allows efficient appending of complete interactions while maintaining timestamp tracking.

**LOGGING IMPLEMENTATION:**

```bash
# Milestone logging (.specpilot/workspace/logs/specpilot.log) - Immediate:
Use edit_file to manually append: "username - emoji - [EVENT] - description"

# Verbose logging (.specpilot/workspace/logs/specpilot_verbose.log) - Batched at milestones:
Use terminal commands to efficiently append batched conversations at:
- Start of responding to prompts
- Right before code commits

Alternative Command Options (use any to avoid EOF stalling):
1. echo "$(date +"%Y-%m-%d %H:%M:%S") - content" >> .specpilot/workspace/logs/specpilot_verbose.log
2. printf "content\n" >> .specpilot/workspace/logs/specpilot_verbose.log
3. echo "content" | tee -a .specpilot/workspace/logs/specpilot_verbose.log >/dev/null

Batch format:
username - emoji - [TRANSCRIPT_BATCH] - Session conversations
---
[Multiple conversation cycles from the session]
---
```

- **Event Formats**:
  - **Commands**: `📝 - [COMMAND] - My full command text`
  - **Mode Switches**:
    `🚦 - [MODE_SWITCH] - Switched to Initialization Mode`
    `🚀 - [MODE_SWITCH] - Switched to Pilot Mode`
    `🌱 - [MODE_SWITCH] - Switched to Bootstrap Mode`
    `🏛️ - [MODE_SWITCH] - Switched to Architecture Mode`
    `🎨 - [MODE_SWITCH] - Switched to Design Mode`
    `📐 - [MODE_SWITCH] - Switched to Spec Mode`
    `🍄 - [MODE_SWITCH] - Switched to Vibe Mode`
    `🕵️ - [MODE_SWITCH] - Switched to Deep Check Mode`
    `🛠️ - [MODE_SWITCH] - Switched to Scripts Mode`
    `💡 - [MODE_SWITCH] - Switched to Product Mode`
    `🎁 - [MODE_SWITCH] - Switched to Commit Mode`
    `⚙️ - [MODE_SWITCH] - Switched to Config Mode`
  - **Pilot Step Execution**:
    `🤖🏛️ - [Pilot_ARCH] - Executing: [Task text from roadmap]`
    `🤖🎨 - [Pilot_DESIGN] - Executing: [Task text from roadmap]`
    `🤖📐 - [Pilot_SPEC] - Executing: [Task text from roadmap]`
  - **Proposals**:
    `🏛️ - [ARCHITECTURE_PROPOSED] - ...`
    `🏛️ - [DESIGN_PROPOSED] - ...`
    `🤔 - [CODE_PROPOSED] - ...`
    `🪄 - [CODE_PROPOSED] - ...`
  - **Product Mode Events**:
    `💡 - [PRODUCT_DEFINITION] - Vision/Problem/Audience/Features/Metrics defined`
    `💡 - [STRATEGIC_ANALYSIS] - Starting/completed strategic analysis phase`
    `💡 - [ROADMAP_GENERATION] - Starting roadmap generation phase`
    `💡 - [ROADMAP_COMPLETE] - Product roadmap generation completed`
  - **Iteration & Failures**:
    `💬 - [PLAN_ITERATION] - User provided feedback on the proposed plan.`
    `❌ - [VERIFICATION_FAILED] - User reported that the implementation did not pass verification.`
    `⚠️ - [AI_ERROR] - I encountered an internal error: [Error details]`
  - **Git Proposals & Success**:
    `▶️ - [GIT_COMMIT_PROPOSAL] - ...`
    `✅ - [GIT_COMMIT_SUCCESS] - ...` with a `###` separator.
