import argparse
import sched
import time

parser = argparse.ArgumentParser()
scheduler = sched.scheduler(time.time, time.sleep)
pumps = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']

i = 0
while i < len(pumps):
    parser.add_argument('--' + pumps[i])
    i += 1

def stop_pump(pump):
    print 'stop pump', pump, '@', time.time()

args = parser.parse_args()

#pump1
if args.p1:
    print 'start pump 1 @', time.time()
    scheduler.enter(float(args.p1), 1, stop_pump, ('1'))

#pump2
if args.p2:
    print 'start pump 2 @', time.time()
    scheduler.enter(float(args.p2), 1, stop_pump, ('2'))

#pump3
if args.p3:
    print 'start pump 3 @', time.time()
    scheduler.enter(float(args.p3), 1, stop_pump, ('3'))


scheduler.run()