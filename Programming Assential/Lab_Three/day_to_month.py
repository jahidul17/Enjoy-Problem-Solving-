days=int(input("Please enter the number of days:"))
month=days//30 # // for without floating
# month=days/30
day=days%30
# print("Conversion of {0} Days = {1} Month and {2} Days".format(days,int(month),day))
print("Conversion of {0} Days = {1} Month and {2} Days".format(days,month,day))

