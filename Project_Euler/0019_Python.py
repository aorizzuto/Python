
# Project Euler: 19
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime

def euler_19(day,start,end): 
  cont = 0

  for year in range(int(start),int(end)+1):
    for month in range(1,13):
      day_name = datetime.date(year, month, 1)
      if day_name.strftime('%A') == day:
        cont+=1
  return cont


##############################################

if __name__ == "__main__":
  a = euler_19('Sunday','1901','2000')
  print("Cantidad de Domingos:\t{}".format(a))
    
##############################################

"""
Cantidad de Domingos:   171
"""

