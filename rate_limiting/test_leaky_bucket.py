from datetime import datetime, timedelta
from libfaketime import fake_time

from .leaky_bucket import LeakyBucket

bucket = LeakyBucket(capacity=10, drain_rate=1)


class TestLeakyBucket:
    def test_traffic_flows(self):
        now = datetime.now()
        print(f"now: {now}")
        for _ in range(100):
            now = now + timedelta(seconds=1)
            print(f"now: {now}")
            with fake_time(now):
                assert bucket.process_request(1)
