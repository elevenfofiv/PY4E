def sales_management(names:list, records:str) -> None:
    member_record_ave = []
    bonus_interview = {}
    bonus_interview['bonus'] = []
    bonus_interview['interview'] = []
    for i in range(len(names)):
        average = sum(records[i])/len(records[i])
        member_record_ave.append(average)
    average_record_sort = member_record_ave[:]
    average_record_sort.sort(reverse=True)
    for i in average_record_sort[0:2]:
        if i > 5:
            bonus_interview['bonus'].append(names[member_record_ave.index(i)])

    for i in average_record_sort[4:6]:
        if i < 3:
            bonus_interview['interview'].append(names[member_record_ave.index(i)])

    for bonus_name in bonus_interview['bonus']:
        print(f'보너스 대상자 {bonus_name}')

    for interview_name in bonus_interview['interview']:
        print(f'\n면담 대상자 {interview_name}')


def main():
    member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
    member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2],
    [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
    [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]
    sales_management(member_names, member_records)

if __name__ == '__main__':
    main()