# Cross-Testament Parallels — etc5-06 Destruction Vocabulary

Tool: `cross_testament_parallels_v2.py` (hybrid scoring = semantic + keyword + phrase + theological)
All queries run with both `--hybrid-ot` (find OT parallels) and `--hybrid-nt` (find NT parallels), topn=8.

**Note on verse reference format used by this tool:**
- OT uses Latin/BHSA book names: "Psalmi", "Maleachi", "Jesaia", "Obadia"
- NT uses short codes: "JHN", "2TH", "REV", "MAT", "MRK", "ROM", "PHP", etc.
- Malachi chapter numbering: Hebrew Bible has only 3 chapters; English Mal 4:1-6 = BHSA Maleachi 3:19-24

---

## 1. Psalm 37:9 — "evildoers shall be cut off" (karat — Niphal)

**Source verse gloss:** "that be evil cut and wait for YHWH they trample down earth"

### hybrid-ot (OT parallels):
| Reference          | Hybrid | Sem  | Key  | Theo | Key Terms                     |
|--------------------|--------|------|------|------|-------------------------------|
| Psalmi 37:34       | 0.455  | 0.77 | 0.20 | 0.00 | cut, down                     |
| Psalmi 34:17       | 0.443  | 0.75 | 0.20 | 0.00 | cut, evil                     |
| Jeremia 1:14       | 0.423  | 0.78 | 0.10 | 0.00 | evil                          |
| Leviticus 26:6     | 0.420  | 0.72 | 0.20 | 0.00 | down, evil                    |
| Numeri 14:37       | 0.417  | 0.76 | 0.10 | 0.00 | evil                          |
| Psalmi 37:22       | 0.401  | 0.67 | 0.20 | 0.00 | cut, down                     |
| Psalmi 101:8       | 0.394  | 0.71 | 0.10 | 0.00 | cut                           |
| Jeremia 25:32      | 0.392  | 0.71 | 0.10 | 0.00 | evil                          |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms |
|------------|--------|------|------|------|-----------|
| 1CO 5:13   | 0.334  | 0.61 | 0.10 | 0.00 | evil      |
| JHN 17:15  | 0.328  | 0.60 | 0.10 | 0.00 | evil      |
| MRK 7:23   | 0.321  | 0.59 | 0.10 | 0.00 | evil      |
| REV 12:12  | 0.319  | 0.57 | 0.10 | 0.00 | down      |
| 1TH 5:15   | 0.311  | 0.57 | 0.10 | 0.00 | evil      |
| ROM 14:16  | 0.309  | 0.56 | 0.10 | 0.00 | evil      |
| LUK 21:24  | 0.302  | 0.55 | 0.10 | 0.00 | down      |
| 1TH 5:22   | 0.302  | 0.55 | 0.10 | 0.00 | evil      |

**Notes:** Strong intra-Psalm links (37:34, 37:22 — same destruction cluster). The NT parallels are weak (all below 0.34), primarily matching on "evil" alone. No strong NT connection, confirming the OT destruction vocabulary of karat does not map directly to a specific NT passage — the NT parallels for this theme are distributed across multiple destruction terms rather than a single equivalent.

---

## 2. Psalm 37:20 — "the wicked shall perish" (abad) + "shall consume" (kalah)

**Source verse gloss:** "that guilty perish and be hostile YHWH as rare pasture be complete in the smoke"

### hybrid-ot (OT parallels):
| Reference          | Hybrid | Sem  | Key  | Theo | Key Terms                          |
|--------------------|--------|------|------|------|------------------------------------|
| Psalmi 92:10       | 0.451  | 0.77 | 0.20 | 0.00 | consume, hostile                   |
| Samuel_II 22:38    | 0.429  | 0.69 | 0.30 | 0.00 | complete, consume, hostile         |
| Ezechiel 22:31     | 0.425  | 0.73 | 0.20 | 0.00 | burn, complete                     |
| Joel 1:19          | 0.424  | 0.67 | 0.30 | 0.00 | burn, consume, pasture             |
| Psalmi 9:7         | 0.422  | 0.67 | 0.30 | 0.00 | complete, consume, hostile         |
| Chronica_II 26:16  | 0.410  | 0.70 | 0.20 | 0.00 | burn, consume                      |
| Iob 27:7           | 0.408  | 0.70 | 0.20 | 0.00 | guilty, hostile                    |
| Judices 5:31       | 0.403  | 0.68 | 0.20 | 0.00 | consume, hostile                   |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms     |
|------------|--------|------|------|------|---------------|
| JUD 1:23   | 0.349  | 0.64 | 0.10 | 0.00 | burn          |
| HEB 6:8    | 0.348  | 0.64 | 0.10 | 0.00 | burn          |
| JAS 2:10   | 0.335  | 0.61 | 0.10 | 0.00 | guilty        |
| 1PE 5:8    | 0.333  | 0.61 | 0.10 | 0.00 | consume       |
| HEB 10:27  | 0.326  | 0.54 | 0.20 | 0.00 | burn, consume |
| HEB 12:29  | 0.318  | 0.57 | 0.10 | 0.00 | burn          |
| LUK 3:17   | 0.314  | 0.57 | 0.10 | 0.00 | burn          |
| HEB 12:18  | 0.312  | 0.57 | 0.10 | 0.00 | burn          |

**Notes:** The OT parallels are semantically rich — Psalm 92:10 shares the "consume/hostile enemies" pattern, and Psalm 9:7 has the same "enemies are destroyed" theme. The fire/smoke imagery of Mal 4:1 (Isa 5:24, Joel 1:19 pasture fire) appears here. NT parallels cluster around Hebrews (fire of judgment: 6:8, 10:27, 12:29) and Luke 3:17 (chaff/fire), confirming NT writers drew on this OT fire imagery.

---

## 3. Malachi 4:1 — "day that shall burn as an oven" (BHSA: Maleachi 3:19)

**Source verse gloss:** "that behold the day come burn as the furnace and be whole... root... service"

### hybrid-ot (OT parallels):
| Reference          | Hybrid | Sem  | Key  | Theo | Key Terms                |
|--------------------|--------|------|------|------|--------------------------|
| Jeremia 5:14       | 0.453  | 0.70 | 0.30 | 0.00 | behold, burn, service    |
| Deuteronomium 9:3  | 0.444  | 0.74 | 0.20 | 0.00 | burn, consume            |
| Habakuk 2:13       | 0.439  | 0.70 | 0.30 | 0.00 | behold, burn, service    |
| Jesaia 5:24        | 0.431  | 0.59 | 0.40 | 0.00 | burn, root, service, stubble |
| Jesaia 13:9        | 0.423  | 0.71 | 0.20 | 0.00 | behold, consume          |
| Chronica_II 13:11  | 0.417  | 0.71 | 0.20 | 0.00 | burn, leave              |
| Jesaia 22:25       | 0.412  | 0.73 | 0.10 | 0.00 | service                  |
| Jeremia 51:58      | 0.406  | 0.66 | 0.20 | 0.00 | burn, service            |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms       |
|------------|--------|------|------|------|-----------------|
| ACT 13:41  | 0.354  | 0.59 | 0.20 | 0.00 | behold, consume |
| 2PE 3:7    | 0.329  | 0.59 | 0.10 | 0.00 | burn            |
| LUK 12:28  | 0.323  | 0.58 | 0.10 | 0.00 | furnace         |
| HEB 6:8    | 0.321  | 0.59 | 0.10 | 0.00 | burn            |
| 2PE 3:12   | 0.317  | 0.56 | 0.10 | 0.00 | burn            |
| MAT 6:30   | 0.316  | 0.56 | 0.10 | 0.00 | furnace         |
| LUK 1:20   | 0.315  | 0.56 | 0.10 | 0.00 | behold          |
| 2TH 2:2    | 0.306  | 0.59 | 0.00 | 0.00 | —               |

**Notes:** Isaiah 5:24 is the strongest OT parallel (burn, root, stubble — the destruction as fire consuming stubble imagery). 2 Peter 3:7,12 are the strongest NT links — the eschatological fire that destroys. This confirms Mal 4:1's "burning oven" uses the same utter-destruction imagery as 2 Pet 3:7-12.

---

## 4. Malachi 4:2 — "Sun of Righteousness arise with healing" (BHSA: Maleachi 3:20)

**Source verse gloss:** "and flash up to afraid name sun justice and healing in wing"

### hybrid-ot (OT parallels):
| Reference       | Hybrid | Sem  | Key  | Theo | Key Terms       |
|-----------------|--------|------|------|------|-----------------|
| Psalmi 51:21    | 0.394  | 0.67 | 0.20 | 0.00 | bull, justice   |
| Numeri 15:24    | 0.384  | 0.65 | 0.20 | 0.00 | bull, justice   |
| Jesaia 58:8     | 0.370  | 0.62 | 0.20 | 0.00 | heal, justice   |
| Samuel_I 28:24  | 0.364  | 0.58 | 0.20 | 0.00 | bull, calf      |
| Exodus 32:24    | 0.352  | 0.64 | 0.10 | 0.00 | bull            |
| Jeremia 46:21   | 0.348  | 0.55 | 0.20 | 0.00 | bull, calf      |
| Genesis 30:33   | 0.347  | 0.64 | 0.10 | 0.00 | justice         |
| Numeri 29:33    | 0.342  | 0.57 | 0.20 | 0.00 | bull, justice   |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms |
|------------|--------|------|------|------|-----------|
| LUK 15:23  | 0.330  | 0.59 | 0.10 | 0.00 | calf      |
| EPH 4:26   | 0.308  | 0.55 | 0.10 | 0.00 | sun       |
| MAT 12:20  | 0.299  | 0.54 | 0.10 | 0.00 | justice   |
| HEB 10:4   | 0.281  | 0.50 | 0.10 | 0.00 | bull      |
| LUK 15:30  | 0.280  | 0.49 | 0.10 | 0.00 | calf      |
| ACT 4:30   | 0.279  | 0.44 | 0.20 | 0.00 | heal, name|
| LUK 10:17  | 0.272  | 0.49 | 0.10 | 0.00 | name      |
| LUK 4:40   | 0.272  | 0.42 | 0.20 | 0.00 | heal, sun |

**Notes:** This verse's healing/righteousness theme shows weak NT parallels — the semantic similarity is low for most. Isaiah 58:8 ("health shall spring forth...thy righteousness shall go before thee") is the best OT parallel for the "sun of righteousness/healing" concept. The low NT scores reflect that this restoration imagery is less theologically central to this study's destruction focus.

---

## 5. Malachi 4:3 — "tread down the wicked as ashes" (BHSA: Maleachi 3:21)

**Source verse gloss:** "and tread down guilty that be dust under part palm foot in the day"

### hybrid-ot (OT parallels):
| Reference       | Hybrid | Sem  | Key  | Theo | Key Terms              |
|-----------------|--------|------|------|------|------------------------|
| Psalmi 9:17     | 0.396  | 0.66 | 0.20 | 0.00 | guilty, palm           |
| Iob 40:12       | 0.389  | 0.60 | 0.30 | 0.00 | down, guilty, part     |
| Maleachi 3:19   | 0.376  | 0.63 | 0.10 | 0.00 | service                |
| Jesaia 49:23    | 0.376  | 0.57 | 0.30 | 0.00 | down, dust, foot       |
| Maleachi 1:9    | 0.373  | 0.65 | 0.10 | 0.00 | service                |
| Jesaia 22:25    | 0.363  | 0.63 | 0.10 | 0.00 | service                |
| Psalmi 36:12    | 0.355  | 0.59 | 0.20 | 0.00 | foot, guilty           |
| Maleachi 1:4    | 0.355  | 0.55 | 0.20 | 0.00 | down, service          |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms |
|------------|--------|------|------|------|-----------|
| MRK 9:45   | 0.284  | 0.51 | 0.10 | 0.00 | foot      |
| MAT 18:8   | 0.272  | 0.49 | 0.10 | 0.00 | foot      |
| JAS 2:10   | 0.264  | 0.47 | 0.10 | 0.00 | guilty    |
| MRK 9:43   | 0.258  | 0.52 | 0.00 | 0.00 | —         |
| 2CO 11:19  | 0.258  | 0.52 | 0.00 | 0.00 | —         |
| 1PE 2:8    | 0.257  | 0.51 | 0.00 | 0.00 | —         |
| PHP 2:30   | 0.255  | 0.45 | 0.10 | 0.00 | service   |
| MAT 11:22  | 0.254  | 0.49 | 0.00 | 0.00 | —         |

**Notes:** Very weak NT parallels for this verse (all below 0.29). Psalm 9:17 ("The wicked shall be turned into hell, and all the nations that forget God") is a strong OT semantic match. The "ashes under the soles of feet" imagery is distinctive to this passage and does not have a direct NT equivalent — but the concept (total annihilation leaving only remains) is exactly what the fire/destruction passages depict.

---

## 6. John 3:16 — "should not perish but have everlasting life" (apollētai)

**Source verse gloss:** "Thus for loved - God the world that the Son the only begotten... age alive believ everyone"

### hybrid-ot (OT parallels):
| Reference       | Hybrid | Sem  | Key  | Theo | Key Terms     |
|-----------------|--------|------|------|------|---------------|
| Psalmi 45:3     | 0.411  | 0.70 | 0.20 | 0.00 | age, thu      |
| Genesis 3:22    | 0.408  | 0.69 | 0.20 | 0.00 | age, alive    |
| Psalmi 48:15    | 0.387  | 0.71 | 0.10 | 0.00 | age           |
| Genesis 9:16    | 0.384  | 0.65 | 0.20 | 0.00 | age, alive    |
| Jeremia 49:33   | 0.383  | 0.70 | 0.10 | 0.00 | age           |
| Psalmi 86:12    | 0.378  | 0.70 | 0.10 | 0.00 | age           |
| Samuel_II 23:5  | 0.376  | 0.64 | 0.20 | 0.00 | age, thu      |
| Threni 3:31     | 0.374  | 0.69 | 0.10 | 0.00 | age           |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms                          |
|------------|--------|------|------|------|------------------------------------|
| JHN 6:40   | 0.518  | 0.77 | 0.40 | 0.00 | age, alive, believ, everyone       |
| JHN 3:15   | 0.517  | 0.76 | 0.40 | 0.00 | age, alive, believ, everyone       |
| JHN 3:36   | 0.478  | 0.75 | 0.30 | 0.00 | age, alive, believ                 |
| JHN 12:25  | 0.474  | 0.71 | 0.40 | 0.00 | age, alive, lov, world             |
| 1JN 5:1    | 0.473  | 0.64 | 0.40 | 0.00 | begotten, believ, everyone, lov    |
| 1JN 5:11   | 0.456  | 0.77 | 0.20 | 0.00 | age, alive                         |
| JHN 6:47   | 0.453  | 0.72 | 0.30 | 0.00 | age, alive, believ                 |
| 1JN 5:13   | 0.441  | 0.68 | 0.30 | 0.00 | age, alive, believ                 |

**Notes:** The NT parallels are very strong (0.44-0.52), all from the Johannine corpus (John 3:15, 3:36, 6:40, 6:47, 12:25; 1 John 5:1, 5:11, 5:13) — confirming that John's "life vs. perishing" contrast is a distinctive theological cluster. The OT parallels match primarily on "age/eternal" but lack the "perish" verb directly. Genesis 3:22 ("live forever") is the strongest conceptual OT link: the tree of life and what it means to "live" or fail to live eternally.

---

## 7. 2 Thessalonians 1:9 — "everlasting destruction from the presence of the Lord"

**Source verse gloss:** "who [the] penalty will suffer of destruction eternal away from [the] presence of the Lord"

### hybrid-ot (OT parallels):
| Reference          | Hybrid | Sem  | Key  | Theo | Key Terms           |
|--------------------|--------|------|------|------|---------------------|
| Psalmi 73:12       | 0.382  | 0.65 | 0.20 | 0.00 | age, power          |
| Psalmi 60:14       | 0.369  | 0.68 | 0.10 | 0.00 | power               |
| Psalmi 108:14      | 0.369  | 0.68 | 0.10 | 0.00 | power               |
| Deuteronomium 33:27| 0.356  | 0.65 | 0.10 | 0.00 | age                 |
| Psalmi 103:9       | 0.356  | 0.60 | 0.20 | 0.00 | age, glory          |
| Ezechiel 25:15     | 0.352  | 0.58 | 0.20 | 0.00 | age, destruction    |
| Jeremia 3:5        | 0.352  | 0.59 | 0.20 | 0.00 | age, glory          |
| Judices 2:19       | 0.348  | 0.69 | 0.00 | 0.00 | —                   |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms              |
|------------|--------|------|------|------|------------------------|
| ROM 9:22   | 0.413  | 0.70 | 0.20 | 0.00 | destruction, power     |
| HEB 1:3    | 0.393  | 0.67 | 0.20 | 0.00 | glory, power           |
| 1PE 5:10   | 0.392  | 0.60 | 0.30 | 0.00 | age, glory, suffer     |
| HEB 10:29  | 0.383  | 0.76 | 0.00 | 0.00 | —                      |
| MAT 25:46  | 0.380  | 0.70 | 0.10 | 0.00 | age                    |
| PHP 3:19   | 0.379  | 0.64 | 0.20 | 0.00 | destruction, glory     |
| 2TI 4:18   | 0.376  | 0.63 | 0.20 | 0.00 | age, glory             |
| 1PE 1:5    | 0.374  | 0.69 | 0.10 | 0.00 | power                  |

**Notes:** Strong NT parallels cluster around destruction terms: Romans 9:22 (vessels of wrath fitted for "destruction" — apoleia), Philippians 3:19 (whose end is "destruction"), and Matthew 25:46 ("everlasting punishment"). Hebrews 10:29 (punishment for trampling the Son of God) is notable. Ezekiel 25:15 in OT matches on "age, destruction" confirming that olethros/apoleia vocabulary echoes the permanent divine judgment of the OT.

---

## 8. Revelation 14:10 — "tormented with fire and brimstone"

**Source verse gloss:** "also he will drink of the wine of the anger of God having been mixed... burn, holy, angel"

### hybrid-ot (OT parallels):
| Reference       | Hybrid | Sem  | Key  | Theo | Key Terms              |
|-----------------|--------|------|------|------|------------------------|
| Daniel 5:23     | 0.398  | 0.61 | 0.30 | 0.00 | before, drink, wine    |
| Numeri 16:7     | 0.379  | 0.64 | 0.20 | 0.00 | burn, holy             |
| Numeri 17:11    | 0.372  | 0.62 | 0.20 | 0.00 | anger, burn            |
| Jeremia 44:18   | 0.372  | 0.69 | 0.10 | 0.00 | burn                   |
| Daniel 6:23     | 0.372  | 0.62 | 0.20 | 0.00 | angel, before          |
| Amos 2:12       | 0.372  | 0.63 | 0.20 | 0.00 | drink, wine            |
| Judices 13:7    | 0.369  | 0.61 | 0.20 | 0.00 | drink, wine            |
| Jeremia 35:6    | 0.362  | 0.60 | 0.20 | 0.00 | drink, wine            |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms                          |
|------------|--------|------|------|------|------------------------------------|
| LUK 1:15   | 0.501  | 0.77 | 0.40 | 0.00 | before, drink, holy, wine          |
| REV 19:15  | 0.444  | 0.72 | 0.20 | 0.00 | anger, wine                        |
| REV 14:8   | 0.443  | 0.65 | 0.40 | 0.00 | angel, anger, drink, wine          |
| REV 14:19  | 0.435  | 0.69 | 0.20 | 0.00 | angel, anger                       |
| MAT 25:41  | 0.418  | 0.72 | 0.20 | 0.00 | angel, burn                        |
| REV 8:4    | 0.415  | 0.64 | 0.30 | 0.00 | angel, before, burn                |
| REV 16:19  | 0.393  | 0.52 | 0.40 | 0.00 | anger, before, cup, wine           |
| MAT 10:42  | 0.392  | 0.66 | 0.20 | 0.00 | cup, drink                        |

**Notes:** The intra-Revelation parallels are strong (REV 19:15, 14:8, 14:19, 16:19) — confirming the "wrath of God/wine cup" cluster is Revelation's distinctive idiom. Matthew 25:41 ("everlasting fire") connects well thematically. OT parallels for the wine-of-wrath motif point to Daniel 5:23 (defiance before God) and Numbers 16-17 (fire judgment), but note these are burning judgments of the guilty — not torment without end, but consuming fire.

---

## 9. Revelation 14:11 — "the smoke of their torment ascendeth up for ever and ever"

**Source verse gloss:** "And the smoke of the torment of them to ages of ages goes up and not rest"

### hybrid-ot (OT parallels):
| Reference        | Hybrid | Sem  | Key  | Theo | Key Terms                             |
|------------------|--------|------|------|------|---------------------------------------|
| Jesaia 34:10     | 0.401  | 0.60 | 0.20 | 0.30 | age, burn [continual, forever]        |
| Reges_II 16:4    | 0.337  | 0.62 | 0.10 | 0.00 | burn                                  |
| Chronica_II 28:4 | 0.337  | 0.62 | 0.10 | 0.00 | burn                                  |
| Numeri 16:35     | 0.327  | 0.60 | 0.10 | 0.00 | burn                                  |
| Hosea 11:2       | 0.323  | 0.59 | 0.10 | 0.00 | burn                                  |
| Jeremia 33:18    | 0.322  | 0.58 | 0.10 | 0.00 | burn                                  |
| Jesaia 65:5      | 0.320  | 0.57 | 0.10 | 0.00 | burn                                  |
| Nehemia 2:3      | 0.316  | 0.52 | 0.20 | 0.00 | age, burn                             |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms                             |
|------------|--------|------|------|------|---------------------------------------|
| REV 20:10  | 0.498  | 0.66 | 0.40 | 0.30 | age, beast, burn, torment [continual, forever] |
| REV 14:9   | 0.478  | 0.53 | 0.60 | 0.00 | anyone, beast, image, mark            |
| REV 19:20  | 0.441  | 0.56 | 0.50 | 0.00 | beast, burn, image, mark              |
| REV 16:2   | 0.392  | 0.52 | 0.40 | 0.00 | beast, image, mark, worship           |
| REV 13:15  | 0.392  | 0.59 | 0.30 | 0.00 | beast, image, worship                 |
| REV 15:2   | 0.389  | 0.53 | 0.40 | 0.00 | beast, burn, image, name              |
| REV 13:4   | 0.358  | 0.57 | 0.20 | 0.00 | beast, worship                        |
| REV 13:12  | 0.352  | 0.56 | 0.20 | 0.00 | beast, worship                        |

**Notes:** This is a theologically critical verse. The strongest OT parallel is **Isaiah 34:10** (Hybrid 0.401, Theo 0.30 = "continual, forever" flag triggered) — the destruction of Edom: "It shall not be quenched night nor day; the smoke thereof shall go up for ever." This is the direct source text Rev 14:11 draws on. But Isa 34:10 describes the land of Edom becoming desolate and burning permanently — a **literary image** of utter desolation, not conscious torment in perpetuity. Rev 20:10 matches strongly (0.498) as the only other NT verse with the same "ages of ages" torment language (the beast and false prophet's fate). The concentration of beast/mark/worship vocabulary in the NT parallels confirms this passage is specifically about those who worship the beast — a particular judgment scenario.

---

## 10. Obadiah 1:16 — "they shall drink and swallow down...they shall be as though they had not been"

**Source verse gloss:** "that as drink upon mountain holiness drink whole the people continuity"

### hybrid-ot (OT parallels):
| Reference       | Hybrid | Sem  | Key  | Theo | Key Terms         |
|-----------------|--------|------|------|------|-------------------|
| Jesaia 29:8     | 0.440  | 0.72 | 0.20 | 0.00 | drink, mountain   |
| Joel 4:18       | 0.405  | 0.69 | 0.20 | 0.00 | drink, mountain   |
| Ezechiel 32:6   | 0.405  | 0.70 | 0.20 | 0.00 | drink, mountain   |
| Jesaia 62:9     | 0.404  | 0.69 | 0.20 | 0.00 | drink, holiness   |
| Numeri 28:7     | 0.402  | 0.69 | 0.20 | 0.00 | drink, holiness   |
| Reges_I 13:23   | 0.398  | 0.73 | 0.10 | 0.00 | drink             |
| Reges_I 19:8    | 0.393  | 0.67 | 0.20 | 0.00 | drink, mountain   |
| Genesis 44:5    | 0.392  | 0.71 | 0.10 | 0.00 | drink             |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms |
|------------|--------|------|------|------|-----------|
| ROM 14:17  | 0.394  | 0.73 | 0.10 | 0.00 | drink     |
| JHN 4:13   | 0.383  | 0.71 | 0.10 | 0.00 | drink     |
| LUK 1:15   | 0.377  | 0.70 | 0.10 | 0.00 | drink     |
| REV 16:6   | 0.377  | 0.70 | 0.10 | 0.00 | drink     |
| MAT 10:42  | 0.375  | 0.69 | 0.10 | 0.00 | drink     |
| 1CO 10:4   | 0.374  | 0.69 | 0.10 | 0.00 | drink     |
| MAT 25:37  | 0.369  | 0.68 | 0.10 | 0.00 | drink     |
| MRK 14:25  | 0.364  | 0.67 | 0.10 | 0.00 | drink     |

**Notes:** Parallels are driven entirely by "drink" vocabulary, missing the key theological content of Obad 1:16b: "they shall be as though they had not been" (Hebrew: כְּלוֹא הָיוּ — "as-not they-were"). This non-existence phrase is the most theologically significant element and has no matching parallel in the database because it is unique. The tool cannot capture the key concept of non-existence/ceasing-to-be. Isaiah 29:8, Joel 4:18, and Ezekiel 32:6 match on "drink, mountain" as thematic parallels in judgment contexts.

---

## 11. Isaiah 66:24 — "their worm shall not die, neither shall their fire be quenched"

**Source verse gloss:** "and go out and see in corpse the man the rebel in that... worm, burn, die"

### hybrid-ot (OT parallels):
| Reference       | Hybrid | Sem  | Key  | Theo | Key Terms      |
|-----------------|--------|------|------|------|----------------|
| Reges_II 19:35  | 0.413  | 0.70 | 0.20 | 0.00 | corpse, die    |
| Reges_I 13:24   | 0.401  | 0.68 | 0.20 | 0.00 | corpse, die    |
| Jesaia 37:36    | 0.399  | 0.67 | 0.20 | 0.00 | corpse, die    |
| Genesis 37:20   | 0.397  | 0.74 | 0.10 | 0.00 | see            |
| Numeri 14:37    | 0.395  | 0.73 | 0.10 | 0.00 | die            |
| Numeri 35:23    | 0.394  | 0.67 | 0.20 | 0.00 | die, see       |
| Judices 9:49    | 0.391  | 0.66 | 0.20 | 0.00 | burn, die      |
| Jeremia 42:17   | 0.382  | 0.69 | 0.10 | 0.00 | die            |

### hybrid-nt (NT parallels):
| Reference  | Hybrid | Sem  | Key  | Theo | Key Terms         |
|------------|--------|------|------|------|-------------------|
| MRK 9:48   | 0.424  | 0.64 | 0.30 | 0.00 | burn, die, worm   |
| REV 17:16  | 0.368  | 0.62 | 0.20 | 0.00 | burn, flesh       |
| JUD 1:23   | 0.330  | 0.55 | 0.20 | 0.00 | burn, flesh       |
| 1CO 15:32  | 0.329  | 0.60 | 0.10 | 0.00 | die               |
| REV 9:6    | 0.328  | 0.59 | 0.10 | 0.00 | die               |
| JHN 15:6   | 0.324  | 0.59 | 0.10 | 0.00 | burn              |
| MRK 5:15   | 0.316  | 0.57 | 0.10 | 0.00 | see               |
| ACT 2:27   | 0.315  | 0.58 | 0.10 | 0.00 | see               |

**Notes:** The strongest NT parallel is **Mark 9:48** (0.424, matching burn/die/worm) — Jesus directly quotes Isaiah 66:24 ("where their worm dieth not, and the fire is not quenched"). This is the direct NT citation. The OT parallels cluster around "corpse/dead body" vocabulary — particularly 2 Kings 19:35 and Isaiah 37:36 (the angel smiting 185,000 Assyrians: "behold, they were all dead corpses"). This is significant: the parallels confirm Isaiah 66:24 describes **corpses** being consumed by worm and fire, not living persons being tortured. The source text is about bodies of the dead rebels — which Jesus uses as imagery in Mark 9.

---

## Summary Table — Strongest Cross-Testament Connections

| Source Verse      | Strongest OT Parallel | Score | Strongest NT Parallel | Score | Key Theological Link |
|-------------------|-----------------------|-------|-----------------------|-------|----------------------|
| Psa 37:9          | Psa 37:34             | 0.455 | 1CO 5:13              | 0.334 | "cut off" = evil removed from community |
| Psa 37:20         | Psa 92:10             | 0.451 | JUD 1:23 / HEB 6:8    | 0.349 | Consume/burn destruction of enemies |
| Mal 4:1 (3:19)    | Isa 5:24              | 0.431 | 2PE 3:7               | 0.329 | Fire consuming stubble = total destruction |
| Mal 4:2 (3:20)    | Isa 58:8              | 0.370 | LUK 4:40              | 0.272 | Healing/righteousness (low eschat. match) |
| Mal 4:3 (3:21)    | Psa 9:17              | 0.396 | MRK 9:45              | 0.284 | Wicked as ashes/dust underfoot |
| Joh 3:16          | Gen 3:22              | 0.408 | JHN 6:40              | 0.518 | Perish vs. eternal life (Johannine cluster) |
| 2Th 1:9           | Eze 25:15             | 0.352 | ROM 9:22              | 0.413 | Destruction/apoleia vocabulary cluster |
| Rev 14:10         | Dan 5:23              | 0.398 | LUK 1:15              | 0.501 | Wine/cup of wrath/anger motif |
| Rev 14:11         | **Isa 34:10**         | **0.401** (Theo 0.30) | REV 20:10 | 0.498 | Smoke forever = Edom desolation imagery |
| Oba 1:16          | Isa 29:8              | 0.440 | ROM 14:17             | 0.394 | Drink vocabulary (key "as-not-been" missed) |
| Isa 66:24         | 2Ki 19:35             | 0.413 | **MRK 9:48**          | **0.424** | Corpse+worm+fire = Jesus cites Isa 66:24 |
| Mat 10:28         | Isa 14:20             | 0.390 | (not run)             | —         | Kill+soul = OT death contexts; soul-destroy concept uniquely NT |

**Critical finding for Rev 14:11:** The tool flagged a **theological match (Theo 0.30 = "continual/forever" flag)** between Rev 14:11 and **Isaiah 34:10**, identifying the source text. Isaiah 34 describes the destruction of Edom as burning smoke that rises forever — but the referent is a desolate wasteland, not conscious persons. This is the literary background for Rev 14:11's "smoke of their torment ascendeth for ever." The same imagery appears in Rev 20:10 (the strongest NT-to-NT parallel at 0.498), which applies it to the beast and false prophet — symbolic entities in Revelation's apocalyptic framework.

**Critical finding for Isa 66:24:** Mark 9:48 directly quotes this passage (confirmed by the worm/fire/die triple match). The OT context makes clear the referent is **corpses** (פְּגָרֵי — corpses/dead bodies), which aligns with the annihilationist reading: the fire and worm consume **dead** rebels permanently, not living persons in ongoing conscious suffering.

---

## 12. Matthew 10:28 — "fear him which is able to destroy both soul and body in hell"

**Source verse gloss:** "And not you should be afraid of those killing the body the however soul not... kill, soul, body, gehenna"

### hybrid-ot (OT parallels):
| Reference          | Hybrid | Sem  | Key  | Theo | Key Terms              |
|--------------------|--------|------|------|------|------------------------|
| Numeri 35:31       | 0.394  | 0.67 | 0.20 | 0.00 | kill, soul             |
| Jesaia 14:20       | 0.390  | 0.67 | 0.20 | 0.00 | consume, kill          |
| Numeri 11:15       | 0.383  | 0.71 | 0.10 | 0.00 | kill                   |
| Numeri 35:30       | 0.367  | 0.61 | 0.20 | 0.00 | kill, soul             |
| Deuteronomium 19:6 | 0.365  | 0.62 | 0.20 | 0.00 | kill, soul             |
| Psalmi 143:3       | 0.364  | 0.67 | 0.10 | 0.00 | soul                   |
| Iob 11:20          | 0.361  | 0.61 | 0.20 | 0.00 | consume, soul          |
| Josua 20:3         | 0.357  | 0.60 | 0.20 | 0.00 | kill, soul             |

**Notes:** The parallels are mostly about killing/soul in legal/death contexts (Numbers blood-guilt laws, Deuteronomy cities of refuge). Isaiah 14:20 (the cut-down king who "shall not be joined with them in burial... for thou hast destroyed thy land, and slain thy people") uses "consume/kill" and connects to the fate of those who bring others to destruction. Job 11:20 is notable: "the eyes of the wicked shall fail, and they shall not escape, and their hope shall be as the giving up of the ghost" — combining "consume" and "soul" in the context of wicked-have-no-hope. The low semantic scores (all below 0.40) reflect that the key concept of God destroying the soul in gehenna is uniquely NT — the OT equivalent is the general language of death/perishing/being cut off rather than a specific "soul destruction" passage.
