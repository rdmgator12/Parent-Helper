# Setup Guide

This guide walks you through connecting the MCP servers that power Parent Helper. Start with Google Calendar (required), then add others as needed.

## Prerequisites

- [Claude Code](https://claude.ai/download) installed — either the **desktop app** (recommended, no terminal needed) or the **terminal CLI** (`npm install -g @anthropic-ai/claude-code`)
- A Google account with your family's calendar populated

## Step 1: Install the Skill

```bash
# Create the skill directory
mkdir -p ~/.claude/skills/parent-helper

# Copy the skill file
cp SKILL.md ~/.claude/skills/parent-helper/SKILL.md
```

Open the skill file and fill in all `{{PLACEHOLDER}}` fields with your family's details. See [`family-config-example.md`](family-config-example.md) for a complete example.

## Step 2: Connect Google Calendar (Required)

Google Calendar is the foundation — it provides work schedules, custody days, school events, and appointments.

### Option A: Use an existing Google Calendar MCP

If you already have a Google Calendar MCP server configured in Claude Code, you're good. Parent Helper will use it automatically.

### Option B: Set up Google Calendar MCP

1. Follow the setup instructions for your preferred Google Calendar MCP server. Popular options:
   - [google-calendar-mcp](https://github.com/nspaeth/google-calendar-mcp)
   - Check the [MCP server directory](https://github.com/modelcontextprotocol/servers) for others

2. Add the MCP server to your Claude Code settings (`~/.claude/settings.json` or project-level `.claude/settings.json`):
   ```json
   {
     "mcpServers": {
       "google-calendar": {
         "command": "npx",
         "args": ["-y", "google-calendar-mcp"],
         "env": {
           "GOOGLE_CLIENT_ID": "your-client-id",
           "GOOGLE_CLIENT_SECRET": "your-client-secret",
           "GOOGLE_REDIRECT_URI": "your-redirect-uri"
         }
       }
     }
   }
   ```

3. Authenticate and authorize calendar access when prompted.

### Calendar Setup Tips

- **Color-code your events** consistently (e.g., blue for "child at Dad's", pink for "child at Mom's", purple for work shifts). Define these colors in the SKILL.md.
- **Create separate calendars** for different purposes (Family, Work, Custody) to keep things organized.
- **Populate work schedules** at least 2 weeks out so the briefing can plan ahead.

## Step 3: Connect Gmail (Optional)

Gmail enables co-parent coordination drafts and partner briefing emails.

1. Set up a Gmail MCP server (same auth flow as Calendar if using Google Workspace).
2. Add to your MCP settings.
3. Parent Helper will use it for:
   - Drafting co-parent emails (never auto-sends — always shows you the draft first)
   - Sending weekly briefing summaries to your partner

## Step 4: Connect Notion (Optional)

Notion provides a persistent family dashboard — a single page that always shows the current week's plan.

1. Set up a Notion MCP server:
   - [notion-mcp](https://github.com/modelcontextprotocol/servers/tree/main/src/notion) (official)
   - Or any Notion MCP that supports page read/write

2. Create your dashboard structure in Notion:
   - **One main page** — this is your dashboard (copy the page ID into SKILL.md)
   - **Three databases** (create as sub-pages or inline databases):
     - **To-Do List**: Columns — Task (title), Assignee, Status, Priority, Due Date, Category
     - **Important Dates**: Columns — Event (title), Date, Type, Recurring, Notes
     - **Recurring Needs**: Columns — Item (title), Category, Frequency, Last Purchased, Notes

3. Copy all IDs into the SKILL.md `Family Dashboard` section:
   - Dashboard page ID
   - Each database ID and data source / collection ID

4. The system will overwrite content sections on each briefing and add rows to databases as needed.

## Step 5: Connect Chrome MCP (Optional)

Chrome MCP enables the multi-store grocery bargain hunter and cart automation.

1. Install [Claude in Chrome](https://chromewebstore.google.com/detail/claude-in-chrome/) browser extension.
2. The Chrome MCP tools will automatically become available in Claude Code.
3. **Important:** Log into your grocery store accounts in Chrome first:
   - Your primary grocery store (e.g., Walmart)
   - Instacart (if using for Aldi/Publix/etc.)
   - Amazon (if using Whole Foods)

4. **Pick your stores** — open [`store-profiles.md`](store-profiles.md) and find your local stores:
   - **15+ pre-built profiles**: Walmart, Kroger, Aldi, Publix, H-E-B, Meijer, Target, Whole Foods, Safeway/Albertsons, WinCo, Costco, Sam's Club, Trader Joe's, Sprouts, Grocery Outlet, Save A Lot, Fresh Market
   - Each profile gives you: search URL, store brand, deal types, cart button, and DOM extraction tips
   - Copy the profiles for your 2-4 local stores into the SKILL.md grocery section

5. **Store not listed?** The "How to Add Any Store" guide at the bottom of `store-profiles.md` walks you through building a profile for any grocery store in 5 minutes. You just need:
   - The search URL pattern (search for an item, note the URL)
   - The store brand name
   - The add-to-cart button description
   - Basic DOM extraction notes

6. Set your local store / zip code in each store's website (prices vary by location)

7. Note your memberships in SKILL.md: Walmart+, Amazon Prime, Kroger Plus, Costco, etc.

## Verifying Your Setup

Once everything is connected, test with these commands in Claude Code:

```
# Test calendar access
> What's on my calendar this week?

# Test meal planning
> What's for dinner tonight?

# Test full briefing
> Plan the week

# Test grocery automation (if Chrome MCP connected)
> Bargain hunt the grocery list
```

## Troubleshooting

**"I don't have access to Google Calendar"**
- Make sure the Google Calendar MCP server is configured in your Claude Code settings
- Re-authenticate if your token has expired

**"Notion page not found"**
- Double-check the page ID in SKILL.md (it's a UUID, not a URL)
- Make sure the Notion MCP has access to the page (check integration permissions)

**"Chrome MCP not responding"**
- Make sure the Claude in Chrome extension is installed and active
- Check that Claude Code and Chrome are connected (you should see the tab group)

**"Grocery prices not loading"**
- Make sure you're logged into each store's website in Chrome
- Try the search URL manually in Chrome to verify it works
- Some stores require location/zip code to show prices — set this in your account
