# Veri sözlüğü / Data dictionary

| CSV / SQL | Workbook column | Birim / Unit |
|---|---|---|
| hayvan_id | Animal ID | Identifier, text; not a measure |
| genetik_grup | Genetic Group | Local, HF50, HF62.5, HF75, HF87.5 |
| thi_grubu | THI Range | T0, T1, T2; categorical |
| tekrar_no | Replication No | Repeated observation index; not a new animal |
| kuru_madde_kg | DMI (kg) | kg |
| sut_litre_gun | Milk Yield (L/day/cow) | L/day/cow |
| somatik_hucre_ml | SCC cells per mL | cells/mL |
| yag_yuzde | Fat% | % |
| yagsiz_kuru_madde_yuzde | SNF% | % |
| protein_yuzde | Protein % | % |
| tuz_yuzde | Salt% | % |
| laktoz_yuzde | Lactose% | % |
| ph | pH | pH |

## Derived variables / Türetilmiş değişkenler
- sut_kaybi_yuzde = 100 × (T0 milk − T2 milk) / T0 milk. Positive means loss / Pozitif kayıp demektir.
- hucre_artisi_yuzde = 100 × (T2 SCC − T0 SCC) / T0 SCC.
- yag_gostergesi = milk L/day × fat % / 100, computed per observation before averaging.
- protein_gostergesi = milk L/day × protein % / 100, computed per observation before averaging.
- The two proxies are not grams/day or verified mass yields. Relative interpretation assumes equal milk density across compared conditions.
- Standart sapma / standard deviation of percentage changes is in percentage points.
- genetik_grup is a recorded ancestry category, not a measured purity certificate. Local is retained as labelled; no specific local breed or verified 0% ancestry is inferred.
