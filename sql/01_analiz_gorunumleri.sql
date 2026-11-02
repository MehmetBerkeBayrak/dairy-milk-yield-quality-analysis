CREATE OR REPLACE VIEW public.sut_analiz AS
SELECT
    TRIM(hayvan_id) AS hayvan_id,
    TRIM(genetik_grup) AS genetik_grup,
    TRIM(thi_grubu) AS thi_grubu,
    REPLACE(NULLIF(TRIM(tekrar_no), ''), ',', '.')::NUMERIC AS tekrar_no,
    REPLACE(NULLIF(TRIM(kuru_madde_kg), ''), ',', '.')::NUMERIC AS kuru_madde_kg,
    REPLACE(NULLIF(TRIM(sut_litre_gun), ''), ',', '.')::NUMERIC AS sut_litre_gun,
    REPLACE(NULLIF(TRIM(somatik_hucre_ml), ''), ',', '.')::NUMERIC AS somatik_hucre_ml,
    REPLACE(NULLIF(TRIM(yag_yuzde), ''), ',', '.')::NUMERIC AS yag_yuzde,
    REPLACE(NULLIF(TRIM(yagsiz_kuru_madde_yuzde), ''), ',', '.')::NUMERIC AS yagsiz_kuru_madde_yuzde,
    REPLACE(NULLIF(TRIM(protein_yuzde), ''), ',', '.')::NUMERIC AS protein_yuzde,
    REPLACE(NULLIF(TRIM(tuz_yuzde), ''), ',', '.')::NUMERIC AS tuz_yuzde,
    REPLACE(NULLIF(TRIM(laktoz_yuzde), ''), ',', '.')::NUMERIC AS laktoz_yuzde,
    REPLACE(NULLIF(TRIM(ph), ''), ',', '.')::NUMERIC AS ph
FROM public.sut_ham;


CREATE OR REPLACE VIEW public.hayvan_ortalamalari AS
SELECT hayvan_id, genetik_grup, thi_grubu, COUNT(*) AS olcum_sayisi,
 AVG(sut_litre_gun) AS sut_litre_gun,
 AVG(yag_yuzde) AS yag_yuzde,
 AVG(protein_yuzde) AS protein_yuzde,
 AVG(somatik_hucre_ml) AS somatik_hucre_ml,
 AVG(sut_litre_gun * yag_yuzde / 100) AS yag_gostergesi,
 AVG(sut_litre_gun * protein_yuzde / 100) AS protein_gostergesi
FROM public.sut_analiz
GROUP BY hayvan_id, genetik_grup, thi_grubu;

CREATE OR REPLACE VIEW public.grup_ortalamalari AS
SELECT genetik_grup, thi_grubu, COUNT(*) AS hayvan_sayisi,
 AVG(sut_litre_gun) AS sut_litre_gun,
 AVG(yag_yuzde) AS yag_yuzde,
 AVG(protein_yuzde) AS protein_yuzde,
 AVG(somatik_hucre_ml) AS somatik_hucre_ml,
 AVG(yag_gostergesi) AS yag_gostergesi,
 AVG(protein_gostergesi) AS protein_gostergesi
FROM public.hayvan_ortalamalari
GROUP BY genetik_grup, thi_grubu;

CREATE OR REPLACE VIEW public.hayvan_degisimleri AS
SELECT a.hayvan_id, a.genetik_grup,
 a.sut_litre_gun AS sut_t0, b.sut_litre_gun AS sut_t2,
 a.somatik_hucre_ml AS hucre_t0, b.somatik_hucre_ml AS hucre_t2,
 100 * (a.sut_litre_gun - b.sut_litre_gun) / NULLIF(a.sut_litre_gun,0) AS sut_kaybi_yuzde,
 100 * (b.somatik_hucre_ml-a.somatik_hucre_ml) / NULLIF(a.somatik_hucre_ml,0) AS hucre_artisi_yuzde
FROM public.hayvan_ortalamalari a
JOIN public.hayvan_ortalamalari b
 ON a.hayvan_id=b.hayvan_id AND a.genetik_grup=b.genetik_grup
WHERE a.thi_grubu='T0' AND b.thi_grubu='T2';
