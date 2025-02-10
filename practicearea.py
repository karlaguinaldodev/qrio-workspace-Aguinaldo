# # # #Sorting

# # # a = [5, 1, 4, 3]
# # # print(sorted(a))
# # # print(a)

# # # strs = ['aa', 'BB', 'zz', 'CC']
# # # print(sorted(strs))
# # # print(sorted(strs, reverse=True))

# # # from operator import itemgetter

# # # grade = [('Freddy', 'Frank', 3), ('Anil', 'Frank', 100), ('Anil', 'Wang', 24)]
# # # print(sorted(grade, key=itemgetter(1,0)))
# # #   # [('Anil', 'Frank', 100), ('Freddy', 'Frank', 3), ('Anil', 'Wang', 24)]

# # # print(sorted(grade, key=itemgetter(1,-1)))
# # #   #[('Anil', 'Wang', 24), ('Anil', 'Frank', 100), ('Freddy', 'Frank', 3)]

# # #Tuples

# # # tuple = (1, 2, 'hi')
# # # print(len(tuple))
# # # print(tuple[2])
# # # tuple = (1, 2, 'bye')
# # # print(tuple[2])

# # tuple = ('karlangeloaguinaldo', )
# # print(len(tuple))

# # (x, y, z) = (42, 13, "hike")
# # print(x)


# #Dicts and Files

# # dict = {}
# # dict['a'] = 'alpha'
# # dict['g'] = 'gamma'
# # dict['o'] = 'omega'

# # # print(dict)

# # # print(dict['a'])
# # # dict['a'] = 6
# # # print(dict['a'])
# # # print(dict['g'])
# # # if 'z' in dict: print(dict['z'])
# # # print(dict.get('z'))

# # # for key in dict:
# # #   print(key)

# # for key in dict.keys():
# #   print(key)

# # print (dict.values())

# # for key in sorted(dict.keys()):
# #   print (key, dict[key])

# # print(dict.items())

# # for k, v in dict.items(): print (k, '>', v)

# #Dict Formatting

# # h = {}
# # h['word'] = 'karl'
# # h['count'] = 42
# # s = 'I want %(count)d copies of %(word)s'% h
# # print(s)

# # s = 'I want {count} copies of {word}'.format(h)
# # print(s)

# #Del

# # var = 6
# # del var

# # list = ['a', 'b', 'c', 'd']
# # del list[0]
# # del list[-2]
# # print(list)

# # dict = {'a':1, 'b':2, 'c':3}
# # del dict['a']
# # print(dict)

# #Files lesson

# # f = open('foo.txt', 'rt', encoding = 'utf=8')
# # for line in f:
# #   print(line, end='')

# # f.close()

# # with open('foo.txt', encoding='utf-8', mode='wt') as f:
# #     f.write('\u20ACunicode\u20AC\n')

# # import re

# # str = 'an example word:cat!!'
# # match = re.search(r'word:\w\w\w', str)
# # if match:
# #   print('found', match.group())
# # else:
# #   print('did not found')

# # class Car:
# #   def start(self):
# #     print("the car is running")
# #   def stop(self):
# #     print("The car is stopped")

# # class Motorcycle(Car):
# #   pass

# # class Boat(Motorcycle):
# #   pass

# # def main():
# #   car = Car()
# #   boat = Boat()

# #   car.start()
# #   boat.start()

# # if __name__ == "__main__":
# #     main()

# import re

# match = re.search(r'iii', 'piiig') 
# match = re.search(r'igs', 'piiig')

# ## . = any char but \n
# match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

#   ## \d = digit char, \w = word char
# match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
# match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"

# import os (CANT UNDERSTAND starting REGULAR EXPRESSIONS UP TO UTILITIES)

# def printdir(dir):
#     filenames = os.qrio-workspace-Aguinaldo(dir)  # Get all file names
#     for filename in filenames:
#         print(filename)  # Print file name
#         print(os.path.join(dir, filename))  # Print full path
#         print(os.path.abspath(os.path.join(dir, filename)))  # Print absolute path