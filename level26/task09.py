import multiprocessing
import os

def worker(name):
    print(f'Process name: {name}, PID: {os.getpid()}')


processes = []
for i in range(4):
    process_name = f'Process-{i+1}'
    p = multiprocessing.Process(target=worker, args=(process_name,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()