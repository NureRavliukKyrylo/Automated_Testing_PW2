from monitor import PingMonitor
from logger_factory import LoggerFactory


def main():

    hosts = [
        "youtube.com",
        "google.com",
        "github.com"
    ]

    interval = 10
    ping_count = 3

    log_format = input("Choose log format (txt/xml/html): ")

    logger = LoggerFactory.create_logger(log_format)

    monitor = PingMonitor(hosts, interval, ping_count, logger)

    monitor.run()


if __name__ == "__main__":
    main()