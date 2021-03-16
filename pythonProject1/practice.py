days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
tasks = ["Java", "Sleep", "Data Science with R", "Python", "Javascript", "Flex", "Flex"]

def modify_week(weeks):
   a = weeks[0]
   weeks.remove(a)
   weeks.append(a)
   # OR
   weeks.append(weeks.pop(0))

def make_daily_plans(week, task):
    # zip(week, task)
    # return dict(zip(week, task))


              # OR
    my_daily_plans = {}
    for x , y in zip (week, task):
        my_daily_plans[x] = y
    return (my_daily_plans )

def create_group_collection():
    group_collection  = {}
    for i in range(3):
        x = input("enter your group number: \n")
        y = input("enter group members:  \n ")
        group_collection[x] = y.split(',')
    return group_collection




squares = ["One", "two", "three", "four", "five"]
values   = [1,2,3,4,5]

def square_numbers(number, square):
    my_squares = {}
    for a , b in zip(squares, values):
        my_squares[a] = b ** 2
    return my_squares

# Or using list comprehension
{x : y * y for x , y in zip(squares, values)}




def main():
    # modify_week(days_of_the_week)
    # print(days_of_the_week)
   # plans = make_daily_plans(days_of_the_week, tasks)
   # print(plans)
   #
   # print(square_numbers(squares, values))

   the_groups = create_group_collection()
   print(the_groups)




if __name__ == "__main__":
    main()