import sys
import time
import threading

from loguru import logger

def spinnner_animation(func):
    def wrapper(*args,**kwargs):
        spinner = ["|", "/", "-", "\\"]  # Spinner characters
        idx = 0
        # run spinner animation in separate thread
        def spin():
            nonlocal idx
            while not done[0]:
                sys.stdout.write(f"\rRunning...  {spinner[idx]}")
                sys.stdout.flush()
                idx = (idx + 1) % len(spinner)
                time.sleep(0.1)
        done = [False] # signals if function is done
        spinner_thread = threading.Thread(target=spin)
        spinner_thread.daemon = True
        spinner_thread.start()
        try:
            result = func(*args, **kwargs)
        finally:
            done[0] = True # Stop the spinner
            spinner_thread.join() # Ensure the spinner thread finishes
            sys.stdout.write("\n")

            sys.stdout.write("\r")
        return result
    return wrapper

def time_function(func) -> None:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.info(f"Error in function {func.__name__}: {e}")
            raise
        elapsed_time = time.time() - start_time

        logger.info(f"Function '{func.__name__}' executed in {elapsed_time:.1f} seconds / {(elapsed_time/60):.1f} mins")

        return result

    return wrapper