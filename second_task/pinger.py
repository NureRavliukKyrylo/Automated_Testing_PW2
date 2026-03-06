from ping3 import ping
import statistics


class Pinger:

    def __init__(self, count: int):
        self.count = count

    def ping_host(self, host: str):

        results = []

        for _ in range(self.count):
            response = ping(host)

            if response:
                results.append(response * 1000) 

        if not results:
            return None

        return statistics.mean(results)