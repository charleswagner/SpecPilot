### ## 🏛️ Architecture Mode Protocol

Focus on creating or updating the `docs/plans/architecture.md` file through a collaborative, multi-step process.

---

## **Architecture Validation Rules**
*(Self-contained validation criteria for Architecture Mode completeness)*

### **Architecture Completeness Criteria:**
An architecture is considered **COMPLETE** when all of the following elements are present and validated:

1. **Core Principles (Required)**
   - ✅ **Complete**: 3+ fundamental design principles clearly stated
   - ✅ **Strong**: Principles address security, performance, maintainability, and scalability
   - ❌ **Incomplete**: Generic principles or fewer than 3 specific rules

2. **System Overview (Required)**
   - ✅ **Complete**: High-level description of all major system components and interactions
   - ✅ **Strong**: Clear data flow, user journey, and component responsibilities
   - ❌ **Incomplete**: Template content or missing component interactions

3. **Component Architecture (Required)**
   - ✅ **Complete**: Detailed breakdown of all system components with defined interfaces
   - ✅ **Strong**: Clear separation of concerns, well-defined APIs, data models
   - ❌ **Incomplete**: Missing component details or undefined interfaces

4. **Technical Diagrams (Required)**
   - ✅ **Complete**: Visual representation using Mermaid.js syntax showing system flow
   - ✅ **Strong**: Multiple diagram types (flowchart, sequence, component diagrams)
   - ❌ **Incomplete**: Generic diagrams or missing visual representations

5. **Product-Architecture Alignment (Required)**
   - ✅ **Complete**: Architecture supports all MVP features from product roadmap
   - ✅ **Strong**: Clear traceability from product features to architectural components
   - ❌ **Incomplete**: Missing coverage of product features or unclear mapping

### **Advanced Architecture Criteria:**

6. **Security Architecture (Advanced)**
   - ✅ **Complete**: Security patterns, authentication, authorization, and data protection defined
   - ✅ **Strong**: Threat model considerations and security by design principles
   - ❌ **Incomplete**: No security considerations or generic security statements

7. **Performance Architecture (Advanced)**
   - ✅ **Complete**: Performance requirements, bottleneck analysis, scaling strategy
   - ✅ **Strong**: Specific performance targets and optimization approaches
   - ❌ **Incomplete**: No performance considerations or vague requirements

8. **Approved Deviations Log (Advanced)**
   - ✅ **Complete**: Documentation of any architectural compromises with rationale
   - ✅ **Strong**: Clear resolution timeline and impact assessment
   - ❌ **Incomplete**: Undocumented deviations or missing justification

### **Technical Roadmap Validation Rules:**
*(Self-contained validation criteria for Technical Roadmap completeness)*

A technical roadmap is considered **COMPLETE** when all of the following elements are present:

9. **Roadmap Structure (Required)**
   - ✅ **Complete**: Clear phases with logical task groupings and dependencies
   - ✅ **Strong**: Tasks organized by feature/component with clear progression
   - ❌ **Incomplete**: Unorganized task list or missing phase structure

10. **Task Definition (Required)**
    - ✅ **Complete**: Each task has specific deliverables and clear acceptance criteria
    - ✅ **Strong**: Tasks follow Golden Thread pattern (Architecture → Spec → Implementation → Testing)
    - ❌ **Incomplete**: Vague tasks or missing implementation details

11. **Product Alignment (Required)**
    - ✅ **Complete**: All product roadmap features are covered by technical tasks
    - ✅ **Strong**: Clear traceability from product features to engineering work
    - ❌ **Incomplete**: Missing coverage of product requirements or unclear mapping

12. **Implementation Readiness (Required)**
    - ✅ **Complete**: First unchecked task `[ ]` has all prerequisites completed
    - ✅ **Strong**: Task dependencies are clearly defined and satisfied
    - ❌ **Incomplete**: Blocked tasks or missing prerequisite work

### **Validation Commands:**
- **Check Core**: Evaluate if fundamental architecture elements meet completeness criteria
- **Check Advanced**: Evaluate if security, performance, and deviation tracking are complete
- **Check Alignment**: Verify architecture supports all product strategy requirements
- **Check Roadmap**: Validate technical roadmap completeness and task readiness
- **Check Readiness**: Determine if architecture is ready for technical roadmap generation

1.  **Pre-Architecture Analysis**: 
    - Log `🏛️ - [MODE_SWITCH] - Switched to Architecture Mode`
    - Before proposing architectural changes, perform comprehensive validation:
    - **Current Implementation Assessment**: Analyze existing `src/` codebase against current architecture
    - **Roadmap Alignment Analysis**: Identify technical roadmap components lacking architectural coverage
    - **Architecture Comprehensiveness Assessment**: Validate that architecture document provides complete coverage of all system components, data flows, external integrations, security patterns, and performance requirements
    - **Implementation-Architecture Gap Report**: Generate severity-classified analysis:
      - **🚨 CRITICAL**: Security violations, unsafe patterns, architectural violations causing system risks
      - **⚠️ WARN**: Suboptimal patterns, missing documentation, interface inconsistencies
      - **✅ COMPLIANT**: Proper architectural implementation
      - **📋 APPROVED EXCEPTIONS**: Documented deviations in architecture deviations log
      - **📝 INCOMPLETE**: Architecture gaps where roadmap components, system flows, or critical patterns lack documentation
    - **Present Validation Report**: Show user current architectural state before proposing changes
    - **Architecture Completeness Questions**: If INCOMPLETE gaps found, ask targeted questions to identify missing architectural elements

2.  **High-Level Discussion**: Initiate a collaborative discussion. First, summarize the **current architecture** as defined in `architecture.md` (if it exists). Then, ask specific collaborative questions to guide architectural decisions:

    **Architecture Gap Analysis Questions:**
    - "I found [X] CRITICAL violations and [Y] WARN issues. Which should we address first?"
    - "For the missing [Component Name], what are your preferences for [specific architectural decision]?"
    - "The current architecture doesn't cover [Phase 2 feature]. How should we integrate this?"
    - "I see [specific violation]. Should we fix the implementation or add it to approved deviations?"

    **Architecture Comprehensiveness Questions:**
    - "The architecture document lacks coverage for [Component/Feature] from the technical roadmap. How should this component integrate with the existing system?"
    - "I don't see architectural patterns for [Data Flow/Integration]. What are your requirements for this interaction?"
    - "The architecture is missing [Security/Performance/Reliability] specifications for [Component]. What are your requirements here?"
    - "Several roadmap components ([List]) lack architectural documentation. Should we prioritize these or focus on current phase requirements?"
    - "The system diagram doesn't show [External Service/Database/API] integration patterns. How should these be architected?"
    - "Error handling and recovery patterns are not fully documented for [Component/Flow]. What's your preferred approach?"

    **Component Design Questions:**
    - "For [Component Name], do you prefer [Option A] or [Option B] approach?"
    - "How should [Component A] interact with [Component B]?"
    - "What security requirements do you have for [specific feature]?"
    - "Should [Component] be synchronous or asynchronous?"

    **Integration Strategy Questions:**
    - "For [External Service], what's your preferred authentication method?"
    - "How should we handle [specific error scenario]?"
    - "What performance requirements do you have for [specific operation]?"
    - "Should [Feature] be configurable or hardcoded?"

    **Phase Planning Questions:**
    - "Which Phase 2 components are most critical for your immediate needs?"
    - "Should we implement [Feature] now or defer to a later phase?"
    - "What's your timeline for [specific architectural change]?"
    - "Are there any constraints I should know about for [Component]?"

    **Collaborative Decision Making:**
    - Present specific options with pros/cons for each architectural decision
    - Ask for user preferences on implementation approaches
    - Confirm architectural trade-offs and their implications
    - Validate that proposed changes align with user's vision and constraints

3.  **Propose Principles**: Based on our collaborative discussion, propose a set of key architectural principles (e.g., "Security: All user data will be encrypted at rest," "Performance: API responses must be under 200ms"). **STOP** and await my approval of these principles.

4.  **Propose Detailed Design**: Once the principles are approved, propose the detailed architectural design. This includes component descriptions, diagrams (using Mermaid.js syntax), and the "Approved Deviations Log" for the current development phase. **STOP** and await my approval of this detailed design.

5.  **Collaborative Refinement**: After detailed design approval, engage in collaborative refinement:
    - **Component-Specific Questions**: "For [Component], should we use [Pattern A] or [Pattern B]?"
    - **Integration Questions**: "How should [Component A] communicate with [Component B]?"
    - **Security Questions**: "What authentication method do you prefer for [Service]?"
    - **Performance Questions**: "What are your latency requirements for [Operation]?"
    - **Implementation Questions**: "Should [Feature] be implemented now or deferred?"
    - **Validation Questions**: "Does this design match your vision for [Feature]?"

6.  **Create/Refine Architecture File**: Once collaborative refinement is complete, create or update the full `architecture.md` file with all the agreed-upon content, following the structure defined in `docs/project_conventions.md`.

7.  **Await Final Approval**: After providing the file, log `🏛️ - [ARCHITECTURE_PROPOSED]` and ask: **"Is this architecture approved?"** Once approved:
    - Log `🏛️ - [ARCHITECTURE_APPROVED] - Architecture approved and completed`
    - Log `🏛️ - [MODE_SWITCH] - Exited Architecture Mode`
    - The task is complete.
