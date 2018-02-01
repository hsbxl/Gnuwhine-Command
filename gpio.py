import RPi.GPIO as GPIO
import argparse
import sched
import time

parser = argparse.ArgumentParser()
scheduler = sched.scheduler(time.time, time.sleep)
pumps = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

# BCM GPIO pinout
pump1 = 27
pump2 = 17
pump3 = 23
pump4 = 24
pump5 = 25
pump6 = 16
pump7 = 26
pump8 = 22

GPIO.setup(pump1, GPIO.OUT)
GPIO.setup(pump2, GPIO.OUT)
GPIO.setup(pump3, GPIO.OUT)
GPIO.setup(pump4, GPIO.OUT)
GPIO.setup(pump5, GPIO.OUT)
GPIO.setup(pump6, GPIO.OUT)
GPIO.setup(pump7, GPIO.OUT)
GPIO.setup(pump8, GPIO.OUT)

i = 0
while i < len(pumps):
    parser.add_argument('--' + pumps[i])
    i += 1

def stop_pump1(pump):
    GPIO.output(pump1, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump2(pump):
    GPIO.output(pump2, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump3(pump):
    GPIO.output(pump3, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump4(pump):
    GPIO.output(pump4, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump5(pump):
    GPIO.output(pump5, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump6(pump):
    GPIO.output(pump6, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump7(pump):
    GPIO.output(pump7, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()

def stop_pump8(pump):
    GPIO.output(pump8, GPIO.LOW)
    print 'stop pump', pump, '@', time.time()


args = parser.parse_args()

#pump1
if args.p1:
    GPIO.output(pump1, GPIO.HIGH)
    print 'start pump 1 @', time.time()
    scheduler.enter(float(args.p1), 1, stop_pump1, ('1'))

#pump2
if args.p2:
    GPIO.output(pump2, GPIO.HIGH)
    print 'start pump 2 @', time.time()
    scheduler.enter(float(args.p2), 1, stop_pump2, ('2'))

#pump3
if args.p3:
    GPIO.output(pump3, GPIO.HIGH)
    print 'start pump 3 @', time.time()
    scheduler.enter(float(args.p3), 1, stop_pump3, ('3'))

#pump4
if args.p4:
    GPIO.output(pump4, GPIO.HIGH)
    print 'start pump 4 @', time.time()
    scheduler.enter(float(args.p4), 1, stop_pump4, ('4'))

#pump5
if args.p3:
    GPIO.output(pump5, GPIO.HIGH)
    print 'start pump 5 @', time.time()
    scheduler.enter(float(args.p5), 1, stop_pump5, ('5'))

#pump6
if args.p3:
    GPIO.output(pump6, GPIO.HIGH)
    print 'start pump 6 @', time.time()
    scheduler.enter(float(args.p6), 1, stop_pump6, ('6'))

#pump7
if args.p7:
    GPIO.output(pump7, GPIO.HIGH)
    print 'start pump 7 @', time.time()
    scheduler.enter(float(args.p3), 1, stop_pump7, ('7'))

#pump8
if args.p8:
    GPIO.output(pump8, GPIO.HIGH)
    print 'start pump 8 @', time.time()
    scheduler.enter(float(args.p8), 1, stop_pump8, ('8'))


scheduler.run()