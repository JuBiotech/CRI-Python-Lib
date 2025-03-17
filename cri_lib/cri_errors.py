import logging

# Retrieve logger instance for this module
logger = logging.getLogger(__name__)

class CRIError(Exception):
    """Base class for CRI-related errors."""
    def __init__(self, message="An error occurred in CRI"):
        self.message = message
        logger.error(f"CRIError: {message}")  # Log error message
        super().__init__(self.message)

class CRIConnectionError(CRIError):
    """Raised when there is a connection error."""
    def __init__(self, message="Not connected to iRC or connection lost."):
        self.message = message
        logger.error(f"CRIConnectionError: {message}")  # Log connection error
        super().__init__(self.message)

class CRICommandTimeOutError(CRIError):
    """Raised when a command times out."""
    def __init__(self, message="Time out waiting for command response."):
        self.message = message
        logger.error(f"CRICommandTimeOutError: {message}")  # Log timeout error
        super().__init__(self.message)