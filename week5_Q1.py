import random

def bs31():
    bs31_list = []
    print('베스킨라빈스 써리원 게임')
    my_turn = input("my turn : ")
    my_turn = [int(i) for i in my_turn.split(' ')]
    if len(my_turn) > 4 :
        print('다시 입력 하시오')
    elif (len(bs31_list) != 0):
        if my_turn[0] < bs31_list[-1]:
            print('다시 입력 하시오')
    
    for i in my_turn:
        bs31_list.append(i)
    if bs31_list[-1] > 31:
        print('컴퓨터의 승리')

    computer_turn_num = random.randint(1,3)
    for i in range(computer_turn_num):
        computer_turn = bs31_list[-1] + 1
        bs31_list.append(computer_turn)
    
    if bs31_list[-1] > 31:
        print('나의 승리')


