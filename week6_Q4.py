def good_customer(info:str) -> None:
    customer_dict = {}
    customer_dict['ID'] = []
    customer_dict['age'] = []
    customer_dict['tel'] = []
    customer_dict['sex'] = []
    customer_dict['region'] = []
    customer_dict['buying'] = []
    info = info.replace('x', '000-0000-0000')   # 전화번호를 000-0000-0000 양식으로 전환
    info = info.split(',')

    for idx, i in enumerate(info):  # 고객정보를 항목별로 customer_dict에 저장
        if idx%6 == 0:
            customer_dict['ID'].append(i)
        elif idx%6 == 1:
            customer_dict['age'].append(i)
        elif idx%6 == 2:
            customer_dict['tel'].append(i)
        elif idx%6 == 3:
            customer_dict['sex'].append(i)
        elif idx%6 == 4:
            customer_dict['region'].append(i)
        elif idx%6 == 5:
            customer_dict['buying'].append(int(i))

    print(customer_dict)

    coupon_customer = {}    # 할인 쿠폰 받을 고객 정보를 저장할 Dictionary 선언
    coupon_customer['ID'] = []
    coupon_customer['age'] = []
    coupon_customer['tel'] = []
    coupon_customer['sex'] = []
    coupon_customer['region'] = []
    coupon_customer['buying'] = []

    for idx, i in enumerate(customer_dict['buying']):
        if (i >= 8) & (customer_dict['tel'][idx] != '000-0000-0000'):
            coupon_customer['ID'].append(customer_dict['ID'][idx])
            coupon_customer['age'].append(customer_dict['age'][idx])
            coupon_customer['tel'].append(customer_dict['tel'][idx])
            coupon_customer['sex'].append(customer_dict['sex'][idx])
            coupon_customer['region'].append(customer_dict['region'][idx])
            coupon_customer['buying'].append(customer_dict['buying'][idx])

    for i in range(len(coupon_customer['ID'])):
        print(f'할인쿠폰을 받을 회원 정보 아이디:{coupon_customer["ID"][i]},나이:{coupon_customer["age"][i]},전화번호:{coupon_customer["tel"][i]},성별:{coupon_customer["sex"][i]},지역:{coupon_customer["region"][i]},구매횟수:{coupon_customer["buying"][i]}')


def main():
    info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
    good_customer(info)

if __name__ =='__main__':
    main()
