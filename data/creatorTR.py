import os

# Hedef klasör
corpus_dir = os.path.join("data", "corpus")

# Klasör yoksa oluştur
if not os.path.exists(corpus_dir):
    os.makedirs(corpus_dir)
    print(f"📁 Klasör oluşturuldu: {corpus_dir}")

# Test Verileri (Türkçe - NLP Test Senaryoları)
test_data = {
    # 1. Temel anahtar kelime testi
    "doc1.txt": "Python, veri bilimi ve yapay zeka için harika bir programlama dilidir.",
    
    # 2. Eş anlamlılar ve alan testi
    "doc2.txt": "Yapay Zeka; makine öğrenmesi ve derin öğrenme gibi alt alanları içerir.",
    
    # 3. Teknik terimler
    "doc3.txt": "Veri yapıları ve algoritmalar, yazılım mühendisliğinin temel taşıdır.",
    
    # 4. Proje bağlamı (Vectoria vb. için)
    "doc4.txt": "Python ile bir arama motoru geliştirmek zorlu ama ödüllendirici bir süreçtir.",
    
    # 5. MORFOLOJİ VE GÖVDELEME TESTİ (Stemming/Lemmatization):
    # Türkçe sondan eklemeli bir dildir. Stemmer bu kelimeleri köküne indirebiliyor mu?
    # 'Kitaplıklarındaki' -> 'Kitap', 'Koşuyorlardı' -> 'Koş', 'Gözlükçü' -> 'Göz'/'Gözlük'
    "doc5.txt": "Kitaplıklarındaki kitapları okuyan çocuklar parkta koşuyorlardı.", 
    
    # 6. STOP-WORD (Etkisiz Kelime) TESTİ:
    # Bu dosya 'preprocessing' işleminden sonra tamamen BOŞ veya çok az kelime kalmalı.
    "doc6.txt": "ve ile veya ama fakat ancak lakin çünkü gibi için de da ki mi mu mü", 
}

# Dosyaları yaz
for filename, content in test_data.items():
    filepath = os.path.join(corpus_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Oluşturuldu (TR): {filename}")

print("\n🚀 Türkçe test verileri hazır! Preprocessing kodunu çalıştırabilirsin.")