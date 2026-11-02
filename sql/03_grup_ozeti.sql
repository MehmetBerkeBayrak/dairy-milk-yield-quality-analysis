SELECT genetik_grup,thi_grubu,hayvan_sayisi,
 ROUND(sut_litre_gun,2) AS ortalama_sut_litre_gun,
 ROUND(yag_yuzde,2) AS ortalama_yag_yuzde,
 ROUND(protein_yuzde,2) AS ortalama_protein_yuzde,
 ROUND(somatik_hucre_ml,0) AS ortalama_somatik_hucre_ml
FROM public.grup_ortalamalari ORDER BY genetik_grup,thi_grubu;
