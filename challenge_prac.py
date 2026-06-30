

def total_sales(number):
    return sum(number)
sales = [45000, 52000, 48000, 61000, 55000, 49000]
print("This is total monthly sales",total_sales(sales))

def avg_sales(number):
    return sum(number)/len(number)
print("This is average monthly sales ",avg_sales(sales))

def highest_sales(number):
    return number.index(max(number))
print("highest sales ",highest_sales(sales))

average = avg_sales(sales)

def month_above_avg(number):
    average = sum(number)/len(number)

    for i in range(len(number)):
        if number[i] > average:
            print(i)

print(month_above_avg(sales))