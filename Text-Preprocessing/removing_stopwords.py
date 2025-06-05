# function to remove stopwords

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure downloads are handled
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = "She is learning Natural Language Processing and it is fun"

# Tokenize and remove stopwords
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
clean_text = " ".join(filtered_tokens)

print("Filtered Text:", clean_text)
