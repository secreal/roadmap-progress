# Roadmap Progress

An AI agent skill that continuously maintains an English-language `ROADMAP.txt` at the root of the current workspace. It records a short progress summary, important notes, context tags, and numbered work items using `DONE`, `IN PROGRESS`, and `NOT STARTED` statuses.

## Install

Copy and send this prompt to an AI agent that can install Codex skills:

```text
Install the roadmap-progress skill locally from https://github.com/secreal/roadmap-progress. The skill is at repository path "." and its installation name must be "roadmap-progress". Tell me when it is available for a new turn.
```

The agent must install the repository as a skill, not merely summarize the GitHub page. A newly installed skill may become available only on the next turn or after restarting the agent session.

## Use

On a new turn after installation, send:

```text
Use $roadmap-progress for this workspace. Create or update ROADMAP.txt at the workspace root before replying. Follow the skill's exact plain-text format; do not return a table in chat.
```

The agent must read `SKILL.md`, write the file with a filesystem tool, and validate its format before claiming completion.

## Output Format

```text
A short one-paragraph summary of the current objective and overall progress.
*An important note, constraint, risk, decision, or verification detail.
*Another important note when relevant.

[Context A][Context B][Context C]
|-[001][DONE] Description of completed work
|-[002][IN PROGRESS] Description of active work
|-[003][NOT STARTED] Description of planned work
```
