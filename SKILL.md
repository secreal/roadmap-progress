---
name: roadmap-progress
description: Create and continuously maintain ROADMAP.txt at the current workspace root as an AI work ledger with a short summary, important notes, context tags, stable numbered tasks, and SELESAI/PROGRESS/BELUM statuses. Use when the user asks to create, show, track, resume, or update a roadmap, progress list, implementation status, work plan, or a record of what the AI has done and will do.
---

# Roadmap Progress

Maintain `ROADMAP.txt` as the durable, current record of work performed by the AI.

## Workflow

1. Determine the workspace root:
   - Use `git rev-parse --show-toplevel` when inside a Git repository.
   - Otherwise use the current working directory.
2. Read `<workspace-root>/ROADMAP.txt` when it exists.
3. Inspect the current request, relevant files, repository state, and available verification evidence before assigning statuses.
4. Create or update `ROADMAP.txt` immediately when the skill starts.
5. Update it again after every material milestone or change in status.
6. Update it once more before the final response so it reflects the actual final state.

Never merely print the roadmap in chat. Always write the file.

## Required File Format

Write plain UTF-8 text in exactly this order:

```text
A short one-paragraph summary of the current objective and overall progress.
*An important note, constraint, risk, decision, or verification detail.
*Another important note when relevant.

[Context A][Context B][Context C]
|-[001][SELESAI] Description of completed work
|-[002][PROGRESS] Description of active work
|-[003][BELUM] Description of planned work
```

Apply these rules:

- Keep the summary to one short paragraph at the top.
- Put important notes immediately after the summary. Start every note with `*` and no space before its text.
- Include only useful notes. Do not add filler.
- Put one context-tag line before each related task group.
- Write context tags as adjacent square-bracketed labels: `[Context A][Context B]`.
- Write each task as `|-[NNN][STATUS] description`.
- Use three-digit, zero-padded, sequential IDs starting at `001`.
- Use only the exact statuses `SELESAI`, `PROGRESS`, and `BELUM`.
- Keep descriptions concise, specific, and outcome-oriented.
- End the file with a newline.

## Status Rules

- `SELESAI`: Work is complete and supported by appropriate verification or direct evidence.
- `PROGRESS`: Work has started and remains active or partially complete.
- `BELUM`: Work is planned, required, or known but has not started.

Do not mark work `SELESAI` merely because code or text was written. Include verification when it is relevant to completion.

## Update Rules

- Preserve existing task IDs. Never renumber an existing item.
- Change an item's status in place as work advances.
- Append new work using the next unused ID.
- Merge duplicate items instead of creating parallel copies.
- Preserve still-relevant history, decisions, blockers, and user constraints.
- Remove or rewrite stale summary and notes so the top section always describes the current state.
- Add or reorganize context groups when doing so improves readability, but keep task IDs stable.
- Record only meaningful AI work. Omit routine shell reads, tool mechanics, and conversational filler.
- Reflect user-authored work only when it materially affects the AI's roadmap, and identify it accurately.
- If blocked, keep the item as `PROGRESS` or `BELUM` as appropriate and explain the blocker in an important note.

## Final Check

Before responding to the user, confirm that:

- `ROADMAP.txt` exists at the workspace root.
- The summary matches the latest state.
- Important notes are current.
- Context tags and task lines follow the required syntax.
- IDs are unique and stable.
- Statuses match actual evidence.
