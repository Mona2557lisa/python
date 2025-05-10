print("name : monalisa.n \n usn : 1AY24Ai073 \n section : O ")
import time
import sys

def zigzag(text, delay=0.1):
    indent = 0
    increasing = True

    while True:
        print(' ' * indent + text)
        time.sleep(delay)

        if increasing:
            indent += 1
          if indent == 20:
                increasing = False
        else:
            indent -= 1
            if indent == 0:
                increasing = True

try:
    zigzag("Zigzag!")
except KeyboardInterrupt:
    sys.exit()
