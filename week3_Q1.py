def gugudan(number:int) -> None:
    '''
    구구단 함수 
    홀수만 출력하며 50 이하 값만 출력
    '''
    print(f'{number}단')
    for i in range(1, 10):
        if i%2 == 1:        # 나머지 연산을 통해 값이 1인 값 출력
            if number*i < 50:
                print(f'{number} X {i} = {number*i}')

def main():
    number = int(input('몇 단?:'))
    gugudan(number)

if __name__ == '__main__':
    main()