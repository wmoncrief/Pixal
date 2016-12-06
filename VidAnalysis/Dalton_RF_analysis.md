## Initial Analysis

#### Genre Classifiers by Themselves (all train, only that genre in test)
- 0 - Country - .29
- 1 - Rock - .90 (*)
- 2 - EDM - .91 (*)
- 3 - Rap - .59
- 4 - Pop - .44

#### Metadata Analysis
- Country is good
- Calls Rock vids EDM
- Calls EDM vids Rock
- Calls half Rap vids Rap, other half calls Pop
- Pop is good

#### Colors Analysis
- Country is good
- Rock is good
- Calls EDM vids Country
- Calls Rap vids Country
- Calls Pop vids Rap

#### Full Analysis (Metadata + Colors)
- Country is good
- Calls Rock vids EDM
- Calls EDM vids Country
- Calls half Rap vids Country, other half calls Pop
- Pop is good

### Genre Breakdown - Country
- Poor by itself
- Good in group
- Strong in: Meta, color, full

### Genre Breakdown - Rock
- Great by itself
- Mixes with EDM in group
- Strong in: Color

### Genre Breakdown - EDM
- Great by itself
- Mixed with Rock, Country in group
- Strong in: None

### Genre Breakdown - Rap
- Okay by itself
- Mixes with Country, Pop in group
- Strong in: None

### Genre Breakdown - Pop
- Okay by itself
- Good in group, mixes with Rap
- Strong in: Meta, full
