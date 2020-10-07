# author: Krai53n
# date: 05.10.25

import time

'''
TODO:
    + make event, not only New Year
    + make to check of difference between event and time in present
'''

### CONSTANTS
DATE_WITH_NEXT_YEAR = '01', '01' # 1 - month, 2 - day
DATE_DEADLINE = '2020-10-08' # year, month, day
DATE_WITH_NEXT_YEAR_OR_NOT = 1 # 1 - yes, 0 - no


### FUNCTIONS
def determine_event_date(date_with_next_year = DATE_WITH_NEXT_YEAR_OR_NOT):
    '''Function determine the date of New Year
    '''
    if date_with_next_year == 1:
        year = time.localtime(time.time())[0] + 1
        date_event = '{}-{}-{} 00:00:00'.format(year,
                                                   DATE_WITH_NEXT_YEAR[0],
                                                   DATE_WITH_NEXT_YEAR[1])
    else:
        date_event = DATE_DEADLINE + ' 00:00:00'
    return date_event

def count_start_of_epoch_to_event():
    '''Function count seconds with start of epoch
    till our date
    '''
    seconds = time.mktime(time.strptime(determine_event_date(),
                                            '%Y-%m-%d %H:%M:%S'))
    return seconds

def difference():
    '''Function count difference between
    seconds of new_year and seconds of our time
    '''
    our_time = time.time()
    epoch_to_event_sec = count_start_of_epoch_to_event()
    if epoch_to_event_sec > our_time:
        dif = epoch_to_event_sec - our_time
        return dif
    else:
        print('You paste not correct deadline\nPlease check it!'.upper())

def count():
    '''Function which count period of time till event
    '''
    seconds = difference()
    minutes = seconds // 60
    seconds = seconds % 60
    hours = int(minutes // 60)
    minutes = int(minutes % 60)
    days = int(hours // 24)
    hours = int(hours % 24)
    time_to_event = {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
    }

    return time_to_event
