__all__ = [
    "cell_counter",
    "time_start",
    "time_end"
]


import time

def cell_counter(n: int) -> None:
    print(f"Cell number: {n}")
    
def time_start() -> float:
    return time.time()

def time_end(start_time: float) -> None:
    final_time = time.time()
    print(f"Cell time: {final_time - start_time:.3f} seconds") 