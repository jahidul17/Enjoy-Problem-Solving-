def leap_year(year):
    # leap=False
    # if year%4==0:
    #     leap= True
    #     if year%100!=0:
    #         leap= False
    #         if year%400==0:
    #             leap= True
    # return leap
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    else:
        return False

year=int(input())
print(leap_year(year))

