list1 = [
        [0,0,6,8,4,0,0,0,0],
        [2,0,1,0,6,0,0,0,7],
        [0,3,9,0,0,0,0,1,0],
        [0,0,0,0,9,8,3,0,0],
        [0,6,0,0,0,0,0,9,0],
        [0,0,7,3,2,0,0,0,0],
        [0,4,0,0,0,0,1,3,0],
        [7,0,0,0,1,0,8,0,4],
        [0,0,0,0,3,5,7,0,0]
        ]

list2 = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]

def draw_list(lst):
    counter2 = 1
    counter1 = 1
    for element in lst:
        for a in element:
            if counter1 % 9 == 0:
                print(a)
                counter2 = 1
            else:
                if counter2%3 == 0:
                    print(a,end = ' ')
                else:
                    print(a,end='')
                counter2 += 1
            counter1 += 1


def solve(lst):
    for i in range(0,9):
        for j in range(0,9):
            if lst[i][j] == 0:
                psb = check_possible(lst,i,j)
                # print(f'{i+1}x{j+1} = {psb}')
                if len(psb) > 0:
                    a = 0
                    lst[i][j] = psb[a]
                    # print(f'{i+1}x{j+1} = {psb[a]} chosen')
                    while solve(lst) == 0:
                        # print(f'{i+1}x{j+1} = {lst[i][j]} not a good choice')
                        lst[i][j] = 0
                        a = a+1
                        try:
                            lst[i][j] = psb[a]
                            # print(f'{i+1}x{j+1} = {psb[a]} chosen')
                        except IndexError:
                            #print(f'{i+1}x{j+1} = {psb[a-1]} not a good one')
                            # print(f'{i+1}x{j+1} = {lst[i][j]} not a good choice')
                            lst[i][j] = 0
                            return 0
                else:
                    # print(f'{i+1}x{j+1} = {lst[i][j]} not a good choice ')
                    lst[i][j] = 0
                    return 0


def check_possible(lst,row,column):
    numbers = [1,2,3,4,5,6,7,8,9]
    for i in range(0,9):
        for j in range(0,9):
            if i == row:
                if lst[i][j] != 0:
                    try:
                        numbers.remove(lst[i][j])
                    except ValueError:
                        pass
    for i in range(0,9):
        for j in range(0,9):
            if j == column:
                if lst[i][j] != 0:
                    try:
                        numbers.remove(lst[i][j])
                    except ValueError:
                        pass
    i1 = row // 3
    j1 = column // 3
    for i in range(i1*3, i1*3+3):
        for j in range(j1*3,j1*3 + 3):
            if lst[i][j] != 0:
                try:
                    numbers.remove(lst[i][j])
                except ValueError:
                    pass
    return numbers



def check_correct(lst):
    for i in range(0,9):
        row_vector = []
        for j in range(0,9):
            if lst[i][j] != 0:
                row_vector.append(lst[i][j])
                if row_vector.count(lst[i][j]) > 1:
                    return 0
    for j in range(0,9):
        column_vector = []
        for i in range(0,9):
            if lst[i][j] != 0:
                column_vector.append(lst[i][j])
                if column_vector.count(lst[i][j]) > 1:
                    return 0

    for i in range(0,9):
        if i % 3 == 0:
            chunk_vector = []
        for j in range(0,3):
            if lst[i][j] != 0:
                chunk_vector.append(lst[i][j])
                if chunk_vector.count(lst[i][j]) > 1:
                    return 0
    for i in range(0,9):
        if i % 3 == 0:
            chunk_vector = []
        for j in range(3,6):
            if lst[i][j] != 0:
                chunk_vector.append(lst[i][j])
                if chunk_vector.count(lst[i][j]) > 1:
                    return 0
    for i in range(0,9):
        if i % 3 == 0:
            chunk_vector = []
        for j in range(6,9):
            if lst[i][j] != 0:
                chunk_vector.append(lst[i][j])
                if chunk_vector.count(lst[i][j]) > 1:
                    return 0
