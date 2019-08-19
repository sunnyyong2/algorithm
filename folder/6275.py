sentence = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
result = ''
char = ['a', 'e', 'i', 'o', 'u']
for i in sentence:
    if i in char:
        pass
    else:
        result += i
print(result)
