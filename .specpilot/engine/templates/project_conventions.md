# Project Conventions

> **Instruction to the Developer:** This document is the official source of truth for all development standards in this project. It is read by the SpecPilot agent to enforce quality and consistency.

---

## 1. The "Golden Thread": File Naming
Every feature must follow a strict naming convention that creates a "golden thread" from specification to implementation to verification.

| Artifact        | Location              | Naming Convention         |
| :-------------- | :-------------------- | :------------------------ |
| **Specification** | `docs/specs/`         | `spec_[feature_name].md`  |
| **Source Code** | `src/[project_name]/` | `[feature_name].py`       |
| **Test File** | `tests/`              | `test_[feature_name].py`  |

## 2. Testing Philosophy
- **Isolation:** Tests must be independent and must not rely on external services (e.g., live databases or APIs). Use mocks and stubs.
- **No Business Logic:** Tests should only contain orchestration and verification logic.
- **Clarity:** Follow a clear Arrange-Act-Assert pattern.

## 3. Commit Messages
All commit messages must follow the [Conventional Commits](https://www.conventionalcommits.org/) specification. This is enforced during the `Commit Mode` review. 