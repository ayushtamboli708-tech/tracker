def check_season(month):
    summar = ["march","april","june","may"]
    winter = ["november","december","january","frburary"]
    spring = ["augast","september","octuber","july"]
    if month in summar:
        return "summer"
    elif month in winter:
        return "winter"
    else :
        return spring
try:
    mon = input("enter the month  ")
except error as err:
    print(f"error '{err}")
else:        
    print(check_season(mon))        