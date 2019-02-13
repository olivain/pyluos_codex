#!/usr/bin/env python3
#coding: utf-8

"""
LICENCE AGPL V3
Please read the following content
https://www.gnu.org/licenses/agpl-3.0.html
"""

# Import from Luos Robotics to manipulate modules
from pyluos import Robot
import time


"""
Class to setup Motor's object
"""
class motor_control():
    def __init__(self):
        print("Initializing routine :\n")
        #roue droite :
        motor_right.positionPid = [3,0.002,100] # position PID [P, I, D]
        motor_right.speedPid = [0.4,0.02,0] # speed PID [P, I, D]
        motor_right.encoder_res = 16 # Encoder resolution before reduction
        motor_right.reduction = 47 # gear reduction ratio of your motor
        motor_right.wheel_size = 38 # Wheel Diameter mm

        #roue gauche :
        motor_left.positionPid = [3,0.002,100] # position PID [P, I, D]
        motor_left.speedPid = [0.4,0.02,0] # speed PID [P, I, D]
        motor_left.encoder_res = 16 # Encoder resolution before reduction
        motor_left.reduction = 47 # gear reduction ratio of your motor
        motor_left.wheel_size = 38 # Wheel Diameter mm

        motor_right.compliant = False # enable the motor
        motor_left.compliant = False # enable the motor


    #power mode
    #percent = energie percentage to send into the motor (min: -100, max: 100)
    #motor = 0 : motor right
    #motor = 1 : motor left
    #motor = 2 : both
    def set_power(self, percent, motor):

        if motor == 0 or motor == 2:
            motor_right.rot_position_mode(False)
            motor_right.rot_speed_mode(False)
            motor_right.power_mode(True)
            motor_right.power_ratio = percent
        if motor == 1 or motor == 2:
            motor_left.rot_position_mode(False)
            motor_left.rot_speed_mode(False)
            motor_left.power_mode(True)
            motor_left.power_ratio = percent
        #time.sleep(0.5)

    #speed mode (can be enabled with position mode)
    # speed (degree per senconds, min = 0, max: 360 (to be verified) )
    #motor = 0 : motor right
    #motor = 1 : motor left
    #motor = 2 : both
    def set_speed(self, speed, motor):
        if motor == 0 or motor == 2:
            motor_right.power_mode(False)
            motor_right.rot_speed_mode(True)
            motor_right.target_rot_speed = speed
        if motor == 1 or motor == 2:
            motor_left.power_mode(False)
            motor_left.rot_speed_mode(True)
            motor_left.target_rot_speed = speed
        #time.sleep(0.5)

    #position mode (can be enabled with position mode)
    #position (degree, min = 0, max: 360 (to be verified))
    #motor = 0 : motor right
    #motor = 1 : motor left
    #motor = 2 : both
    def set_pos(self, pos, motor):
        if motor == 0 or motor == 2:
            motor_right.power_mode(False)
            motor_right.rot_position_mode(True)
            motor_right.target_rot_position = pos
        if motor == 1 or motor == 2:
            motor_left.power_mode(False)
            motor_left.rot_position_mode(True)
            motor_left.target_rot_position = speed
        #time.sleep(0.5)

    #speed = mm/s
    #motor = 0 : motor right
    #motor = 1 : motor left
    #motor = 2 : both
    def set_trans_speed(self, speed, motor):
        if motor == 0 or motor == 2:
            motor_right.power_mode(False)
            motor_right.rot_position_mode(False)
            motor_right.rot_speed_mode(False)
            motor_right.trans_speed_mode(True)
            motor_right.target_trans_speed = speed
        if motor == 1 or motor == 2:
            motor_left.power_mode(False)
            motor_left.rot_position_mode(False)
            motor_left.rot_speed_mode(False)
            motor_left.trans_speed_mode(True)
            motor_left.target_trans_speed = -speed



    #stop motors
    def stop_motor(self, motor):
        if motor == 0 or motor == 2:
            motor_right.compliant = True# disable the motor
            time.sleep(0.5)
        if motor == 1 or motor == 2:
            motor_left.compliant = True # disable the motor
            time.sleep(0.5)



#test   area ::
if __name__== "__main__":
    print("deep in the main function")
    # Set the Object by connecting Rpy by IP
    r = Robot("raspberrypi.local")
    if Robot is None:
        print ("Cannot connect to Pi")
    
    print("loading modules :\n")
    print (r.modules)

    print("setting motor controls :\n")
    # get the motor alias (anyway to have it dynamically ?)
    motor_right = r.controlled_mot0
    motor_left = r.controlled_moto

    print("setting class :\n")
    zer = motor_control()
    print("running set_trans_speed :\n")
    zer.set_trans_speed(1000,2) # 1000mm/second = 1m/s
    time.sleep(2)
    print("set the power to zero :\n")
    zer.stop_motor(2)

    print("over !")
