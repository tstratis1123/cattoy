#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import pygame

#THIS IS THE BASIC CODE FOR MOTOR CONTROL
#GOALS: TO TRIGGER MOTOR MOVEMENT BY PUSHING KEYS ON KEYBOARD
MotorPin1 = 11  # pin11
MotorPin2 = 12  # pin12
MotorEnable = 13  # pin13


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(MotorPin1, GPIO.OUT)  # mode --- output
    GPIO.setup(MotorPin2, GPIO.OUT)
    GPIO.setup(MotorEnable, GPIO.OUT)
    GPIO.output(MotorEnable, GPIO.LOW)  # motor stop


def loop():
    while True:
        print('Press Ctrl+C to end the program...')
        GPIO.output(MotorEnable, GPIO.HIGH)  # motor driver enable
        GPIO.output(MotorPin1, GPIO.HIGH)  # clockwise
        GPIO.output(MotorPin2, GPIO.LOW)
        time.sleep(5)

        GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
        time.sleep(5)

        GPIO.output(MotorEnable, GPIO.HIGH)  # motor driver enable
        GPIO.output(MotorPin1, GPIO.LOW)  # anticlockwise
        GPIO.output(MotorPin2, GPIO.HIGH)
        time.sleep(5)

        GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
        time.sleep(5)


def destroy():
    GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

#THIS WAS TO EXPERIEMENT WITH PYGAME TO USE KEY EVENTS TO CONTROL THE TOY
#GOALS: ADD BASIC VISUALS TO TRACK WHERE THE TOY PHYSICALLY IS(IE A SLIDER OF SOME SORT)
pygame.init()
WIDTH=600
HEIGHT=480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
t = time.time()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                start = time.time()
                print('Left Pressed')
            elif event.key == pygame.K_RIGHT:
                start = time.time()
                print('Right Pressed')
            elif event.key == pygame.K_UP:
                start = time.time()
                print('Up Pressed')
            elif event.key == pygame.K_DOWN:
                start = time.time()
                print('Down Pressed')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print('Left Released')
                end = time.time()
                print("Key Pressed Time: ", end - start)
            elif event.key == pygame.K_RIGHT:
                print('Right Released')
                end = time.time()
                print("Key Pressed Time: ", end - start)
            elif event.key == pygame.K_UP:
                print('Up Released')
                end = time.time()
                print("Key Pressed Time: ", end - start)
            elif event.key == pygame.K_DOWN:
                print('Down Released')
                end = time.time()
                print("Key Pressed Time: ", end - start)