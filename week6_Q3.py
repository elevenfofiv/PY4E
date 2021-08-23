def stock_profit(stocks:str, sells:list) -> None:
    stocks = stocks.split(',')
    stocks = [i.split('/') for i in stocks]
    stocks_dict = {}
    stocks_dict['name'] = []
    stocks_dict['amount'] = []
    stocks_dict['buy_price'] = []
    stocks_dict['sell_price'] = []
    stocks_dict['profit_rate'] = []

    for i in stocks:
        stocks_dict['name'].append(i[0])
        stocks_dict['amount'].append(int(i[1]))
        stocks_dict['buy_price'].append(int(i[2]))

    for i in sells:
        stocks_dict['sell_price'].append(i)

    for i in range(len(sells)):
        profit_rate = ((stocks_dict['sell_price'][i] * stocks_dict['amount'][i])/(stocks_dict['buy_price'][i] * stocks_dict['amount'][i]) * 100) - 100
        stocks_dict['profit_rate'].append(profit_rate)

    profit_sort = stocks_dict['profit_rate'][:]
    profit_sort.sort(reverse=True)

    for i in profit_sort:
        name = stocks_dict['name'][stocks_dict['profit_rate'].index(i)]
        print(f'{name}의 수익률 {i:.3}')


def main():
    stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
    sells = [82000, 160000, 835000, 410000]

    stock_profit(stocks, sells)

if __name__ =='__main__':
    main()