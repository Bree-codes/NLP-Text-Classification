# function to remove stopwords

import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

from nltk.tokenize import word_tokenize
text = "She is learning Natural Language Processing and it is fun"
tokens = word_tokenize(text)

filtered_tokens = [word for word in tokens if word.lower()not in stopwords]

clean_text = " ".join(filtered_tokens)
print(clean_text)
