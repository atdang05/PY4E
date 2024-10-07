str = "X-DSPAM-Confidence: 0.8475"
sppos = str.find(" ")
print(float(str[sppos + 1 :]))
