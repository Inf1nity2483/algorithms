import time
import tracemalloc

from task14 import main

def measure(func, *args, **kwargs):
    tracemalloc.start()
    
    start_time = time.time()
    
    result = func(*args, **kwargs)
    
    end_time = time.time()
    
    _, peak = tracemalloc.get_traced_memory()
    
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Время выполнения: {execution_time:.3f} секунды")
    print(f"Пиковое использование памяти: {peak / 10**6:.3f} МБ")
    
    return result

if __name__ == '__main__':
    measure(main)

