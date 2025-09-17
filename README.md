# Learning CI/CD with GitHub Actions

This project represents my first hands-on experience with CI/CD pipelines using GitHub Actions. I built a small Python project with math operations and integrated it with an automated testing workflow, allowing me to connect the theory of CI/CD with practical implementation.


## Understanding CI/CD  <!-- second level -->

CI/CD (Continuous Integration / Continuous Deployment) is a software development practice that automates how code is integrated, tested, and deployed.

Continuous Integration (CI): Ensures new code changes are automatically built and tested to detect issues early.

Continuous Deployment (CD): Ensures that tested and verified code is consistently deployed without manual intervention.


### Why this matters: <!-- third level -->


Improves reliability by identifying problems before they reach production.

Reduces manual, repetitive work through automation.

Speeds up the release cycle, enabling teams to deliver software more quickly and safely.


### GitHub Actions in this context: <!-- third level -->

GitHub Actions provides a way to automate workflows directly within GitHub using YAML configuration files. A workflow defines:

Triggers (for example, on every push or pull request).

Jobs and steps (such as setting up the environment, installing dependencies, linting, and testing).

Execution environments (such as Ubuntu runners to simulate builds).


## Project Implementation <!-- second level -->

I implemented these concepts in a simple Python project as follows:

### Core Code <!-- third level -->

Created a file math_operations.py containing two basic functions: add() and subtract().

### Unit Tests <!-- third level -->

Wrote unit tests using pytest to validate both functions.


### CI/CD Wokflow <!-- third level -->

Built a GitHub Actions workflow (.github/workflows/python-ci.yml) to:

Trigger automatically on every push or pull request to the main branch.

Set up Python (v3.10).

Install dependencies (flake8, pytest).

Perform linting checks for code quality.

Run automated unit tests.


## GitHub Actions Workflow Highlights <!-- second level -->

The workflow file has several important features:

Triggers: Activated on push and pull request events to the main branch.

Environment: Uses the ubuntu-latest virtual machine for execution.

Linting: Enforces Python style and complexity standards with flake8.

Testing: Executes unit tests with pytest to ensure correctness.

Fail-fast behavior: If linting or tests fail, the build fails immediately.

Example excerpt from the workflow:

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  unit_testing:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

      - name: Test with pytest
        run: PYTHONPATH=. pytest


## Learnings and Takeaways <!-- second level -->

From this project, I was able to:

Refresh my understanding of GitHub fundamentals such as committing, pushing, and pulling code from a local repository.

Learn how to design an automated workflow with GitHub Actions to execute unit tests reliably.

Gain insight into how CI/CD creates a repeatable, reliable, and efficient development process.


## Big Picture Insight:<!-- second level -->

After learning and applying CI/CD through GitHub Actions, I developed a clearer understanding of how development, deployment, integration, and maintenance of code are managed in production environments. This project reinforced why these practices are critical for building efficient and scalable workflows.

This project may be simple in scope, but it gave me a strong foundation in CI/CD. More importantly, it showed me how automation links engineering practices directly to real-world software reliability and business value.


