# Store Profiles

Pre-built profiles for common US grocery stores. Copy the profiles for your local stores into the SKILL.md grocery section.

**Don't see your store?** See [How to Add Any Store](#how-to-add-any-store) at the bottom to build your own profile in 5 minutes.

---

## How to Use These Profiles

1. Find your local stores below
2. Copy the store table row, search URL, store brand, deal types, and DOM tips into your SKILL.md
3. Log into each store's website in Chrome (so Chrome MCP can access your account pricing)
4. Set your local store / zip code in each account (prices vary by location)

---

## Budget Tier ($)

### Walmart
| Field | Value |
|-------|-------|
| **Website** | walmart.com |
| **Search URL** | `https://www.walmart.com/search?q=<search+terms>&cat_id=976759` |
| **Store Brand** | Great Value |
| **Membership** | Walmart+ ($98/yr) — free delivery, free pickup, no minimums. Works without membership too (pickup is always free). |
| **Deal Types** | Rollback (yellow badge), Clearance, "Overall Pick" / "Best Seller" badges |
| **Cart Button** | Blue "+ Add" button on product cards. Click multiple times for qty > 1. |
| **DOM Tips** | Product cards with `data-item-id`. Prices visible in card text. Per-lb pricing available for produce/meat. `__NEXT_DATA__` JSON exists but is auth-blocked — use DOM scraping instead. |
| **Platform** | Direct website |
| **Notes** | Great Value is the price floor for most staples. Walmart consistently wins on milk, eggs, bread, and pantry basics. |

### Aldi
| Field | Value |
|-------|-------|
| **Website** | Via Instacart (no direct e-commerce) |
| **Search URL** | `https://www.instacart.com/store/aldi/search/<search%20terms>` |
| **Store Brand** | Most items are Aldi house brands (no national brand markup) |
| **Membership** | None required. Instacart+ optional for free delivery. |
| **Deal Types** | "Aldi Finds" (limited-time specialty items), "Best seller" tag, "Store choice" tag |
| **Cart Button** | Green "Add" button on Instacart product cards. |
| **DOM Tips** | Instacart CSS classes are dynamic (change on deploy). Use `aria-label` attributes and `innerText` extraction. Look for sale % badges. |
| **Platform** | Instacart |
| **Notes** | Smallest selection but consistently lowest base prices. Not every item will be available. Great for staples, produce basics, and dairy. |

### WinCo Foods
| Field | Value |
|-------|-------|
| **Website** | wincofoods.com (limited online — primarily in-store) |
| **Search URL** | `https://www.wincofoods.com/search?q=<search+terms>` |
| **Store Brand** | WinCo brand |
| **Membership** | None |
| **Deal Types** | Bulk bins (priced per lb), weekly ad specials |
| **Cart Button** | Limited online ordering — generate a **pickup list** instead of cart automation. |
| **DOM Tips** | Website has basic product listings. Prices may require screenshot extraction. |
| **Platform** | In-store / limited online |
| **Notes** | Employee-owned, no-frills. Rivals Aldi on price. Bulk bins are unbeatable for grains, nuts, baking supplies. Best as a pickup list store. Pacific NW, Mountain West, Southwest regions. |

### Grocery Outlet
| Field | Value |
|-------|-------|
| **Website** | groceryoutlet.com |
| **Search URL** | Limited online inventory — check weekly ad at `https://www.groceryoutlet.com/circular` |
| **Store Brand** | Varies (discount/overstock model — brands change weekly) |
| **Membership** | None |
| **Deal Types** | Everything is a deal (overstock/closeout model). Inventory is unpredictable. |
| **Cart Button** | No online cart — generate a **pickup list**. |
| **DOM Tips** | N/A — use for weekly circular scanning only. |
| **Platform** | In-store only |
| **Notes** | Amazing prices but zero consistency. Can't count on specific items being available. Best used as a "check the ad for windfalls" store rather than a primary cart. West Coast primarily. |

### Save A Lot
| Field | Value |
|-------|-------|
| **Website** | savealot.com |
| **Search URL** | Limited online — check weekly ad |
| **Store Brand** | Multiple house brands (Mondo, Coburn Farms, Ginger Evans, etc.) |
| **Membership** | None |
| **Deal Types** | Weekly specials, "Smart Buy" items |
| **Cart Button** | No online cart — generate a **pickup list**. |
| **Platform** | In-store only |
| **Notes** | Deep discount chain. Good for staples, limited selection. Eastern US / Midwest primarily. |

---

## Mid-Range Tier ($$)

### Kroger (and Kroger-owned: Ralphs, Fred Meyer, King Soopers, Fry's, Smith's, QFC, Mariano's, Harris Teeter, Pick 'n Save)
| Field | Value |
|-------|-------|
| **Website** | kroger.com (or regional domain: ralphs.com, fredmeyer.com, kingsoopers.com, etc.) |
| **Search URL** | `https://www.kroger.com/search?query=<search+terms>` (swap `kroger.com` for your regional domain) |
| **Store Brand** | Kroger, Simple Truth (organic), Private Selection (premium) |
| **Membership** | Free loyalty card (required for sale prices). Boost membership ($59/yr) for free delivery. |
| **Deal Types** | Digital coupons (clip before adding to cart!), Weekly ad, Buy 5 Save $5, Fuel Points deals |
| **Cart Button** | "Add to Cart" button on product cards. Digital coupons have a separate "Clip" button — clip first, then add item. |
| **DOM Tips** | Product cards with prices and unit prices. Digital coupon badges visible on cards. Sale vs. regular price clearly marked. |
| **Platform** | Direct website |
| **Notes** | Largest traditional grocery chain in the US. Digital coupons stack with sale prices — always clip available coupons before adding items. Kroger brand is solid quality at good prices. If you're in a Kroger market, this is likely your best mid-range option. |

### Publix
| Field | Value |
|-------|-------|
| **Website** | Via Instacart |
| **Search URL** | `https://www.instacart.com/store/publix/search/<search%20terms>` |
| **Store Brand** | Publix brand, GreenWise (organic) |
| **Membership** | None required |
| **Deal Types** | **BOGO (Buy One Get One Free)** — Publix is legendary for these. They effectively halve the price. Also: weekly ad specials, digital coupons. |
| **Cart Button** | Green "Add" button on Instacart product cards. |
| **DOM Tips** | Instacart CSS classes are dynamic. Use `aria-label` and `innerText`. Look for "BOGO" badges — these are the game changers. Sale % shown on cards. |
| **Platform** | Instacart |
| **Notes** | Southeast US. Premium feel but BOGO deals are the real story. A BOGO chicken breast at Publix beats Walmart's regular price. Always check Publix BOGOs before finalizing the smart split. Also has publix.com/savings for weekly ad preview. |

### H-E-B
| Field | Value |
|-------|-------|
| **Website** | heb.com |
| **Search URL** | `https://www.heb.com/search/?q=<search+terms>` |
| **Store Brand** | H-E-B, Hill Country Fare (budget), Central Market (premium) |
| **Membership** | None required |
| **Deal Types** | Combo Locos (multi-buy deals), weekly ad, Meal Deal bundles, digital coupons |
| **Cart Button** | "Add to cart" button on product cards. |
| **DOM Tips** | Clean product cards with prices. Combo Loco deals shown as badges. Unit pricing available. |
| **Platform** | Direct website |
| **Notes** | Texas only but beloved. H-E-B house brands are genuinely excellent quality. Combo Locos are like Publix BOGOs — they change which store wins. Curbside pickup is free and excellent. |

### Meijer
| Field | Value |
|-------|-------|
| **Website** | meijer.com |
| **Search URL** | `https://www.meijer.com/shopping/search.html?text=<search+terms>` |
| **Store Brand** | Meijer, True Goodness (organic), Purple Cow (dairy) |
| **Membership** | mPerks loyalty (free — required for digital coupons) |
| **Deal Types** | mPerks digital coupons, Buy 5 Save $5 (10 for $10), weekly specials |
| **Cart Button** | "Add to Cart" on product cards. Clip mPerks coupons separately. |
| **DOM Tips** | Product cards with pricing. mPerks deals shown as badges. |
| **Platform** | Direct website |
| **Notes** | Midwest superstore (Michigan, Ohio, Indiana, Illinois, Wisconsin, Kentucky). Similar to Kroger in pricing. mPerks coupons stack with sales. |

### Target
| Field | Value |
|-------|-------|
| **Website** | target.com |
| **Search URL** | `https://www.target.com/s?searchTerm=<search+terms>` |
| **Store Brand** | Good & Gather, Favorite Day (bakery/snacks), Market Pantry (budget) |
| **Membership** | Target Circle (free — 5% off with Target debit/credit card). |
| **Deal Types** | Target Circle offers (clip before buying), Same Day Delivery deals, weekly ad |
| **Cart Button** | "Add to cart" button. "Ship it" vs "Pick it up" vs "Same Day Delivery" options. |
| **DOM Tips** | Clean product cards. Circle offers shown as badges. Sale prices clearly marked. |
| **Platform** | Direct website |
| **Notes** | Grocery selection is growing but still limited vs. dedicated grocers. Good for pantry staples, snacks, dairy. Good & Gather is surprisingly good quality. Nationwide. |

### Safeway / Albertsons (and owned: Vons, Jewel-Osco, Shaw's, Acme, Tom Thumb, Randalls, Star Market)
| Field | Value |
|-------|-------|
| **Website** | safeway.com or albertsons.com (or regional domain) |
| **Search URL** | `https://www.safeway.com/shop/search-results.html?q=<search+terms>` |
| **Store Brand** | Signature Select, O Organics, Open Nature |
| **Membership** | Free loyalty card (Club Card — required for sale prices) |
| **Deal Types** | Club Card specials (big discounts), Just for U digital coupons, weekly ad |
| **Cart Button** | "Add to Cart" on product cards. |
| **DOM Tips** | Product cards with Club Card price vs. regular price. Digital coupons need clipping. |
| **Platform** | Direct website |
| **Notes** | Western US, Mid-Atlantic, Northeast. Club Card prices are significantly lower than shelf price — always factor in the loyalty discount. |

---

## Premium Tier ($$$)

### Whole Foods (Amazon)
| Field | Value |
|-------|-------|
| **Website** | amazon.com (Whole Foods section) |
| **Search URL** | `https://www.amazon.com/s?k=<search+terms>&i=wholefoods` |
| **Store Brand** | 365 by Whole Foods Market |
| **Membership** | Amazon Prime ($139/yr) — free delivery on orders $35+, exclusive Prime deals |
| **Deal Types** | Prime Member Deals, weekly sales, "previously purchased" quick-add |
| **Cart Button** | "Add to cart" on product listings. IMPORTANT: Amazon Fresh and Whole Foods have **separate carts** — always use `&i=wholefoods` in the URL to stay in the WF section. |
| **DOM Tips** | Standard Amazon product listings. "Prime" savings badges. "Previously purchased" tags for fast re-ordering. Subscribe & Save discounts on some items. |
| **Platform** | Amazon |
| **Notes** | Most expensive baseline but 365 brand is reasonable. Best for organic, specialty, and items where quality matters most. Use as the "quality fill" store — buy the bulk at cheaper stores, get specialty items here. |

### Trader Joe's
| Field | Value |
|-------|-------|
| **Website** | traderjoes.com (no e-commerce) |
| **Search URL** | N/A — no online ordering |
| **Store Brand** | Everything is Trader Joe's brand |
| **Membership** | None |
| **Deal Types** | No sales — fixed low prices. Fearless Flyer highlights new/seasonal items. |
| **Cart Button** | No online cart — generate a **pickup list**. |
| **DOM Tips** | N/A — in-store only. Can scan traderjoes.com product listings for price reference. |
| **Platform** | In-store only |
| **Notes** | No online ordering but unique products at good prices. Best handled as a pickup list. Great for frozen meals, snacks, specialty items, wine. Fixed pricing means no deal hunting needed — if TJ's has it, the price is what it is. |

### Sprouts Farmers Market
| Field | Value |
|-------|-------|
| **Website** | sprouts.com |
| **Search URL** | `https://shop.sprouts.com/search?search_term=<search+terms>` |
| **Store Brand** | Sprouts brand |
| **Membership** | None required |
| **Deal Types** | Weekly ad (Wednesday-Wednesday), bulk bin specials, Double Ad Wednesday (old + new ad overlap) |
| **Cart Button** | "Add to Cart" on product cards. |
| **DOM Tips** | Product cards with pricing. Sale items clearly marked. |
| **Platform** | Direct website |
| **Notes** | Natural/organic focus. Double Ad Wednesday is the move — two sets of deals overlap. Bulk bins rival WinCo for grains/nuts. Western and Southern US. |

### Fresh Market
| Field | Value |
|-------|-------|
| **Website** | thefreshmarket.com |
| **Search URL** | Limited online — check weekly specials |
| **Store Brand** | The Fresh Market brand |
| **Membership** | The Ultimate Loyalty Card (free) |
| **Deal Types** | Weekly specials, Little Big Meal (meal deal bundles) |
| **Cart Button** | Limited online — generate a **pickup list**. |
| **Platform** | Primarily in-store |
| **Notes** | Southeast / East Coast. Premium quality. Little Big Meal deals are good value for a complete dinner. |

---

## Warehouse Tier

### Costco
| Field | Value |
|-------|-------|
| **Website** | costco.com |
| **Search URL** | `https://www.costco.com/CatalogSearch?dept=All&keyword=<search+terms>` |
| **Store Brand** | Kirkland Signature |
| **Membership** | Required ($65/yr Gold Star, $130/yr Executive with 2% back) |
| **Deal Types** | Monthly coupon book, Manager's markdowns (asterisk on price tag = last chance), Instant Savings |
| **Cart Button** | "Add to Cart" on product cards. Note: online prices often differ from in-store. |
| **DOM Tips** | Product cards with pricing. May show "Online Only" vs "In Warehouse" availability. |
| **Platform** | Direct website |
| **Notes** | Bulk buying — great per-unit prices but large quantities. Best for: toilet paper, paper towels, diapers, meat (freeze portions), olive oil, nuts, cheese. Kirkland Signature is consistently excellent quality. Factor in the membership cost when calculating savings. |

### Sam's Club
| Field | Value |
|-------|-------|
| **Website** | samsclub.com |
| **Search URL** | `https://www.samsclub.com/s/<search+terms>` |
| **Store Brand** | Member's Mark |
| **Membership** | Required ($50/yr Club, $110/yr Plus with free shipping) |
| **Deal Types** | Instant Savings, Scan & Go (app), Surprising Values |
| **Cart Button** | "Add to cart" on product cards. |
| **DOM Tips** | Product cards with prices and per-unit pricing. Member's Mark items clearly branded. |
| **Platform** | Direct website |
| **Notes** | Walmart's warehouse club. Member's Mark is excellent value. Scan & Go app makes in-store shopping fast. Similar to Costco but often slightly lower prices on overlapping items. |

---

## How to Add Any Store

Don't see your local store above? Here's how to build a profile for any grocery store in 5 minutes:

### Step 1: Find the Search URL Pattern
1. Open the store's website in Chrome
2. Search for "chicken breast" using their search bar
3. Look at the URL in the address bar — it will look something like:
   ```
   https://www.yourstore.com/search?q=chicken+breast
   ```
4. Replace `chicken+breast` with `<search+terms>` — that's your pattern:
   ```
   https://www.yourstore.com/search?q=<search+terms>
   ```
5. If the store uses Instacart, the pattern is:
   ```
   https://www.instacart.com/store/{{store-slug}}/search/<search%20terms>
   ```
   Find the store slug by navigating to your store on instacart.com and noting the URL.

### Step 2: Identify the Store Brand
Every store has a house brand that's cheaper than national brands:
- Search for "milk" or "bread" and see what the store's own brand is called
- This is what you'll tell the system to prefer for staples

### Step 3: Find the Cart Button
1. Search for any item
2. Note what the "Add to Cart" button looks like (color, text, position)
3. If there's no online cart → this is a "pickup list" store

### Step 4: Check for Deal Types
- Does the store have a loyalty card with member pricing?
- Are there digital coupons that need to be "clipped"?
- Does the store run BOGO, Buy 5 Save 5, or similar promotions?
- Is there a weekly ad with sale items?

### Step 5: Test DOM Extraction
1. Navigate to a search results page
2. Right-click a product → Inspect
3. Note how prices are structured in the HTML
4. Key things to document:
   - Are prices in a specific CSS class or data attribute?
   - Is there a unit price (per oz, per lb)?
   - Are sale/deal badges in the DOM or just images?
   - Does `innerText` extraction give clean price data?
5. If DOM extraction is messy → note "use screenshot extraction as primary method"

### Step 6: Write Your Profile
Fill in this template and add it to your SKILL.md:

```markdown
- **{{Store Name}}**: {{website}}
  - Search URL: `{{url pattern}}`
  - Store brand: {{brand name}}
  - Membership: {{membership details or "None"}}
  - Deal types: {{BOGO / digital coupons / weekly ad / loyalty pricing}}
  - Cart button: {{description — e.g., "Blue 'Add to Cart' button on product cards"}}
  - DOM tips: {{how to extract prices — e.g., "Product cards with aria-labels, use innerText"}}
  - Notes: {{anything unique — delivery minimums, pickup options, regional availability}}
```

### Step 7: Test It
In Claude Code, try:
```
> Search for "whole milk" on {{your store}} and tell me the price
```
If it finds the price, your profile works. If not, adjust the search URL or DOM tips.
