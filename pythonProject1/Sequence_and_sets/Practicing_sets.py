colors = {'red', 'orange', 'yellow', 'green', 'red','aquamarine' 'blue', }
print(colors)

# temperature samples for each of four days. What does the for statement do?
temperatures = {
'Monday': [66, 70, 74],
'Tuesday': [50, 56, 64],
'Wednesday': [75, 80, 83],
'Thursday': [67, 74, 81]
}
for k, v in temperatures.items():
    print(f'{k}: {sum(v)/len(v):.2f}')