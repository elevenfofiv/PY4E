import random

def rsp(my:str) -> str:
    '''
    Main함수에서 전달 받은 0, 1, 2는 가위, 바위, 보로 변환
    가위, 바위, 보는 그대로 다시 Main 함수로 Return
    그 외 값을 Argument로 받을 경우에는 Return값이 정의 되지 않으므로 Error 발생
    '''
    if my == '0':
        my_rsp = '가위'
    elif my == '1':
        my_rsp = '바위'
    elif my == '2':
        my_rsp = '보'
    elif my in ['가위', '바위', '보']:
        my_rsp = my
    
    return my_rsp

def rsp_advanced(games:int) -> None:
    result = []                                     # 가위 바위 보 게임의 승부 결과를 저장하는 리스트
    for i in range(1, games+1):
        while 1:                                    # try except 구문을 이용해서 0,1,2,가위,바위,보 외 다른 입력값을 받았을 때, 재입력 진행
            my = input("가위 바위 보: ")
            try:
                my_rsp = rsp(my)                    # 0,1,2,가위,바위,보외 입력값을 받으면 rsp 함수에서 Return 시 Unbound Error 발생하게 됨으로 다시 재입력을 요청하게 됨
                break
            except:
                continue
        print(f'나:{my_rsp}')

        com_rsp_dict = {0:'가위', 1:'바위', 2:'보'} # 문제 힌트 가운데 Computer의 가위,바위,보를 randint 명령어를 사용함으로, 0,1,2를 Key값으로 가위,바위,보를 Value값을 갖는 Dict 정의
        com_rsp = com_rsp_dict[random.randint(0,2)] # randint를 통해 생성된 0~2사이의 값을 Key값으로 하는 Value값를 할당
        print(f'컴퓨터:{com_rsp}')

        '''
        가위 바위 보 게임의 Rule 정의
        '''

        # 무승부일 경우에는 result에 0을 추가
        # 내가 이겼을 때에는 result에 1을 추가
        # 컴퓨터가 이겼을 때에는 result에 2를 추가
        if com_rsp == '가위':
            if my_rsp == '가위':
                print(f'{i}번째 판 무승부')
                result.append(0)                    
            elif my_rsp == '바위':
                print(f'{i}번째 판 나의 승리!')
                result.append(1)
            elif my_rsp == '보':
                print(f'{i}번째 판 컴퓨터 승리!')
                result.append(2)

        elif com_rsp == '바위':
            if my_rsp == '가위':
                print(f'{i}번째 판 컴퓨터 승리!')
                result.append(2)
            elif my_rsp == '바위':
                print(f'{i}번째 판 무승부')
                result.append(0)
            elif my_rsp == '보':
                print(f'{i}번째 판 나의 승리!')
                result.append(1)

        elif com_rsp == '보':
            if my_rsp == '가위':
                print(f'{i}번째 판 나의 승리!')
                result.append(1)
            elif my_rsp == '바위':
                print(f'{i}번째 판 컴퓨터 승리!')
                result.append(2)
            elif my_rsp == '보':
                print(f'{i}번째 판 무승부')
                result.append(0)
    #print(result)
    print(f'나의 전적:{result.count(1)}승 {result.count(0)}무 {result.count(2)}패')     #count 메소드를 사용해서 result 내 0, 1, 2가 각각 몇개 있는지를 출력
    print(f'컴퓨터의 전적:{result.count(2)}승 {result.count(0)}무 {result.count(1)}패')

def main():
    games = int(input("몇 판을 진행하시겠습니까? : "))
    rsp_advanced(games)

if __name__ == '__main__':
    main()