
import time

class TimeMeasureModule:

    cur_time: float

    def __init__(self):
        self.cur_time = 0
        return
    
    def begin_record(self) -> None:
        self.cur_time = time.time()

    def get_time(self) -> float:
        return time.time() - self.cur_time
