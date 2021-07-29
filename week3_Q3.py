def find_even_number(n:int, m:int) -> None:
    number = [i for i in range(n, m+1) if i%2 == 0]
    print(number)
    for idx, i in enumerate(number):
        print(f'{i} 짝수')
        if idx == (len(number)-1)/2:
            print(f'{i} 중앙값')

def main():
    n = int(input("첫 번째 수 입력: "))
    m = int(input("두 번째 수 입력: "))
    find_even_number(n, m)

if __name__ == "__main__":
    main()