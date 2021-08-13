def grader(s:list, a:list) -> None:
    name = []
    answer_sheet = []
    score = []

    for i in s:
        name.append(i.split(',')[0])
        answer_sheet.append(i.split(',')[1])


    for i in range(len(answer_sheet)):
        correct = 0
        for j in range(len(a)):
            if int(answer_sheet[i][j]) == a[j]:
                correct += 1
        score.append(correct)
    
    score_sort = score[:]
    score_sort.sort(reverse=True)
    for idx, i in enumerate(score_sort):
        print(f'학생:{name[score.index(i)]} 점수:{i*10}점 {idx+1}등')



def main():
    s = ['김갑,3242524215', '이을,3242524223', '박병,2242554131', '최정,4245242315', '정무,3242524315']
    a = [3,2,4,2,5,2,4,3,1,2]
    grader(s, a)


if __name__ == '__main__':
    main()