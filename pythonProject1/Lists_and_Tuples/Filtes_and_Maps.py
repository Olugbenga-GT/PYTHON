numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def is_odd(x):
    """Returns x if true"""
    return x % 2 != 0

def main():
 a = list(   filter(is_odd, numbers) )
 print(a)

 b = [item for item in numbers if is_odd(item)]
 print(b)

 c = list(filter(lambda x: x % 2 == 0, numbers))
 print(c)

if __name__ == "__main__":
    main()

# name = ["Gbenga" ,"Samuel", "Ibrahim", "Amanda", "Luci"]
# grades = ["A", "B", "C", "B", "A"]
# position = ["1st", "2nd", "3rd", "4th", "5th"]
#
# for name, grade, position in zip(name, grades, position:
#     print(f'')





names = ['Bob', 'Sue', 'Amanda']
grade_point_averages = [3.5, 4.0, 3.75]
position = ["1st", "2nd", "3rd", "4th", "5th"]
for name, gpa, position in zip(names, grade_point_averages, position):
    print(f'Name={name}; GPA={gpa}, position= {position}')
