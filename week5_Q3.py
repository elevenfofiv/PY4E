import random

def guess_numbers():
    numbers = []
    for i in range(3):
        number = random.randint(0, 100)
        numbers.append(number)

    numbers.sort()
    game = 0
    success = 0
    my_numbers = []
    print(numbers)

    while 1:
        game += 1
        print(f'{game}차 시도')
        my_number = int(input('숫자를 예측해 보세요:'))
        if my_number in my_numbers:
            print("이미 예측에 사용한 숫자입니다.")
            continue
        else:
            my_numbers.append(my_number)

        if my_number in numbers:
            success += 1
            if numbers.index(my_number) == 0:
                decision = '최소값'
            elif numbers.index(my_number) == 1:
                decision = '중간값'
            elif numbers.index(my_number) == 2:
                decision = '최댓값'
            
            print(f'숫자를 맞추셨습니다. {my_number}는 {decision}입니다')

        else:
            print(f'{my_number}는 없습니다')
            if game == 5:
                if my_number < numbers[0]:
                    print(f'최솟값은 {my_number}보다 큽니다')
                else:
                    print(f'최소값은 {my_number}보다 작습니다')

            elif game == 10:
                if my_number < numbers[2]:
                    print(f'최댓값은 {my_number}보다 큽니다')
                else:
                    print(f'최대값은 {my_number}보다 작습니다')

        if success == 3:
            print('게임 종료')
            print(f'{game}번 시도만에 예측 성공')
            break

def main():
    guess_numbers()


if __name__ == '__main__':
    main()