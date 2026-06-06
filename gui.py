import customtkinter as ctk
import os
import threading
from pathlib import Path
from src.indexer import InvertedIndex
from src.preprocessing import ensure_nltk_resources, mining_text
from src.query_engine import QueryEngine

def init_search_engine(folder_path, extensions):
    ensure_nltk_resources()
    index = InvertedIndex()
    data_folder = Path(folder_path)
    file_map = {}
    doc_id_counter = 1
    
    files = []
    for ext in extensions:
        files.extend(list(data_folder.rglob(f"*{ext}")))

    for file_path in files:
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            index.add_document(doc_id_counter, mining_text(text))
            file_map[doc_id_counter] = {"name": file_path.name, "path": str(file_path.absolute())}
            doc_id_counter += 1
        except Exception: continue
        
    index.compute_idf()
    engine = QueryEngine(index)
    return lambda q: [{"file": file_map[id]["name"], "path": file_map[id]["path"], "score": score} for id, score in engine.search(q)]

class VectoriaUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.search_function = None
        self.title("Vectoria Search") # Başlık güncellendi
        self.geometry("700x650")
        ctk.set_appearance_mode("dark")
        
        ctk.CTkLabel(self, text="Vectoria", font=("Arial", 28, "bold")).pack(pady=10) # Başlık güncellendi
        self.entry_ext = ctk.CTkEntry(self, width=150)
        self.entry_ext.insert(0, ".txt,.md,.py")
        self.entry_ext.pack(pady=5)
        self.lbl_status = ctk.CTkLabel(self, text="Klasör seçerek başlayın.", text_color="gray")
        self.lbl_status.pack(pady=5)
        ctk.CTkButton(self, text="📁 Klasör Seç ve İndeksle", command=self.start_thread).pack(pady=10)
        self.entry_query = ctk.CTkEntry(self, placeholder_text="Arama yap...", width=500)
        self.entry_query.pack(pady=10)
        self.entry_query.bind("<Return>", self.perform_search)
        self.scroll_frame = ctk.CTkScrollableFrame(self, height=300)
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def start_thread(self):
        folder = ctk.filedialog.askdirectory()
        if folder: threading.Thread(target=self.run_indexing, args=(folder,), daemon=True).start()

    def run_indexing(self, folder):
        self.lbl_status.configure(text="⚙️ İndeksleniyor...", text_color="yellow")
        try:
            self.search_function = init_search_engine(folder, [e.strip() for e in self.entry_ext.get().split(",")])
            self.lbl_status.configure(text="✅ İndeksleme Başarılı!", text_color="green")
        except Exception as e:
            self.lbl_status.configure(text=f"❌ Hata: {str(e)}", text_color="red")

    def perform_search(self, event=None):
        if not self.search_function: return
        for w in self.scroll_frame.winfo_children(): w.destroy()
        
        results = self.search_function(self.entry_query.get())
        
        if not results:
            ctk.CTkLabel(self.scroll_frame, text="Sonuç bulunamadı.", text_color="gray").pack(pady=20)
            return

        for res in results:
            frame = ctk.CTkFrame(self.scroll_frame)
            frame.pack(fill="x", pady=2)
            ctk.CTkLabel(frame, text=f"{res['file']} (Skor: {res['score']:.4f})").pack(side="left", padx=10)
            ctk.CTkButton(frame, text="Aç", width=40, command=lambda p=res['path']: os.startfile(p)).pack(side="right", padx=10)

if __name__ == "__main__":
    VectoriaUI().mainloop()