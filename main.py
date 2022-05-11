from alarm import AlarmClock


what_is_the_current_time = AlarmClock()

what_is_the_current_time.set_current_time(input('What time would you like your alarm to be set for? '))

print(what_is_the_current_time.current_time)

change_current_time = AlarmClock()
change_current_time.set_alarm_time('7:00 AM')
print(change_current_time.set_time)


power_onoff_alarm = AlarmClock()

power_onoff_alarm.turn_alarm_on()

print(power_onoff_alarm.power)

power_onoff_alarm.turn_alarm_off()

print(power_onoff_alarm.power)