from loggers import TxtLogger, XmlLogger, HtmlLogger


class LoggerFactory:

    _loggers = {
        "txt": TxtLogger,
        "xml": XmlLogger,
        "html": HtmlLogger
    }

    @staticmethod
    def create_logger(format_type: str):

        format_type = format_type.lower()

        logger_class = LoggerFactory._loggers.get(format_type)

        if not logger_class:
            raise ValueError("Unsupported format")

        return logger_class()