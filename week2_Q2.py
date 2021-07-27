def yearly_payment(monthly_payment:float) -> None:
    '''
    연봉 계산 함수
    '''
    salary_before_tax = monthly_payment * 12    # 전달 받은 월급으로 세전 연봉 계산
    
    if salary_before_tax <= 1200:
        tax_rate = 0.06
    elif (salary_before_tax > 1200) and (salary_before_tax <= 4600):
        tax_rate = 0.15
    elif (salary_before_tax > 4600) and (salary_before_tax <= 8800):
        tax_rate = 0.24
    elif (salary_before_tax > 8800) and (salary_before_tax <= 15000):
        tax_rate = 0.35
    elif (salary_before_tax > 15000) and (salary_before_tax <= 30000):
        tax_rate = 0.38
    elif (salary_before_tax > 30000) & (salary_before_tax <= 50000):
        tax_rate = 0.4
    elif (salary_before_tax) > 50000:
        tax_rate = 0.42

    salary_after_tax = salary_before_tax * (1 - tax_rate)
    
    print(f'세전 연봉:{int(salary_before_tax)}만원')
    print(f'세후 연봉:{int(salary_after_tax)}만원') # 소숫점 이하 단위는 버림

def main():
    monthly_payment = float(input('monthly_payment='))
    yearly_payment(monthly_payment)

if __name__ == '__main__':  # Main 함수를 호출하기 위한 부분
    main()