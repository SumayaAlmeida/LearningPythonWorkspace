
is_leap = True

while (is_leap):
    year = int(input("Please, enter the year you would like to check if is Leap Year:\n"))
    if year%4 == 0:
        if year%100 ==0:
            if year%400 == 0:
                print('It is a Leap year')
            else:
                print('Not a Leap year')
                is_leap = False
        else:
            print('It is a Leap year')

    else:
        print('Not a Leap year')
        is_leap = False
            

