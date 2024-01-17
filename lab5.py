time_in = float(input('time in: '))
time_out = float(input('time out: '))
minute_in = (time_in * 100 )
minute_out = (time_out * 100 )
n1 = minute_out - minute_in
hour_ = n1 //100
total_minute = n1%100
if(total_minute > 60 ):
   total_minute -= 40
total_time = int((hour_*60)+ total_minute)
first = 40
print(total_time)
if(total_time <= 30):
    print('You parked in for %d hour(s) and %d minute(s)'%(hour_,total_minute))
    print('You will not be chared !!!.')
    print('You will pay 0 bath.')
elif(total_time > 30 and total_time <= 60 ):
    print('You parked in for %d hour(s) and %d minute(s)'%(hour_,total_minute))
    print('You will be chaared for the first 2 hour(s) !!!.')
    print('You will pay 40 bath.')
elif(total_time > 60 and total_time <= 120):
    print('You parked in for %d hour(s) and %d minute(s)'%(hour_,total_minute))
    print('You will be chaared for the first 2 hour(s) !!!.')
    print('You will pay 40 bath.')
elif(total_time > 120 and total_time <= 180):
    first += 100
    print('You parked in for %d hour(s) and %d minute(s)'%(hour_,total_minute))
    print('You will be chaared for the first 3 hour(s) !!!.')
    print('You will pay %d bath.' %(first))
elif(total_time > 180 and total_time <= 240):
    first += 200
    print('You parked in for %d hour(s) and %d minute(s)'%(hour_,total_minute))
    print('You will be chaared for the first 4 hour(s) !!!.')
    print('You will pay %d bath.' %(first))
elif(total_time > 240 and total_time <= 300):
    first += 300
    print('You parked in for %d hour(s) and %d minute(s)'%(hour_,total_minute))
    print('You will be chaared for the first 5 hour(s) !!!.')
    print('You will pay %d bath.' %(first))
elif(total_time > 300 and total_time <=  360):
    print('You parked in for %d hour(s) and %d minute(s)'%(hour_,total_minute))
    print('You will be chaared for the first 5 hour(s) !!!.')
    print('You will pay 500 bath.')
elif(total_time > 360):
    print('You parked in for %d hour(s) and %d minute(s)'%(hour_,total_minute))
    print('You will be chaared for the maximum rate !!!.')
    print('You will pay 2000 bath.')










