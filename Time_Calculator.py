def add_time(start, duration, startDay=''):

    
    dayspassed = ''
    finalday = ''
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    # Get Hours , Minutes and the moment of the day of the initial time
    srt = start.split(':')
    srth = int(srt[0])
    srtm = int(srt[1][:2])
    momento = srt[1][3:]
    # Get Hours and minutes of the duration passed
    drt = duration.split(':')
    drth = int(drt[0])
    drtm = int(drt[1])
    # Add the initial time to the duration passed
    fh = srth + drth
    fm = srtm + drtm
    # Add one hour if the total of minutes is more than 60
    if fm>59:
        fh += 1
        fm = fm%60
    # Check to see how much days passed since the initial time
    x = (fh-12+24)//24
    if startDay != '':
      finalday = ', '+startDay.lower().capitalize()

    if momento == 'PM' and fh > 11 :
        if startDay != '':
          finalday = ', '+week[(week.index(startDay.lower().capitalize())+x)%7]
        if fh < 36:
            dayspassed = ' (next day)'
        elif momento == 'PM' and fh >= 36:
            dayspassed = f' ({x} days later)'
        
    if momento == 'AM' and fh > 23 :
        if startDay != '':
          finalday = ', '+week[(week.index(startDay.lower().capitalize())+x)%7]
        if fh < 48:
            dayspassed = ' (next day)'
        elif fh >= 48:
            dayspassed = f' ({x} days later)'   
        
    # Never let the hour to be more than 12
    if fh > 12:
        fh = fh%12
        if fh%12==0:
          fh = 12

    # Check the moment of the day of the final hour
    if drth%24 >= 12-srth and drth%24 < 24-srth or fh%12==0 :
        if momento == 'PM':

            momento = 'AM'
        else:
            momento = 'PM'

    new_time = f'{fh}:{str(fm).zfill(2)} {momento}{finalday}{dayspassed}'

    return new_time

print(add_time("11:59 PM", "24:05"))

# 12:04 AM (2 days later)