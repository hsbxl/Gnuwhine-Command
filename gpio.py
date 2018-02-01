import RPi.GPIO as GPIO
import argparse
import sched
import time

parser = argparse.ArgumentParser()
scheduler = sched.scheduler(time.time, time.sleep)
pumps = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

# BCM GPIO pinout
p1 = 27
p2 = 17
p3 = 23
p4 = 24
p5 = 25
p6 = 16
p7 = 26
p8 = 22

GPIO.setup(p1, GPIO.OUT)
GPIO.setup(p2, GPIO.OUT)
GPIO.setup(p3, GPIO.OUT)
GPIO.setup(p4, GPIO.OUT)
GPIO.setup(p5, GPIO.OUT)
GPIO.setup(p6, GPIO.OUT)
GPIO.setup(p7, GPIO.OUT)
GPIO.setup(p8, GPIO.OUT)

i = 0
while i < len(pumps):
    parser.add_argument('--' + pumps[i])
    i += 1

def stop_pump1(pump):
    GPIO.output(p1, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump2(pump):
    GPIO.output(p2, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump3(pump):
    GPIO.output(p3, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump4(pump):
    GPIO.output(p4, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump5(pump):
    GPIO.output(p5, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump6(pump):
    GPIO.output(p6, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump7(pump):
    GPIO.output(p7, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump8(pump):
    GPIO.output(p8, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()


args = parser.parse_args()

#pump1
if args.p1:
    GPIO.output(p1, GPIO.HIGH)
    print 'start pump 1 @', time.time()
    scheduler.enter(float(args.p1), 1, stop_pump, ('1'))

#pump2
if args.p2:
    GPIO.output(p2, GPIO.HIGH)
    print 'start pump 2 @', time.time()
    scheduler.enter(float(args.p2), 1, stop_pump, ('2'))

#pump3
if args.p3:
    GPIO.output(p3, GPIO.HIGH)
    print 'start pump 3 @', time.time()
    scheduler.enter(float(args.p3), 1, stop_pump, ('3'))

#pump4
if args.p4:
    GPIO.output(p4, GPIO.HIGH)
    print 'start pump 4 @', time.time()
    scheduler.enter(float(args.p4), 1, stop_pump, ('4'))

#pump5
if args.p3:
    GPIO.output(p5, GPIO.HIGH)
    print 'start pump 5 @', time.time()
    scheduler.enter(float(args.p5), 1, stop_pump, ('5'))

#pump6
if args.p3:
    GPIO.output(p6, GPIO.HIGH)
    print 'start pump 6 @', time.time()
    scheduler.enter(float(args.p6), 1, stop_pump, ('6'))

#pump7
if args.p7:
    GPIO.output(p7, GPIO.HIGH)
    print 'start pump 7 @', time.time()
    scheduler.enter(float(args.p3), 1, stop_pump, ('7'))

#pump8
if args.p8:
    GPIO.output(p8, GPIO.HIGH)
    print 'start pump 8 @', time.time()
    scheduler.enter(float(args.p8), 1, stop_pump, ('8'))


scheduler.run()