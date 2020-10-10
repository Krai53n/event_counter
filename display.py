# author: Krai53n
# date: 08.10.20

from pyfiglet import Figlet as fig
from time import sleep
from os import system as sys
from random import choice
from colorama import init
from colorama import Fore, Style
init()


### CONSTANTS
FONT = 'slant' # if you whant look all fonts: pyfilget --list-fonts


### FUNCTIONS
def display(text = 'New Year?', font = FONT):
    '''Function accept text(time) and font
    return string with ascii symbols
    '''
    custom_fig = fig(font = FONT)
    print(custom_fig.renderText(text), end = '')

def clear():
    '''Function which clear
    what was before'''
    sys('clear')


if __name__ == '__main__':
    while 1:
        from count_time_to_event import count
        colors = ('RED', 'GREEN', 'YELLOW', 'BLUE',
                  'MAGENTA', 'CYAN', 'WHITE')
        r_clr = eval('Fore.RED')
        clear()
        print(eval('Fore.{}'.format(choice(colors))), end = '')
        date = count()
        date = '{}:{}:{}:{}'.format(
                                     date['days'],
                                     date['hours'],
                                     date['minutes'],
                                     date['seconds'])
        # 84:09:55:59
        display(date)
        sleep(1)