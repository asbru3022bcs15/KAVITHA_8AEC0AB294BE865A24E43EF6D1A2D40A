#leap year.
def isleapyear(year):
if (year%4==0 and year%100!=0): or year%400==0:
  return true
else:
  return false
  year=int(input("Enter a year:"))
  if is leap year(year):
print('{}is a leap year.'. format(year))
else:
print('{} is not a leap year.'. format(year))