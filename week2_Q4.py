def bus_fare(age:int, method:str):
    if method == '카드':
        if age < 8:
            fare = '무료'