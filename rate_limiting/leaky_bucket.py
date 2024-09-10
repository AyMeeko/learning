"""
Leaky bucket as a meter

A bucket has a set capacity. A counter is initialized at 0 and each request that comes in
increments the counter. When the counter reaches the bucket's capacity, requests are rate limited.
The counter is decremented at a set rate, which creates capacity in the bucket.

This can work where the requests into the system are all a single unit, or variable units.
"""

from datetime import datetime


class LeakyBucket:
    def __init__(self, capacity, drain_rate):
        self.capacity = capacity
        self.drain_rate = drain_rate
        self.fill_level = 0
        self.last_drain_time = datetime.now()

    def _drain(self):
        now = datetime.now()
        elapsed_time = (now - self.last_drain_time).total_seconds()
        drained = elapsed_time * self.drain_rate
        self.fill_level = max(0, self.fill_level - drained)
        print(f"set last_drain_time to {now}")
        self.last_drain_time = now

    def process_request(self, request_size):
        self.debug()
        self._drain()
        if self.fill_level + request_size <= self.capacity:
            self.fill_level += request_size
            return True
        return False

    def debug(self):
        # readable_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.last_drain_time))
        print(f"fill level: {self.fill_level}, last_drain_time: {self.last_drain_time}")
