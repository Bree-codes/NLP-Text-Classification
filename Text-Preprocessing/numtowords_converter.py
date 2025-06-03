#converting numerical values to text

from num2words import num2words

text = "Bree has ksh 50000 in her wallet and ksh 100 coins."
converted = text.replace("50000", num2words(50000)).replace("100", num2words(100))

print(converted)
