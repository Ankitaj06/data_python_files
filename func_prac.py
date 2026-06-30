def calculate_avg(numbers):
    return sum(numbers) /len(numbers)

marks = [85,90,95,70,75]
print(calculate_avg(marks))

#list comprehension
squares = [x**2 for x in range(1,9) ]
print(squares)

evennum = [x for x in range(20) if x%2 ==0]
print(evennum)