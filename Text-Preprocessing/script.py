import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
punctuations = set(string.punctuation)

def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in punctuations])
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word, pos='v') for word in tokens]

    return tokens

sample_reports = [
    "The doctors were running tests on several patients.",
    "He studies machines that learn from data.",
    "Cleaning and normalizing text is essential for NLP!"
]

# Process each report individually
result = [preprocess_text(report) for report in sample_reports]

for i, tokens in enumerate(result, start=1):
    print(f"Report {i}: {' '.join(tokens)}\n")
