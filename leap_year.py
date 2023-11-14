#Create a function that checks if given year is a leap year
#Use the rules that define leap years (divisible by 4, not by 100 unless also by 400)

def is_leap_year(year):
    return (year%4==0 and year%100!=0) or year%400==0

print(is_leap_year(2100))