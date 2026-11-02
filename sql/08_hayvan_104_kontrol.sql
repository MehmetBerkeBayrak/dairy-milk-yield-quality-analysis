SELECT hayvan_id,genetik_grup,thi_grubu,tekrar_no,sut_litre_gun,somatik_hucre_ml
FROM public.sut_analiz WHERE hayvan_id='104' AND thi_grubu IN ('T0','T2')
ORDER BY thi_grubu,tekrar_no;
-- An unusual point is reviewed, not automatically removed.
