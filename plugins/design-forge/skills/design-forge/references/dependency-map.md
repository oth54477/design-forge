# Dependency map

`scripts/inspect-deps.py` is the authority. `references/deps.json` is the inventory it reads. If they disagree with this page, trust the script. The inventory names skill directories and home-relative globs. It does not store absolute paths. A row the script prints as `absent` is not on this machine.

Run the script before naming any skill as available. A row whose path is missing is unavailable. Use that row's `fallback`. Do not claim the skill ran.

## How to choose

Open a row only when the current stage matches its `open_when`. Most requests open none of the style skills during 01 Discover.

One visual-direction skill per run. design-director already chooses among installed style skills. Opening it means you do not also open taste-skill-v2, design-taste-frontend, hallmark, frontend-design, or ui-ux-pro-max.

## Collisions and non-skills

- taste-skill-v2 is the plugin whose frontmatter name is `design-taste-frontend`. For dashboards, admin, and settings, open its `app-screens.md` only. The separate agents skill `design-taste-frontend` is for landing pages and portfolios.
- The requested name `gril-me` is the installed stub `grill-me`. No grilling skill body is installed. Use workflow stage 01.
- The requested spelling `web-design-guidlines` is not an id. The installed id is `web-design-guidelines`.
- `design` is an architecture-document loop. It is not visual production.
- `responsive-design`, `visual-regression`, and `ux-research` are absent. Fallbacks are in their rows.
- brainstorming is installed and must not be opened on a Design Forge run.

Skills that are not rows in `deps.json` are outside this orchestrator. Open one only when the user names it.

design-director's own catalog is not copied here. When you open that skill, follow the body you read.
