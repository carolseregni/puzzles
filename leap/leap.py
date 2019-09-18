#on every year that is evenly divisible by 4
#  except every year that is evenly divisible by 100
#    unless the year is also evenly divisible by 400

def leap_year(year):
    div_4 = year % 4 == 0
    div_100 = year % 100 == 0
    div_400 = year % 400 ==0
    leap = ((div_4) & (not div_100)) | ((div_4) & (div_100) & (div_400)) 
    
    return leap

print(leap_year(2000))