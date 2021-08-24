string = input()
# print(ord('a'), ord('z'))
# print(ord('A'), ord('Z'))
# print(ord('0'), ord('9'))
sum = 0
number_index = []
for s in string:
    if ord(s) >= 48 and ord(s) <= 57:
        sum += int(s)
print(sum)
sum = str(sum)
for i in range(len(string)):
    if ord(string[i]) >= 48 and ord(string[i]) <= 57:
        number_index.append(i)
print(number_index)
count = 0
for i in number_index:
    string = list(string)
    del string[i-count]
    count += 1
    print(string)
sorted_string = sorted(string)
string = "".join(sorted_string)

print(string+sum)