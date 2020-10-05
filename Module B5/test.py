# text = 'aaabbccccdaa'
text = input('Введите текст: ')

dictionary = {}

for char in text:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

result = ''

for lmnt in dictionary:
    result += lmnt + str(dictionary[lmnt])

print(result)