class Clock:
    def sayTime(self, time):
        if time == '07:00:00':
           return 'wake up!'
        if time[3:8] == '00:00':
            return 'beep'
        elif time[6:8] == '00':
            return "tick"