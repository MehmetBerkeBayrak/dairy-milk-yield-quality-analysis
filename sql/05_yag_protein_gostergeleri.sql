-- Volume-composition proxies, not exact mass yields.
SELECT a.genetik_grup,
 ROUND(a.yag_gostergesi,4) AS yag_t0,ROUND(b.yag_gostergesi,4) AS yag_t1,ROUND(c.yag_gostergesi,4) AS yag_t2,
 ROUND(100*(b.yag_gostergesi-a.yag_gostergesi)/NULLIF(a.yag_gostergesi,0),2) AS yag_t0_t1_degisim_yuzde,
 ROUND(100*(c.yag_gostergesi-a.yag_gostergesi)/NULLIF(a.yag_gostergesi,0),2) AS yag_t0_t2_degisim_yuzde,
 ROUND(a.protein_gostergesi,4) AS protein_t0,ROUND(b.protein_gostergesi,4) AS protein_t1,ROUND(c.protein_gostergesi,4) AS protein_t2,
 ROUND(100*(c.protein_gostergesi-a.protein_gostergesi)/NULLIF(a.protein_gostergesi,0),2) AS protein_t0_t2_degisim_yuzde
FROM public.grup_ortalamalari a
JOIN public.grup_ortalamalari b ON a.genetik_grup=b.genetik_grup AND b.thi_grubu='T1'
JOIN public.grup_ortalamalari c ON a.genetik_grup=c.genetik_grup AND c.thi_grubu='T2'
WHERE a.thi_grubu='T0' ORDER BY 1;
