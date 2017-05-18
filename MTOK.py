print("are we converting (1) mi to ki or (2) ki to mi press (1)or (2)")

unit_convert = input()

if unit_convert == '1':
    mi_per_ki = 0.621371

    print('How many ki?')
    ki = float(input())


    mi = mi_per_ki * ki


    print(str(ki) + ' ki is ' + str(mi) + ' mi.')


elif unit_convert == '2':
    ki_per_mi = 1.60934

    print('How many mi?')
    mi = float(input())


    ki = ki_per_mi * mi


    print(str(mi) + ' mi is ' + str(ki) + ' ki.')
else:
    print("that's not a '1' or a '2'!")
