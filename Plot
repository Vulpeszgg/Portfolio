def print_arr(matrix):
    for i in matrix:
        for j in i:
            if j == 2:
                print("_", end="")
            elif j == 1:
                print("/", end="")
            elif j == -1:
                print("\\", end="")
            else:
                print(" ", end="")
        print()

def clean(matrix):
    arr = list()
    l = len(matrix[0])
    target = [0 for _ in range(l)]
    for row in matrix:
        if row != target:
            arr.append(row)
    return arr

def plot(s):
    max_ = len(s)
    array = list(list(0 for _ in range(max_+2)) for _ in range(max_*2+3))
    cursor = len(array)//2+1
    array[cursor][0] = 2 # 2 is Start or End
    for i in range(0, len(s)):
        if i == 0 and s[i] == "D":
            cursor += 1
        if s[i:i+2] == "UD": # 1 is Up
            array[cursor][i+1] = 1
        elif s[i:i+2] == "DU": # -1 is Down
            array[cursor][i+1] = -1
        elif s[i:i+2] == "UU": # 1 is Up
            array[cursor][i+1] = 1
            cursor -= 1
        elif s[i:i+2] == "DD": # -1 is Down
            array[cursor][i+1] = -1
            cursor += 1
        else:
            array[cursor][i+1] = 1 if s[i] == "U" else -1
    if s[-1] == "U":
        cursor -= 1
    array[cursor][-1] = 2
    print_arr(clean(array))

plot(input())
