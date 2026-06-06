# src/query_engine.py
from src.preprocessing import mining_text

class QueryEngine:
    def __init__(self, inverted_index):
        """
        QueryEngine, artık hem index_map'i (TF) hem de idf_map'i (IDF) kullanacak.
        """
        self.inverted_index = inverted_index

    def search(self, query):
        """
        Sorgudaki kelimelere göre dokümanları puanlar ve sıralar.
        Algoritma: TF-IDF (Term Frequency - Inverse Document Frequency)
        """
        # 1. Sorguyu temizle
        tokens = mining_text(query)
        
        if not tokens:
            return []
            
        # Puan Tablosu: { doc_id: toplam_puan }
        # Örnek: { 1: 0.45, 5: 2.12 }
        scores = {}
        
        # Depodaki haritaları kısayol değişkenlere alalım
        index_map = self.inverted_index.index_map
        idf_map = self.inverted_index.idf_map
        
        # 2. Her arama kelimesi için döngüye gir
        for token in tokens:
            # Eğer kelime indeksimizde varsa işlem yap
            if token in index_map:
                
                # A) Bu kelimenin 'Nadirlik Değeri'ni (IDF) al
                idf_val = idf_map.get(token, 0)
                
                # B) Bu kelimenin geçtiği tüm dokümanları ve kaç kere geçtiğini (TF) al
                # doc_occurrences formatı: { doc_id: count, doc_id2: count ... }
                doc_occurrences = index_map[token]
                
                # C) Her doküman için puanı hesapla ve hanesine yaz
                for doc_id, count in doc_occurrences.items():
                    
                    # BASİT TF-IDF FORMÜLÜ: (Kelime Sayısı * Nadirlik)
                    term_score = count * idf_val
                    
                    # Puanı dokümanın toplam skoruna ekle
                    if doc_id in scores:
                        scores[doc_id] += term_score
                    else:
                        scores[doc_id] = term_score

        # 3. Sonuçları Puana Göre Sırala (Yüksekten Düşüğe)
        # sorted fonksiyonu bize [(doc_id, score), (doc_id, score)] listesi verir
        sorted_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        # Kullanıcıya sadece Doc ID'leri döndür (Skorları gizle)
        # İstersen [(doc_id, score), ...] şeklinde de döndürebilirsin.
        return sorted_results