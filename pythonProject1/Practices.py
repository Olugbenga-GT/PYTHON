




#





# 2.9 (Integer Value of a Character) Here’s a peek ahead. In this chapter, you learned
# about strings. Each of a string’s characters has an integer representation. The set of characters
# a computer uses together with the characters’ integer representations is called that
# computer’s character set. You can indicate a character value in a program by enclosing that
# character in quotes, as in 'A'. To determine a character’s integer value, call the built-in
# function ord:
# In [1]: ord('A')
# Out[1]: 65
# Display the integer equivalents of B C D b c d 0 1 2 $ * + and the space character.
ord('A')


# 2.10 (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.
# 2.11 (Separating the Digits in an Integer) Write a script that inputs a five-digit integer
# from the user. Separate the number into its individual digits. Print them separated by three
# spaces each. For example, if the user types in the number 42339, the script should print
# 4 2 3 3 9
# Assume that the user enters the correct number of digits. Use both the floor division and
# remainder operations to “pick off ” each digit.
# 2.12 (7% Investment Return) Some investment advisors say that it’s reasonable to expect
# a 7% return over the long term in the stock market. Assuming that you begin with
# $1000 and leave your money invested, calculate and display how much money you’ll have
# after 10, 20 and 30 years. Use the following formula for determining these amounts:
# a = p(1 + r)n
# where
# p is the original amount invested (i.e., the principal of $1000),
# r is the annual rate of return (7%),
# n is the number of years (10, 20 or 30) and
# a is the amount on deposit at the end of the nth year.