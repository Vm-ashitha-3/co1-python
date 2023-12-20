current_year = int(input("enter the current year"))
future_year = int(input("enter the future year"))
if (current_year<future_year):
    print("the years are")
    for year in range(current_year,future_year+1):
        if(year%4==0 and year%100!=0):
            print(year)
else:
    print("no future years found")

