my_bd = {}
inner_dict = {}
count_transaction = 0

while True:
    x = input()
    command = x.split(' ')[0]

    if command == 'END':
        count_transaction = 0
        break

    elif command == 'SET':
        if count_transaction == 1:
            inner_dict[x.split(' ')[1]] = x.split(' ')[2]
        else:
            my_bd[x.split(' ')[1]] = x.split(' ')[2]

    elif command == 'GET':
        try:
            print(my_bd[x.split(' ')[1]])
        except KeyError:
            print('NULL')

    elif command == 'UNSET':
        try:
            del my_bd[x.split(' ')[1]]
        except KeyError:
            print(f"No value: \"{x.split(' ')[1]}\" in Base Date")

    elif command == 'COUNT':
        counter = 0
        for key, value in my_bd.items():
            if value == x.split(' ')[1]:
                counter += 1
        print(counter)

    elif command == 'BEGIN':
        count_transaction += 1

    elif command == 'ROLLBACK':
        for key in inner_dict.keys():
            my_bd[key] = inner_dict[key]

    elif command == 'COMMIT':
        count_transaction = 0

    else:
        print('Wrong command')
