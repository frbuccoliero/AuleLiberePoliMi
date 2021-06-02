from .find_classrooms import find_classrooms
import datetime
from pprint import pprint

def _is_room_free(lessons , starting_time , ending_time):
    if len(lessons) == 0:
        return True
    for lesson in lessons:
        start = float(lesson['from'])
        end = float(lesson['to'])
        if starting_time < start and start < ending_time:
            return False
        if start < starting_time and end > starting_time:
            return False
    return True
        

def find_free_room(starting_time , ending_time , location , day , month , year):
    free_rooms = {}
    infos = find_classrooms(location , day , month , year)
    for building in infos:
        for room in infos[building]:
            lessons = infos[building][room]['lessons']
            if _is_room_free(lessons , starting_time , ending_time):
                if building not in free_rooms:
                    free_rooms[building] = []
                free_rooms[building].append(room)
    
    return free_rooms


if __name__ == "__main__":
    now = datetime.datetime.now()
    find_free_room(9 , 13 , 'MIA', 1 , 6 , 2021)