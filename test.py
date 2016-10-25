"""
tests for brevet equations
"""
import arrow
import acp_times

NOW = arrow.Arrow(2016, 5, 11, 8, 0)

def test_one():
	val = acp_times.open_time(0, 200, NOW.isoformat())
	if val == NOW.isoformat():
		print("true")
	else:
		print("now: " + NOW.isoformat())
		print("got: " + val)

def test_two():
	val = acp_times.close_time(0, 200, NOW.isoformat())
	if val == NOW.replace(hours = 1).isoformat():
		print("true")
	else:
		print("now: " + NOW.isoformat())
		print("got: " + val)

def test_three():
	val = acp_times.open_time(50, 200, NOW.isoformat())
	if val == NOW.replace(hours = 1, minutes = 28).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 1, minutes = 28).isoformat())
		print("got: " + val)

def test_four():
	val = acp_times.close_time(50, 200, NOW.isoformat())
	if val == NOW.replace(hours = 3, minutes = 21).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 3, minutes = 21).isoformat())
		print("got: " + val)

def test_five():
	val = acp_times.open_time(200, 200, NOW.isoformat())
	if val == NOW.replace(hours = 5, minutes = 52).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 5, minutes = 52).isoformat())
		print("got: " + val)

def test_six():
	val = acp_times.close_time(200, 200, NOW.isoformat())
	if val == NOW.replace(hours = 13, minutes = 30).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 13, minutes = 30).isoformat())
		print("got: " + val)

def test_seven():
	val = acp_times.open_time(210, 200, NOW.isoformat())
	if val == NOW.replace(hours = 5, minutes = 52).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 5, minutes = 52).isoformat())
		print("got: " + val)

def test_eight():
	val = acp_times.close_time(210, 200, NOW.isoformat())
	if val == NOW.replace(hours = 13, minutes = 30).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 13, minutes = 30).isoformat())
		print("got: " + val)

def test_nine():
	val = acp_times.open_time(300, 1000, NOW.isoformat())
	if val == NOW.replace(hours = 9).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 9).isoformat())
		print("got: " + val)

def test_ten():
	val = acp_times.close_time(300, 1000, NOW.isoformat())
	if val == NOW.replace(hours = 20).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 20).isoformat())
		print("got: " + val)

def test_eleven():
	val = acp_times.open_time(1000, 1000, NOW.isoformat())
	if val == NOW.replace(hours = 33, minutes = 5).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 33, minutes = 5).isoformat())
		print("got: " + val)

def test_twelve():
	val = acp_times.close_time(1000, 1000, NOW.isoformat())
	if val == NOW.replace(hours = 75).isoformat():
		print("true")
	else:
		print("now: " + NOW.replace(hours = 75).isoformat())
		print("got: " + val)


if __name__ == "__main__":
    # Standalone. 
    test_one()
    test_two()
    test_three()
    test_four()
    test_five()
    test_six()
    test_seven()
    test_eight()
    test_nine()
    test_ten()
    test_eleven()
    test_twelve()