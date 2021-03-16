# def square(number):
#     return number ** 2
# a = square(64)
# print(a)
# print(square(7))
# maxColor = max('yellow', 'pink','Yellow','Orange')
# print(maxColor)

# import random
# frequency1  = 0
# frequency2  = 0
# frequency3  = 0
# frequency4  = 0
# frequency5  = 0
# frequency6  = 0
#
# for roll in range(6000000):
#     face = random.randrange(1,7)
#
#     if face == 1:
#         frequency1 += 1
#     elif face == 2:
#         frequency2 += 1
#     elif face == 3:
#         frequency3 += 1
#     elif face == 4:
#         frequency4 += 1
#     elif face == 5:
#         frequency5 += 1
#     else:frequency6 += 1
#
# print(" FACE     FREQUENCY")
# print(f'{1:>5}{frequency1:>13}')
# print(f'{2:>5}{frequency2:>13}')
# print(f'{3:>5}{frequency3:>13}')
# print(f'{4:>5}{frequency4:>13}')
# print(f'{5:>5}{frequency5:>13}')
# print(f'{6:>5}{frequency6:>13}')

list = [5,9,11,4,1,8]
print(list)
new_list = list.sort()
print(new_list)