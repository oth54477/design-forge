# Workflow

Stage procedure for Design Forge. Skill availability is `references/deps.json`, printed by `scripts/inspect-deps.py`. Critique language is `references/critique.md`. Modes are `references/modes.md`.

## Adaptive path

- new: 01 → brief gate → 02 → 03 → direction gate → 04 → 05 → 06.
- existing-major: inspect the current screen first, then the same path as new.
- existing-minor: token `inspect`, critique if the tweak harms use, then 05 and 06. Skip 01, 02, 03, and 04 unless the inspect shows the change is really a new direction.
- A recorded waiver of concepts on a new design skips 02 and 03 and goes from a confirmed brief to 04.

Do not ask for facts already in the conversation or the project.

## 01 Discover

Ask one question. Add a follow-up only after the answer. Say why the question matters when the reason is not obvious. Mark each answer as a requirement or a preference. Stop when the brief can be filled without inventing facts.

When two answers conflict, or a request fights the product goal, challenge that one assumption before the next question. This is the grill-me fallback. Do not claim a grill-me run.

If `inspect-deps.py` marks deep-interview available, borrow its one-question targeting only. Do not enter its pipeline, state files, or execution menu.

Brief fields, in this order:

1. Product overview
2. Design objectives
3. Target users
4. Core user journeys
5. Functional requirements
6. Visual preferences, including dislikes
7. Design constraints and references
8. Technical constraints, including the existing design system
9. Success criteria
10. Open questions

Show the brief and wait. The Brief gate applies to new and existing-major.

Copy `assets/design-brief.md` into the project only when the brief must outlive the chat.

## 02 Explore

Produce at least three concepts. Each pair must differ in at least four of these: visual identity, layout, hierarchy, typography, color strategy, component treatment, navigation, interaction model, atmosphere. A palette swap of one layout fails this stage.

The style menu is Swiss, bento, dark tech, liquid glass, solid glass, editorial, minimal, clay, neo-brutalism, spatial, scroll-driven 3D, and dense enterprise UI. Pick for the product. Combine when that serves the job. Do not import a trend that fights the task.

For each concept record: name, philosophy, target experience, visual references, layout, typography, color, component examples, interaction examples, strengths and weaknesses, implementation complexity.

Visuals, in this order:

1. Comparable HTML prototypes that share the same content and actions. This is the default.
2. Screenshot them. Read aside-browser and follow it before any other browser. If no screenshot was taken, say so in the same message.
3. Mood, material, or photography images only after reading the imagine skill, and only on a host with image generation. Never generate labeled UI, numbers, or charts as images.
4. imagegen-frontend-web only for a marketing page, one image per section, each labeled as an image. Never call an image an implementation. Do not use it for a product dashboard.
5. One visual-direction skill, chosen from `open_when`. Dashboards, admin, and settings use the taste-skill-v2 `app-screens.md` path when that row is available. Do not open the agents `design-taste-frontend` skill for those surfaces.

## 03 Decide

Score every concept on product fit, usability, visual quality, distinctiveness, information hierarchy, accessibility, responsiveness, implementation feasibility, and long-term maintainability.

Recommend the best product fit, including a hybrid when the strengths split. Do not crown the most spectacular concept by default. Apply `references/critique.md`.

Write the decision with the fields in `assets/design-decision.md`. The Direction gate stays closed until the user approves one concept or a named hybrid.

## 04 Design

Specify only what this product uses. A product with no table does not get a table spec.

Cover, as they apply:

- Visual system: tokens, color, type scale, spacing, radius, shadow, elevation, iconography, grid, breakpoints.
- Components in use: buttons, inputs, cards, navigation, dialogs, tables, data visualization, empty, loading, error.
- Interaction: navigation behavior, hover, focus, active, transition, keyboard, responsive behavior, reduced motion.

If the project has `DESIGN.md` or tokens, extend those. Do not start a second system.

Open tailwind-design-system only when its `open_when` matches. Its recipe is for Tailwind v4 or the greenfield default stack.

## 05 Build

Read the codebase first: framework, architecture, components, routing, styling, dependencies, tokens, conventions. Preserve them. Change architecture only when the current one cannot meet the approved direction, and say why.

Greenfield, and only when there is no project and no stack constraint: React, Vite, TypeScript, Tailwind CSS, shadcn/ui. Open the shadcn skill only when `components.json` exists or this default stack was chosen.

Build reusable components. Keep tokens out of one-off component files. Do not duplicate styles or add a dependency you can avoid. Use semantic HTML, keyboard access, and a responsive layout. Implement loading, error, and empty states. Do not present a placeholder as finished behavior.

## 06 Validate

Compare the approved mockup, the implementation, and a written difference list. Check layout, alignment, spacing, typography, color, component consistency, responsive behavior, interaction states, accessibility, overflow, and hierarchy.

Browser order is the aside-browser row, then agent-browser, then a connected Playwright MCP, then ego-browser. Name the tool you actually used.

When both an approved screenshot and an implementation screenshot exist, open the visual-verdict file printed by `scripts/inspect-deps.py` and follow that file's output contract. If its verdict is not pass, edit and shoot again. There is no visual-regression skill and no pixel baseline unless the project already has one.

Phone and touch layouts: open mobile-native when its `open_when` matches. Check a narrow viewport even on desktop products. Device hardware that you did not hold is untested.

Data-heavy UI: after the happy path renders, open break-ui. It reports breaks. It does not pick a new direction.

Copy `assets/visual-qa.md` into the project only when the report must persist. The report lists completed features, the decision followed, components implemented, validation evidence, remaining issues, and recommended improvements.

Iterate. The first successful build is not the end.

## Project docs

Create a file under `design/` only when it will stay true:

| File | When |
| --- | --- |
| `design/00-design-brief.md` | Brief confirmed and the work continues later |
| `design/01-discovery.md` | Interview notes that the brief does not fit |
| `design/02-design-concepts.md` | Three concepts were shown |
| `design/03-design-decisions.md` | A direction was approved |
| `design/04-design-system.md` | New or extended tokens |
| `design/05-component-specification.md` | Component behavior beyond the tokens |
| `design/06-implementation-plan.md` | Build is larger than one sitting |
| `design/07-visual-qa.md` | 06 Validate finished and the result must persist |

existing-minor does not create this folder. If the built UI diverges from a doc, update the doc in the same change.
