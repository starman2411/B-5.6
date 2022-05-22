def make_turn(field, player_name, turn):
    print(f'{player_name}, ваш ход!')
    while True:
        pos = list(map(int, input('Введите координаты ячейки через пробел: ').split()))
        if len(pos) == 2:
            if (pos[0] not in [0,1,2]) or (pos[1] not in [0,1,2]):
                print('Координаты введены неверно. Попробуйте ещё раз!')
                pos = list(map(int, input('Введите координаты ячейки через пробел: ').split()))

            if (turn == 1) and (field[pos[0]][pos[1]] == '-'):
                field[pos[0]][pos[1]] = 'x'
                break
            elif (turn == 2) and (field[pos[0]][pos[1]] == '-'):
                field[pos[0]][pos[1]] = 'o'
                break
            else:
                print('Клетка уже занята. Попробуйте снова!')
        else:
            print('Координаты введены неверно. Попробуйте ещё раз!')
    return field


def check_winner(field):
    if (field[0][0] == field[1][1] == field[2][2]):
        return field[0][0]
    if (field[0][2] == field[1][1] == field[2][0]):
        return field[0][2]    
    if (field[0][0] == field[0][1] == field[0][2]):
        return field[0][0]    
    if (field[1][0] == field[1][1] == field[1][2]):
        return field[1][0]  
    if (field[2][0] == field[2][1] == field[2][2]):
        return field[2][0]    
    if (field[0][1] == field[1][1] == field[2][1]):
        return field[0][1]    
    if (field[0][0] == field[1][0] == field[2][0]):
        return field[0][0]  
    if (field[0][2] == field[1][2] == field[2][2]):
        return field[0][2]    
    return '-'


field = [['-' for _ in range(3)] for _ in range(3)]
print('Игрок 1 (крестики), представьтесь:')
player_1 = input()
print('Игрок 2 (нолики), представьтесь:')
player_2 = input()
turn = 1
while sum([row.count('-') for row in field]):
    if turn == 1:
        field = make_turn(field, player_1, turn)
        turn = 2
    elif turn == 2:
        field = make_turn(field, player_2, turn)
        turn = 1
        
    print('\n  0  1  2')
    for k in range(3):
        print(f'{k} {field[k][0]}  {field[k][1]}  {field[k][2]}')
    print()
    
    if check_winner(field) == 'x':
        print(f'\n Игра окончена. Победил {player_1}(крестики)')
        break
    elif check_winner(field) == 'o':
        print(f'\n Игра окончена. Победил {player_2}(нолики)')
        break
if (check_winner(field) != 'o') and (check_winner(field) != 'x'):
    print('\n Игра окончена. Ничья!')

