def gugudan(number:int) -> None:
    print(f'{number}단')
    for i in range(1, 10):
        if i%2 == 1:
            if number*i <50:
                print(f'{number} X {i} = {number*i}')

def main():
    number = int(input('몇 단?:'))
    gugudan(number)

if __name__ == '__main__':
    main()