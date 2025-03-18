import logging

logger = logging.getLogger(__name__)

class CRIError(Exception):
    """Base class for CRI-related errors."""
    def __init__(self, message="An error occurred in CRI"):
        self.message = message
        super().__init__(self.message)

class CRIConnectionError(CRIError):
    """Raised when there is a connection error."""
    def __init__(self, message="Not connected to iRC or connection lost."):
        self.message = message
        super().__init__(self.message)

class CRICommandTimeOutError(CRIError):
    """Raised when a command times out."""
    def __init__(self, message="Time out waiting for command response."):
        self.message = message
        super().__init__(self.message)