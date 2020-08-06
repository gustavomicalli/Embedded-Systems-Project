"""
Dependência: Adafruit_BBIO
"""

from __future__ import division
import Adafruit_BBIO.GPIO as GPIO
import time
import math


def initialize_pins(pins):
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def set_all_pins_low(pins):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
        
def wavedrive(pins, pin_index):
    for i in range(len(pins)):
        if i == pin_index:
            GPIO.output(pins[i], GPIO.HIGH)
        else:
            GPIO.output(pins[i], GPIO.LOW)

def fullstep(pins, pin_index):
    """pin_index is the lead pin"""
    GPIO.output(pins[pin_index], GPIO.HIGH)
    GPIO.output(pins[(pin_index+3) % 4], GPIO.HIGH)
    GPIO.output(pins[(pin_index+1) % 4], GPIO.LOW)
    GPIO.output(pins[(pin_index+2) % 4], GPIO.LOW)

class Motor(object):
""" 
Classe responsável pela definição do motor
"""
    def __init__(self, steps_per_rev=2048.0,
                 pins=["P8_13", "P8_14", "P8_15", "P8_16"]):

        self.pins = pins
        
        initialize_pins(self.pins)
        set_all_pins_low(self.pins)
        
        self.angle = 0
        self.steps_per_rev = steps_per_rev
        
        # Inicializa o stepping mode
        self.drivemode = fullstep
    
    def rotate(self, degrees=360, rpm=15):
        step = 0
        
        # Calcula o tempo entre steps em segundos
        wait_time = 60.0/(self.steps_per_rev*rpm)
        
        # Converte graus para steps
        steps = math.fabs(degrees*self.steps_per_rev/360.0)
        self.direction = 1
        
        if degrees < 0:
            self.pins.reverse()
            self.direction = -1
        
        while step < steps:
            for pin_index in range(len(self.pins)):
                self.drivemode(self.pins, pin_index)
                time.sleep(wait_time)
                step += 1
                self.angle = (self.angle + self.direction/self.steps_per_rev \
                *360.0) % 360.0
        
        if degrees < 0:
            self.pins.reverse()
    	
        set_all_pins_low(self.pins)
        
    def zero_angle(self):
        self.angle = 0
        

def main():
    stepper = Stepper()
    stepper.rotate()
    
class Sensor:
    """
    Classe responsável pela definição do sensor
    """

    def __init__(self):
        #Sem aproximação = False / Distância < 15mm = True
        self.__estado = False


    def setEstado(self, estado):
        self.__estado = estado


    def getEstado(self):
        return self.__estado
    
class Porta:
    """
    Classe responsável pela definição da porta do cofre
    """
    def __init__(self, motor, sensor):
        self.sensor = sensor
        self.motor = motor
        
        #Fechada = False / Aberta = True
        self.__estadoPorta = False
        
    def destravar(self):

        #Se o reconhecimento facial for positivo e o sensor capacitivo detectar o objeto porta
        if self.face_recognition.getEstado() == True and self.sensor.getEstado() == True:

            #Aciona o motor para abrir a trava   
            self.girarmotor+.setEstado(True)
     
            #Atualiza o sensor
            if self.sensor.getEstado() == True:
                self.sensor.setEstado(False)
                self.motor.setEstado(False)
                self.__estadoPorta = True
               
    def travar(self):

        #Se o sensor capacitivo indicar presença (detectar o objeto porta)
        if self.sensor.getEstado() == True:

            #Aciona o motor para fechar a trava   
            self.girarmotor-.setEstado(True)
     
            #Atualiza o sensor
            if self.sensor.getEstado() == False:
                self.sensor.setEstado(True)
                self.motor.setEstado(False)
                self.__estadoPorta = False

    
