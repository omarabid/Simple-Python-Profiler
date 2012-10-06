import time
import json

__author__ = 'Abid Omar'
__version__ = '1.0'

def profiler():
    return SimpleProfiler()


class SimpleProfiler:
    def __init__(self):
        self.timers = {}
        self.running = {}
        self.average = {}

    def start(self, timer, stat=None):
        if (timer not in self.timers) or (timer in self.timers and self.running[timer] == False):
            self.timers[timer] = time.time()
            self.running[timer] = True


    def end(self, timer, stat=None):
        if timer in self.timers and self.running[timer] == True:
            self.timers[timer] = time.time() - self.timers[timer]
            self.running[timer] = False
            if stat == 'average':
                if timer in self.average:
                    self.average[timer].append(self.timers[timer])
                    self.timers[timer] = sum(self.average[timer]) / float(len(self.average[timer]))
                else:
                    self.average[timer] = [self.timers[timer]]

    def log(self, output):
        if output == 'print':
            print(self.timers)
        if output == 'return':
            return self.timers
        if output == 'file':
            file = open('simple_profiler.log', 'w')
            file.write(json.dumps(self.timers) + '\n')
            file.close()