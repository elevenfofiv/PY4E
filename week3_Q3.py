def find_even_number(n:int, m:int) -> None:
    number = [i for i in range(n, m+1) if i%2 == 0]     # list comprehension을 통해 n부터 m까지의 짝수로만 이뤄진 list 생성
    # print(number)     # 코드 Debug용
    for idx, i in enumerate(number):        #enumerate를 이용해서 리스트 요소의 index와 value를 함께 받음.      
        print(f'{i} 짝수')
        if idx == (len(number)-1)/2:        #enumerate를 이용해서 전달 받은 idx값이 리스트의 정중앙에 있는 index와 같으면 중앙값 출력
            print(f'{i} 중앙값')

def main():
    n = int(input("첫 번째 수 입력: "))
    m = int(input("두 번째 수 입력: "))
    find_even_number(n, m)

if __name__ == "__main__":
    main()