word=input("type a word to reverse:")
#using Slicing method
Reveresed_word=word[::-1]
print(Reveresed_word)

#using For Loop
Reverse=""
for i in word:
    Reverse=i+Reverse
print(Reverse)