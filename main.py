from pygame import mixer
from time   import sleep,time
from datetime import datetime
print(datetime.now())
A=input("Enter your name:\n")
print(A)
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        A=input("Enter: ")
        if A==stopper:
            mixer.music.stop()
            break
        A=input("Enter: ")
        if A==stopper:
            mixer.music.stop()
            break
        A = input("Enter: ")
        if A == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("notify.txt","a") as f:
        f.write(f"{msg}  at this time = {datetime.now()}\n")


if __name__ == '__main__':
    init_Water=time()
    init_Eyes=time()
    init_Health=time()
    Water=1*60
    Eyes=1*60
    Health=1*60
    while True:
        # Water
        if time()-init_Water > Water:
            print("Water")
            musiconloop("water.mp3","yes")
            init_Water=time()
            log_now(msg=input("Enter Your msg: "))

        # Eyes
        if time() - init_Eyes > Eyes:
            print("Eyes")
            musiconloop("eyes.mp3","yes")
            init_Eyes=time()
            log_now(msg=input("Enter Your msg: "))
        # health
        if time() - init_Health > Health:
            print("health")
            musiconloop("health.mp3","yes")
            init_Health=time()
            log_now(msg=input("Enter Your msg: "))


