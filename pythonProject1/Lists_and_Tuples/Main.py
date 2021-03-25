letters = []

letters += 'Interdenominational'
print(letters)

list1 = [10, 20, 30]
list2 = [40, 50]
list1+=list2
print(list1)

def display_Barchart():
    """Displaying a bar chart"""
    numbers = [1,5,9,11,9,5,1]
    print('\nCreating a bar chart from numbers:')
    print(f'Index{"Value":>8}      Bar')

    for index, value in enumerate(numbers):
        print(f'{index:>5}{value:>8}     {"*"  * value}')

def main():
    display_Barchart()


if __name__ == "__main__":
    main()

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
# slicing from 4 -> 7
print(numbers[4:7])

zeroes =  [4, 7, 2 , 0 , 0 , 3 , 0]
print(all(zeroes))
print(any(zeroes))
