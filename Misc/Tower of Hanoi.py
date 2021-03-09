def move(orig, dest):
    print(f'Move disc from {orig} to {dest}')

def move_via(orig, via, dest):
    move(orig, via)
    move(via, dest)

def hanoi(number_discs, orig, via, dest):
    if number_discs == 0:
        pass #do nothing
    else:
        hanoi(number_discs-1, orig, dest, via)
        move(orig, dest)
        hanoi(number_discs-1, via, orig, dest)

hanoi(4, 'A', 'B', 'C')