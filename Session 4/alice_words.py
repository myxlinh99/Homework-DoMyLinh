stories = open("alice_words").read()

stories_count = {}
for word in stories:
    stories_count[word] = word_counts.get(word,0) + 1

print (stories_count)
