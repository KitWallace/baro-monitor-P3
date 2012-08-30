points = ["N","NNE","NE","ENE","E","ESE","SE" ,"SSE" ,"S", "SSW","SW","WSW","W", "WNW","NW","NNW","N"]

def deg_to_dms(dd,latlong) :

   if (latlong == "lat"):
      if (dd< 0) :
         dir = "West"
      else :
         dir = "East"
   else :
      if (dd< 0) :
         dir = "South"
      else :
         dir = "North"

   dd = abs(dd)
   deg = int(dd)
   min = (dd - deg ) * 60
   dmin = int(min)
   sec = int((min - dmin) * 60)
   return "".join([str(deg)," degrees ", str(dmin), "minutes ",str(sec) , " seconds ", dir])

def degree_to_compass_point(deg) :
   dp = deg + 11.25
   dp = dp % 360 
   dp = int(dp // 22.5)
   return points[dp]

def trend_to_tendancy(trend) :
    """ trend is the trend over 1 hour """
    
    atrend = abs(trend)

    if atrend <= 0.033 :
      tendancy = "steady"
    elif atrend <= 0.5 :
      tendancy = "slowly"
    elif atrend <= 1.1 :
      tendancy = ""
    elif atrend <= 2.0 :
      tendancy = "quickly"
    elif atrend > 2 :
      tendancy = "very rapidly" 

    if atrend <= 0.033 :
      pass
    elif trend > 0 : 
      tendancy = "rising " + tendancy
    else :
      tendancy = "falling " + tendancy

    return tendancy



