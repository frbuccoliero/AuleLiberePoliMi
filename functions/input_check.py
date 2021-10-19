import pytz
from datetime import datetime , timedelta
from utils.find_classrooms import MAX_TIME , MIN_TIME
from typing import Tuple


def location_check(message: str , location) -> bool:
    if message not in location:
        return False
    return True



def day_check(message:str , texts , lang) -> bool:
    current_date = datetime.now(pytz.timezone('Europe/Rome')).date()
    if message != texts[lang]["keyboards"]["today"] and message != texts[lang]["keyboards"]["tomorrow"]:
        chosen_date = datetime.strptime(message, '%d/%m/%Y').date()
        if chosen_date < current_date or chosen_date > (current_date + timedelta(days=6)):
            return False
    return True



def start_time_check(message:str) -> Tuple[bool, int]:
    start_time = 0
    try:
        start_time = int(message)
    except Exception:
        return (False,0)
    

    if start_time > MAX_TIME or start_time < MIN_TIME:
        return (False,0)
    return (True,start_time)


def end_time_check(message:str , start_time:int) -> Tuple[bool, int]:
    
    end_time = 0
    try:
        end_time = int(message)
    except Exception:
        return (False,0)    

    if int(start_time) >= end_time or end_time > MAX_TIME + 1:
        return (False,0)
    return (True,end_time)

def language_check(message ,texts):
    if message not in texts:
        return False
    return True


def time_check(message):
    time = 0
    try:
        time = int(message)
    except Exception as e:
        return False
    
    if time < 1 or time > 8:
        return False
    
    return True


