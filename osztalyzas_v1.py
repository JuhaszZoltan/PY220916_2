jegy:int = int(input('hányast kaptál? '))

if jegy == 1:
    print('elégtelen')
else:
    if jegy == 2:
        print('elégséges')
    else:
        if jegy == 3:
            print('közepes')
        else:
            if jegy == 4:
                print('jó')
            else:
                print('jeles')