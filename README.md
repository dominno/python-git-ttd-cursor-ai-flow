# passgen - Secure & Configurable Password Generator

> **Example Project**: This repository demonstrates how to implement a Test-Driven Development (TDD) workflow with Git in Cursor AI. It serves as a practical example of writing tests first, implementing features, and maintaining a clean Git history.

## Setting Up Cursor for TDD Workflow

To use this same TDD workflow in your own projects with Cursor AI, follow these setup steps:

### 1. Create Cursor Rules Directory

First, create a `.cursor/rules` directory in your project root:

```bash
mkdir -p .cursor/rules
```

### 2. Add TDD Rule File

Create a file named `ttd.mdc` in the `.cursor/rules` directory with the following content:

```markdown
description: Automate Git Flow with TDD
globs: *.py
---
# Workflow for Feature Implementation
- Start by creating a new branch for the feature.
- Write failing tests before implementing any functionality.
- Generate minimal code to pass the tests.
- Commit changes after passing tests.
- Refactor code only after all tests pass.
- Run all tests before merging the branch into `develop`.
- Revert branch if any test fails during CI or manual testing.
- Merge only if all tests pass.

# Automated Prompts:
1. "Create a new branch for {feature_name}."
2. "Write a failing test for {feature_name}."
3. "Generate code to pass the test."
4. "Commit changes after passing tests."
5. "Run all tests and ensure they pass."
6. "Merge branch into `develop` if all tests pass."
7. "Revert branch if any test fails."
```

Note: This is set for python files in "globs: *.py", set this to your project's file type.


### 3. Configure Cursor AI

1. Open Cursor AI settings
2. Navigate to the "Rules" section
3. Ensure the rule is enabled for your project

### 4. Using the TDD Workflow in Cursor

When working on a new feature:

1. Open Cursor AI and type "Create a new branch for [feature name]"
2. Follow the prompts to create your feature branch
3. Use "Write a failing test for [feature name]" to start with tests
4. Implement the feature using "Generate code to pass the test"
5. Commit changes and run tests as prompted
6. Merge your changes when all tests pass

The rule will guide you through the TDD process, ensuring you follow the "test first" approach consistently.

### 5. Required Git Workflow Rules

To ensure consistent Git workflow and PR management, you must add these exact rules to your Cursor AI rules configuration: 

```markdown
# Interfacing with Github
When asked, to submit a PR - use the Github CLI and assume I am already authenticated correctly. When asked to create a PR follow this process:

1. git status - to check if there are any changes to commit
2. git add . - to add all the changes to the staging area (IF NEEDED)
3. git commit -m "your commit message" - to commit the changes (IF NEEDED)
4. git push - to push the changes to the remote repository (IF NEEDED)
5. git branch - to check the current branch
6. git log main..[insert current branch] - specifically log the changes made to the current branch
7. git diff --name-status main - check to see what files have been changed
8. gh pr create --title "Title goes here..." --body "Example body..."

When asked to create a commit, first check for all files that have been changed using git status. Then, create a commit with a message that briefly describes the changes either for each file individually or in a single commit with all the files message if the changes are minor.

When writing a message for the PR, do not include new lines in the message. Just write a single long message.
```

These Git workflow rules ensure:
- Consistent commit and PR creation process
- Proper change verification before commits
- Clean and readable commit history
- Standardized PR format

### Example Workflow excuted by Cursor AI

For implementing a new password generation feature:

1. Create a feature branch: `git checkout -b feature/special-chars-generator`
2. Write tests in `tests/test_special_chars.py` that define requirements
3. Run tests to see them fail: `pytest -v tests/test_special_chars.py`
4. Implement the feature in `src/passgen/`
5. Run tests until they pass
6. Refactor code while maintaining passing tests
7. Merge feature branch back to develop

This workflow ensures every feature is thoroughly tested, well-documented, and properly integrated.

## Git & TDD Workflow

This project follows a strict Git branching strategy combined with Test-Driven Development principles to ensure high-quality code and maintainable features.

### Branch Structure

- **main**: Production-ready code
- **develop**: Integration branch for completed features
- **feature/x**: Feature-specific branches (e.g., `feature/basic-password-generation`)

### TDD Process for Each Feature

1. **Create Feature Branch**
   ```bash
   git checkout develop
   git checkout -b feature/new-feature-name
   ```

2. **Write Failing Tests First**
   - Create test file(s) in the `tests/` directory
   - Define expected behavior through test assertions
   - Run tests to confirm they fail (as functionality doesn't exist yet)

3. **Implement Minimal Code**
   - Write the minimal code necessary to make tests pass
   - Focus on meeting the requirements defined by tests
   - Avoid implementing anything not specified by tests

4. **Run Tests and Refactor**
   ```bash
   pytest -v tests/test_feature_name.py
   ```
   - Ensure all tests pass
   - Refactor code for clarity and maintainability
   - Run tests again after refactoring

5. **Commit Changes and Merge**
   ```bash
   git add .
   git commit -m "Implement feature-name functionality"
   git checkout develop
   git merge feature/new-feature-name
   ```




A pure Python library for generating secure, customizable passwords.

## Features

- Generate passwords with configurable length and character sets
- Include/exclude specific character categories (uppercase, lowercase, digits, symbols)
- Optionally exclude ambiguous characters
- Generate pronounceable passwords
- Estimate password strength

## Installation

```bash
pip install passgen
```

## Quick Start

```python
import passgen

# Generate a random password with default settings (length=12)
password = passgen.generate()
print(password)

# Generate a longer password with specific requirements
password = passgen.generate(
    length=16,
    uppercase=True,
    lowercase=True,
    digits=True,
    symbols=True,
    exclude_ambiguous=True
)
print(password)

# Generate a pronounceable password
pronounceable_password = passgen.generate_pronounceable(length=12)
print(pronounceable_password)

# Check password strength
strength = passgen.check_strength(password)
print(f"Password strength: {strength}")  # Weak, Medium, or Strong
```

## Development

This project uses Test-Driven Development (TDD).

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=passgen
```




## License

MIT 