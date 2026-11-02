# Araştırma notları ve bulgular

## Çerçeve
Araştırmaya genetik grupları tanıyarak başladım. İlk “saflık” ifademi daha dikkatli bir adlandırmayla “kaynakta kayıtlı HF oranı / genetik grup” olarak düzelttim. Local grubunun belirli bir yerel ırk veya genetik olarak doğrulanmış sıfır HF taşıdığı çıkarımını yapmıyorum.

750 satır, 50 hayvanın T0/T1/T2 koşullarındaki beşer tekrarıdır. Replication No bağımsız bir hayvan değildir. Hayvan kimliğiyle eşleştirme yaptım; aynı tekrar numarasını farklı T koşulları arasında aynı gün olarak kabul etmedim.

## Veri kontrolü ve SQL'e geçiş
Python ile Excel'i okuyup başlıkları ve tekrar sayılarını kontrol ettim. PostgreSQL ham tablosunda sütunlar metin olarak tutuldu. TRIM, ondalık ayırıcı dönüşümü ve NUMERIC kullanarak hesaplamaya uygun alanlar oluşturdum. Ham veri korunur.

Beşer ölçümü hayvan-koşul düzeyinde özetledim (150 satır); ardından grup-koşul düzeyinde 15 satıra indirdim. Araştırmanın temel bağımsız birimi hayvandır; grup başına 10 hayvan vardır.

## Süt ve bileşim
T0'dan T2'ye bütün grupların ortalama süt miktarı düştü. Grup ortalamalarının oransal süt kayıpları Local %47,89; HF50 %19,60; HF62.5 %15,78; HF75 %15,12; HF87.5 %8,65 idi.

Yağ yüzdesi T0'dan T1'e bütün gruplarda arttı, T2'de T0 altına düştü. Protein T1'de sınırlı değişirken T2'de bütün gruplarda T0'dan düşüktü. Hücre sayısı bütün gruplarda T0→T1→T2 boyunca arttı.

HF87.5 grubunda hücre artışının oransal olarak düşük olması düşük mutlak hücre düzeyi anlamına gelmiyordu: grup T0'da 229.180, T2'de 306.080 hücre/mL ile en yüksek ortalamaya sahipti. Local %57,47 grup ortalaması artışına rağmen T2'de 220.580 hücre/mL ile en düşük gruptu.

## Süt miktarıyla birlikte bileşim
Her gözlemde süt L/gün × bileşen yüzdesi / 100 hesapladım; sonra hayvan ve grup ortalamalarını aldım. Ortalama süt ile ortalama yüzdeyi çarpmadım. Sonuçlar kesin gram/gün değildir.

Protein göstergesi T0–T2 kayıpları: Local %49,25; HF50 %22,23; HF62.5 %18,18; HF75 %18,08; HF87.5 %10,98.
Yağ göstergesi T0–T1 kayıpları: Local %18,44; HF50 %6,30; HF62.5 %3,86; HF75 %0,99; HF87.5 %0,46. T1 yağ yüzdesi artışı süt azalmasını tamamen karşılamadı.
Yağ göstergesi T0–T2 kayıpları: Local %51,48; HF50 %25,68; HF62.5 %21,33; HF75 %21,95; HF87.5 %15,34. Düzenli HF sıralaması her göstergede oluşmadı.

## Bireysel değişim
50 hayvanın tamamında süt düştü ve hücre sayısı arttı. Bireysel süt kayıplarının ortalaması Local %45,78; HF50 %19,51; HF62.5 %15,73; HF75 %15,01; HF87.5 %8,54 idi. Bu rakamlar grup ortalamalarının yüzde değişiminden farklı tanımlıdır.
Local grubunda süt kaybının standart sapması 18,24 yüzde puan, HF gruplarında 4,04–4,42 yüzde puandı. Local grubundaki hayvanların hepsine tek bir tipik kayıp atamak doğru olmaz.

## Korelasyon ve kaynak kontrolü
Grup içi Pearson r: HF50 0,528; HF62.5 0,492; HF75 -0,003; HF87.5 0,149; Local 0,177. Grup başına n=10. Anlamlılık ya da korelasyonlar arası fark testi yapılmadı. Sıfıra yakın Pearson her türlü ilişkinin yokluğunu kanıtlamaz.

104 numaralı Local hayvanın süt ortalaması 1,302→1,220 L/gün (%6,30 kayıp), hücre ortalaması 134.000→207.600 hücre/mL (%54,93 artış). T2 süt değerleri 0,72–1,94 arasında değişiyordu. 1,94 değerini yalnızca yüksek olduğu için silmedim. Bu kaynak kontrolü kaydın doğruluğunu dış laboratuvar düzeyinde kanıtlamaz, fakat grafiğin ham tabloyla uyumlu olduğunu gösterir. Kullanıcının tercihiyle medyan duyarlılık incelemesine devam edilmedi.

## Power BI öğrenimi
CSV'de ondalık noktalar Türkçe yerel ayarda yanlış yorumlandığında eksenler 10^17 ölçeğine çıkmıştı. İngilizce (ABD) yerel ayarıyla ondalık sayı dönüşümü sorunu düzeltti. hayvan_id nokta kimliği, genetik_grup açıklama, X hücre artışı, Y süt kaybı olarak ayarlandı. Kimlik eklendiğinde X/Y Ortalama seçildi; her hayvana tek satır olduğundan değerler değişmedi.

## Sonuçların kapsamı
Genetik grup veya THI koşullarına nedensellik atanmıyor. Mevsim, hayvan özellikleri ve yönetim gibi etkenler modellenmedi. Çalışmanın kaynağı ve eşik açıklamaları DATA_SOURCE.md içinde; eşik sınırları analizde yeniden tanımlanmadı. Klinik değerlendirme ve tek bir süt kalite puanı üretilmedi.
