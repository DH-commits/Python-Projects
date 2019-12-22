for i in range(1, 10):
    if i == 9:
        continue
    print(i)

    i = 0

    while i < 8 in range(1, 10):
        print(i)
        i += 1

    availableNames = ['dan', 'james', 'john']
    nameInput = input('input a name')
    while nameInput not in availableNames:
        print('not a valid name')
        break


