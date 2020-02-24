str = '''Hello World
Bye World
Hello Hadoop
Bye Hadoop'''

print(str)

strl_ist = str.replace('\n', ' ').lower().split(' ')
print(strl_ist)
count_dict = {}

for str in strl_ist:
    if str in count_dict.keys():
        count_dict[str] += 1
    else:
        count_dict[str] = 1

print(count_dict)


