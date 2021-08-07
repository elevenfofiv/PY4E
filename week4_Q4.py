def check_id(id_number:str) -> None:
    if len(id_number) != 14 or id_number[6] != '-':
        print("잘못된 번호입니다")
        raise ValueError
    else:
        if int(id_number[0:2]) <= 21:
            answer = input("2000년 이후 출생자 입니까? 맞으면 o 틀리면 x : ")
            if answer == 'o':
                if id_number[7] not in ['3', '4']:
                    print("잘못된 번호입니다")
                    raise ValueError
                elif id_number[7] == '3':
                    gender = '남성'
                elif id_number[7] == '4':
                    gender = '여성'
            elif answer == 'x':
                if id_number[7] not in ['1', '2']:
                    print("잘못된 번호입니다")
                elif id_number[7] == '1':
                    gender = '남성'
                elif id_number[7] == '2':
                    gender = '여성'
        else:
            if id_number[7] not in ['1', '2']:
                print("잘못된 번호입니다")
            elif id_number[7] == '1':
                gender = '남성'
            elif id_number[7] == '2':
                gender = '여성'

        print(f'{id_number[0:2]}년{id_number[2:4]}월 {gender}')

def main():
    while True:
        try:
            a = input("a: ")
            check_id(a)
            break
        except:
            print('올바른 번호를 넣어주세요')
            continue

if __name__ == '__main__':
    main()

