# Yeniden çalıştırma

## Python
Proje kökünde PowerShell açın. Komutları ayrı satırlarda çalıştırın:
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/analyze.py
```
Bu işlem ham Excel'den tüm CSV, SVG ve doğrulama sonuçlarını üretir. Excel'i değiştirmez. İlk doğrulama için kullanılan sürümler requirements-validated.txt içindedir.

## PostgreSQL
1. pgAdmin'de boş bir veritabanı oluşturun; 00_tablo_yapisi.sql dosyasını çalıştırın.
2. psql içinde aşağıdaki komutu tek satırda çalıştırın. DOSYA_YOLU yerine kendi proje kökünüzü ve ileri eğik çizgileri kullanın. Bu psql komutudur; pgAdmin Query Tool içinde çalışmaz.
```text
\copy public.sut_ham FROM 'DOSYA_YOLU/data/processed/sut_verisi.csv' WITH (FORMAT CSV, HEADER TRUE, ENCODING 'UTF8');
```
3. İçe aktarmayı aynı tabloya tekrar çalıştırmayın; ham kopyalar eklenir. Mevcut dolu sut_ham tablonuz varsa tekrar yüklemek yerine sayıyı kontrol edin.
4. 01_analiz_gorunumleri.sql ardından 02–08 sorgularını çalıştırın.
5. Beklenen: ham 750, hayvan ortalamaları 150, grup ortalamaları 15, eşleştirilmiş hayvan 50 satır.

## Power BI
- powerbi/ klasöründeki tasarım kopyası yalnızca hayvan_degisimleri modelini korur. Power BI Desktop içinde açılış/render testi yapılmamıştır; taslak olarak teslim edilmiştir.
- Yağ/protein ve genel bakış için data/processed/grup_ozeti.csv, grup_degisimleri.csv ve bilesim_gostergeleri.csv dosyalarını Metin/CSV yoluyla yükleyin.
- CSV kodlaması UTF-8, ayırıcı virgül, ondalık ayırıcı noktadır. Türkçe yerel ayarda sayıları İngilizce (ABD) yerel ayarıyla dönüştürün.
- hayvan_id ve genetik_grup metin; sayısal alanlar ondalık sayı olmalı. Yüzde değişim alanları 52.02 gibi yüzde ölçeğindedir; Percentage veri türüne dönüştürmeyin.
- Orijinal PBIX kişisel eski CSV yolu içerebilir. Yenilemeden önce Veri kaynağı ayarlarından kaynağı yerel hayvan_degisimleri.csv olarak değiştirin.
- Ayrıntılı rapor planı: powerbi/REPORT_GUIDE_TR_EN.md.
