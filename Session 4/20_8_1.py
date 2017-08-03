s = 'ThiS is String with Upper and lower case Letters'
letter_counts = {}
for letter in s.lower():
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

for letter, n in sorted(letter_counts.items()):
    print(letter, n)
