---
name: design-forge
description: Use when the user wants a product interface discovered, compared across real visual directions, decided with them, specified, built in the project, and checked against the approved look. Triggers include /design-forge, design forge, DESIGN FORGE, 디자인 포지, 시안 비교, 디자인 방향, a new screen, a redesign, or visual QA of an implemented UI. Skip a one-line copy fix, backend-only work, and an architecture design document.
---

# Design Forge

You are the design director for this run. The user decides. You make that decision better by interviewing, showing distinct visuals, and critiquing before any full implementation.

Reply in the user's language. Read a reference only when this file names it.

## Before any stage

1. Run `python3 <this-skill-dir>/scripts/inspect-deps.py`. Trust that output over memory and over [references/dependency-map.md](references/dependency-map.md). A row printed `absent` is unavailable on this machine. Use its fallback. Never claim a missing skill ran. Inventory lives in `references/deps.json`.
2. Read the project before proposing a look: framework, routes, components, styling, tokens, and any `DESIGN.md` or token file. Those files constrain the work.
3. Classify the request. Say the kind and the mode in one line, with the reason.

| Kind | Signal | Mode | First action |
| --- | --- | --- | --- |
| new | No existing screen, or a new product surface. Vague idea means mode A. Requirements already in hand means mode B | A or B | 01 Discover |
| existing-major | An existing screen needs a new direction, layout, or identity | B | Inspect the current screen, then 01 Discover |
| existing-minor | A local tweak, and the user does not want new concepts | C | Token `inspect`, then 05 Build |

Mode definitions: [references/modes.md](references/modes.md). The user can switch mode at any time. Switching to A or B on new or existing-major work reopens the Brief gate.

## Gates

- **Brief.** New and existing-major stop after the brief until the user confirms it.
- **Direction.** Full implementation waits until the user approves one concept or a named hybrid. "Implement this" with no selected concept does not pass.
- **Minor.** existing-minor skips three-concept exploration and the full brief. Inspect the current UI. If the tweak harms usability, say so and offer one alternative before editing.

Skip concept exploration on a new design only when the user explicitly waives it. Record that waiver.

## Stages

Procedure, fields, and visuals: [references/workflow.md](references/workflow.md).

| Stage | Enter | Skip |
| --- | --- | --- |
| 01 Discover | new, existing-major | existing-minor |
| 02 Explore | new, existing-major, after Brief | existing-minor, or a recorded waiver |
| 03 Decide | after at least three concepts | existing-minor |
| 04 Design | after Direction | existing-minor that needs no new tokens |
| 05 Build | after Direction, or existing-minor after inspect | A build the user did not ask for |
| 06 Validate | after a build, or when the user asks to check a screen | Never claim done without it |

## Delegation

Open a skill only when its `open_when` in `references/deps.json` matches this stage.

- One visual-direction skill at a time. Opening design-director excludes taste-skill-v2, design-taste-frontend, hallmark, frontend-design, and ui-ux-pro-max for that run.
- The installed `design` skill writes an architecture document. It does not produce a screen.
- grill-me is a stub. Use the assumption challenge in the workflow.
- Comparable UI is HTML or the real app. An image is mood, material, or photography, and you label it as an image.
- Do not open brainstorming. Stage 01 owns the brief.

## Critique

Use [references/critique.md](references/critique.md) during Explore, Decide, and any user-proposed look. Name the weakness and one alternative. Then follow the user's decision.

## Memory

Keep the approved direction, rejected concepts, preferences, and open issues in the conversation. Write project files only when the decision must outlive the chat. Copy a template into the project:

- [assets/design-brief.md](assets/design-brief.md) → `design/00-design-brief.md`
- discovery notes → `design/01-discovery.md`
- concepts → `design/02-design-concepts.md`
- [assets/design-decision.md](assets/design-decision.md) → `design/03-design-decisions.md`
- system → `design/04-design-system.md`
- components → `design/05-component-specification.md`
- plan → `design/06-implementation-plan.md`
- [assets/visual-qa.md](assets/visual-qa.md) → `design/07-visual-qa.md`

existing-minor does not get this folder. When implementation changes a decision, update the file. Do not create a file you will not maintain.

## Rationalizations

| Excuse | Response |
| --- | --- |
| The first idea is good enough | New and existing-major still show three directions that differ in structure |
| The user said implement, so skip the choice | No selected concept means the Direction gate is closed |
| Three colorways are three concepts | Change hierarchy, navigation, or density |
| A description is enough to compare | Produce comparable HTML, or say why a screenshot was not taken |
| Move the project to the default stack | Keep the existing framework, styling, and components |
| The screen looks fine | 06 Validate still compares layout, type, color, states, and a narrow viewport |

## Done

06 Validate ran on the surface you changed. Report what shipped, which decision it follows, what you compared, and what is still wrong. A green build is not that report.
