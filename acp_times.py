"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import Math
import dateutil.parser

MAX_SPEED = {"200":34, "300":32, "400":30, "600":28, "1000":26`}
MIN_SPEED = {"200-400":15, "600":11.428, "1000":13.333}
FINISH_TIME = {"200":13.5, "300":20, "400":27, "600":40, "1000":75}

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#



INC_DIST = 200 #increment of distance to decrementing speed
def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    con_dist = control_dist_km
    brev_dist = brevet_dist_km
    brev_strt = brevet_start_time
    speed = MXA_SPEED[str(brev_dist)]
    total_time = 0.0
    hours_to_open = 0
    mins_to_open = 0
    loop_count = Math.ceil(condist/INC_DIST) #for while loop
    i = 0 # for while loop

    # while the distance needed to be traveled is greater than 200 km
    # the max speed will decriment by 2 km/hr 
    # decrement con_dist to get out of the initial while loop
    if brev_dist < con_dist:
      con_dist = brev_dist
    while con_dist > INC_DIST:
      while i < loop_count:
        total_time += INC_DIST/speed
        con_dist -= INC_DIST
        if speed > MAX_SPEED["1000"]
          speed = speed - 2

    # final (or only) time added
    total_time  += INC_DIST/speed

    # total hours
    hours_to_open = int(total_time)

    # mins in fraction of a hours
    mins_to_open = total_time - hours_to_open
    # mins  
    mins_to_open = Math.ceil(mins_to_open * 60)

    # parse ISO 8601 format
    date_time_format = dateutil.parser.parse(brev_strt)

    # reformat to arrow
    arrow_format_date = arrow.fromdatetime(date_time_format)

    #set open time
    open_time = arrow_format_date.replace(hours =+ hours_to_open, minutes =+ mins_to_open)

    return open_time.isoformat()

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    con_dist = control_dist_km
    brev_dist = brevet_dist_km
    brev_strt = brevet_start_time
    total_time = 0.0
    hours_to_close = 0
    mins_to_close = 0

    if brev_dist > con_dist:

    while(con_dist > 600):

      while(con_dist > 1000):
        # to get to 1000 km
        i = (con_dist - 1000)
        total_time += i/MIN_SPEED["1000"]
        con_dist -= i
        # end while

      # to get to 600 km
      j = (con_dist - 600)
      total_time += j/MIN_SPEED["600"]
      con_dist -= j
      # end while

      total_time += con_dist/MIN_SPEED["200-400"]

      # total hours
      hours_to_close = int(total_time)

      # mins in fraction of a hours
      mins_to_close = total_time - hours_to_close
      # mins  
      mins_to_close = Math.ceil(mins_to_close * 60)

      # parse ISO 8601 format
      date_time_format = dateutil.parser.parse(brev_strt)

      # reformat to arrow
      arrow_format_date = arrow.fromdatetime(date_time_format)

    else:
      hours_to_close = int(FINISH_TIME[str(brev_dist)])
      mins_to_close = Math.ceil((FINISH_TIME[str(brev_dist)] - hours_to_close) * 60)

    #set open time
    open_time = arrow_format_date.replace(hours =+ hours_to_close, minutes =+ mins_to_close)

    return open_time.isoformat()


