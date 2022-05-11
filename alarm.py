class AlarmClock:

    def __init__(alarm):
        alarm.current_time = '12:00 AM'
        alarm.power = False
        alarm.set_time = '7:00 AM'

    def turn_alarm_on(alarm):
        alarm.power = True

    def turn_alarm_off(alarm):
        alarm.power = False

    def set_current_time(alarm, get_current_time):
        alarm.current_time = get_current_time
        

    def set_alarm_time(alarm, current_alarm_time):
        alarm.set_time = current_alarm_time
     