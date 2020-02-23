
import numpy as np

# table = [
#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],

#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],

#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#     [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
# ]

table = [
    [ 3, 0, 9, 2, 0, 0, 6, 0, 7 ],
    [ 0, 0, 0, 6, 0, 0, 3, 0, 4 ],
    [ 1, 0, 0, 0, 0, 0, 0, 8, 0 ],

    [ 0, 0, 0, 0, 2, 5, 0, 0, 0 ],
    [ 0, 0, 0, 9, 0, 0, 0, 0, 0 ],
    [ 6, 2, 0, 0, 3, 0, 9, 0, 0 ],

    [ 4, 0, 6, 0, 0, 0, 0, 0, 0 ],
    [ 0, 7, 2, 0, 9, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 0, 0, 8, 5, 0 ]
]

def possible( y, x, value):
    global table

    # check if the cell is already used
    if table[y][x] != 0:
        return False


    # check of the value is found on Y axis
    for i in range( 9 ):
        if table[i][x] == value:
            return False

    # check of the value is found on X axis
    for i in range( 9 ):
        if table[y][i] == value:
            return False
    
    # check of the value is found inside block
    block_x = (x // 3) * 3
    block_y = (y // 3) * 3
    for i in range( 3 ):
        for j in range( 3 ):
            if table[block_y+j][block_x+i] == value:
                return False

    return True

iterations = 0

def solve():
    global table
    global iterations

    for y in range(9):
        for x in range(9):
            if table[y][x] == 0:
                for value in range(1,10):
                    if possible(y,x,value):
                        table[y][x] = value
                        iterations+=1
                        solve()
                        table[y][x] = 0
                return

    print("iterations = {}".format(iterations))
    print(np.matrix(table))
    input("more?")

print(np.matrix(table), "\n\n")
solve()

