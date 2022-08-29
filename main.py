from concurrent.futures import ThreadPoolExecutor
import sys
import time
import Valve
import HeartRate


interval = 100000

def valve_motor(heartrate_interval):
    
    doingTask = True
    open_time = 0.1
    task_finish = 60
    task_count = 0
    
    valve = Valve.ControlValve()
    
    print("Start")
    
    while doingTask:
        task_count += 1
        if(task_count < task_finish):
            valve.openValve(open_time)
            time.sleep(heartrate_interval)
        else:
            valve.stopValveControl()
            doingTask = False
            sys.exit("time over")

def heartrate_sensor():
    heartrate = HeartRate.HeartRateMonitor()
    interval = heartrate.getInterval()
    

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(valve_motor(), interval)
        executor.submit(heartrate_sensor())
    
