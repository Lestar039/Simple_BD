my_bd = {}
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
            current_dict[x.split(' ')[1]] = x.split(' ')[2]
        except IndexError:
            print('Wrong command! Use: SET KEY VALUE')

    elif command == 'GET':
        try:
            print(current_dict[x.split(' ')[1]])
        except KeyError:
            try:
                print(my_bd[x.split(' ')[1]])
            except KeyError:
                print('NULL')
        except IndexError:
            print('Wrong command! Use: GET VALUE')

    elif command == 'UNSET':
        try:
            del current_dict[x.split(' ')[1]]
        except KeyError:
            try:
                del my_bd[x.split(' ')[1]]
            except IndexError:
                pass
        except IndexError:
            print('Wrong command! Use: UNSET KEY')

    elif command == 'COUNTS':
        counter = 0
        try:
            for key, value in my_bd.items():
                if value == x.split(' ')[1]:
                    counter += 1
            print(counter)
        except IndexError:
            print('Wrong command! Use: COUNTS KEY')

    elif command == 'BEGIN':
        count_transaction += 1
        new_dict = dict()
        dict_controller.append(new_dict)

    elif command == 'ROLLBACK':
        if count_transaction > 1:
            count_transaction -= 1
            del dict_controller[-1]
        elif count_transaction == 0:
            print('No one transaction now. Try BEGIN for start it')

    elif command == 'COMMIT':
        while len(dict_controller) > 1:
            my_bd.update(dict_controller[1])
            del dict_controller[1]

    else:
        print('Wrong command! Use: SET, GET, UNSET, BEGIN, ROLLBACK, COMMIT, END')
