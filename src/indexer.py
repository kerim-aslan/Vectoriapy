import json
import math
from collections import Counter

class InvertedIndex:
    def __init__(self):
        self.index_map = {}
        self.doc_count = 0 
        self.idf_map = {} 

    def add_document(self, doc_id, tokens):
        self.doc_count += 1 
        token_counts = Counter(tokens)
        for token, count in token_counts.items():
            if token not in self.index_map:
                self.index_map[token] = {}
            self.index_map[token][doc_id] = count

    def compute_idf(self):
        N = self.doc_count
        if N == 0: return
        for token in self.index_map:
            df = len(self.index_map[token])
            # Skorun 0 gelmemesi için düzeltme (Smoothing)
            self.idf_map[token] = math.log10(N / (df + 1)) + 1
            
    def save_to_json(self, filename):
        save_data = {"doc_count": self.doc_count, "index_map": self.index_map, "idf_map": self.idf_map}
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=4)