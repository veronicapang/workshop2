import sys
import string

# yourinput = sys.stdin.read().split()
# print("Input of histogram.py file:")
# print(yourinput)



yourinput = sys.stdin.readlines()
# print("Input of histogram.py file:")
# print(yourinput[0])
print(yourinput)

total = 0
dictionary = dict()

for i in yourinput:
    line = i.strip().split()
    word = line[0]
    count = line[1]
    dictionary[word] = count
    total += int(count)

for word in dictionary.keys():
    count = int(dictionary[word])
    print(word + "\t" + '[' + "**" * count + ']\t' + str(round((count / total * 100))) + '%')



# *2 , average