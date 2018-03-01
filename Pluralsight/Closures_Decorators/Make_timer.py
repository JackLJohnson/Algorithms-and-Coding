# Elapsed is using nonlocal to create a binding which will exist through multiple calls to create a form persistent storage
# we can create independent timers here also
import time
def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called=now
        return result

    return elapsed
