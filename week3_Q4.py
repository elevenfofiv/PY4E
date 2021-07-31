def count_prime_number(n:int, m:int) -> None:
    prime_number = []
    for i in range(n , m+1):
        if i == 1:  # 1은 소수가 아니므로 Pass
            pass
        elif i == 2 : #2는 소수가 맞으므로 2가 입력되면 prime_number 리스트에 append함
            prime_number.append(i)
        else:
            result_table = []
            for j in range (2, i):
                if i%j == 0:
                    result_table.append(0)
                else:
                    result_table.append(1)
            print(result_table)
            if 0 in result_table:
                pass
            else:
                prime_number.append(i)  # result_table에 1만 있을 때, 해당 i값을 Prime number list에 추가
    # print(prime_number)   # 코드 debug용
    print(f'소수개수 {len(prime_number)}') # 최종 prime_number의 Length를 구해서 소수의 개수로 출력



def main():
    '''
    두 정수값을 입력 받아 소수 개수 구하는 함수
    '''
    n = int(input("첫 번째 수 입력: "))
    m = int(input("두 번째 수 입력: "))
    count_prime_number(n, m)

if __name__ == "__main__":
    main()