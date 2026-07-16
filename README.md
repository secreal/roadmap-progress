# Roadmap Progress

An AI agent skill that continuously maintains `ROADMAP.txt` at the root of the current workspace. It records a short progress summary, important notes, context tags, and numbered work items using `SELESAI`, `PROGRESS`, and `BELUM` statuses.

## Usage

Copy and send this prompt to your AI agent:

```text
Use this skill for the current workspace: https://github.com/secreal/roadmap-progress
```

Or ask the agent to install it locally first:

```text
Install this skill locally from https://github.com/secreal/roadmap-progress and use it for the current workspace.
```

The agent should read the repository's `SKILL.md`, follow its workflow, and create or update `ROADMAP.txt` while it works.

## Output Format

```text
A short one-paragraph summary of the current objective and overall progress.
*An important note, constraint, risk, decision, or verification detail.
*Another important note when relevant.

[Context A][Context B][Context C]
|-[001][SELESAI] Description of completed work
|-[002][PROGRESS] Description of active work
|-[003][BELUM] Description of planned work
```
