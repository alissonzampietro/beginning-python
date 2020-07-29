import multiprocessing
import time

start = time.perf_counter()

def sleep():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Waking up dude...')

# Here, we've called two multiprocessing processes
process1 = multiprocessing.Process(target=sleep)
process2 = multiprocessing.Process(target=sleep)

# We need to start them
process1.start()
process2.start()

#With join() method, you set when multiprocessing start, if it's not defined, to it will trigger in the end of execution
process1.join()
process2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')