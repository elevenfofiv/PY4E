import random

def bs31():
    bs31_list = []
    print('베스킨라빈스 써리원 게임')
    while 1:
        my_turn = input("my turn - 숫자를 입력하세요: ")
        my_turn = [int(i) for i in my_turn.split(' ')]
        if len(my_turn) > 3 :
            print('다시 입력 하시오')
            continue
        elif (len(bs31_list) != 0):
            if my_turn[0] < bs31_list[-1]:
                print('다시 입력 하시오')
                continue

        for i in my_turn:
            bs31_list.append(i)
        print(f'현재숫자: {bs31_list[-1]}')
        if bs31_list[-1] >= 31:
            print('컴퓨터의 승리')
            break

        computer_turn_num = random.randint(1,3)
        for i in range(computer_turn_num):
            computer_turn = bs31_list[-1] + 1
            print(f'컴퓨터 숫자 : {computer_turn}')
            bs31_list.append(computer_turn)
        print(f'현재 숫자: {bs31_list[-1]}')
        if bs31_list[-1] >= 31:
            print('나의 승리')
            break

def main():
    bs31()

if __name__ == '__main__':
    main()



