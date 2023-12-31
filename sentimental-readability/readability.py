# TODO
text = input("Text: ")

letters = words = sentences = 0

for i in range(len(text)):
    if text[i].isalpha():
        letters += 1
    elif text[i] == " ":
        words += 1
    elif text[i] == "." or text[i] == "?" or text[i] == "!":
        sentences += 1
words += 1

L = (letters / words) * 100
S = (sentences / words) * 100

index = int(round(0.0588 * L - 0.296 * S - 15.8))

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print("Grade", index)
