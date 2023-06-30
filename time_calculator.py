def add_time(start, duration, day_of_week=None):
    # Split the start string into the number and the time indicator.
    start_components = start.split()
    time_indicator_old = start_components[-1]

    # Split the time component of the string into hours and minutes.
    start_str = start_components[0].split(":")

    # Convert the hours and minutes into a floating-point number.
    hours, mins = [float(component) for component in start_str]
    start_float = hours + (mins / 60)
    
    # Convert the time into a 24-hour time.
    if (time_indicator_old == "PM") and (start_float < 12):
        start_float += 12
    elif (time_indicator_old == "AM") and (start_float >= 12):
        start_float -= 12

    # Split the duration into hours and minutes.
    hours, mins = duration.split(":")

    # Convert the hours and minutes into a floating-point number.
    duration_float = float(hours) + (float(mins) / 60)

    # Add start_float and duration_float.
    calculated_time = start_float + duration_float

    # Create a dictionary of days of the week and an integer to represent each 
    # one.
    days_of_week_names = [
        "Monday", "Tuesday", "Wednesday", 
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    days_of_week_dict = dict(zip(days_of_week_names, range(7)))

    # If the calculated_time resulted in the passing of at least one day, then 
    # the number of days that passed is saved to days_later and the new_time is
    # adjusted to correctly reflect the time.
    days_later = 0
    new_time_24 = calculated_time % 24
    if calculated_time >= 24:
        days_later = round(calculated_time / 24)

    # Identify whether the time is in the AM or PM.
    time_indicator_new = None
    if int(new_time_24) < 12:
        time_indicator_new = "AM"
    elif int(new_time_24) >= 12:
        time_indicator_new = "PM"

    # Convert the 24-hour time back into a 12-hour time.
    new_time_12_float = None
    if new_time_24 < 1:
        new_time_12_float = new_time_24 + 12
    elif (new_time_24 >= 1) and (new_time_24 < 13):
        new_time_12_float = new_time_24
    elif new_time_24 >= 13:
        new_time_12_float = new_time_24 % 12
    new_time_12_str = str(new_time_12_float)
    new_time_12_hours, new_time_12_mins = new_time_12_str.split(".")
    new_time_12_hours = round(float(new_time_12_hours))
    new_time_12_mins = round(float("0." + new_time_12_mins) * 60)

    # Convert the minutes into a string with a leading zero if the value is 
    # less than 10.
    if new_time_12_mins < 10:
        new_time_12_mins = "0" + str(new_time_12_mins)

    # If a day of the week was passed as a third argument, then the change in 
    # day is calculated
    new_day_of_week = None
    if day_of_week is not None:
        new_day_of_week_index = (days_of_week_dict[day_of_week.title()] + days_later) % 7
        for day, index in days_of_week_dict.items():
            if new_day_of_week_index == index:
                new_day_of_week = day

    # Create an appropriately formatted string.
    new_time_str = None
    if day_of_week is None:
        if days_later < 1:
            new_time_str = f"{new_time_12_hours}:{new_time_12_mins} {time_indicator_new}"
        elif days_later == 1:
            new_time_str = f"{new_time_12_hours}:{new_time_12_mins} {time_indicator_new} (next day)"
        elif days_later > 1:
            new_time_str = f"{new_time_12_hours}:{new_time_12_mins} {time_indicator_new} ({days_later} days later)"
    elif day_of_week is not None:
        if days_later < 1:
            new_time_str = f"{new_time_12_hours}:{new_time_12_mins} {time_indicator_new}, {new_day_of_week}"
        elif days_later == 1:
            new_time_str = f"{new_time_12_hours}:{new_time_12_mins} {time_indicator_new}, {new_day_of_week} (next day)"
        elif days_later > 1:
            new_time_str = f"{new_time_12_hours}:{new_time_12_mins} {time_indicator_new}, {new_day_of_week} ({days_later} days later)"        

    return new_time_str
