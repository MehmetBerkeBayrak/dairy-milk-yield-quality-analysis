SELECT COUNT(*) AS satir, COUNT(DISTINCT hayvan_id) AS hayvan FROM public.sut_analiz;
SELECT hayvan_id, genetik_grup, thi_grubu, COUNT(*) AS n
FROM public.sut_analiz GROUP BY 1,2,3 HAVING COUNT(*)<>5;
SELECT hayvan_id, genetik_grup, thi_grubu, tekrar_no, COUNT(*)
FROM public.sut_analiz GROUP BY 1,2,3,4 HAVING COUNT(*)>1;
SELECT COUNT(*) FILTER (WHERE sut_litre_gun IS NULL) AS bos_sut,
 COUNT(*) FILTER (WHERE yag_yuzde IS NULL) AS bos_yag,
 COUNT(*) FILTER (WHERE protein_yuzde IS NULL) AS bos_protein,
 COUNT(*) FILTER (WHERE somatik_hucre_ml IS NULL) AS bos_hucre,
 COUNT(*) FILTER (WHERE sut_litre_gun<0 OR somatik_hucre_ml<0) AS negatif
FROM public.sut_analiz;
