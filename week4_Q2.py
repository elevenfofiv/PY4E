def count_word(lines:str, find_word:str) -> None:
    lines_list = lines.strip().split('\n')
    with open('text.txt','a', encoding='utf-8') as f:
        for line in lines_list:
            f.writelines(line.strip()+'\n')
    count = 0
    for line in lines_list:
        if find_word in line:
            count += 1
    print(count)

def main():
    a = '''
    말 한마디에 천냥 빚을 갚는다고 했다. 
    대표팀 감독이라면 공식 석상에서 신중하게 판단하고 입을 열어야 한다. 
    온 국민의 기대와 응원 속 국제대회에 나서 아주 중요한 경기에서 패했다면 더욱 조심해야 한다.
    '''
    count_word(a, '을')

if __name__ =='__main__':
    main()