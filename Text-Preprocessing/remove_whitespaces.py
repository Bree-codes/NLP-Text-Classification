# removing white spaces from a text

original_txt = " I love   coding  "
clean_txt = " ".join(original_txt.split())

print(clean_txt)