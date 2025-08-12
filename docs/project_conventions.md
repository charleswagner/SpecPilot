# Project Conventions

This document defines the development standards for this project. It is the source of truth for all automated checks.

## 1. The "Golden Thread": File Naming
Every feature must follow a strict naming convention that creates a "golden thread" from specification to implementation to verification.

| Artifact | Location | Naming Convention |
| :--- | :--- | :--- |
| **Specification** | `docs/specs/` | `spec_[feature_name].md` |
| **Source Code**| `src/[project_name]/`| `[feature_name].py` |
| **Test File** | `tests/` | `test_[feature_name].py`|

## 2. Testing Philosophy
- **Isolation:** Tests must be independent and must not rely on external services (e.g., live databases or APIs). Use mocks and stubs.
- **No Business Logic:** Tests should only contain orchestration and verification logic.
- **Clarity:** Follow a clear Arrange-Act-Assert pattern.

## 3. Commit Messages
All commit messages must follow the Conventional Commits specification. 