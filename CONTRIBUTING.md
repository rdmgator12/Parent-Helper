# Contributing to Parent Helper

Thanks for wanting to make Parent Helper better! Here's how to contribute.

## Store Profiles

The easiest way to contribute is adding a new grocery store profile to `setup/store-profiles.md`. Each profile needs:

1. **Store name and tier** (Budget $, Mid-Range $$, Premium $$$, Warehouse)
2. **Search URL pattern** — search for any item on the store's website, note the URL structure
3. **Store brand** — the house/generic brand name (e.g., "Great Value" for Walmart)
4. **Membership info** — any loyalty program or delivery subscription
5. **Deal types** — what kind of sales the store runs (BOGO, digital coupons, weekly ads, etc.)
6. **Cart button** — what the "Add to Cart" button looks like (text, aria-label)
7. **DOM extraction tips** — how prices, sale badges, and product names appear in the page structure
8. **Platform** — direct website, Instacart, or other delivery platform

See the "How to Add Any Store" guide at the bottom of `setup/store-profiles.md` for a step-by-step walkthrough.

### Testing Your Profile

Before submitting, test your store profile by:
1. Pasting the search URL into Chrome with a real item (e.g., "whole milk")
2. Verifying prices load and are visible
3. Confirming the add-to-cart button description matches what's on screen
4. Checking that the DOM extraction tips actually find price elements

## Other Contributions

We also welcome:

- **Meal plan templates** — common dietary patterns (vegetarian, keto, allergen-free) as example configs
- **Integration guides** — setup instructions for additional MCP servers
- **Localization** — non-US school systems, international grocery chains, regional store coverage
- **Bug fixes** — if something in the skill file doesn't work as documented

## How to Submit

1. Fork the repo
2. Create a branch (`git checkout -b add-kroger-profile`)
3. Make your changes
4. Test with your own family setup if possible
5. Open a PR with a clear description of what you added/changed

## Guidelines

- **Don't include personal data.** No real names, addresses, Notion IDs, or calendar details. Use fictional examples if you need to demonstrate something. This is enforced by a PHI/secret pre-commit hook (see below) — but the hook is a backstop, not a substitute for judgment.
- **Keep store profiles consistent.** Follow the existing format in `store-profiles.md` so all profiles look the same.
- **One store per PR** makes review easier, but bundling related stores (e.g., all Kroger subsidiaries) in one PR is fine.

## PHI / secret protection

This repo ships a defense-in-depth gate against committing personal data, credentials, or
patient information:

- **Pre-commit hook** — install it once per clone:
  ```sh
  ln -sf ../../hooks/pre-commit .git/hooks/pre-commit
  ```
  It blocks staged credential/env files, PHI-risk binaries, structured-data exports
  (`.csv`/`.tsv`), and content that looks like a name next to a DOB/MRN. Override only when
  you're certain it's a false positive: `git commit --no-verify`.
- **Retroactive audit** — scan a repo's entire history (the hook only guards new commits):
  ```sh
  python hooks/scan-history.py
  ```
- **Tests** — `python -m unittest discover -s hooks/tests` (86 cases, zero deps). Add a
  regression test alongside any change to the gate's patterns.

The hook is a heuristic backstop with known limits — it raises the floor, it is not a
guarantee. Real-name/PHI hygiene is still the contributor's responsibility.

## Questions?

Open an issue if you're unsure about anything. We'd rather help you contribute than have you give up.
