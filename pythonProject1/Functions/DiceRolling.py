import random
import datetime
def dice_rolling():
    frequency1, frequency2, frequency3, frequency4, frequency5, \
    frequency6 = 0, 0, 0, 0, 0, 0

    for rolls in range(100):
        face = random.randrange(1,7)
        if face == 1:
            frequency1 += 1
        elif face == 2:
            frequency2 += 1
        elif face == 3:
            frequency3 += 1
        elif face == 4:
            frequency4 += 1
        elif face == 5:
            frequency5 += 1
        else:
            frequency6 += 1

    print(f'Face  {"Frequency"}')
    print(f'{1:<6}{frequency1:>7}')
    print(f'{2:<6}{frequency2:>7}')
    print(f'{3:<6}{frequency3:>7}')
    print(f'{4:<6}{frequency4:>7}')
    print(f'{5:<6}{frequency5:>7}')
    print(f'{6:<6}{frequency6:>7}')

def main():
    dice_rolling()
    print(datetime.datetime.today())



if __name__ == "__main__":
    main()



