import pynput
import time
from pynput.keyboard import Key, Controller, Listener

kc=pynput.keyboard.KeyCode
keyboard=Controller()

left=kc.from_char('q')
down=kc.from_char('w')
right=kc.from_char('e')
up=Key.space
test=kc.from_char('k')

downLeft=[down,left]
downRight=[down,right]
halfCircle=[left,down,right]
rightLeft=[right,left]
downUp=[down,up]

speed=0.012

current=set()

#keyboard monitoring

hcl=0   #half circle left
hcr=0   #half circle right
crouch=0


def pressed(key):
    global hcl
    global hcr
    global crouch
    crouch=(key==down)
    if hcl==0 and hcr==0 and key in halfCircle:
        current.add(key)
        if all(k in current for k in downLeft):
            if crouch==1:
                time.sleep(speed)
                keyboard.release(left.char)
            hcr=1
        if all(k in current for k in downRight):
            if crouch==1:
                time.sleep(speed)
                keyboard.release(right.char)
            hcl=1
    if hcl==1:
        current.add(key)
        if all(k in current for k in downLeft):
            time.sleep(speed)
            keyboard.release(right.char)
            hcl=0
    if hcr==1:
        current.add(key)
        if all(k in current for k in downRight):
            time.sleep(speed)
            keyboard.release(left.char)
            hcr=0
            
    if key in downUp:
        current.add(key)
        if all(k in current for k in downUp):
            keyboard.release(down.char)

def released(key):
    try:
        current.remove(key)
    except KeyError:
        pass

with Listener(on_press=pressed, on_release=released) as listener:
    listener.join()