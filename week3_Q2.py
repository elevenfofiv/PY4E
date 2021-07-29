import random

def rsp_advanced(games:int) -> None:
    for i in range(1, games+1):
        rsp



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

def main():
    '''
    가위 바위 보의 메인 함수
    '''
    # while 문과 Try - except를 사용하여 0,1,2,가위,바위,보 중 하나를 입력 받을 때까지 계속 진행
    while 1:
        my = input("가위 바위 보:")
        try: 
            my_rsp = rsp(my)
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

    if com_rsp == '가위':
        if my_rsp == '가위':
            print('무승부')
        elif my_rsp == '바위':
            print('나의 승리!')
        elif my_rsp == '보':
            print('컴퓨터 승리!')

    elif com_rsp == '바위':
        if my_rsp == '가위':
            print('컴퓨터 승리!')
        elif my_rsp == '바위':
            print('무승부')
        elif my_rsp == '보':
            print('나의 승리!')

    elif com_rsp == '보':
        if my_rsp == '가위':
            print('나의 승리!')
        elif my_rsp == '바위':
            print('컴퓨터 승리')
        elif my_rsp == '보':
            print('무승부')

if __name__ == '__main__':  # main함수를 호출하기 위한 부분
    main()