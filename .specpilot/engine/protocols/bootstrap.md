### ## 🚀 Bootstrap Mode Protocol

This mode is for initializing a new project. You must follow these steps:

---

## **Bootstrap Completion Validation Rules**
*(Self-contained validation criteria for Bootstrap Mode completeness)*

### **Project Setup Completeness Criteria:**
A bootstrap setup is considered **COMPLETE** when:

1. **Directory Structure (Required)**
   - ✅ **Complete**: All required directories created (docs/plans, docs/specs, src/, tests/, .specpilot/)
   - ✅ **Strong**: Proper directory hierarchy with appropriate permissions
   - ❌ **Incomplete**: Missing directories or incorrect structure

2. **Framework Installation (Required)**
   - ✅ **Complete**: SpecPilot engine copied to .specpilot/engine/ with all protocols
   - ✅ **Strong**: All protocol files, commands, and templates properly installed
   - ❌ **Incomplete**: Missing framework files or incomplete installation

3. **User Configuration (Required)**
   - ✅ **Complete**: User workspace created with proper namespacing ([username]/ directories)
   - ✅ **Strong**: Personal directives, config files, and notes initialized
   - ❌ **Incomplete**: Missing user workspace or configuration files

4. **Documentation Foundation (Required)**
   - ✅ **Complete**: Template files created for architecture.md, product_roadmap.md, technical_roadmap.md
   - ✅ **Strong**: Project conventions established with Golden Thread naming rules
   - ❌ **Incomplete**: Missing documentation templates or conventions

5. **User Approval (Required)**
   - ✅ **Complete**: User has approved the complete project structure plan
   - ✅ **Strong**: All destructive operations confirmed by user
   - ❌ **Incomplete**: Setup proceeding without explicit user approval

### **Validation Commands:**
- **Check Structure**: Verify all required directories and files are created
- **Check Installation**: Confirm SpecPilot framework is properly installed
- **Check Configuration**: Validate user-specific setup is complete
- **Check Readiness**: Determine if project is ready for Product Mode

1.  When I say **"Bootstrap new project,"**:
    - Use Logging Helper to write: `🌱` `MODE_SWITCH` `Switched to Bootstrap Mode` (full timestamped prefix required)
    - Await my next message, which will be the project brief.

2.  Analyze the brief to determine a `project_name` (in snake_case).
    - Log `🌱 - [PROJECT_ANALYSIS] - Project analyzed: [project_name]`

3.  Propose the creation of the entire standard directory structure (`docs/plans`, `docs/specs/project_name`, `src/project_name`, `tests/project_name`, `settings`).

4.  Propose the creation of all standard configuration files (`.cursor-rules.json`, `.gitignore`, `requirements.txt`).

5.  Populate `docs/plans/product_roadmap.md` and `docs/plans/technical_roadmap.md` with a summary derived from the project brief.

6.  **Crucially**, you must also propose the creation of `settings/spec_driven_prompt.md` (populating it with these instructions) and `docs/project_conventions.md` (populating it with the content from the "Documentation Templates" section of this prompt).

7.  Create a `.specpilot/workspace/notepad/note.md` file using the standardized notepad template with sections: "Ideas", "To Do List", "Decisions to Make", and "Other Notes".

8.  Present this entire file and directory creation plan for my approval.
    - Log `🌱 - [BOOTSTRAP_PLAN] - Project structure plan presented for approval` 

9.  **Product Mode Recommendation:** After the project structure is created:
    - Log `🌱 - [BOOTSTRAP_COMPLETE] - Project structure created successfully`
    - Log `🌱 - [MODE_SWITCH] - Exited Bootstrap Mode`
    - Announce: "Your new project is set up successfully! I recommend we now enter **Product Mode** to define your product vision, conduct strategic analysis, and create a comprehensive product roadmap. This will ensure we have a solid strategic foundation before beginning development work. Shall we proceed to Product Mode?"
