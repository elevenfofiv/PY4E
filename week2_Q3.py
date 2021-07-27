def grader(name:str, score:int) -> None:
    '''
    점수에 따른 학점 배정 함수
    '''
    if (score >= 95) & (score <= 100):
        grade = 'A+'
    elif (score >= 90) & (score < 94):
        grade = 'A'
    elif (score >= 85) & (score < 89):
        grade = 'B+'
    elif (score >= 80) & (score < 84):
        grade = 'B'
    elif (score >= 75) & (score < 79):
        grade = 'C+'
    elif (score >= 70) & (score < 74):
        grade = 'C'
    elif (score >= 65) & (score < 69):
        grade = 'D+'
    elif (score >= 60) & (score < 64):
        grade = 'D'
    elif (score < 64):
        grade = 'F'
    
    print(f'학생이름:{name}')
    print(f'점수:{score}')
    print(f'학점:{grade}')

def main():
    grader('이호창', 99)


if __name__ == '__main__':  #main함수를 호출하기 위한 부분
    main()
    