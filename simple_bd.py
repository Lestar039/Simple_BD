main_bd = {}
count_transaction = 0
dict_controller = [main_bd]

while True:
    current_dict = dict_controller[-1]
    x = input()
    command = x.split(' ')[0]

    if command == 'END':
        break

    elif command == 'SET':
        try:
            current_dict[x.split(' ')[1]] = x.split(' ')[2]
        except IndexError:
            print('Wrong command! Use: SET KEY VALUE')
        print(dict_controller)

    elif command == 'GET':
        try:
            for one_dict in reversed(dict_controller):
                try:
                    print(one_dict[x.split(' ')[1]])
                    break
                except KeyError:
                    pass
            else:
                print('NULL')
        except IndexError:
            print('Wrong command! Use: GET VALUE')

    elif command == 'UNSET':
        try:
            for one_dict in reversed(dict_controller):
                try:
                    del one_dict[x.split(' ')[1]]
                    break
                except KeyError:
                    pass
        except KeyError:
            pass
        except IndexError:
            print('Wrong command! Use: UNSET KEY')

    elif command == 'COUNTS':
        counter = 0
        try:
            for one_dict in reversed(dict_controller):
                for key, value in one_dict.items():
                    if value == x.split(' ')[1]:
                        counter += 1
            print(counter)

        except IndexError:
            print('Wrong command! Use: COUNTS VALUE')

    elif command == 'BEGIN':
        count_transaction += 1
        new_dict = dict()
        dict_controller.append(new_dict)

    elif command == 'ROLLBACK':
        if count_transaction > 1:
            del dict_controller[-1]
            count_transaction -= 1
        else:
            print('No one transaction now. Try BEGIN for start it')

    elif command == 'COMMIT':
        while len(dict_controller) > 1:
            main_bd.update(dict_controller[1])
            del dict_controller[1]
        count_transaction = 0

    else:
        print('Wrong command! Use: SET, GET, UNSET, BEGIN, ROLLBACK, COMMIT, END')
