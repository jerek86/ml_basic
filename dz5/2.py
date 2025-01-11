def is_valid_format(date):
   vec = date.split('.')
   return len(vec) == 3 and len(vec[0]) == 2 and len(vec[1]) == 2 and len(vec[2]) == 4

def is_leap_year(year) :
    if year % 400 == 0 :
        return True
    if year % 100 == 0 :
        return False
    if year % 4 == 0 :
        return True

    return False

def get_month_max_days(month, year) :
    if month == 2 :
        if is_leap_year(year) :
            return 29
        else :
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11 :
        return 30

    return 31

def is_valid_date(date):
    if not is_valid_format(date) :
        return False

    vec = date.split('.')
    day = int(vec[0])
    month = int(vec[1])
    year = int(vec[2])

    if not 1 <= month <= 12 :
        return False

    if not 1 <= day <= get_month_max_days(month, year) :
        return False

    return True


print('29.02.200 ->', is_valid_date('29.02.200'))
print('29.02.2000 ->', is_valid_date('29.02.2000'))
print('29.02.2001 ->', is_valid_date('29.02.2001'))
print('31.04.1962 ->', is_valid_date('31.04.1962'))