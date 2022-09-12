from textblob import TextBlob

sentence = input("Please enter a grammatically incorrect sentence?")
a = TextBlob(sentence)

b = a.correct()
print(a)
print(b)