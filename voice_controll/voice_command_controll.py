import snowboy.snowboydecoder as snowboydecoder
from djitellopy import tello
import time

def down():
    me.send_rc_control(0,0,-20,0)

def up():
    me.send_rc_control(0,0,20,0)

def right():
    me.send_rc_control(20,0,0,0)

def left():
    me.send_rc_control(-20,0,0,0)

def land():
    me.send_rc_control(0,0,0,0)
    time.sleep(2)
    me.land()

def takeoff():
    me.takeoff()
    time.sleep(2)
    me.send_rc_control(0,0,0,0)

def quit():
    exit(0)

me = tello.Tello()
me.connect()

models = ["resources/dolje.pmdl","resources/gore.pmdl",'resources/desno.pmdl','resources/lijevo.pmdl','resources/land.pmdl','resources/poleti.pmdl']
sensitivity = [0.4]*len(models)
detector = snowboydecoder.HotwordDetector(models,sensitivity=sensitivity)
detector.start([lambda : down(),lambda : up(),lambda : right(),lambda : left(),lambda : land(),lambda : takeoff()])
