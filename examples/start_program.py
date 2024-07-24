from time import sleep

from cri_lib import CRIController

# CRIController is the main interface for controlling the iRC
controller = CRIController()

#connect to default iRC IP
#if not controller.connect("127.0.0.1", 3921):
if not controller.connect("192.168.3.11"):
    print("Unable to connect")
    quit()

#acquire active control.
controller.set_active_control(True)

print("enable")
#enable motors
controller.enable()

print("waiting")
#wait until kinematics are ready to move
controller.wait_for_kinematics_ready(10)

controller.set_override(50.0)

print("Load program")
if not controller.load_programm("ReBeL_6DOF_01_Tischtest.xml"):
    print("unable to load programm")
    controller.disable()
    controller.close()
    quit()

print("Start program")
if not controller.start_programm():
    print("Unable to start programm")
    controller.disable()
    controller.close()
    quit()

sleep(5)

print("Pause program")
if not controller.pause_programm():
    print("Unable to pause programm")
    controller.disable()
    controller.close()
    quit()

sleep(5)

print("Start programm again")
if not controller.start_programm():
    print("Unable to start programm")
    controller.disable()
    controller.close()
    quit()

sleep(5)

print("Stop program")
if not controller.stop_programm():
    print("Unable to stop programm")
    controller.disable()
    controller.close()
    quit()

#Disable motors and disconnect
controller.disable()
controller.close()