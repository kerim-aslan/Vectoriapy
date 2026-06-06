import os

# Hedef klasör
corpus_dir = os.path.join("data", "corpus")

# Klasör yoksa oluştur
if not os.path.exists(corpus_dir):
    os.makedirs(corpus_dir)
    print(f"📁 Klasör oluşturuldu: {corpus_dir}")

# Test Verileri (İngilizce - NLP Test Senaryoları)
test_data = {
    # Temel anahtar kelime testi
    "doc1.txt": "Python is a great programming language for data science and artificial intelligence.",
    
    # Eş anlamlılar ve terim testi
    "doc2.txt": "Artificial Intelligence includes fields like machine learning and deep learning.",
    
    # Teknik terimler
    "doc3.txt": "Data structures and algorithms are the foundation of software engineering.",
    
    # Proje bağlamı
    "doc4.txt": "Building a search engine with Python is a challenging but rewarding process.",
    
    # MORFOLOJİ TESTİ: (Lemmatization için kritik)
    # 'wolves' -> 'wolf', 'running' -> 'run', 'faster' -> 'fast' dönüşüyor mu bakmak için.
    "doc5.txt": "The wolves are running faster than the dogs in the forest.", 
    
    # STOP-WORD TESTİ:
    # Bu dosyanın ön işlemeden sonra tamamen BOŞ kalması gerekir.
    "doc6.txt": "the and is are of with but because however a an", 
}

# Dosyaları yaz
for filename, content in test_data.items():
    filepath = os.path.join(corpus_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Oluşturuldu (EN): {filename}")

print("\n🚀 İngilizce test verileri hazır! Preprocessing kodunu çalıştırabilirsin.")