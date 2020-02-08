from re import split
import operator

sentence = input("Please enter the text: ")
wordFreq = {}

words = split(' ',sentence)
words_set = set(words)

#initalization
for w in words_set:
    wordFreq[w] = 1
print(wordFreq)

# #adding duplicates
# for w in words_set:
#     for i in range(0,len(words)):
#

sorted_words = sorted(wordFreq.items(), key=operator.itemgetter(1))
print(sorted_words)
