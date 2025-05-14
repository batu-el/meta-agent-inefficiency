from contextvars import ContextVar

_CURRENT_TRACKER: ContextVar["CostTracker | None"] = ContextVar(
    "_CURRENT_TRACKER", default=None
)