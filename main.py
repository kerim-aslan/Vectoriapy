# main.py
import os 
import sys
from pathlib import Path

# Kütüphaneleri yükle
try:
    from src.indexer import InvertedIndex
    from src.preprocessing import ensure_nltk_resources, mining_text
    from src.query_engine import QueryEngine
except ImportError as e:
    print("HATA: Kütüphaneler yüklenemedi. 'src' klasörünün varlığından emin olun.")
    print(f"Hata detayı: {e}")
    sys.exit(1)

def main():
    # 1. Kaynak Kontrolü
    ensure_nltk_resources()
    
    # 2. İndeks Deposunu Başlat
    index = InvertedIndex()
    
    # 3. Veri Klasörü
    data_folder = Path("Vectoria")
    if not data_folder.exists():
        print(f"HATA: '{data_folder}' klasörü bulunamadı.")
        return

    print("--- Dokümanlar İndeksleniyor ---")
    
    file_map = {} 
    doc_id_counter = 1
    files = list(data_folder.glob("*.md"))

    # --- DÖNGÜ BAŞLIYOR ---
    for file_path in files:
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            tokens = mining_text(text)
            
            # BURASI ARTIK HEM KELİMELERİ HEM SAYILARINI KAYDEDİYOR
            index.add_document(doc_id_counter, tokens)
            
            file_map[doc_id_counter] = file_path.name
            doc_id_counter += 1
            
        except Exception as e:
            print(f"Hata ({file_path.name}): {e}")
    
    print(f"\nToplam {len(file_map)} dosya işlendi.")
   
    index.compute_idf()

  
    index.save_to_json("tf_idf_index.json")

   
    engine = QueryEngine(index) 

    print("-" * 30)
    print("ARAMA MOTORU HAZIR! (Çıkmak için 'q')")
    print("-" * 30)

    while True:
        query = input("\nArama yap: ")
        if query.lower() == 'q':
            break
            
        results = engine.search(query)
        
        if results:
            print(f"✅ Sonuçlar ({len(results)} doküman):")
            
          
            # Artık 'results' listesi ikililerden oluşuyor: (doc_id, score)
            for doc_id, score in results:
                file_name = file_map.get(doc_id, "Bilinmeyen")
                
                # Puanı virgülden sonra 4 hane olacak şekilde yazdırıyoruz
                print(f"  📄 {file_name}  --> (Skor: {score:.4f})")
        else:
            print("❌ Sonuç bulunamadı.")

if __name__ == "__main__":
    main()