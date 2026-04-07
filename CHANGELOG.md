# Changelog

All notable changes to Parent Helper are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.2.0] - 2026-04-07

### Added
- **Weekly Chore System** — New core capability (Section 6) for assigning and tracking household chores. Custody-aware: child chores only assigned on days they're home. Configurable per-person task tables with frequency. Integrates with Notion To-Do List database.
- **Chores section in weekly briefing** — Briefing format now includes a Chores block between "What's Going On" and "Action Items".
- **"Chores" / "Who's doing what?" interaction pattern** — On-demand chore queries.
- Chore tables added to `family-config-example.md` (Mike/Lily example).
- Chore section added to `sunday-briefing-example.md`.

### Changed
- **Structural refactor** — SKILL.md trimmed from 534 to 408 lines. Removed verbose instructional comments, moved cart automation details to `setup/store-profiles.md` reference, consolidated grocery budget into grocery section.
- Weekly briefing pipeline updated: 9 → 10 steps (chore generation added as step 8).
- Renamed "Sarah" to "Eliza" in example config to avoid overlap with common family names.

---

## [1.1.0] - 2026-03-22

### Added
- **Local Events Scout** — New core capability (Section 6) that surfaces real, confirmed events happening near the family each week. Searches local event calendars, farmers markets, festivals, sports, and community activities.
- **Zip code configuration** — Users set their zip code and nearby cities in SKILL.md. The events scout uses this to search the right metro area and calculate approximate drive times.
- **Recurring event anchors** — Configurable list of weekly/monthly recurring events (farmers markets, art walks, sunset celebrations) that always appear in the briefing when they fall in the week.
- **Age tagging** — Each event is tagged as Toddler-friendly, Kid-friendly, Teen-friendly, Adult, or Family (all ages) so parents can quickly filter.
- **Events section in weekly briefing** — "What's Going On This Week" is now part of the standard Sunday briefing output, organized by day and proximity.
- **On-demand event queries** — Trigger words: "what's going on", "things to do", "events this weekend", "anything happening", "stuff to do", "what can we do with the kids".
- **CHANGELOG.md** — This file.

### Changed
- Weekly briefing pipeline now includes the events scout step between grocery list and action items.
- Skill description updated with event-related trigger words.
- Sunday briefing example updated to include a sample "What's Going On This Week" section.

---

## [1.0.0] - 2026-03-08

### Added
- Initial release: Family coordination engine for Claude Code.
- Weekly family briefing (Sunday night) with calendar integration.
- Meal planning engine with per-person food profiles, cooking assignment logic, and headcount-adjusted portions.
- Multi-store grocery bargain hunter with Chrome MCP cart automation.
- Pre-built store profiles for 15+ US grocery stores (Walmart, Kroger, Publix, H-E-B, Aldi, Meijer, Whole Foods, Target, Safeway, Costco, and more).
- Smart split optimization: price-compare across stores, assign each item to cheapest source, calculate savings.
- Custody schedule awareness for blended families with irregular calendars.
- Co-parent communication drafts via Gmail MCP.
- Family dashboard via Notion MCP (To-Do List, Important Dates, Recurring Needs databases).
- Schedule conflict detection with resolution suggestions.
- Grocery budget tracking with weekly target and overage alerts.
- Templatized SKILL.md with `{{PLACEHOLDER}}` fields for easy family customization.
- Setup guide, family config example, and Sunday briefing example.
- CONTRIBUTING.md with guidelines for store profiles and other contributions.
