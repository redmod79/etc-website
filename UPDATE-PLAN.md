# Plan: Update etc-website with Latest etc6 Series

## Summary of Changes

The etc6 source series has been extensively updated since the website was last built. Content additions were made to **15 of 18 existing studies** (CONCLUSION.md and 03-analysis.md), plus **2 entirely new studies** were added. This is a bulk update, not a minor patch.

---

## Change Inventory

### A. New Studies (not in website)

| Source | Content | Website Folder |
|--------|---------|---------------|
| `etc6-19-matthew-10-28` | Matt 10:28 same-author analysis (apollymi + psyche + gehenna in Matthew) | `etc-20-matthew-10-28` |
| `etc6-20-judgment-parables-imagery` | Jesus' judgment parables: wheat/tares, dragnet, katakaio, kaminos, outer darkness, gnashing | `etc-21-judgment-parables-imagery` |

**Numbering note:** The website already has `etc-19-2-corinthians-5-intermediate-state` (from a standalone study, not part of the etc6 series). The two new etc6 studies are added as etc-20 and etc-21 to avoid renumbering.

### B. Content Updates by File Type

**`CONCLUSION.md` — Updated in 15 of 18 studies:**

| Study | Lines Added | Key Additions |
|-------|-------------|---------------|
| 01 | +22 | 2 Cor 5:8 I-B classification, Gen 35:18/1 Kings 17:21-22 analysis, NT anthropology paragraph |
| 02 | +18 | Acts 17:18-32 paragraph (Greek philosophers mocked resurrection, not soul immortality) |
| 03 | +22 | Genesis 2:17 "spiritual death" rebuttal (mot tamut = physical death; Gen 3:19,22; Gen 5:5) |
| 04 | +24 | 2 Cor 5:4 disembodiment analysis, Psalm 31:5→Luke 23:46→Acts 7:59 chain, 1 Samuel 28 narrator-endorsement |
| 05 | +14 | Gehenna-as-trash-dump paragraph (no attestation before Kimhi c. 1200 CE) |
| 06 | +15 | Obadiah 1:16 reference, apollymi/Luke 15 counter-argument (illegitimate totality transfer) |
| 07 | 0 | No content changes |
| 08 | 0 | No content changes |
| 09 | +16 | Abraham's Bosom intertestamental background section |
| 10 | 0 | No content changes |
| 11 | +16 | Rev 14:10 enōpion analysis, Ezekiel 38:22 fire-and-brimstone chain |
| 12 | +16 | Heb 2:14 katargeo analysis, beast-as-representative counter-argument |
| 13 | +18 | Targum tradition (mota tinyana), "X is Y" interpretive formula, Rev 21:4 ECT tension |
| 14 | +16 | Isaiah 2:10,19,21 source text for 2 Thess 1:9, "weeping and gnashing" OT background + kolasis LXX |
| 15 | +14 | Degrees of punishment analysis (many/few stripes are finite; sorer punishment = second death) |
| 16 | +20 | Intertestamental texts (Judith 16:17, 4 Maccabees), Apostolic Fathers quotations |
| 17 | +26 | 1 Tim 2:4/Ezek 33:11/Lam 3:33 verses, Anselmian argument paragraph, evidence ID fixes |
| 18 | +154 | Full rewrite: 17→19 studies, 597→632 evidence, updated all study summaries, added etc6-19/20 |

**`03-analysis.md` — Updated in 15 of 18 studies:**

| Study | Delta (lines) | Study | Delta (lines) |
|-------|--------------|-------|--------------|
| 01 | +34 | 10 | 0 |
| 02 | +15 | 11 | +43 |
| 03 | +32 | 12 | +40 |
| 04 | +34 | 13 | +46 |
| 05 | +29 | 14 | +40 |
| 06 | +40 | 15 | +32 |
| 07 | 0 | 16 | +76 |
| 08 | 0 | 17 | +105 |
| 09 | +25 | 18 | +21 |

**`04-word-studies.md` — Updated in 2 studies:**
- Study 12: +37 lines (katargeo semantic range analysis)
- Study 14: +5 lines (kolasis LXX usage)

**`02-verses.md`, `01-topics.md`, `PROMPT.md` — No content changes** (website versions only differ by BLB links and Related Studies footer)

### C. Naming Convention

All source files use `etc6-XX` prefix in cross-references. Website uses `etc-XX`. Every copied file needs:
- `etc6-01b` → `etc-01`
- `etc6-` → `etc-`

### D. Website-Only Content (preserve during update)

1. **`conclusion-simple.md`** (19 files) — Simplified reader-friendly conclusions. Source does not have these. Must not be overwritten. New studies need them generated.
2. **"Related Studies" footer** — Appended to each study's CONCLUSION.md in the website (links to law-website, genesis-6-website, bible-studies-website). Must be re-appended to updated files.
3. **BLB links** — `add_blb_links.py` and `add_word_links.py` add hyperlinks to Strong's numbers. Must be re-run after content updates.

### E. Master Evidence File

Source: 650 lines, 98KB (updated evidence counts, 632 items). Website: 669 lines, 101KB (stale counts + BLB links). Source version supersedes.

---

## Execution Steps

### Step 1: Revert BLB Links

```bash
cd D:/bible/etc-website
python add_blb_links.py --revert
```

This removes all BLB hyperlinks from website files, making them comparable to source files (minus the naming convention and Related Studies footer).

### Step 2: Extract Related Studies Footer

Save the "Related Studies" footer block from any existing study so it can be re-appended later:

```bash
# The footer appears at the end of each CONCLUSION.md in the website
# Save it as a template for re-insertion
```

### Step 3: Bulk Copy Updated Files (15 studies)

For each study with content changes (01, 02, 03, 04, 05, 06, 09, 11, 12, 13, 14, 15, 16, 17, 18):

```bash
# For each changed study:
# 1. Copy CONCLUSION.md from source → website
# 2. Copy 03-analysis.md from source → website
# 3. For studies 12, 14: also copy 04-word-studies.md
# 4. Fix naming: sed 's/etc6-01b/etc-01/g; s/etc6-/etc-/g'
# 5. Append Related Studies footer to CONCLUSION.md
```

Studies 07, 08, 10: No changes needed (skip).

**Folder mapping:**

| Source Folder | Website Folder |
|--------------|---------------|
| `etc6-01b-what-is-man` | `etc-01-what-is-man` |
| `etc6-02-who-has-immortality` | `etc-02-who-has-immortality` |
| `etc6-03-biblical-death` | `etc-03-biblical-death` |
| `etc6-04-state-of-the-dead` | `etc-04-state-of-the-dead` |
| `etc6-05-four-hell-words` | `etc-05-four-hell-words` |
| `etc6-06-destruction-vocabulary` | `etc-06-destruction-vocabulary` |
| `etc6-09-rich-man-lazarus` | `etc-09-rich-man-lazarus` |
| `etc6-11-smoke-ascending-forever` | `etc-11-smoke-ascending-forever` |
| `etc6-12-tormented-forever` | `etc-12-tormented-forever` |
| `etc6-13-lake-of-fire-second-death` | `etc-13-lake-of-fire-second-death` |
| `etc6-14-judgment-passages` | `etc-14-judgment-passages` |
| `etc6-15-ect-strongest-case` | `etc-15-ect-strongest-case` |
| `etc6-16-origins-of-ect` | `etc-16-origins-of-ect` |
| `etc6-17-gods-character-and-justice` | `etc-17-gods-character-and-justice` |
| `etc6-18-comprehensive-synthesis` | `etc-18-comprehensive-synthesis` |

### Step 4: Add New Study — etc-20-matthew-10-28

1. Create folder: `etc-website/docs/studies/etc-20-matthew-10-28/`
2. Copy all files from `bible-studies/etc6-19-matthew-10-28/`:
   - `01-topics.md`, `02-verses.md`, `03-analysis.md`, `04-word-studies.md`
   - `CONCLUSION.md`, `PROMPT.md`
   - `raw-data/` (all files)
3. Fix naming: `etc6-` → `etc-` in all copied files
4. Append Related Studies footer to CONCLUSION.md
5. Generate `conclusion-simple.md`

### Step 5: Add New Study — etc-21-judgment-parables-imagery

1. Create folder: `etc-website/docs/studies/etc-21-judgment-parables-imagery/`
2. Copy all files from `bible-studies/etc6-20-judgment-parables-imagery/`:
   - Same file list as Step 4
3. Fix naming: `etc6-` → `etc-`
4. Append Related Studies footer to CONCLUSION.md
5. Generate `conclusion-simple.md`

### Step 6: Update Master Evidence File

1. Copy `bible-studies/etc6-master-evidence.md` → `etc-website/docs/master-evidence.md`
2. Fix naming: `etc6-` → `etc-`

### Step 7: Update mkdocs.yml

1. Update `site_description` from "19-study" to "21-study"
2. Add nav entries for Study 20 (Matt 10:28) — place in Tier 3 (Key Passages)
3. Add nav entries for Study 21 (Judgment Parables) — place in Tier 3 (Key Passages)
4. Each new study nav follows the standard pattern:
   ```yaml
   - "20 -- Matthew 10:28: Destroy Soul and Body":
     - studies/etc-20-matthew-10-28/conclusion-simple.md
     - Conclusion: studies/etc-20-matthew-10-28/CONCLUSION.md
     - Analysis: studies/etc-20-matthew-10-28/03-analysis.md
     - Verses: studies/etc-20-matthew-10-28/02-verses.md
     - Word Studies: studies/etc-20-matthew-10-28/04-word-studies.md
     - Topics: studies/etc-20-matthew-10-28/01-topics.md
     - Research Scope: studies/etc-20-matthew-10-28/PROMPT.md
     - Raw Data:
       - [list raw-data files from the folder]
   ```

### Step 8: Generate conclusion-simple.md for New Studies

For each new study (20, 21), create a reader-friendly simplified conclusion. Format matches existing `conclusion-simple.md` files:
- Clear heading with study title
- "What This Study Examined" section
- "What the Text Actually Says" with key findings in accessible language
- No evidence IDs or tier classifications
- ~1-2 page summary

### Step 9: Re-Run BLB Link Scripts

```bash
cd D:/bible/etc-website
python add_blb_links.py            # Apply to all study files (including new ones)
python add_word_links.py           # Apply word links
```

### Step 10: Local Build & Test

```bash
cd D:/bible/etc-website
mkdocs serve   # local preview at localhost:8000
```

Verify:
- [ ] All 21 studies accessible in navigation
- [ ] New studies (20, 21) render correctly
- [ ] All 15 updated studies show new content
- [ ] BLB links work in updated/new files
- [ ] Master evidence page shows updated counts (632 items)
- [ ] Search finds content from new studies
- [ ] No broken internal cross-references
- [ ] Related Studies footer present on all CONCLUSION.md files
- [ ] conclusion-simple.md files intact for all 21 studies

### Step 11: Commit & Deploy

```bash
cd D:/bible/etc-website
git add .
git commit -m "Update with latest etc6 series: 15 studies updated, 2 new studies (20-21)"
git push origin master
```

GitHub Actions auto-deploys to https://redmod79.github.io/etc-website/

---

## Study Update Matrix

| # | Study | CONCLUSION | 03-analysis | 04-word-studies | 02-verses | New? |
|---|-------|-----------|-------------|-----------------|-----------|------|
| 01 | What Is Man | **+22 lines** | **+34 lines** | — | — | |
| 02 | Who Has Immortality | **+18 lines** | **+15 lines** | — | — | |
| 03 | Biblical Death | **+22 lines** | **+32 lines** | — | — | |
| 04 | State of the Dead | **+24 lines** | **+34 lines** | — | — | |
| 05 | Four Hell Words | **+14 lines** | **+29 lines** | — | — | |
| 06 | Destruction Vocabulary | **+15 lines** | **+40 lines** | — | — | |
| 07 | Olam (OT Forever) | — | — | — | — | |
| 08 | Aionios (NT Eternal) | — | — | — | — | |
| 09 | Rich Man & Lazarus | **+16 lines** | **+25 lines** | — | — | |
| 10 | Souls Under Altar | — | — | — | — | |
| 11 | Smoke Ascending | **+16 lines** | **+43 lines** | — | — | |
| 12 | Tormented Forever | **+16 lines** | **+40 lines** | **+37 lines** | — | |
| 13 | Lake of Fire | **+18 lines** | **+46 lines** | — | — | |
| 14 | Judgment Passages | **+16 lines** | **+40 lines** | **+5 lines** | — | |
| 15 | ECT Strongest Case | **+14 lines** | **+32 lines** | — | — | |
| 16 | Origins of ECT | **+20 lines** | **+76 lines** | — | — | |
| 17 | God's Character | **+26 lines** | **+105 lines** | — | — | |
| 18 | Comprehensive Synthesis | **+154 lines** | **+21 lines** | — | — | |
| 19 | 2 Cor 5 Intermediate | — | — | — | — | (keep) |
| 20 | Matthew 10:28 | — | — | — | — | **NEW** |
| 21 | Judgment Parables | — | — | — | — | **NEW** |

**Total: 15 studies updated + 2 new studies added = 17 studies touched**

---

*Created: 2026-03-02*
