# author: Krai53n
# date: 05.10.25

import time

'''
TODO:
    - make event, not only New Year
    - make to check of difference between event and time in present
'''

def determine_new_year_date():
    '''Function determine the date of New Year
    '''
    year = time.localtime(time.time())[0] + 1
    date_new_year = '{}-01-01 00:00:00'.format(year)
    return date_new_year

def count_start_of_epoch_to_new_year():
    '''Function count seconds with start of epoch
    till our date
    '''
    seconds = time.mktime(time.strptime(determine_new_year_date(),
                                            '%Y-%m-%d %H:%M:%S'))
    return seconds

def difference():
    '''Function count difference between
    seconds of new_year and seconds of our time
    '''
    our_time = time.time()
    dif = count_start_of_epoch_to_new_year() - our_time
    return dif

def count():
    '''Function which count period of time till event
    '''
    seconds = difference()
    print(difference())
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