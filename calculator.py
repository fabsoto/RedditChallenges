input_list = input('Input: ')
#print(input_list)
input_list = input_list.split()

if not input_list:
    print("The list is empty")
    print("Press any key to exit")
    input()
    exit()

input_list = list(map(int,input_list)) #convert list to int
money = input_list[0]
coins = input_list[1:len(input_list)]

coins.sort()
coins.reverse()
sum_val = 0
coin_quantity = []

for i in range(len(coins)):
    if sum_val >= money:
        coin_quantity = i+1
        break
    sum_val += coins[i]

if not coin_quantity:
    print("not enough coins")
else: 
        print("Output: ", coin_quantity)