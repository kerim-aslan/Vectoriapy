# src/preprocessing.py
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def ensure_nltk_resources():
    """Ensure necessary NLTK resources are available."""
    resources = {
        'punkt': 'tokenizers/punkt',
        'punkt_tab': 'tokenizers/punkt_tab',
        'stopwords': 'corpora/stopwords',
    }
    
    for resource, find_path in resources.items():
        try:
            nltk.data.find(find_path)
        except LookupError:
            print(f"Downloading {resource}...")
            nltk.download(resource, quiet=True)

# Modül import edildiğinde kaynakları bir kez kontrol etsin ve listeyi hazırlasın
ensure_nltk_resources()

# Performans İçin: Stopwords listesini her fonksiyon çağrısında değil,
# modül yüklendiğinde sadece bir kere hafızaya alıyoruz.
TURKISH_STOP_WORDS = set(stopwords.words('turkish'))

def mining_text(text):
    """
    Metni normalize eder, token'lara ayırır, stop word'leri temizler.
    """
    # 1. Normalizasyon (Küçük harfe çevirme)
    text = text.lower()
    
    # 2. Noktalama işaretlerini kaldırma
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Tokenization (Kelimelere ayırma)
    tokens = word_tokenize(text)
    
    clean_tokens = []
    for token in tokens:
        # Global değişkeni kullanarak kontrol et (Daha hızlı)
        if token not in TURKISH_STOP_WORDS:
            clean_tokens.append(token)
            
    return clean_tokens