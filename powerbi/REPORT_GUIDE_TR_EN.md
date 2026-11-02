# Power BI raporu / report

## Delivered / Teslim edilen
- Original.pbix: user-supplied original, unchanged.
- Tasarim.pbix: externally edited report-definition draft. Embedded model preserved byte-for-byte. Three pages: group comparison, individual scatter, methods.
- Critical limitation / Önemli sınır: Native Power BI Desktop open, rendering and interaction tests could not run because the desktop control tool returned no windows. This is NOT a fully verified final dashboard.
- Structural checks: ZIP integrity, JSON parse, visual bounds/non-overlap, embedded-model equality; see reports/pbix_structure_validation.json.

## Wider report plan / Geniş rapor planı
1. Overview / Genel bakış: import grup_ozeti.csv (15 rows). Use THI group on X, average milk L/day on Y, genetic group as legend. Separate chart for each composition metric; never combine SCC and percentages on one undifferentiated scale.
2. Composition / Bileşim: fat and protein percentages by condition and group; cell counts in a separate visual. Import bilesim_gostergeleri.csv for volume-composition proxies. Explain they are not exact mass yields.
3. Individual scatter / Bireysel ilişki: hayvan_degisimleri.csv; X=hucre_artisi_yuzde (Average), Y=sut_kaybi_yuzde (Average), category/values=hayvan_id, legend=genetik_grup. One record per animal, so Average preserves individual values. Keep fixed X=0–80 and Y=0–70 when comparing filters.
4. Methods / Yöntem: distinguish mean individual changes from changes in group means. Correlation table is a documented SQL snapshot, not a filter-reactive measure.

## Review checklist / Kontrol
- 50 scatter points overall, 10 per genetic group.
- HF50: milk loss 12.74–26.68%, SCC increase 40.56–66.08% (rounded).
- Local animal 104: milk loss 6.30%, SCC increase 54.93%.
- No Percentage formatting that multiplies values by 100.
- No pooled trend claimed as within-group correlation.
- No THI causal/clinical/purity rankings.
- Save source path updates, test filters, then export report screenshots/PDF from Desktop.

Suggested palette: teal #00897B, blue #3974CB, ochre #D38B25, purple #8B5CB8, rose #C7557A. Page background #F3F5F9, text #172B4D, white panels.
