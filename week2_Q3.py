def grader(name:str, score:int):
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
    
    return grade

def main():
    name = input('학생이름:')
    score = int(input('점수:'))
    print(f'학생이름:{name}')
    print(f'점수:{score}')
    print(f'학점:{grader(name,score)}')

if __name__ =='__main__':
    main()
    