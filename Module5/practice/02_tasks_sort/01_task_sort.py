numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 13  # Задайте самостоятельно, выбрав произвольное число
sum_ = 0
for i in range (len(numbers)):
    if numbers[i] > a:
        sum_ += numbers[i]
print(sum_)
