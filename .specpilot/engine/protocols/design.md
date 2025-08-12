### ## 🎨 Design Mode Protocol

Focus on creating `.md` spec files. **You do not write code or propose commits in this mode.**

---

## **Design Specification Validation Rules**
*(Self-contained validation criteria for Design Mode completeness)*

### **Design Completeness Criteria:**
A design specification is considered **COMPLETE** when all of the following elements are present:

1. **Feature Overview (Required)**
   - ✅ **Complete**: Clear description of what the feature does and why it's needed
   - ✅ **Strong**: Links back to product requirements and architectural context
   - ❌ **Incomplete**: Vague feature description or missing business context

2. **User Stories & Acceptance Criteria (Required)**
   - ✅ **Complete**: 3+ user stories with specific acceptance criteria for each
   - ✅ **Strong**: Clear "As a [user], I want [goal] so that [benefit]" format
   - ❌ **Incomplete**: Missing user stories or vague acceptance criteria

3. **Technical Requirements (Required)**
   - ✅ **Complete**: Specific inputs, outputs, data models, and API contracts
   - ✅ **Strong**: Detailed interface definitions and data validation rules
   - ❌ **Incomplete**: Vague technical requirements or missing interface details

4. **Architecture Alignment (Required)**
   - ✅ **Complete**: Clear mapping to architectural components and design patterns
   - ✅ **Strong**: Follows established architectural principles and interfaces
   - ❌ **Incomplete**: No architectural context or conflicts with system design

5. **Implementation Guidance (Required)**
   - ✅ **Complete**: Specific guidance on implementation approach and key decisions
   - ✅ **Strong**: Clear development priorities and complexity considerations
   - ❌ **Incomplete**: No implementation guidance or unclear development path

### **Advanced Design Criteria:**

6. **Error Handling & Edge Cases (Advanced)**
   - ✅ **Complete**: Comprehensive error scenarios and handling strategies
   - ✅ **Strong**: Specific error messages, fallback behaviors, and recovery paths
   - ❌ **Incomplete**: Missing error handling or generic error considerations

7. **Performance Considerations (Advanced)**
   - ✅ **Complete**: Performance requirements, optimization opportunities, and constraints
   - ✅ **Strong**: Specific performance targets and measurement criteria
   - ❌ **Incomplete**: No performance considerations or vague requirements

8. **Testing Strategy (Advanced)**
   - ✅ **Complete**: Testability considerations and verification approach
   - ✅ **Strong**: Specific test scenarios and validation methods
   - ❌ **Incomplete**: No testing considerations or unclear verification plan

### **Validation Commands:**
- **Check Core**: Evaluate if fundamental design elements meet completeness criteria
- **Check Advanced**: Evaluate if error handling, performance, and testing are complete
- **Check Alignment**: Verify design aligns with architecture and product requirements
- **Check Implementation Readiness**: Determine if design is ready for Spec Mode implementation

1.  **Propose Design Content**: 
    - Log `🎨 - [MODE_SWITCH] - Switched to Design Mode`
    - First, describe the proposed design for the spec in plain language and await my approval.

2.  **Create/Refine Design File**: Once the content plan is approved, create the full `.md` file, following the structure for spec files defined in `docs/project_conventions.md`.

3.  **Await Approval**: After providing the `.md` file, log `🎨 - [DESIGN_PROPOSED]` and ask: **"Is this design approved?"** Once approved:
    - Log `🎨 - [DESIGN_APPROVED] - Design approved and completed`
    - Log `🎨 - [MODE_SWITCH] - Exited Design Mode`
    - The task is complete.
