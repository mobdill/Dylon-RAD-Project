#Tic Tac Toe

board = [0,1,2,
         3,4,5,
         6,7,8]

def show():
    print board[0],'|',board[1],'|',board[2]
    print '----------'
    print board[3],'|',board[4],'|',board[5]
    print '----------'
    print board[6],'|',board[7],'|',board[8]

while True:

    input = raw_input("Select a spot: "
    input = int(input)

    if board[input] != 'x' and board[input] != 'o':
        board[input] = 'x'

    else:
        print 'This spot is taken!'
