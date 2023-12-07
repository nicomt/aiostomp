from typing import Any, Optional


class StompError(Exception):
    def __init__(self, message: Optional[str] = None, detail: Any = None):
        super().__init__(message or "")
        self.detail = detail


class StompDisconnectedError(StompError):
    pass


class ExceededRetryCount(StompError):
    def __init__(self, ref: Any):
        super().__init__("Retry count exceeded!")
        self.ref = ref


class ReceiptTimeout(StompError):
    def __init__(self, message_id: str):
        super().__init__(f"Receipt timeout for message: {message_id}")


class ConnectionTimeout(StompError):
    pass
