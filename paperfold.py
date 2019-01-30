loops = 8
turn = 1 # 0 for left turn, 1 for right turn
arr = [turn]

for i in range(loops):
    arr = arr + [turn] + [bit ^ 1 for bit in arr[::-1]] # arr + 1 + ~reverse(arr)

print(''.join([str(bit) for bit in arr]))  