### ## 🍄 Vibe Mode Protocol

Focus on debugging. **You do not propose commits in this mode.**

---

## **Debugging Solution Validation Rules**
*(Self-contained validation criteria for Vibe Mode completeness)*

### **Solution Completeness Criteria:**
A debugging solution is considered **COMPLETE** when:

1. **Problem Diagnosis (Required)**
   - ✅ **Complete**: Root cause identified with clear explanation
   - ✅ **Strong**: Understanding of why the issue occurred and impact analysis
   - ❌ **Incomplete**: Symptoms treated without addressing underlying cause

2. **Solution Quality (Required)**
   - ✅ **Complete**: Fix addresses the actual problem and follows code quality standards
   - ✅ **Strong**: Minimal, focused changes that don't introduce new issues
   - ❌ **Incomplete**: Hacky workarounds or overly complex solutions

3. **User Verification (Required)**
   - ✅ **Complete**: User confirms "the vibe worked" and problem is resolved
   - ✅ **Strong**: Solution tested in realistic scenarios and edge cases
   - ❌ **Incomplete**: User reports continued issues or incomplete fix

### **Validation Commands:**
- **Check Diagnosis**: Verify root cause analysis is accurate and complete
- **Check Solution**: Evaluate fix quality and potential side effects
- **Check Resolution**: Confirm user verification and problem resolution

1.  **Suggest Fixes**: 
    - Log `🍄 - [MODE_SWITCH] - Switched to Vibe Mode`
    - Provide direct answers and potential fixes.
2.  **Log and Await Feedback**: After providing a solution, log `🍄 - [CODE_PROPOSED]` and ask me: **"Did the vibe work?"**
3.  **Log Failure or Finish**: If I confirm it worked:
    - Log `🍄 - [VIBE_SUCCESS] - Vibe debugging completed successfully`
    - Log `🍄 - [MODE_SWITCH] - Exited Vibe Mode`
    - The task is complete.
    If I report failure, you **MUST** first log `🍄 - [VERIFICATION_FAILED]` and continue the conversation.
