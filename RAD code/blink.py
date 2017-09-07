import RPI.GPIO as Prog1
import time

Prog1.setmode (Prog1.BOARD)
Prog1.setup (7, Prog1.OUT)
for if in range (0, 100000):
    Prog1.output (7, True)
    time.sleep (1)
    Prog1.output (7, False)
    time.sleep (1)
Prog1.cleanup ()
    
