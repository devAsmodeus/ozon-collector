"""Настройка логирования в JSON → stdout → Docker → Promtail → Loki."""
import logging
import sys

from pythonjsonlogger.json import JsonFormatter


def setup_logging(level: str = "INFO") -> None:
    formatter = JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(name)s %(message)s %(module)s",
        rename_fields={
            "asctime": "timestamp",
            "levelname": "level",
            "name": "logger",
        },
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level)
    root.addHandler(handler)

    # Подавляем шум от библиотек
    for name in ("httpx", "httpcore", "uvicorn.access"):
        logging.getLogger(name).setLevel(logging.WARNING)
