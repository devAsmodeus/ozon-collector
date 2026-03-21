"""Prometheus метрики для ozon-collector."""
from prometheus_client import Counter, Gauge, Histogram

# ---------------------------------------------------------------------------
# Ozon API
# ---------------------------------------------------------------------------

ozon_api_requests_total = Counter(
    "ozon_api_requests_total",
    "Total Ozon API requests",
    ["endpoint", "method"],
)

ozon_api_errors_total = Counter(
    "ozon_api_errors_total",
    "Total Ozon API errors",
    ["endpoint", "error_type"],
)

ozon_api_response_time = Histogram(
    "ozon_api_response_seconds",
    "Ozon API response time",
    ["endpoint"],
    buckets=(0.1, 0.25, 0.5, 1, 2.5, 5, 10, 30),
)

ozon_api_rate_limits = Counter(
    "ozon_api_rate_limits_total",
    "Total Ozon API rate limit responses (429)",
    ["endpoint"],
)

# ---------------------------------------------------------------------------
# Коллекторы
# ---------------------------------------------------------------------------

collector_runs_total = Counter(
    "collector_runs_total",
    "Total collector runs",
    ["module", "status"],
)

collector_items_total = Counter(
    "collector_items_total",
    "Total items collected",
    ["module"],
)

collector_duration = Histogram(
    "collector_duration_seconds",
    "Collector run duration",
    ["module"],
    buckets=(1, 5, 10, 30, 60, 120, 300, 600),
)

collector_last_success = Gauge(
    "collector_last_success_timestamp",
    "Timestamp of last successful collection",
    ["module"],
)


def record_collection(module: str, items: int, duration: float, error: bool = False) -> None:
    """Записывает метрики сбора данных."""
    status = "error" if error else "success"
    collector_runs_total.labels(module=module, status=status).inc()
    collector_duration.labels(module=module).observe(duration)
    if not error:
        collector_items_total.labels(module=module).inc(items)
        collector_last_success.labels(module=module).set_to_current_time()
