Harika bir `README.md` dosyası, projenin profesyonel görünmesi ve başkalarının (veya senin) projeyi anlaması için olmazsa olmazdır. GitHub'daki deponun ana sayfasında doğrudan gözükecek şekilde şu içeriği kullanabilirsin:

---

### `README.md`

```markdown
# Vectoria Pro - Yerel Arama Motoru

Vectoria Pro, bilgisayarınızdaki metin dosyalarını (.txt, .md, .py vb.) otomatik olarak indeksleyen ve **TF-IDF (Term Frequency-Inverse Document Frequency)** algoritmasını kullanarak sorgularınıza en alakalı sonuçları getiren yerel bir arama motorudur.

## 🚀 Özellikler
- **Yerel Veri Toplama:** Kendi verinizi oluşturun veya Wikipedia'dan gerçek içerikler çekin.
- **Akıllı İndeksleme:** Metinleri temizler (stop-words temizliği), tokenize eder ve skorlar.
- **TF-IDF Sıralama:** Arama sonuçlarını alaka düzeyine göre yüksekten düşüğe otomatik sıralar.
- **Modern Arayüz:** `CustomTkinter` ile hazırlanmış karanlık mod destekli şık bir arayüz.
- **Çoklu Format Desteği:** .txt, .md, .py ve daha fazla dosya türünü destekler.

## 🛠 Kurulum

1. **Depoyu Klonlayın:**
   ```bash
   git clone [https://github.com/kerim-aslan/Vectoriapy.git](https://github.com/kerim-aslan/Vectoriapy.git)
   cd Vectoriapy
   

```

2. **Gerekli Kütüphaneleri Yükleyin:**
```bash
pip install -r requirements.txt

```


2. **Arayüzü Başlatın:**
```bash
python gui.py

```


3. **İndeksleme:**
Arayüz açıldığında "📁 Klasör Seç ve İndeksle" butonuna basın ve verilerinizin bulunduğu klasörü seçin. İndeksleme tamamlandıktan sonra arama çubuğunu kullanmaya başlayabilirsiniz.

## 🔍 Teknik Detaylar

* **Preprocessing:** NLTK kütüphanesi ile Türkçe stop-word temizliği ve tokenization.
* **Ranking:** TF-IDF algoritması ile terim ağırlıklandırma.
* **UI:** CustomTkinter ile modern masaüstü deneyimi.

## ⚖️ Lisans

Bu projedeki veri setleri Wikipedia (tr.wikipedia.org) kaynağından alınmıştır. İçerik **CC BY-SA 4.0** lisansı ile sunulmaktadır.

*Proje, Kerim Aslan tarafından geliştirilmiştir.*

```

