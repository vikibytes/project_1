sent = input("Enter the sentence  ")
sent = sent.lower()
letters = 0
digits = 0
for i in range(0, len(sent)):
	if 97 <= ord(sent[i]) <= 122 :
		letters += 1
	elif 48 <= ord(sent[i]) <= 57 :
		digits += 1
	else :
		pass
print(f"Letters = {letters} \n Digits = {digits}")			