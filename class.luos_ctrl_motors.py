#!/usr/bin/env python3
#coding: utf-8

from pyluos import Robot
import time

# Set the Object by connecting Rpy by IP
r = Robot("raspberrypi.local")
print (r.modules)

# get the motor alias (anyway to have it dynamically ?)
motor_right = r.controlled_mot0
motor_left = r.controlled_moto

class motor_control():
    def __init__(self):
        #roue droite :
        motor_right.positionPid = [3,0.002,100] # position PID [P, I, D]
        motor_right.speedPid = [0.4,0.02,0] # speed PID [P, I, D]
        motor_right.encoder_res = 16 # Encoder resolution before reduction
        motor_right.reduction = 47 # gear reduction ratio of your motor
        motor_right.wheel_size = 100 # Wheel Diameter mm

        #roue gauche :
        motor_left.positionPid = [3,0.002,100] # position PID [P, I, D]
        motor_left.speedPid = [0.4,0.02,0] # speed PID [P, I, D]
        motor_left.encoder_res = 16 # Encoder resolution before reduction
        motor_left.reduction = 47 # gear reduction ratio of your motor
        motor_left.wheel_size = 100 # Wheel Diameter mm

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
            motor_right.power_mode(False)
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
            motor_right.power_mode(False)
            motor_left.rot_position_mode(True)
            motor_left.target_rot_position = speed
        #time.sleep(0.5)

    #stop motors
    def stop_motor(self, motor):
        if motor == 0 or motor == 2:
            motor_right.compliant = True# disable the motor
        if motor == 1 or motor == 2:
            motor_left.compliant = True # disable the motor


            
#test   area ::
if __name__== "__main__":

    zer = motor_control()
    zer.set_power(50,1)
    time.sleep(2)
    zer.set_power(80,0)
    time.sleep(2)

    zer.set_power(0,1)
    time.sleep(3)
    zer.set_power(0,0)
    time.sleep(3)
    print("over yet ?")
    zer.stop_motor(2)

    time.sleep(5)
    print("over")
