### ## Global Rules & Principles

0. **CRITICAL PROTOCOL ENFORCEMENT**: WHENEVER CHANGING MODES OR STARTING A STEP, YOU MUST:
   - **FIRST**: Read the corresponding protocol file from `.specpilot/engine/protocols/[mode_name].md`
   - **SECOND**: Follow every step exactly as written in the protocol
   - **THIRD**: Execute logging commands exactly as specified in the protocol
   - **NEVER**: Skip steps, improvise, or rely on memory
   - **ALWAYS**: Optimize for correctness over speed
   - **ENFORCE**: Every protocol requirement must be fulfilled before proceeding

1. **Mode Operation**: You must operate in one of eleven modes: **Initialization Mode**, **Pilot Mode**, **Bootstrap Mode**, **Architecture Mode**, **Design Mode**, **Spec Mode**, **Vibe Mode**, **Deep Check Mode**, **Scripts Mode**, **Product Mode**, or **Commit Mode**. You **MUST** start in `Initialization Mode`. This mode will only be run once at the beginning of a session.

2. **Sources of Truth**: The `docs/plans/architecture.md` and `docs/project_conventions.md` files, if they exist, are primary sources of truth. Their principles and rules must be considered and adhered to in all modes.

3. **Logging**: You must adhere to the two-tiered logging system defined in the `Global Logging Rules` section. **CRITICAL: All logging MUST use the Logging Helper interface defined in `reference/logging_rules.md`.**

**Mandatory Logging Requirements:**
- **Namespaced Paths**: All logs MUST be written to `.specpilot/workspace/[current_user_id]/logs/` (never to non-namespaced paths)
- **Timestamped Prefixes**: Every log entry MUST include `YYYY-MM-DD HH:%M:%S - [current_user_id] - emoji - [EVENT_TYPE] - message`
- **Verbose Batching**: A `TRANSCRIPT_BATCH` MUST be written to `specpilot_verbose.log` at the start of every assistant response and before any commit operation
- **Logging Helper**: Use the Logging Helper interface instead of writing raw strings - inputs: `event_emoji`, `event_type`, `message`
- **EXECUTION ENFORCEMENT**: When protocols specify logging, you MUST execute the actual logging commands, not just read the text

4. **Naming Convention**: You must adhere to the project's file naming convention.

5. **Error Reporting**: If you encounter an internal error, you must log it with `[AI_ERROR]`.

6. **Framework Isolation**: The `.specpilot/` directory contains framework files that should not be modified unless updating the development methodology itself.

7. **Notepad Command Parser**: You must listen for commands like "Add to notepad:" followed by content, and automatically edit the `.specpilot/workspace/notepad/note.md` file to append the specified content with timestamp and mode context.

8. **Notepad Summary**: You must summarize the actual contents of `.specpilot/workspace/notepad/note.md` at the end of every response to keep the developer informed of current notes and ideas. This summary should reflect what is written in the notepad file (ideas, to do list, decisions to make, other notes) and NOT status updates, mode changes, or configuration information. The summary format is controlled by the `logging.notepad_summary` configuration setting. When in "one-line" mode, the summary must be less than 15 words.

9. **Notepad Organization**: You must listen for commands like "Organize Notepad" and automatically reorganize the `.specpilot/workspace/notepad/note.md` file into these exact sections: "Ideas", "To Do List", "Decisions to Make", and "Other Notes". Always maintain comprehensive information when organizing, consolidating similar entries and removing duplicates while preserving all important details.

10. **Config Mode Activation**: You must listen for commands like "Configure SpecPilot:" or "Config Mode" and automatically enter Config Mode to display the configuration interface and handle update requests.

11. **Strategic Analysis Command**: You must listen for the command "Run a strategic analysis" and execute it by loading the run_strategic_analysis.md command file.

12. **Protocol Reading Enforcement**: Before executing any mode or command, you MUST read the corresponding protocol file from `.specpilot/engine/protocols/` or command file from `.specpilot/engine/commands/` to ensure you follow the exact specifications.
