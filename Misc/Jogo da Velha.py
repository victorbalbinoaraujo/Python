import itertools

def winner(jogo):
    def equals(value):
        if len(set(value)) == 1 and value[0] != 0:
            return True
        else:
            return False

    for lin in jogo:
        if equals(lin):
            print(f"Jogador {actual_player} You win!")
            return True

    for col in range(len(jogo)):
        check = []
        for lin in jogo:
            check.append(lin[col])
        if equals(check):
            print(f"Jogador {actual_player} You win!")
            return True
            
    check = []
    for i in range(len(jogo)):
        check.append(jogo[i][i])
    if equals(check):
            print(f"Jogador {actual_player} You win!")
            return True

    check = []
    for lin, col in enumerate(reversed(range(len(jogo)))):
        check.append(jogo[lin][col])
    if equals(check):
            print(f"Jogador {actual_player} You win!")
            return True

    return False

def print_map(jogo_map, jogador=0, linha=0, coluna=0):
    signal = False 
    if jogo_map[linha][coluna] != 0:
        signal = True
        return jogo_map, signal
    jogo_map[linha][coluna] = jogador
    print("   0  1  2")
    for conta, linha in enumerate(jogo_map):
        print(conta, linha)
    return jogo_map, signal

play = True
player = itertools.cycle([1, 2])
while play:
    print()
    jogo = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
    print_map(jogo, 0, 0, 0)
    won = False
    while not won:
        signal = False
        actual_player = next(player)
        print()
        print(f'Jogador: {actual_player}')
        choose_line = int(input("Line [0, 1, 2]: "))
        choose_col = int(input("Column [0, 1, 2]: "))
        print()
        jogo, signal= print_map(jogo, actual_player, choose_line, choose_col)
        print()
        if signal:
            print("Already filled!")
            actual_player = next(player)
        if winner(jogo):
            won = True
            play = False
    
