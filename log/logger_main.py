import logging
import os

from concurrent_log_handler import ConcurrentRotatingFileHandler

from config.envion import LOG_PATH, ENV

DEFAULT_FORMAT = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")


def create_handler(level, filename, formatter=None, max_bytes=50 * 50 * 1024, backup_count=10):
    log_name = f"{str(filename).lower()}.log"
    formatter = formatter if formatter is not None else DEFAULT_FORMAT
    log_path = os.path.join(LOG_PATH, log_name)
    handler = ConcurrentRotatingFileHandler(
        log_path, maxBytes=max_bytes, backupCount=backup_count
    )
    logger = logging.getLogger(filename)
    logger.handlers.clear()  # 清除默认的处理器
    if ENV == "dev":
        handler.setFormatter(DEFAULT_FORMAT)
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(logging.INFO)  # 设置日志级别为 INFO
        stdout_handler.setFormatter(DEFAULT_FORMAT)  # 设置日志格式
        logger.addHandler(stdout_handler)
    else:
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level.upper())  # 不需要强制转换为大写字母
    return logger


class LogManage:
    def __init__(self):
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)

    @staticmethod
    def main():
        """
        兜底日志
        :return:
        """
        return create_handler("info", "main")

    @staticmethod
    def error():
        """
        兜底日志
        :return:
        """
        return create_handler("error", "error")

    @staticmethod
    def job():
        """
        兜底日志
        :return:
        """
        return create_handler("info", "job")

    @staticmethod
    def platform():
        """
        兜底日志
        :return:
        """
        return create_handler("info", "platform")


logger = LogManage()

if __name__ == '__main__':
    loggers = LogManage()
    loggers.main().info("abc")
    loggers.job().info("hello")
    loggers.error().error("cd")

