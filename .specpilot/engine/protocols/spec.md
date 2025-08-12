### ## 📐 Spec Mode Protocol

Focus on implementing code based on a spec. **You do not propose commits in this mode.**

---

## **Implementation Validation Rules**
*(Self-contained validation criteria for Spec Mode completeness)*

### **Implementation Completeness Criteria:**
An implementation is considered **COMPLETE** when all of the following elements are validated:

1. **Design Compliance (Required)**
   - ✅ **Complete**: Implementation follows all design specifications exactly
   - ✅ **Strong**: All user stories and acceptance criteria are fully implemented
   - ❌ **Incomplete**: Missing features or deviations from design without approval

2. **Code Quality Standards (Required)**
   - ✅ **Complete**: Code follows project conventions, is well-documented, and maintainable
   - ✅ **Strong**: Clear function/class names, comprehensive docstrings, proper error handling
   - ❌ **Incomplete**: Poor code quality, missing documentation, or unclear logic

3. **Test Coverage (Required)**
   - ✅ **Complete**: Comprehensive unit tests covering all functionality and edge cases
   - ✅ **Strong**: Tests follow testing philosophy (independent, clear, no business logic)
   - ❌ **Incomplete**: Missing tests, poor test quality, or business logic in tests

4. **Architecture Alignment (Required)**
   - ✅ **Complete**: Implementation maintains architectural integrity and patterns
   - ✅ **Strong**: Proper separation of concerns, follows interface definitions
   - ❌ **Incomplete**: Architectural violations or improper component interactions

5. **Golden Thread Compliance (Required)**
   - ✅ **Complete**: File naming follows conventions (spec_[name].md → [name].py → test_[name].py)
   - ✅ **Strong**: Clear traceability from specification through implementation to tests
   - ❌ **Incomplete**: Naming convention violations or missing Golden Thread elements

### **Advanced Implementation Criteria:**

6. **Security Implementation (Advanced)**
   - ✅ **Complete**: Security requirements properly implemented with no vulnerabilities
   - ✅ **Strong**: Input validation, output encoding, proper authentication/authorization
   - ❌ **Incomplete**: Security gaps, hardcoded credentials, or unsafe practices

7. **Performance Implementation (Advanced)**
   - ✅ **Complete**: Performance requirements met with efficient algorithms and data structures
   - ✅ **Strong**: Optimization opportunities identified and implemented
   - ❌ **Incomplete**: Performance issues or inefficient implementation

8. **Human Verification Passed (Required)**
   - ✅ **Complete**: Manual testing confirms all functionality works as expected
   - ✅ **Strong**: Edge cases tested, error scenarios validated, user experience verified
   - ❌ **Incomplete**: Failed manual verification or untested scenarios

### **Validation Commands:**
- **Check Design Compliance**: Verify implementation matches design specifications
- **Check Code Quality**: Evaluate code standards, documentation, and maintainability
- **Check Test Coverage**: Verify comprehensive testing of all functionality
- **Check Architecture**: Ensure architectural integrity is maintained
- **Check Readiness**: Determine if implementation is ready for integration

**Step 1: Propose a Design & Verification Plan**
- Log `📐 - [MODE_SWITCH] - Switched to Spec Mode`
- Before writing any code, respond with a detailed plan. This plan MUST include:

- **Implementation Design**: A summary of the proposed solution, classes, and functions.
- **API Integration Strategy**: If any external APIs are used, this plan MUST detail which API and library will be used and the proposed method for handling credentials. You must default to a secure, environment-based method and NEVER propose hardcoding API keys.
- **Your Self-Check Plan**: How you will ensure your work is correct.
- **📋 Human Verification Plan**: A list of specific, step-by-step instructions for me to manually test the code. This should include any necessary commands to run, sample inputs to provide, and the expected output to look for. You must also provide the `echo` command to print these verification steps to the console for me to follow.

After presenting this complete plan, **STOP** and await my approval.

**🚨 CRITICAL ENFORCEMENT: You are FORBIDDEN from writing ANY implementation code, creating ANY files, or making ANY code changes until you receive explicit approval of your design and verification plan. Violation of this rule is a severe protocol breach.**

**Step 2: Iterate on the Plan**
If my response is not approval, you **MUST** first log `📐 - [PLAN_ITERATION]` before addressing my feedback.

**Step 3: Implement and Await Verification**
Write code and tests, log `📐 - [CODE_PROPOSED]`, then await my verification result.

**Step 4: Log Failure or Finish**
If I confirm success:
- Log `📐 - [SPEC_COMPLETE] - Specification implementation completed successfully`
- Log `📐 - [MODE_SWITCH] - Exited Spec Mode`
- The task is complete.
If I report a failure, you **MUST** first log `📐 - [VERIFICATION_FAILED]` and await my next instruction.
