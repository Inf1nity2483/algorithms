import time
from memory_profiler import memory_usage
from task18 import main

def measure_memory_and_time(func, *args, **kwargs):
    start_time = time.time()
    
    mem_usage = memory_usage((func, args, kwargs), interval=0.1) 
    end_time = time.time()
    
    total_time = end_time - start_time
    max_memory = max(mem_usage)  
    
    return total_time, max_memory

if __name__ == "__main__":
    execution_time, memory_usage1 = measure_memory_and_time(main)
    print(f"Execution time: {execution_time:.4f} seconds")
    print(f"Max memory usage: {memory_usage1:.4f} MiB")
