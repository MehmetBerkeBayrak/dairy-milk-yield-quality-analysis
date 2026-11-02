-- Group-mean percentage changes; not the mean of individual changes.
SELECT a.genetik_grup,
 ROUND(100*(b.sut_litre_gun-a.sut_litre_gun)/NULLIF(a.sut_litre_gun,0),2) AS sut_degisim_yuzde,
 ROUND(b.yag_yuzde-a.yag_yuzde,2) AS yag_degisim_yuzde_puan,
 ROUND(100*(b.protein_yuzde-a.protein_yuzde)/NULLIF(a.protein_yuzde,0),2) AS protein_degisim_yuzde,
 ROUND(100*(b.somatik_hucre_ml-a.somatik_hucre_ml)/NULLIF(a.somatik_hucre_ml,0),2) AS hucre_degisim_yuzde
FROM public.grup_ortalamalari a
JOIN public.grup_ortalamalari b ON a.genetik_grup=b.genetik_grup
WHERE a.thi_grubu='T0' AND b.thi_grubu='T2' ORDER BY 1;
