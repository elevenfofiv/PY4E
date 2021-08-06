def make_comma(number:int) -> None:
    number_str = str(number)
    number_intermediate = ','.join(number_str)
    number_split = number_intermediate.split(',')
    number_add = int(len(number_str)/3)
    print()
    print(number_add, (-(len(number_split)+1+number_add)))
    for idx, i in enumerate(range(-1, -(len(number_split)+1+number_add), -1)):
        # print(i)
        # if (int(i/(-3)) - abs(i%(-3))) == 1:
        if (idx/2)%2 == 1:
            print(i)
            number_split.insert(i, ',')
        else:
            pass
    number_final = "".join(number_split)
    print(number_final)

def main():
    make_comma(2093402938093825023904820)


if __name__ == '__main__':
    main()

