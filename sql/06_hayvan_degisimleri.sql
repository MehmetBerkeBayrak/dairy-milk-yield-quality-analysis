SELECT * FROM public.hayvan_degisimleri ORDER BY genetik_grup,hayvan_id;
SELECT genetik_grup,COUNT(*) AS hayvan_sayisi,
 COUNT(*) FILTER(WHERE sut_kaybi_yuzde>0) AS sutu_azalan,
 COUNT(*) FILTER(WHERE hucre_artisi_yuzde>0) AS hucresi_artan,
 ROUND(AVG(sut_kaybi_yuzde),2) AS ortalama_sut_kaybi,
 ROUND(STDDEV_SAMP(sut_kaybi_yuzde),2) AS sut_kaybi_std_yuzde_puan,
 ROUND(AVG(hucre_artisi_yuzde),2) AS ortalama_hucre_artisi,
 ROUND(STDDEV_SAMP(hucre_artisi_yuzde),2) AS hucre_artisi_std_yuzde_puan
FROM public.hayvan_degisimleri GROUP BY genetik_grup ORDER BY genetik_grup;
