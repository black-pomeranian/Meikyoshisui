import time
from collections import deque
 
import RPi.GPIO as GPIO
 
class HeartRateMonitor:
    INTERRUPT_PIN = 12
    MAX_DETECTED_TIMES_COUNT = 20
    MAX_PULSE_INTERVAL = 2.0
    MAX_INTERVALS_COUNT = 10
 
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.INTERRUPT_PIN, GPIO.IN)
 
        self._init_array()
 
    def _init_array(self):
        self.detected_times = deque([])
        self.intervals = deque([])
    
    def _calc_HeartRate_mean(self):
        self.detected_times.append(time.time())
        interval_mean = None
 
        if(len(self.detected_times) == 1):
            return
 
        interval = self.detected_times[-1] - self.detected_times[-2]
        self.intervals.append(interval)
        
        if interval > self.MAX_PULSE_INTERVAL:
            print('Heart rate measure error. Monitoring will restart!')
            self._init_array()
            return
 
        if(len(self.detected_times) >= self.MAX_DETECTED_TIMES_COUNT):
            self.detected_times.popleft()
            
        if(len(self.intervals) >= self.MAX_INTERVALS_COUNT):
            interval_mean = sum(self.intervals) / len(self.intervals) 
            self.intervals.popleft()
        
        return interval_mean
            
    def getHeartRate(self):
        
        while True:
            GPIO.wait_for_edge(self.INTERRUPT_PIN, GPIO.RISING)
            interval = self._calc_HeartRate_mean()
            print('interval: {}'.format(interval))
            return interval
            
        
 
if __name__ == '__main__':
    monitor = HeartRateMonitor()
    monitor.execute()