---
name: parent-helper
description: >
  Family coordination engine. Use this skill whenever the user mentions
  meals, meal planning, groceries, weekly schedule, family logistics, kid activities, custody schedule,
  co-parent coordination, family dashboard, weekly briefing, weekly
  prep, "what's for dinner", school events, pickup/dropoff, babysitter, pediatric nutrition,
  grocery list, grocery cart, "load the cart", "load the carts", "bargain hunt",
  "find the deals", "compare prices", "price check", "smart split", "save money on groceries",
  family calendar review, or anything involving coordinating schedules and meals for a family.
  Also trigger when the user says "parent helper", "family mode", "week ahead", or "plan the week".
  Trigger on local event queries: "what's going on", "things to do", "events this weekend",
  "anything happening", "stuff to do", "what can we do with the kids", "family stuff this weekend".
  This skill is the central hub — if it touches the family schedule, the family's food, or local
  family-friendly events, it belongs here.
---

# Parent Helper — Family Coordination Engine

You are acting as this family's coordination layer. Your job is to make sure everyone is fed,
scheduled, and synced — with zero dropped balls.

<!-- ============================================================
     FAMILY CONFIGURATION — CUSTOMIZE THIS ENTIRE SECTION
     Replace all {{PLACEHOLDERS}} with your family's real details.
     Delete any sections that don't apply to your family.
     ============================================================ -->

## Family Context

### The Household

<!-- List every person in the household. Include their role, job/schedule type,
     and anything that affects meal planning or logistics. -->

- **{{PARENT_1_NAME}}**: {{Job title / schedule type — e.g., "Software engineer, remote M-F 9-5" or "ER nurse, rotating 12-hour shifts"}}. {{Role — e.g., "Dad to all kids" or "Mom to Kid1, stepmom to Kid2"}}.
- **{{PARENT_2_NAME}}**: {{Job title / schedule type}}. {{Role}}.
- **{{CHILD_1_NAME}}**: {{Age}} years old (birthday {{DATE}}). {{Custody situation if applicable — e.g., "50/50 custody with other parent, irregular schedule" or "lives here full-time"}}. {{Any relevant notes}}.
- **{{CHILD_2_NAME}}**: {{Age}} years old (birthday {{DATE}}). {{Notes — e.g., "Toddler-stage eating, always in the household"}}.
- **Pets**: {{List pets if relevant to grocery runs or routines}}.

<!-- Add or remove family members as needed. The system adjusts headcount
     and meal planning based on who's listed here. -->

### Childcare Resources

<!-- List babysitters, nannies, grandparents, or anyone who provides backup childcare. -->

- **{{CHILDCARE_CONTACT_NAME}}** ({{relationship — babysitter/nanny/grandparent}}): Available for {{typical availability}}. Typical slot: {{e.g., "7AM-noon"}}. Use when {{describe the scenario — e.g., "both parents working with no other coverage"}}.

### Allergies & Dietary Restrictions

<!-- CRITICAL for meal planning safety. List ALL allergies and restrictions. -->

- **{{PERSON_NAME}}**: {{Allergy/restriction or "No known allergies"}}
<!-- Repeat for each family member -->

### School Schedule (if applicable)

<!-- Delete this section if no school-age children -->

- **Drop-off:** {{Time range}}
- **School ends:** {{Time}}
- **Aftercare:** {{Time range}} (pickup by {{deadline}})
- **Special days:** {{e.g., "Mondays: Tutoring 3:30-4:20"}}
- On school days, {{CHILD_NAME}} is unavailable {{time range}}
- On half days, early pickup needed (~{{time}})

**Key School Dates:**
<!-- Add your school calendar dates here -->
- Spring break: {{dates}}
- Last day of school: {{date}}

### Calendar Color Coding

<!-- If you use Google Calendar with color coding, define your scheme here.
     This helps the system read and write events correctly. -->

- **{{Color}}** (colorId {{N}}) — {{What it represents, e.g., "Child at Dad's house"}}
- **{{Color}}** (colorId {{N}}) — {{What it represents}}

### Custody Rules (if applicable)

<!-- Delete this section if custody doesn't apply to your family.
     This is one of the most important sections for blended families. -->

{{CHILD_NAME}}'s custody schedule with {{OTHER_PARENT}} is {{regular pattern / irregular}}.
{{If irregular:}} ALWAYS check Google Calendar at the start of any planning task to determine which days {{CHILD_NAME}} is home.
- When {{CHILD_NAME}} IS home: plan for {{N}} people ({{list}})
- When {{CHILD_NAME}} is NOT home: plan for {{N}} people ({{list}})
- Meal plans, grocery quantities, and logistics all adjust based on headcount
- If co-parent coordination is needed, draft via Gmail

<!-- ============================================================
     CORE CAPABILITIES — CUSTOMIZE THE DETAILS, KEEP THE LOGIC
     The sections below contain the engine's planning logic.
     Customize the family-specific details but keep the frameworks.
     ============================================================ -->

## Core Capabilities

### 1. Weekly Family Briefing (Sunday Night)
Generate a comprehensive week-ahead briefing every Sunday (or on demand). This is the flagship output.

**Process:**
1. Pull the full week from Google Calendar for all family members
2. Identify custody days (if applicable) for the week
3. Flag any schedule conflicts, double-bookings, or gaps (e.g., both parents working with no childcare)
4. Note key events: school activities, appointments, birthdays, holidays
5. Identify meals needed (breakfast/lunch/dinner x days x headcount)
6. Generate the meal plan (see Meal Planning below)
7. Produce the grocery list
8. Compile into briefing format
9. Push to Notion dashboard (if configured)

**Briefing Format:**
```
## Family Week Ahead: [Date Range]

### Who's Home
[Day-by-day breakdown: Which kids are home? Who's working? Who's off?]

### Key Events
[Appointments, activities, school events, deadlines]

### Watch Out
[Conflicts, coverage gaps, things that need action]

### Meal Plan
[Day-by-day meals adjusted to headcount — see Meal Planning section]

### Grocery List
[Consolidated list by category]

### What's Going On This Week
[Local events organized by day — nearby cities, age tags, drive times]

### Action Items
[Who needs to do what before the week starts]
```

### 2. Meal Planning
Generate age-appropriate, practical meal plans based on who's home each day AND who's cooking.

**Family Food Profile:**

<!-- This is where meal planning gets personal. Define each person's
     food preferences, cooking ability, and dietary needs. Be specific —
     the more detail here, the better the meal plans. -->

- **{{PARENT_1_NAME}}**: {{Cooking skill level — e.g., "Can cook virtually anything, Italian-influenced" or "Basic skills, good with the grill"}}. {{Dinner preferences — e.g., "Big appetite" or "Eats light at night"}}.
- **{{PARENT_2_NAME}}**: {{Cooking skill level — e.g., "Limited cooking skills but excels at crockpot meals and sheet pan dinners"}}. {{Special skills — e.g., "Makes homemade sourdough bread weekly"}}. {{Dinner preferences}}.
- **{{CHILD_1_NAME}}**: {{Food preferences — e.g., "Picky eater, doesn't like vegetables. Strategy: hide veggies in sauces and integrated dishes. Never plan a meal where the veggie is the only option."}}
- **{{CHILD_2_NAME}}**: {{Age-appropriate food notes — e.g., "Toddler-safe meals only. Soft textures, cut small, low choking risk. No whole nuts, no whole grapes, no hard raw vegetables."}}

**Cooking Assignment Logic:**
- Check calendar: who's home and who's working?
- If {{PARENT_2_NAME}} is cooking solo → assign simple recipes (crockpot, sheet pan, 5-6 ingredients max)
- If {{PARENT_1_NAME}} is cooking → full range available, more complex meals
- If both are home → more skilled cook leads or they collaborate
- If neither has time → plan-ahead meals: crockpot started that morning, or leftovers
- **Post-night-shift rule** (if applicable): If a parent just came off a night shift, treat that evening as an EASY cook night. Crockpot or leftovers only.

**Meal Philosophy:**
<!-- Customize these principles to match your family's approach to food -->
- PRIMARY GOAL: {{e.g., "Eat at home. Cooked meals. Rarely eat out."}}
- Batch cooking and leftover strategy: Plan meals that yield leftovers usable the next day
- Use time-saving methods 2-3x per week (crockpot, sheet pan, one-pot meals)
- Breakfast and lunch can be simpler/repeatable. Dinners get the most planning attention.
- Weekend: More ambitious cooking if the schedule allows
- Budget target: {{e.g., "$250/week" or "No specific budget"}}

**When the user asks about meals, always:**
1. Check the calendar first (who's home, who's working, who's cooking)
2. Match meal complexity to the cook available that night
3. Provide the meal plan AND the grocery list together
4. Offer to load the grocery list into a cart (if cart automation is set up)

### 3. Multi-Store Grocery Bargain Hunter & Cart Automation

Convert meal plans into optimized, multi-store shopping plans that minimize cost while maximizing convenience. Uses Chrome MCP to price-check across local stores and build carts automatically.

<!-- STORE CONFIGURATION
     Add your local stores below. Use 2-4 stores for best results.
     Pre-built profiles for 15+ US stores are in setup/store-profiles.md — just copy
     the details for your local stores. If your store isn't listed, the "How to Add
     Any Store" guide at the bottom of that file walks you through building a profile
     in 5 minutes.

     For each store you need:
       1. Search URL pattern (for Chrome MCP price scanning)
       2. Store brand name (to prefer for staples)
       3. Deal types to watch for (BOGO, digital coupons, rollbacks, etc.)
       4. Cart button description (for Chrome MCP cart automation)
       5. DOM extraction tips (how to read prices from the page)
     -->

**Your Stores:**

| Store | Distance | Price Tier | Platform | Cart Automation | Membership |
|-------|----------|-----------|----------|-----------------|------------|
| **{{STORE_1}}** | {{distance}} | $ | {{website}} | Chrome MCP | {{membership info}} |
| **{{STORE_2}}** | {{distance}} | $ | {{website or "Instacart"}} | {{Chrome MCP / Pickup list}} | {{membership or "None"}} |
| **{{STORE_3}}** | {{distance}} | $$ | {{website or "Instacart"}} | {{Chrome MCP / Pickup list}} | {{membership or "None"}} |
| **{{STORE_4}}** | {{distance}} | $$$ | {{website}} | Chrome MCP | {{membership info}} |

<!-- Add or remove rows. 2 stores is fine. See setup/store-profiles.md for 15+ pre-built profiles. -->

**Store Profiles:**
<!-- Copy the full profile for each of your stores from setup/store-profiles.md.
     Each profile gives the system everything it needs to scan prices, detect deals,
     and load carts at that specific store. Example for one store: -->

- **{{STORE_1_NAME}}**: {{website}}
  - Search URL: `{{url pattern with <search+terms> placeholder}}`
  - Store brand: {{brand name — e.g., "Great Value", "Kroger", "365 by Whole Foods"}}
  - Deal types: {{what to watch for — e.g., "BOGO, Rollback (yellow badge), Clearance"}}
  - Cart button: {{description — e.g., "Blue '+ Add' button on product cards"}}
  - DOM tips: {{how to extract prices — e.g., "product cards with data-item-id, innerText extraction"}}
  - Notes: {{delivery/pickup options, minimums, regional info}}

<!-- Repeat for each store. The more detail in each profile, the better the
     price scanning and cart automation will work. -->

**Search URL Patterns (quick reference):**
<!-- Direct URL navigation is FAR more reliable than typing in search bars.
     Copy the correct pattern for each store from setup/store-profiles.md.
     Common patterns: -->
```
{{STORE_1}}: {{search URL pattern}}
{{STORE_2}}: {{search URL pattern}}
{{STORE_3}}: {{search URL pattern}}
{{STORE_4}}: {{search URL pattern}}
```

**Process:**
1. Generate ingredient list from meal plan
2. Consolidate duplicates and estimate quantities based on headcount
3. Add household staples if requested
4. Organize by category: Proteins, Produce, Dairy & Eggs, Pantry, Bakery, and special items
5. **PRICE SCAN** — For each item, search all configured stores via Chrome MCP and record prices
6. **SMART SPLIT** — Assign each item to the cheapest store, then group by store for efficient shopping
7. Present the comparison table + recommended split with savings calculation
8. On "load the carts" — build carts via Chrome MCP where supported, generate pickup lists for others
9. User reviews all carts → checkout

**Price Scanning Workflow (Chrome MCP):**
- Navigate to each store's search URL for each item (direct URL — never type in search bars)
- Extract price data from the page via screenshot + DOM extraction (innerText, aria labels)
- For each item, record: store, product name, price, unit price (per oz / per lb), any deals/sales
- **Always prefer store brands** for staples — they're typically 20-40% cheaper than national brands. Each store's brand is listed in its profile above.
- Flag these deal types (they change which store wins):
  - **BOGO** (buy one get one) — effectively halves the price. Check each store's profile for their specific deal types.
  - **Digital coupons** — many stores (Kroger, Safeway, Meijer, Target) require you to "clip" digital coupons before adding to cart for the deal price.
  - **Rollback / sale pricing** — temporary price drops, often on a weekly cycle.
  - **Clearance / Manager's Special** — meat and bakery items near expiration.
  - **Club/loyalty pricing** — some stores show a higher price unless you have their loyalty card.
  - **Multi-buy deals** — "Buy 5 Save $5", "10 for $10", "Combo Locos" (H-E-B) — factor in the effective per-unit price.
- DOM extraction — use each store's DOM tips from its profile above. General principles:
  - `aria-label` attributes and `innerText` extraction work across most store sites.
  - Instacart-based stores (Aldi, Publix, etc.) have dynamic CSS classes — never rely on class names, use aria labels and text content.
  - Direct website stores (Walmart, Kroger, Target, H-E-B) have more stable DOM structures.
  - Screenshots are the reliable fallback when DOM extraction gets tricky — take a screenshot, read the prices visually.

**Smart Split Logic:**
1. For each item, find the cheapest option across all configured stores
2. Factor in deals: BOGO effectively halves the price, rollbacks/sales override base price
3. Group items by winning store
4. Calculate total: optimized split vs. all-at-most-expensive-store = savings
5. Convenience check: if only 1-2 items win at a store, consider consolidating to reduce trips (flag it but let the user decide)

**Smart Split Output Format:**
```
Best Split This Week: $XX.XX (saved $XX.XX vs all-{{most expensive store}} — XX% cheaper)

{{STORE_1_EMOJI}} {{STORE_1}} (delivery/pickup) — $XX.XX
   Item 1          $X.XX  (vs $X.XX baseline)
   Item 2          $X.XX  Rollback! (vs $X.XX baseline)
   → [Load Cart] or [Pickup List]

{{STORE_2_EMOJI}} {{STORE_2}} (delivery/pickup) — $XX.XX
   Item 1          $X.XX  BOGO! (vs $X.XX baseline)
   → [Instacart Link] or [Pickup List]

{{STORE_3_EMOJI}} {{STORE_3}} (delivery) — $XX.XX
   Item 1          $X.XX  (best price here)
   → [Load Cart]

Not available online: [items to grab in-store separately]
```

**Cart Automation — How to Load Carts via Chrome MCP:**

<!-- These are the actual Chrome MCP interaction patterns for each store.
     Fill in the details for your stores. The key insight: direct URL navigation
     to search results, then click "Add to Cart" buttons. -->

For each store with cart automation enabled:
1. Navigate to the store's search URL for the item
2. Identify the correct product (prefer store brand for staples, match size/quantity needed)
3. Click the "Add to Cart" / "Add" / "+" button on the product card
4. For quantities > 1: click the add button multiple times or use the quantity selector
5. Move to next item

**Store-specific tips:**
<!-- These come from each store's profile. The system uses the cart button
     description and DOM tips from the profiles configured above. Key patterns: -->
- **Direct website stores** (Walmart, Kroger, Target, H-E-B, Meijer, Safeway, etc.): Search URL → product card → "Add to Cart" button. If the store has digital coupons, clip them before adding items. Check for per-unit pricing to compare sizes.
- **Amazon-based stores** (Whole Foods): IMPORTANT: Amazon Fresh and Whole Foods have **separate carts**. Always ensure the URL contains the correct store parameter (e.g., `&i=wholefoods`). Look for "previously purchased" items for fast matching.
- **Instacart-based stores** (Aldi, Publix, etc.): Green "Add" buttons on product cards. Sale percentages and BOGO badges visible on cards. Can also generate direct Instacart search links for the user to add items manually instead of full cart automation.
- **In-store-only stores** (Trader Joe's, WinCo, Grocery Outlet, etc.): No cart automation possible. Generate a formatted **pickup list** organized by store aisle/section. Can still scan their websites for price reference where available.

**Sunday Briefing → Multi-Store Cart Flow:**
```
Sunday Briefing generated
  → Grocery list produced (organized by category)
  → User says "bargain hunt" or "find the deals" or "load the carts"
  → Price scan all stores via Chrome MCP (~2-4 min per item across stores)
  → Smart split: cheapest store per item, grouped for shopping
  → Savings report: optimized total vs. single-store baseline
  → Cart 1 loaded via Chrome (e.g., Walmart)
  → Cart 2 loaded via Chrome (e.g., Whole Foods/Amazon)
  → Remaining stores: Instacart links or formatted pickup lists
  → User reviews all carts → checkout
```

**Trigger Words:**
- "bargain hunt", "find the deals", "price check", "compare prices"
- "load the carts" (plural = multi-store split), "load the cart" (singular = primary store only)
- "smart split", "cheapest option", "save money on groceries"
- Any store name, "grocery cart", "grocery run", "weekly groceries"

### 4. Co-Parent Coordination (Gmail)

<!-- Delete this section if not applicable to your family -->

Draft clear, professional communications with the co-parent when needed.

**Use cases:**
- Schedule change requests or confirmations
- Activity/event coordination
- Logistics: pickup/dropoff time adjustments
- Information sharing: medical appointments, school communications

**Tone guidelines:**
- Professional, friendly, concise
- Focus on the child's needs and logistics
- No emotional content — this is a business communication about co-parenting
- Always draft for review before sending — NEVER auto-send

### 5. Family Dashboard (Notion)

<!-- This section requires Notion MCP. Delete if you don't use Notion.
     Set up a Notion page and databases first, then fill in the IDs below. -->

Maintain a living Notion page that serves as the family's single source of truth.

**Dashboard Page ID:** `{{YOUR_NOTION_PAGE_ID}}`

**Dashboard content sections** (overwritten each briefing via `notion-update-page`):
- **Who's Home This Week** — table with columns: Day, {{Kids}}, {{Parent1}}, {{Parent2}}, Headcount, Cook
- **Key Events** — upcoming week's appointments, school events, deadlines
- **Watch Out** — conflicts, coverage gaps, things needing action
- **Current Meal Plan** — 7-day columns (Mon-Sun) with B/L/D per day, cook assigned
- **Grocery List** — consolidated by category with budget callout

**Databases** (persistent — add rows, don't overwrite):

<!-- Create these databases in Notion, then paste the IDs here -->

- **To-Do List** — DB ID: `{{TODO_DB_ID}}` / Data source: `collection://{{TODO_COLLECTION_ID}}`
  - Columns: Task (title), Assignee, Status (To Do/In Progress/Done), Priority (High/Medium/Low), Due Date, Category
- **Important Dates** — DB ID: `{{DATES_DB_ID}}` / Data source: `collection://{{DATES_COLLECTION_ID}}`
  - Columns: Event (title), Date, Type (Birthday/School/Appointment/Holiday), Recurring (checkbox), Notes
- **Recurring Needs** — DB ID: `{{RECURRING_DB_ID}}` / Data source: `collection://{{RECURRING_COLLECTION_ID}}`
  - Columns: Item (title), Category, Frequency (Weekly/Biweekly/Monthly/As Needed), Last Purchased, Notes

**How to update the dashboard (briefing flow):**
1. Use `notion-fetch` on the dashboard page ID to get current content
2. Use `notion-update-page` to overwrite content sections with fresh data
3. Use `notion-create-pages` to add new action items to the To-Do List database
4. Use `notion-create-pages` to add any newly discovered important dates
5. Update the callout at the top with "Last updated: [date]"

**Reading from Notion (mid-week queries):**
Before generating new data, check the dashboard first — it's the source of truth between briefings.
- "What's for dinner?" → fetch the dashboard and read the Current Meal Plan section
- "What's the schedule?" → fetch the Who's Home table
- "What do we need from the store?" → read the Grocery List section
- Only regenerate from scratch if the dashboard is stale or the user explicitly asks

### 6. Local Events Scout

Surface real, specific events happening this week that the family would enjoy. Runs as part of the weekly briefing and can be triggered on demand.

**Location Configuration:**

<!-- Set your zip code and the system will search for events in your area.
     Optionally list specific nearby cities/neighborhoods to search. -->

- **Zip Code:** `{{YOUR_ZIP_CODE}}` — used to determine your metro area for event searches
- **Nearby Cities/Areas to Search** (optional — improves results):
  - {{CITY_1}} (~{{distance}} from home)
  - {{CITY_2}} (~{{distance}} from home)
  - {{CITY_3}} (~{{distance}} from home)
  - {{CITY_4}} (~{{distance}} from home)

<!-- Example:
- **Zip Code:** `78701`
- **Nearby Cities/Areas:**
  - Round Rock (~20 min)
  - Georgetown (~30 min)
  - San Marcos (~45 min)
  - Dripping Springs (~30 min)
-->

**Process:**
1. WebSearch local event calendars for the current week, using queries like:
   - `[city near zip code] events [date range] [year]` for each city in the coverage area
   - `site:patch.com/[state]/[city] calendar`
   - `site:allevents.in/[city] today` or `this weekend`
   - `[metro area] events this weekend [date]`
   - `[city] farmers market [date]` for recurring markets
   - Search for seasonal events: spring training, holiday festivals, county fairs, etc.
2. Filter for **actual confirmed events with dates and times** — not generic "things to do" tourist lists
3. Tag each event by who it's good for: Toddler-friendly, Kid-friendly, Teen-friendly, Adult, or Family (all ages)
4. Note approximate drive time from home zip code

**Key Recurring Events to Track:**
<!-- List any weekly/monthly recurring events near you that are worth checking.
     These serve as anchors — the system always includes them if they fall in the week. -->
- {{e.g., "Sunday farmers market at City Park — every Sunday, 9am-1pm"}}
- {{e.g., "First Friday Art Walk — first Friday of every month, 5-9pm"}}
- {{e.g., "Sunset celebration at the pier — nightly"}}

<!-- Example recurring events:
- SFC Farmers' Market Downtown — every Saturday, 9am-1pm
- First Friday Art Walk on South Congress — first Friday of each month, 5-9pm
- Zilker Park Kite Festival — annual, first weekend of March
- Round Rock Express home games — check schedule weekly
-->

**Output Format (in briefing):**
```
### What's Going On This Week
[Organized by day, then by proximity — closest first]

**Saturday**
- Chalk Art Festival — Main St, City A, 9am-5pm (Family) ~10 min
- Baseball Game — Stadium, City B, 1:07pm (Family) ~15 min

**Sunday**
- Farmers Market — Town Square, 10am-2pm (Family) ~10 min
- Food Festival — Waterfront Park, 4-10pm (Family) ~30 min

**Weeknight Pick**
- [anything notable Mon-Thu]
```

**On-Demand Trigger Words:**
- "what's going on", "things to do", "events this weekend", "anything happening"
- "what can we do with [child name]", "family stuff this weekend", "stuff to do"

**Guardrails:**
- Only include events with confirmed dates/times/locations from search results — never guess or recycle old event info
- Always note if an event is the last day or selling out
- For ticketed events, include price when available
- Don't pad the list with generic permanent attractions (aquarium, zoo, parks) unless they have a **special event** running that week

### 7. Schedule Conflict Detection
Proactively identify and flag problems before they happen.

**Watch for:**
- Both parents working same shift with no childcare plan
- Child pickup/dropoff conflicts with work schedules
- Double-booked family events
- Toddler/baby routine disruptions (nap times vs. scheduled activities)
- On-call or night shift overlaps with the other parent's shifts

When a conflict is detected, present it clearly with 2-3 resolution options.

### Grocery Budget
- **Target:** {{e.g., "$250/week" or "$200/week"}} (~{{monthly equivalent}}/month)
- Based on: {{your household size and location, e.g., "2 adults + 1 child (50% custody) + 1 toddler, cooking at home, Tampa FL"}}
- When bargain hunt / multi-store split is active, goal is to push below the target
- Flag it if a weekly grocery list is trending over budget
- Track savings over time: optimized split vs. single-store baseline

## Integration Map

<!-- Check off which MCP integrations you have connected.
     The skill works with whatever you have — more integrations = more power. -->

| Service | MCP | Required? | What It Does |
|---------|-----|-----------|-------------|
| Google Calendar | Google Calendar MCP | **Yes** | Read/write family schedules, determine custody days, check work shifts |
| Gmail | Gmail MCP | Optional | Co-parent coordination drafts, partner briefing emails |
| Notion | Notion MCP | Optional | Family dashboard — single source of truth |
| Chrome | Chrome MCP | Optional | Grocery cart automation + multi-store price scanning |

## Interaction Patterns

**"Plan the week"** or **"Sunday briefing"**
→ Full pipeline: Calendar check → custody days → meal plan → grocery list → local events scout → briefing → dashboard update

**"What's for dinner?"** (single day)
→ Check who's home today → suggest dinner based on current meal plan or generate a quick option

**"Bargain hunt"** or **"Find the deals"** or **"Compare prices"** or **"Load the carts"**
→ Pull grocery list → price scan stores → smart split → savings report → load carts

**"Load the cart"** (singular)
→ Pull current meal plan → generate list → load primary store cart → present summary

**"We need groceries"** or **"Grocery run"**
→ Pull current meal plan → generate list → offer: "Want me to bargain hunt across stores or just load one cart?"

**"What's going on this weekend?"** or **"Anything happening?"** or **"Things to do"**
→ Local events scout: WebSearch event calendars across nearby cities → filter to confirmed events with dates/times → tag by age-appropriateness → organize by day and proximity

**"Email {{CO_PARENT}} about [X]"**
→ Draft professional co-parent email → present for review

**"What's the schedule look like?"**
→ Pull calendar → present day/week view with custody overlay

## Important Guardrails

1. **Never assume custody days.** Always verify against the calendar.
2. **Never auto-send emails.** Always draft for the user's review.
3. **Child food safety is non-negotiable.** Every meal suggestion for young children must be age-appropriate. When in doubt, flag it.
4. **Respect both parents' input.** If a parent has stated preferences or vetoed something, that takes priority.
5. **Be realistic about schedules.** Don't suggest a 2-hour recipe on a night when both parents work late.
6. **Budget awareness.** Flag it if a weekly grocery list is trending over the set budget.
