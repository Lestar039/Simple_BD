my_bd = {}
first_inner_dict = {}
count_transaction = 0
dict_controller = [my_bd]

while True:
    current_dict = dict_controller[-1]
    x = input()
    command = x.split(' ')[0]

    if command == 'END':
        count_transaction = 0
        break

    elif command == 'SET':
        try:
            if count_transaction == 1:
                first_inner_dict[x.split(' ')[1]] = x.split(' ')[2]
            else:
                current_dict[x.split(' ')[1]] = x.split(' ')[2]
        except IndexError:
            print('Wrong command! Use: SET KEY VALUE')

    elif command == 'GET':
        try:
            print(current_dict[x.split(' ')[1]])
        except KeyError:
            print('NULL')
        except IndexError:
            print('Wrong command! Use: GET VALUE')

    elif command == 'UNSET':
        try:
            del current_dict[x.split(' ')[1]]
        except KeyError:
            pass
        except IndexError:
            print('Wrong command! Use: UNSET KEY')

    elif command == 'COUNTS':
        counter = 0
        for one_dict in dict_controller:
            for key, value in current_dict.items():
                if value == x.split(' ')[1]:
                    counter += 1
        print(counter)

    elif command == 'BEGIN':
        count_transaction += 1
        if count_transaction == 1:
            dict_controller.append(first_inner_dict)
        else:
            new_dict = dict()
            dict_controller.append(new_dict)

    elif command == 'ROLLBACK':
        count_transaction = 0
        dict_controller = dict_controller[:2]
        if len(dict_controller[-1]) == 0:
            del dict_controller[-1]

    elif command == 'COMMIT':
        while len(dict_controller) > 1:
            for key in dict_controller[-1].keys():
                my_bd[key] = dict_controller[-1][key]
            del dict_controller[-1]

    else:
        print('Wrong command! Use: SET, GET, UNSET, BEGIN, ROLLBACK, COMMIT, END')
