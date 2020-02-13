# name = input("What's your name?")
# print("Hello,%s" % name)
# num = 100 + 10
# print("num is %d" % num)
#
# lists = ['a', 'b', 'c']
# lists.append('d')
# print(lists)
# print(len(lists))
# lists.insert(0, 'mm')
# lists.pop()
# print(lists)


while True:
  try:
    line = input()
    num = line.split()
    print(int(num[0]) + int(num[1]))
  except:
    break