import time
from pinger import Pinger


class PingMonitor:

    def __init__(self, hosts, interval, count, logger):

        self.hosts = hosts
        self.interval = interval
        self.pinger = Pinger(count)
        self.logger = logger

    def run(self):

        while True:

            results = {}

            for host in self.hosts:
                avg = self.pinger.ping_host(host)

                if avg:
                    results[host] = round(avg, 2)
                else:
                    results[host] = "timeout"

            self.logger.log(results)

            time.sleep(self.interval)