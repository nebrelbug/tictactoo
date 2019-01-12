from string import Template

tmp = Template("""
$a|$b|$c
$d|$e|$f
$g|$h|$i
""")

def print_board(brd):
    board = ['X' if x == -1 else x for x in brd]
    board = ['O' if x == 1 else x for x in board]
    board = [' ' if x == 0 else x for x in board]

    print(tmp.substitute(a=board[0],b=board[1],c=board[2],d=board[3],e=board[4],f=board[5],g=board[6],h=board[7],i=board[8]))

#print_board([0, -1, -1, 1, 1, 0, 1, -1, 0])