def count_prime_number(n:int, m:int) -> None:
    prime_number = []
    for i in range(n , m+1):
        if i == 1:
            pass
        elif i == 2 :
            prime_number.append(i)
        else:
            truth_table = []
            for j in range (2, i):
                if i%j == 0:
                    truth_table.append(0)
                else:
                    truth_table.append(1)
            print(truth_table)
            if 0 in truth_table:
                pass
            else:
                prime_number.append(i)
    print(prime_number)
    print(f'소수개수 {len(prime_number)}')



def main():
    n = int(input("첫 번째 수 입력: "))
    m = int(input("두 번째 수 입력: "))
    count_prime_number(n, m)

if __name__ == "__main__":
    main()