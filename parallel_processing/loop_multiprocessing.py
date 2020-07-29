import multiprocessing
import mtprocessing
import time

start = time.perf_counter()

processes = []

# "_" it throw away a variable name, because we are only looping
for _ in range(10):
    process = multiprocessing.Process(target=mtprocessing.sleep)
    process.start()
    processes.append(process)

# basically the join method say that multiprocessing should finish the process before finish the rest of script
for process in processes:
    process.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')