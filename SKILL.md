---
name: roadmap-progress
description: Create and continuously maintain ROADMAP.txt at the current workspace root as an English-language AI work ledger with a short summary, important notes, context tags, stable numbered tasks, and DONE/IN PROGRESS/NOT STARTED statuses. Use when the user asks to create, show, track, resume, or update a roadmap, progress list, implementation status, work plan, or a record of what the AI has done and will do.
---

# Roadmap Progress

Maintain `ROADMAP.txt` as the durable, current record of work performed by the AI.

## Non-Negotiable Contract

- Use a filesystem editing tool to create or update `<workspace-root>/ROADMAP.txt` before presenting any roadmap result.
- Do not substitute a chat response, terminal table, Markdown table, progress dashboard, or percentage summary for the file.
- Do not add a `Roadmap Progress` heading or any other heading to `ROADMAP.txt`.
- Follow the literal line syntax in this skill. Do not redesign or prettify it.
- Write the summary, notes, context tags, task descriptions, and statuses in English.
- If the file was not successfully written and validated, state that the operation failed instead of claiming success.

## Workflow

1. Determine the workspace root:
   - Use `git rev-parse --show-toplevel` when inside a Git repository.
   - Otherwise use the current working directory.
2. Read `<workspace-root>/ROADMAP.txt` when it exists.
3. Inspect the current request, relevant files, repository state, and available verification evidence before assigning statuses.
4. Create or update `ROADMAP.txt` immediately when the skill starts. Use `<skill-directory>/assets/ROADMAP.template.txt` as the structural template when creating a new file. Resolve `<skill-directory>` as the directory containing this `SKILL.md`.
5. Update it again after every material milestone or change in status.
6. Run `python <skill-directory>/scripts/validate_roadmap.py <workspace-root>/ROADMAP.txt` after every update. Fix the file and rerun the validator until it passes.
7. Update and validate it once more before the final response so it reflects the actual final state.

Never merely print the roadmap in chat. Always write the file.

## Required File Format

Write plain UTF-8 text in exactly this order:

```text
A short one-paragraph summary of the current objective and overall progress.
*An important note, constraint, risk, decision, or verification detail.
*Another important note when relevant.

[Context A][Context B][Context C]
|-[001][DONE] Description of completed work
|-[002][IN PROGRESS] Implement the active workflow and verify every milestone against the current workspace requirements
                     before recording the final state in ROADMAP.txt.
|-[003][NOT STARTED] Description of planned work
```

Apply these rules:

- Keep the summary to one short paragraph at the top.
- Put important notes immediately after the summary. Start every note with `*` and no space before its text.
- Include at least one important note. If there are no blockers or special constraints, state that explicitly in one note.
- Put exactly one context-tag line before the task list.
- Write context tags as adjacent square-bracketed labels: `[Context A][Context B]`.
- Write each task as `|-[NNN][STATUS] description`.
- Use three-digit, zero-padded, sequential IDs starting at `001`.
- Use only the exact statuses `DONE`, `IN PROGRESS`, and `NOT STARTED`.
- Keep descriptions concise, specific, and outcome-oriented.
- Limit each physical task-description line to 100 characters, excluding the task prefix or continuation indentation.
- Wrap long descriptions at a word boundary before they exceed 100 characters. Do not rely on editor word wrap.
- Indent every continuation line with exactly enough spaces to align its first character with the first character of the description above.
- Calculate continuation indentation from the full prefix `|-[NNN][STATUS] ` because different statuses produce different prefix widths.
- Do not repeat `|-`, the task ID, or the status on continuation lines.
- End the file with a newline.
- Do not use box-drawing characters, tables, columns, or standalone percentage rows.

## Status Rules

- `DONE`: Work is complete and supported by appropriate verification or direct evidence.
- `IN PROGRESS`: Work has started and remains active or partially complete.
- `NOT STARTED`: Work is planned, required, or known but has not started.

Do not mark work `DONE` merely because code or text was written. Include verification when it is relevant to completion.

## Update Rules

- Preserve existing task IDs. Never renumber an existing item.
- Change an item's status in place as work advances.
- Append new work using the next unused ID.
- Merge duplicate items instead of creating parallel copies.
- Preserve still-relevant history, decisions, blockers, and user constraints.
- Remove or rewrite stale summary and notes so the top section always describes the current state.
- Update the context tags when the work areas change, but keep task IDs stable.
- Record only meaningful AI work. Omit routine shell reads, tool mechanics, and conversational filler.
- Reflect user-authored work only when it materially affects the AI's roadmap, and identify it accurately.
- If blocked, keep the item as `IN PROGRESS` or `NOT STARTED` as appropriate and explain the blocker in an important note.

## Final Check

Before responding to the user, confirm that:

- `ROADMAP.txt` exists at the workspace root.
- `<skill-directory>/scripts/validate_roadmap.py` exits successfully for the file.
- The summary matches the latest state.
- Important notes are current.
- Context tags and task lines follow the required syntax.
- IDs are unique and stable.
- Statuses match actual evidence.
