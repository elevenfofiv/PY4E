import random

def rcp(my:str) -> str:
    if my == '0':
        my_rsp = '가위'
    elif my == '1':
        my_rsp = '바위'
    elif my == '2':
        my_rsp = '보'
    elif my in ['가위', '바위', '보']:
        my_rsp = my
    
    return my_rsp


my = input("가위 바위 보\n")
my_rsp = rcp(my)
print(f'나:{my_rsp}')


com_rsp_dict = {0:'가위', 1:'바위', 2:'보'}
com_rsp = com_rsp_dict[random.randint(0,2)]
print(f'컴퓨터:{com_rsp}')

if com_rsp =='가위':
    if my_rsp == '가위':
        print('무승부')
    elif my_rsp == '바위':
        print('나의 승리!')
    elif my_rsp == '보':
        print('컴퓨터 승리!')

elif com_rsp =='바위':
    if my_rsp == '가위':
        print('컴퓨터 승리!')
    elif my_rsp == '바위':
        print('무승부')
    elif my_rsp == '보':
        print('나의 승리!')

elif com_rsp =='보':
    if my_rsp == '가위':
        print('나의 승리!')
    elif my_rsp == '바위':
        print('컴퓨터 승리')
    elif my_rsp == '보':
        print('무승부')

