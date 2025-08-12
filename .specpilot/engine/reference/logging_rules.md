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

**IMPLEMENTATION NOTE: Logging uses a batched milestone approach - milestone events are logged immediately to .specpilot/workspace/[current_user_id]/logs/specpilot.log, while verbose transcripts are collected and batched for writing only at specific trigger points: (1) right before code commits, and (2) at the end of completed command/response cycles. This minimizes visible logging operations while maintaining complete audit trails.**

**VERBOSE LOGGING FORMAT**: For verbose log transcripts, use a single timestamp prefix for the entire entry, followed by clean transcript content without additional prefixes. This allows efficient appending of complete interactions while maintaining timestamp tracking.

**LOGGING IMPLEMENTATION:**

```bash
# Milestone logging (.specpilot/workspace/logs/specpilot.log) - Immediate:
Use edit_file to manually append: "username - emoji - [EVENT] - description"

# Verbose logging (.specpilot/workspace/logs/specpilot_verbose.log) - Batched at milestones:
Use terminal commands to efficiently append batched conversations at:
- Start of responding to prompts
- Right before code commits

**EFFICIENT TRANSCRIPT BATCHING**: Use a single command to write the entire transcript batch at once:

```bash
cat << 'EOF' >> .specpilot/workspace/[current_user_id]/logs/specpilot_verbose.log
$(date +"%Y-%m-%d %H:%M:%S") - [current_user_id] - [emoji] - [TRANSCRIPT_BATCH] - [description]
---
USER: [user message]
---
CURSOR: [assistant response]
EOF
```

Alternative Command Options (use any to avoid EOF stalling):
1. echo "$(date +"%Y-%m-%d %H:%M:%S") - content" >> .specpilot/workspace/[current_user_id]/logs/specpilot_verbose.log
2. printf "content\n" >> .specpilot/workspace/[current_user_id]/logs/specpilot_verbose.log
3. echo "content" | tee -a .specpilot/workspace/[current_user_id]/logs/specpilot_verbose.log >/dev/null

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

## Canonical Log Destinations (namespaced)

All logging MUST use the current user's namespaced workspace paths:

- Milestone log: `.specpilot/workspace/[current_user_id]/logs/specpilot.log`
- Verbose log (batched transcripts): `.specpilot/workspace/[current_user_id]/logs/specpilot_verbose.log`

The `[current_user_id]` MUST be resolved per the boot sequence (see `main.md` and `initialization.md`). Do not write to non-namespaced paths.

## Logging Helper (required interface)

All protocols MUST use this helper behavior instead of writing raw strings:

- Inputs: `event_emoji`, `event_type`, `message`
- Milestone write (immediate): Append one line to `specpilot.log` in this exact format:
  `YYYY-MM-DD HH:MM:SS - [current_user_id] - {event_emoji} - [{event_type}] - {message}`
- Verbose batching: At batching triggers, append a transcript block to `specpilot_verbose.log`:
  `current_user_id - mode_emoji - [TRANSCRIPT_BATCH] - Session conversations` followed by `---` fenced sections for USER/CURSOR turns per the existing template.
- Create-on-missing: Ensure the logs directory exists; if created, first write `[LOG_DIR_CREATED]` to the milestone log.
- Migration-on-mismatch: If logs exist under a different user (e.g., `cursor/`), move them into the current user's logs and write `[LOGS_MIGRATED]` with source and destination.
- Error handling: On any write failure, write `⚠️ - [AI_ERROR] - Logging failure at [path]: [error]` to whichever file can be written.

## Batching Triggers (enforced)

You MUST append a transcript batch to the verbose log at:
- The end of every completed command/response cycle
- Immediately before any commit operation

If batching is not possible in a given runtime, write an immediate one-turn transcript entry as a fallback.

## Event Format (non-optional prefix)

Every milestone line MUST include the timestamp and username prefix as defined above. The short examples in protocols (e.g., `🚀 - [MODE_SWITCH] - …`) are symbolic; do not write them verbatim to files.
