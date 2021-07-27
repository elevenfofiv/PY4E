def bus_fare(age:int, method:str) -> None:
    '''
    버스 요금 계산기
    '''
    if method == '카드':
        if age < 8:
            fare = '무료'
        elif (age >= 8) & (age < 14):
            fare = '450원'
        elif (age >= 14) & (age < 20):
            fare = '720원'
        elif (age > 20) & (age < 75):
            fare = '1200원'
        else:
            fare = '무료'
            
    elif method == '현금':
        if age < 8:
            fare = '무료'
        elif (age >= 8) & (age < 14):
            fare = '450원'
        elif (age >= 14) & (age < 20):
            fare = '1000원'
        elif (age > 20) & (age < 75):
            fare = '1300원'
        else:
            fare = '무료'
    print(f'나이: {age}세')
    print(f'지불유형:{method}')
    print(f'버스요금:{fare}')

def main():
    bus_fare(30, "현금")


if __name__ == '__main__':  # main함수 호출을 위한 부분
    main()