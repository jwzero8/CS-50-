import cs50
letter = word = sentence = 0
text = cs50.get_string("Text: ")

for j in text:
    if j.isalpha():
        letter = letter + 1

    elif j == ' ':
        word = word + 1

    elif j in ['!', '?', '.']:
        sentence = sentence + 1

word = word + 1

L = (100 / word) * letter
S = (100 / word) * sentence
index = int(round(0.0588 * L - 0.296 * S - 15.8))

if index < 1:
    print("Before Grade 1")

elif index >= 16:
    print("Grade 16+")

else:
    print(f"Grade {index}")

