# removing punctuations by importing string, then deleting all the punctuations listed in string.punctuation

import string

print(string.punctuation)

text = "Hello, Bree! You're doing great, keep going."
new_txt = text.translate(str.maketrans(' ',' ', string.punctuation))

print(new_txt)

