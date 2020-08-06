"""
Dependência: Adafruit_BBIO
"""

from __future__ import division
from encode_faces import reconhecer
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

class Motor:
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
        
    def destravar(self, motor, sensor):

        #Se o reconhecimento facial for positivo e o sensor capacitivo detectar o objeto porta
        if reconhecimento.getEstado() == True and sensor.getEstado() == True and self.__estadoPorta == False:

            #Aciona o motor para abrir a trava   
            motor.setEstado(True)
            motor.rotate()
     
            #Atualiza o sensor
            if sensor.getEstado() == True:
                sensor.setEstado(False)
                motor.setEstado(False)
               
    def travar(self, motor, sensor):

        #Se o sensor capacitivo indicar presença (detectar o objeto porta)
        if sensor.getEstado() == True and self.__estadoPorta == True:

            #Aciona o motor para fechar a trava   
            motor.setEstado(True)
            motor.rotate()
     
            #Atualiza o sensor
            if sensor.getEstado() == False:
                sensor.setEstado(True)
                motor.setEstado(False)

    
class Display:
    """
    Classe responsável pela definição do display
    'True' = ligado
    'False' = desligado
    """
    
    def __init__(self):
        self.__estado = False
        self.tentativas = 3

    def setDisplay(self, estado):
        self.__estado = estado
        
    def getEstado(self):
        return self.__estado
    
    def ErroReconhecimento(self):
        #Caso o reconhecimento falhe, esta mensagem aparecerá ao usuário
        if self.__estado == True and self.tentativas < 3
            self.tentativas = self.tentativas -1 
            i = input("Rosto não identificado. \nDeseja tentar novamente? (S/N)\nNúmero restante de tentativas: {self.tentativas}")
            if i == 's'
                return True, self.tentativas
            else return False, self.tenativas
            
def main():
    #Setando as classes
    motor = Motor()
    sensor = Sensor()
    porta = Porta(motor,sensor)
    display = Display()
    
    #Ligando o Display e executando o reconhecimento
    #A função reconhecer retornará 'True' se o rosto identificado der match e 'False' caso falhe
    display.setDisplay(True)
    R_reconhecer = reconhecer()
    
    
    #Se reconhecer, abrir a porta
    if R_reconhecer == True
        porta.destravar(motor, sensor)
        #Se não reconhecer, dar a opção ao usuário de tentar novamente
        else while R_reconhecer == False
            Resp,tentativas = display.ErroReconhecimento()
            if Resp == True and tentativas > 0
                R_reconhecer = reconhecer()
            #Numero máximo de tentativas não deve ser excedido
            if tentativas == 0
                display.setDisplay(False)
                
    porta.travar(motor, sensor)
                
                
    
            
        
    
    
    
