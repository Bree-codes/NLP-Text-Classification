import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
punctuations = set(string.punctuation)

# Preprocessing function
def preprocess_text(text):
    # 1. Lowercase
    text = text.lower()

    # 2. Remove punctuation
    text = ''.join([char for char in text if char not in punctuations])

    # 3. Tokenize
    tokens = word_tokenize(text)

    # 4. Remove non-alphabetic tokens
    tokens = [word for word in tokens if word.isalpha()]

    # 5. Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # 6. Lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens

# Test with sample reports
sample_reports = [
    "The doctors were running tests on several patients.",
    "He studies machines that learn from data.",
    "Cleaning and normalizing text is essential for NLP!"
]

preprocess_text(sample_reports)
print()
for i, report in enumerate(sample_reports, 1):
    print(f"\nReport {i}:")
    print(preprocess_text(report))

