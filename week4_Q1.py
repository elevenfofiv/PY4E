def make_comma(number:int) -> None:
    number_str = str(number)    # int형을 str형으로 변환
    number_intermediate = ','.join(number_str)  #변환된 str형의 모든 문자 사이에 ',' 삽입
    number_split = number_intermediate.split(',')   # ','를 seperator로 해서 각 숫자를 List에 저장
    number_add = int(len(number_str)/3) # Comma 추가로 인해 List의 Length가 길어짐으로 얼마나 추가 되어야 하는지 계산
    for idx, i in enumerate(range(-1, -(len(number_split)+1+number_add), -1)):  #range 함수과 enumerate함수를 이용해서 -1부터 -Len(number_split)-number_add까지 숫자가 저장된 list의 idx와 value 받음
        if (idx/2)%2 == 1:  # range(-1, -(len(number_split)+1+number_add)의 idx 값을 2로 나눈 후 2로 나머지 계산을 했을 때 1이면
            number_split.insert(i, ',')     #number_split List의 i index에 ',' 삽입
        else:
            pass
    number_final = "".join(number_split)    #List의 Value 합치기
    print(number_final)

def main():
    make_comma(-2093402938093825023904820)


if __name__ == '__main__':
    main()

