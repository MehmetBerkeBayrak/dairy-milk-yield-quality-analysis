# Methods and findings

## Design and units
The workbook contains 750 repeated observations from 50 cows: five observations within each of three THI categories. The five recorded genetic groups contain ten cows each. Replication No is not a new animal and matching replication numbers across THI categories was not assumed to identify a common sampling day. HF labels are source ancestry categories, not independently verified genetic-purity measurements.

## Preparation
The raw workbook is preserved. Python validates schema, missingness, repeat counts and measurement identities. PostgreSQL keeps a text raw table and converts numeric fields inside analysis views. Five observations are averaged within animal × condition (150 rows), followed by equal-weight animal averages within group × condition (15 rows).

## Group summaries
From T0 to T2, milk volume fell in all groups. Percentage losses calculated from group means were Local 47.89%, HF50 19.60%, HF62.5 15.78%, HF75 15.12%, and HF87.5 8.65%.
Fat percentage rose at T1 but fell below T0 at T2 in every group. Protein changed little at T1 and was lower at T2 in all groups. SCC rose across T0/T1/T2 in all groups.
HF87.5 had the smallest proportional group-mean SCC increase but the highest absolute mean SCC: 229,180 at T0 and 306,080 cells/mL at T2. Local had a 57.47% group-mean SCC increase but the lowest T2 mean, 220,580 cells/mL. Relative change and absolute level must be distinguished.

## Volume–composition proxies
Milk L/day × component % / 100 was calculated per observation before averaging; products of separate group averages were not used. These proxies are not exact mass yields. Relative interpretation assumes equal milk density.
Protein-proxy T0–T2 losses: Local 49.25%, HF50 22.23%, HF62.5 18.18%, HF75 18.08%, HF87.5 10.98%.
Fat-proxy T0–T1 losses: Local 18.44%, HF50 6.30%, HF62.5 3.86%, HF75 0.99%, HF87.5 0.46%. Thus higher T1 fat percentage did not fully offset lower milk volume at group-average level.
Fat-proxy T0–T2 losses: Local 51.48%, HF50 25.68%, HF62.5 21.33%, HF75 21.95%, HF87.5 15.34%. Not every outcome followed a monotonic HF ordering.

## Individual changes
All 50 animals had lower mean milk yield and higher SCC at T2. Mean individual milk losses: Local 45.78%, HF50 19.51%, HF62.5 15.73%, HF75 15.01%, HF87.5 8.54%. These differ from percentage changes in group means.
The standard deviation of individual milk loss was 18.24 percentage points in Local versus 4.04–4.42 in the HF groups.

## Correlation and point review
Within-group Pearson r: HF50 0.528, HF62.5 0.492, HF75 -0.003, HF87.5 0.149, Local 0.177; n=10 per group. No significance tests, uncertainty intervals or tests of correlation differences were performed. Near-zero Pearson correlation does not exclude nonlinear associations.
Animal 104 had mean milk 1.302→1.220 L/day (6.30% loss) and SCC 134,000→207,600 cells/mL (54.93% increase). T2 milk ranged from 0.72 to 1.94 L/day. The high observation was retained rather than removed merely because it was unusual. A median-sensitivity analysis was deliberately not pursued at the user's request.

## Power BI lessons and delivery status
A decimal-locale error initially produced axes around 10^17. Parsing dot decimals with English (United States) locale corrected the values. IDs identify points; X/Y use Average, which preserves values because each animal has one change row. The delivered wider report remains a design draft pending Desktop opening/render/filter tests; composition pages were not implemented inside PBIX.

## Limits
The study is descriptive and exploratory. It does not establish causal THI/genetic effects, clinical diagnoses or a single overall milk-quality ranking. Seasonal/management factors and animal covariates were not modelled. See DATA_SOURCE.md for attribution and categorical THI limitations.
