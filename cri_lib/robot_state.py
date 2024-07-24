from dataclasses import dataclass, field
from enum import Enum


class RobotMode(Enum):
    JOINT = "joint"
    CARTBASE = "cartbase"
    CARTTOOL = "carttool"
    PLATFORM = "platform"
    FSM = "fsm"


class KinematicsState(Enum):
    NO_ERROR = 0
    JOINT_MIN = 13
    JOINT_MAX = 14
    SIGULARITY_CENTER = 21
    SIGULARITY_REACH = 23
    SIGULARITY_WRIST = 24
    VIRTUAL_BOX0 = 30
    VIRTUAL_BOX1 = 31
    VIRTUAL_BOX2 = 32
    VIRTUAL_BOX3 = 33
    VIRTUAL_BOX4 = 34
    VIRTUAL_BOX5 = 35
    MOTION_NOT_ALLOWED = 99


class OperationMode(Enum):
    NOT_ENABLED = -1
    NORMAL = 0
    MANUAL = 1
    MOTION_NOT_ALLOWED = 2


class RunState(Enum):
    STOPPED = 0
    PAUSED = 1
    RUNNING = 2


class ReplayMode(Enum):
    SINGLE = 0
    REPEAT = 1
    STEP = 2
    FAST = 3


@dataclass
class ErrorStates:
    over_temp: bool = False
    estop_lowv: bool = False
    motor_not_enabled: bool = False
    com: bool = False
    position_lag: bool = False
    ENC: bool = False
    overcurrent: bool = False
    driver: bool = False


@dataclass
class RobotCartesianPosition:
    X: float = 0.0
    Y: float = 0.0
    Z: float = 0.0
    A: float = 0.0
    B: float = 0.0
    C: float = 0.0


@dataclass
class PlatformCartesianPosition:
    X: float = 0.0
    Y: float = 0.0
    RZ: float = 0.0


@dataclass
class JointsState:
    A1: float = 0.0
    A2: float = 0.0
    A3: float = 0.0
    A4: float = 0.0
    A5: float = 0.0
    A6: float = 0.0
    E1: float = 0.0
    E2: float = 0.0
    E3: float = 0.0
    G1: float = 0.0
    G2: float = 0.0
    G3: float = 0.0
    P1: float = 0.0
    P2: float = 0.0
    P3: float = 0.0
    P4: float = 0.0


@dataclass
class PosVariable:
    X: float = 0.0
    Y: float = 0.0
    Z: float = 0.0
    A: float = 0.0
    B: float = 0.0
    C: float = 0.0
    A1: float = 0.0
    A2: float = 0.0
    A3: float = 0.0
    A4: float = 0.0
    A5: float = 0.0
    A6: float = 0.0
    E1: float = 0.0
    E2: float = 0.0
    E3: float = 0.0


@dataclass
class OperationInfo:
    program_starts_total: int = 0
    up_time_complete: float = 0.0
    up_time_enabled: float = 0.0
    up_time_motion: float = 0.0
    up_time_last: float = 0.0
    last_programm_duration: int = 0
    num_program_starts_since_startup: int = 0


class ReferencingAxisState(Enum):
    NOT_REFERENCED = 0
    REFERENCED = 1
    REFERENCING = 2

@dataclass
class ReferencingState:
    global_state:ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    mandatory: bool = True
    ref_prog_enabled: bool = False
    ref_prog_running: bool = False

    A1: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    A2: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    A3: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    A4: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    A5: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    A6: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    E1: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    E2: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    E3: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    E4: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    E5: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    E6: ReferencingAxisState = ReferencingAxisState.NOT_REFERENCED
    

@dataclass
class RobotState:
    """
    Dataclass which holds the current state of the robot.
    """

    mode: RobotMode = RobotMode.JOINT
    joints_set_point: JointsState = field(default_factory=JointsState)
    joints_current: JointsState = field(default_factory=JointsState)

    position_robot: RobotCartesianPosition = field(
        default_factory=RobotCartesianPosition
    )
    position_platform: PlatformCartesianPosition = field(
        default_factory=PlatformCartesianPosition
    )

    cart_speed_mm_per_s: float = 0.0

    override: float = 100.0

    din: list[bool] = field(default_factory=lambda: [False] * 64)
    dout: list[bool] = field(default_factory=lambda: [False] * 64)

    emergency_stop_ok = False
    main_relay = False

    supply_voltage: float = 0.0
    battery_percent: float = 0.0

    current_total = 0.0

    current_joints: list[float] = field(default_factory=lambda: [0.0] * 16)

    kinematics_state: KinematicsState = KinematicsState.MOTION_NOT_ALLOWED

    operation_mode: OperationMode = OperationMode.NOT_ENABLED

    global_signals: list[bool] = field(default_factory=lambda: [False] * 128)

    frame_name: str = ""
    frame_position_current: RobotCartesianPosition = field(
        default_factory=RobotCartesianPosition
    )

    main_main_program: str = ""
    main_current_program: str = ""

    logic_main_program: str = ""
    logic_current_program: str = ""

    main_commands_count: int = 0
    logic_commands_count: int = 0

    main_current_command: int = 0
    logic_current_command: int = 0

    main_runstate: RunState = RunState.STOPPED
    logic_runstate: RunState = RunState.STOPPED

    main_replay_mode: ReplayMode = ReplayMode.SINGLE
    logic_replay_mode: ReplayMode = ReplayMode.SINGLE

    error_states: list[ErrorStates] = field(
        default_factory=lambda: [ErrorStates()] * 16
    )

    cycle_time: float = 0.0
    workload: float = 0.0

    gripper_state: float = 0.0

    variabels: dict[str : [PosVariable | float]] = field(default_factory=dict)

    operation_info: OperationInfo = field(default_factory=OperationInfo)

    active_control: bool = False

    robot_control_version: str = ""

    robot_configuration: str = ""
    robot_type: str = ""
    gripper_type: str = ""

    project_file: str = ""

    referencing_state: ReferencingState = field(default_factory=ReferencingState)