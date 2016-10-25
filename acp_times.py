"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math
import dateutil.parser

MAX_SPEED = {"200":34, "400":32, "600":30, "1000":28, "1300":26}
MIN_SPEED = {"200-600":15, "1000":11.428, "1300":13.333}
FINISH_TIME = {"200":13.5, "300":20, "400":27, "600":40, "1000":75}

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#

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
    speed = MAX_SPEED[str(brev_dist)]
    total_time = 0.0
    hours_to_open = 0
    mins_to_open = 0

    # parse ISO 8601 format
    date_time_format = dateutil.parser.parse(brev_strt)

    # reformat to arrow
    arrow_format_date = arrow.Arrow.fromdatetime(date_time_format)

    i = 0 # for while loop



    if con_dist == 0:
      return arrow_format_date.isoformat()

    # while the distance needed to be traveled is greater than 200 km
    # the max speed will decriment by 2 km/hr 
    # decrement con_dist to get out of the initial while loop
    if brev_dist < con_dist:
      con_dist = brev_dist
      
    while con_dist > 200: 

      while con_dist > 400:

        while con_dist > 600:

          while con_dist > 1000:
            # to get to 1000 km
            a = (con_dist - 1000)
            total_time += a/MAX_SPEED["1300"]
            con_dist -= a
            # end while

          # to get to 600 km
          b = (con_dist - 600)
          total_time += b/MAX_SPEED["1000"]
          con_dist -= b
          # end while

        # to get to 400 km
        c = (con_dist - 400)
        total_time += c/MAX_SPEED["600"]
        con_dist -= c
        # end while

      # to get to 300 km
      d = (con_dist - 200)
      total_time += d/MAX_SPEED["400"]
      con_dist -= d
      # end while


    # final (or only) time added
    total_time  += con_dist/MAX_SPEED["200"]

    # total hours
    hours_to_open = int(total_time)

    # mins in fraction of a hours
    mins_to_open = total_time - hours_to_open
    # mins  
    mins_to_open = int(mins_to_open * 60)

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

    # parse ISO 8601 format
    date_time_format = dateutil.parser.parse(brev_strt)

    # reformat to arrow
    arrow_format_date = arrow.Arrow.fromdatetime(date_time_format)

    if con_dist == 0:
      return arrow_format_date.replace(hours = 1).isoformat()

    if brev_dist > con_dist:

      while con_dist >= 600:

        while con_dist > 1000:
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

      total_time += con_dist/MIN_SPEED["200-600"]

    else:
      total_time = FINISH_TIME[str(brev_dist)]

    # total hours
    hours_to_close = int(total_time)

    # mins in fraction of a hours
    mins_to_close = total_time - hours_to_close
    # mins  
    mins_to_close = math.ceil(mins_to_close * 60)

    #set open time
    open_time = arrow_format_date.replace(hours =+ hours_to_close, minutes =+ mins_to_close)

    return open_time.isoformat()


