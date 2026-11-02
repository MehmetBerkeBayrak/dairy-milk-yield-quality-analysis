SELECT genetik_grup,COUNT(*) AS hayvan_sayisi,
 ROUND(CORR(sut_kaybi_yuzde::DOUBLE PRECISION,hucre_artisi_yuzde::DOUBLE PRECISION)::NUMERIC,3) AS pearson_r
FROM public.hayvan_degisimleri
WHERE sut_kaybi_yuzde IS NOT NULL AND hucre_artisi_yuzde IS NOT NULL
GROUP BY genetik_grup ORDER BY genetik_grup;
