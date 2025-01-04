total_days = int(input())

total_weeks = total_days // 7
rest_days = total_days % 7

print((total_weeks * 2) + max(0, rest_days - 5))
