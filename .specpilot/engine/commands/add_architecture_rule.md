### ## 🏛️ Add Architecture Rule Command Protocol

This command adds new architecture rules to the `docs/plans/architecture.md` file in the appropriate section.

**Usage:** "Add Architecture Rule [rule description]"

**Step 1: Validate Architecture File**
- Check if `docs/plans/architecture.md` exists
- If missing, recommend running Architecture Mode first to create the base architecture

**Step 2: Locate Rule Insertion Point**
- Read the current architecture.md file
- Identify the "Core Principles" section (typically Section 1)
- Find the appropriate subsection or create a new one if needed

**Step 3: Format the Rule**
- Format the rule with proper numbering/bullet structure
- Ensure consistency with existing rule formatting
- Include rationale if the rule needs explanation

**Step 4: Insert the Rule**
- Add the rule to the appropriate section
- Maintain proper document structure and formatting
- Update numbering if necessary

**Step 5: Log and Confirm**
- Log `🏛️ - [ARCHITECTURE_RULE_ADDED] - Rule added: [brief description]`
- Announce: "Architecture rule has been added to `docs/plans/architecture.md`"
- Display the new rule for confirmation 