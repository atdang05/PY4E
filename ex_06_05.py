str = "X-DSPAM-Confidence: 0.8475"
colpos = str.find(":")
print(float(str[colpos + 1 :]))
