# fill in the missing code

def seconds_since_midnight(hour, minutes, seconds):
	if hour > 24 and hour < 0:
		return 'Invalid input for hour'

	elif minutes > 59 and minutes < 1:
		return 'Invalid input for hour'

	elif seconds > 59 and seconds < 0:
		return'Invalid input for seconds'

	else:
		hour_in_seconds = hour * 3600
		minute_in_seconds = minutes * 60
		output = seconds + hour_in_seconds + minute_in_seconds

		return output

print(seconds_since_midnight(1, 30, 45))