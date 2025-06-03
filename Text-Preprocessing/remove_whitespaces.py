# removing white spaces from a text

original_txt = " Bree   is   awesome  and she loves   coding  "
clean_txt = " ".join(original_txt.split())

print(clean_txt)