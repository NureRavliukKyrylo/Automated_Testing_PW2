from abc import ABC, abstractmethod


class Logger(ABC):

    @abstractmethod
    def log(self, data):
        pass


class TxtLogger(Logger):

    def log(self, data):

        with open("log.txt", "a") as f:
            for host, value in data.items():
                f.write(f"{host}: {value} ms\n")


class XmlLogger(Logger):

    def log(self, data):

        with open("log.xml", "a") as f:
            f.write("<log>\n")

            for host, value in data.items():
                f.write(f"  <host name='{host}' time='{value}' />\n")

            f.write("</log>\n")


class HtmlLogger(Logger):

    def log(self, data):

        with open("log.html", "a") as f:
            f.write("<table border='1'>\n")

            for host, value in data.items():
                f.write(f"<tr><td>{host}</td><td>{value} ms</td></tr>\n")

            f.write("</table>\n")