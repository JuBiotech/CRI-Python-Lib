"""
.. include:: ../README.md
"""

import logging

# Configure logging for the cri_lib package
logging.basicConfig(
    level=logging.DEBUG,  # Keep to DEBUG if you want more detailed logs
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Create a logger for the package
logger = logging.getLogger(__name__)
logger.info("cri_lib package initialized")


from .robot_state import (
    RobotMode,
    KinematicsState,
    OperationMode,
    RunState,
    ReplayMode,
    ErrorStates,
    RobotCartesianPosition,
    PlatformCartesianPosition,
    JointsState,
    RobotState,
    PosVariable,
    OperationInfo,
    ReferencingAxisState,
    ReferencingState,
)
from .cri_controller import CRIController
from .cri_protocol_parser import CRIProtocolParser

from .cri_errors import CRIError, CRIConnectionError, CRICommandTimeOutError
