import logging
from time import sleep
from cri_lib import CRIController
from cri_lib.robot_state import KinematicsState  # Ensure KinematicsState is imported
from cri_lib.robot_state import OperationMode

# 🔹 Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Creating an instance
controller = CRIController()
logging.info("Connecting to CRI server at 127.0.0.1:3921...")

# Connect to the simulator at 127.0.0.1 with port 3921
if not controller.connect("127.0.0.1", 3921):
    logging.error("Unable to connect to iRC! Check if the simulator is running.")
    quit()

# Acquire active control
controller.set_active_control(True)

# Check if active control is enabled
if not controller.robot_state.active_control:
    logging.warning("Active control is NOT enabled! Check connection.")
    controller.close()
    quit()
else:
    logging.info("Active control enabled! You can now send commands.")

# Enable the motors
if not controller.enable():
    logging.error("Error: Unable to enable motors. Check the simulator.")
    controller.disable()
    controller.close()
    quit()
logging.info("Robot enabled.")

# **TRY TO RELEASE BRAKES**
BRAKE_DOUT = 21  # Using DOut21 based on the panel
logging.info(f"Releasing brake using DOUT {BRAKE_DOUT}...")
controller.set_dout(BRAKE_DOUT, True)  # This should release the brake
sleep(2)  # Wait for the brake to disengage

# Print the current kinematics state
logging.info(f"Current Kinematics State: {controller.robot_state.kinematics_state}")

# Check if the robot is in a valid motion state
if controller.robot_state.kinematics_state not in KinematicsState.__members__.values():
    logging.warning("Unexpected Kinematics State received. Motion might not be allowed.")
    controller.disable()
    controller.close()
    quit()

# Wait until kinematics are ready before moving
if not controller.wait_for_kinematics_ready(10):
    logging.error("Error: Kinematics not ready. Check the simulator.")
    controller.disable()
    controller.close()
    quit()

logging.info("Kinematics Ready. Moving to start position...")

# Move the robot to fixed position zero
if not controller.move_joints(A1=0, A2=0, A3=0, A4=0, A5=0, A6=0,
                               E1=0, E2=0, E3=0, velocity=50, wait_move_finished=True):
    logging.error("Error: Movement to zero failed! Check simulator settings.")
    controller.disable()
    controller.close()
    quit()

logging.info("Successfully moved to zero position.")

# Perform a relative movement from the fixed position
if not controller.move_joints_relative(A1=10, A2=10, A3=5, A4=0, A5=0, A6=0,
                                       E1=0, E2=0, E3=0, velocity=30, wait_move_finished=True):
    logging.error("Error: Relative movement failed! Check simulator settings.")
    controller.disable()
    controller.close()
    quit()

logging.info("Successfully completed relative movement.")

# Pause, stop, and disable the robot
sleep(2)
controller.pause_programm()
logging.info("Paused the program.")

sleep(2)
controller.stop_programm()
logging.info("Stopped the program.")

# Disable active control and stop the motors
controller.set_active_control(False)

# Check if robot is still enabled before disabling
if controller.robot_state.operation_mode != OperationMode.NOT_ENABLED:
    logging.info("Disabling motors...")
    controller.disable()
    logging.info("Motors disabled successfully.")
else:
    logging.info("Robot is already disabled, skipping disable command.")

controller.close()
logging.info("Disconnected from iRC.")
