def wrong_guest_book(guest_book:str) -> None:
    guest_book_list = guest_book.strip().split('\n')
    with open('guest_book.txt', 'w', encoding='UTF-8') as f:
        for guest in guest_book_list:
            f.writelines(guest.strip()+'\n')
    for guest in guest_book_list:
        guest_list = guest.strip().split(',')
        if guest_list[1][0:3] != '010':
            print(f'잘못 쓴 사람: {guest_list[0]}')
            print(f'잘못 쓴 번호: {guest_list[1]}')
            print('\n')
        elif '-' not in guest_list[1]:
            print(f'잘못 쓴 사람: {guest_list[0]}')
            print(f'잘못 쓴 번호: {guest_list[1]}')
            print('\n')
        elif len(guest_list[1]) != 13:
            print(f'잘못 쓴 사람: {guest_list[0]}')
            print(f'잘못 쓴 번호: {guest_list[1]}')
            print('\n')

        else:
            pass

def main():
    guest_book = '''김갑,123456789
    이을,010-1234-5678
    박병,010-5678-111
    최정,111-1111-1111
    정무,010-3333-3333'''
    wrong_guest_book(guest_book)

if __name__ == '__main__':
    main()