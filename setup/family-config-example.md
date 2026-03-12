# Family Config Example

This shows what a fully filled-in family configuration looks like inside SKILL.md. This is a fictional family — replace with your own details.

---

## Family Context

### The Household
- **Mike**: Firefighter (24-on/48-off shift rotation). Dad to Lily and Owen.
- **Sarah**: Marketing manager, remote M-F 9-5 with some travel weeks. Mom to Owen, stepmom to Lily.
- **Lily**: 10 years old (birthday June 3, 2015). Mike shares 50/50 custody with Lily's mom (week-on/week-off). Check Google Calendar each week — the schedule occasionally shifts for holidays.
- **Owen**: 3 years old (birthday September 22, 2023). Always in the household. Toddler-stage eating.
- **Pets**: One dog (Biscuit, golden retriever — buy dog food monthly).

### Childcare Resources
- **Grandma Linda** (Mike's mom): Available weekdays. Typical slot: 8AM-3PM. Use when Mike is on shift and Sarah has a conflict or travel day.
- **Teen neighbor Jess**: Available after school for emergency pickups. Use as last resort only.

### Allergies & Dietary Restrictions
- **Mike**: No allergies. Eats everything.
- **Sarah**: Lactose intolerant — use dairy-free alternatives where possible. Can handle small amounts of cooked cheese.
- **Lily**: Tree nut allergy (serious — no almonds, cashews, walnuts, pecans). Always check labels. Carries EpiPen.
- **Owen**: No known allergies. Toddler-safe food only.

### School Schedule
- **Drop-off:** 7:45-8:00 AM
- **School ends:** 3:15 PM
- **Aftercare:** 3:15-6:00 PM (pickup by 6:00 PM)
- **Wednesdays:** Soccer practice 4:00-5:30 PM (coach picks up from aftercare, Sarah picks up from field)
- On school days, Lily is unavailable 8:00 AM-3:15 PM (or 6:00 PM if aftercare)

**Key School Dates:**
- Spring break: April 6-10, 2026
- Last day of school: June 5, 2026 (half day, noon dismissal)

### Calendar Color Coding
- **Blue** (default / colorId 1) — Lily at Dad's
- **Pink** (Flamingo / colorId 4) — Lily at Mom's
- **Green** (Sage / colorId 2) — Mike's fire shifts
- **Purple** (Grape / colorId 3) — Sarah's travel days

### Custody Rules
Lily's custody schedule with her mom (Karen) is week-on/week-off, switching Sundays at 5 PM.
ALWAYS check Google Calendar — holidays and school breaks cause swaps.
- When Lily IS home: plan for 4 people (Mike, Sarah, Lily, Owen)
- When Lily is NOT home: plan for 3 people (Mike, Sarah, Owen)

---

## Family Food Profile

- **Mike**: Great cook — spent years in the firehouse kitchen. Specialties: grilling, BBQ, big batch meals (chili, stews, jambalaya). Can handle complex recipes. Eats a lot. Loves spicy food.
- **Sarah**: Decent cook but prefers low-effort. Sheet pan dinners and Instant Pot are her sweet spots. Good at meal prep on Sundays. Dairy-free when possible. Eats lighter portions at dinner.
- **Lily**: Typical 10-year-old palate. Likes pasta, tacos, chicken nuggets, pizza. Will eat carrots and cucumber with ranch. Won't touch most cooked vegetables. Strategy: hide veggies in sauces, serve raw veggies with dip on the side. **TREE NUT ALLERGY — check all sauces, baked goods, and packaged foods.**
- **Owen**: Toddler-safe only. Cut everything small. Loves bananas, blueberries, scrambled eggs, cheese quesadillas (use dairy-free cheese to share with Sarah). No whole nuts, no whole grapes, no raw hard vegetables.

**Cooking Assignment Logic:**
- If Mike is on shift (24 hrs) → Sarah cooks. Instant Pot or sheet pan, 5-6 ingredients max.
- If Mike is off → Mike cooks or they split (Mike does protein, Sarah does sides).
- If both are busy → Instant Pot meal started in morning, or leftovers from Mike's batch cook.
- Post-shift rule: After Mike's 24-hr shift, he sleeps. That dinner = Sarah's domain (easy meal).

**Meal Philosophy:**
- PRIMARY GOAL: Eat at home. Real food. Takeout max 1x/week.
- Mike does a big batch cook every other day off — chili, pulled pork, soup. Leftovers stretch 2-3 meals.
- Budget target: $200/week.

---

## Stores (Tampa, FL)

| Store | Distance | Price Tier | Platform | Cart Automation |
|-------|----------|-----------|----------|-----------------|
| **Walmart** | 2 mi | $ | walmart.com (Walmart+ member) | Yes — Chrome MCP |
| **Aldi** | 3 mi | $ | Instacart | No — pickup list |
| **Publix** | 0.5 mi | $$ | Instacart | No — pickup list |

```
Walmart:  https://www.walmart.com/search?q=<search+terms>
Aldi:     https://www.instacart.com/store/aldi/search/<search%20terms>
Publix:   https://www.instacart.com/store/publix/search/<search%20terms>
```

---

## Notion Dashboard

> **Note:** The IDs below are example placeholders — do not use them literally. Replace each one with your actual Notion page and database IDs. To find your IDs, open the page/database in Notion, click "Share," and copy the ID from the URL.

- Dashboard Page ID: `a1b2c3d4-e5f6-7890-abcd-ef1234567890`
- To-Do List DB: `11111111-2222-3333-4444-555555555555` / `collection://aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`
- Important Dates DB: `66666666-7777-8888-9999-000000000000` / `collection://ffffffff-1111-2222-3333-444444444444`
- Recurring Needs DB: `aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee` / `collection://55555555-6666-7777-8888-999999999999`
