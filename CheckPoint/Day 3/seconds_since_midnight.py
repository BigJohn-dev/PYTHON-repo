
def seconds_since_midnight(hours, minutes, seconds):
    if hours < 0 or minutes < 0 or seconds < 0:
        return "Invalid input: hours, minutes, and seconds must be non-negative."
    hour_in_seconds = 3600 * hours
    minute_in_seconds = 60 * minutes
    total_seconds = hour_in_seconds + minute_in_seconds + seconds
    return total_seconds

print(seconds_since_midnight(1, 30, 45))