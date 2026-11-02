-- TR: Boş bir PostgreSQL veritabanında çalıştırın. Ham kayıtları silmez.
-- EN: Run in an empty PostgreSQL database. Does not delete raw records.
CREATE TABLE IF NOT EXISTS public.sut_ham (
 hayvan_id TEXT, genetik_grup TEXT, thi_grubu TEXT, tekrar_no TEXT,
 kuru_madde_kg TEXT, sut_litre_gun TEXT, somatik_hucre_ml TEXT,
 yag_yuzde TEXT, yagsiz_kuru_madde_yuzde TEXT, protein_yuzde TEXT,
 tuz_yuzde TEXT, laktoz_yuzde TEXT, ph TEXT
);
-- Import data/processed/sut_verisi.csv with client-side psql \copy.
-- See docs/REPRODUCE_EN.md and docs/YENIDEN_CALISTIRMA_TR.md.
