import time
import random

class Frame():
    def _init_(self,x,data):
        self.data=data
        self.x=x
def stop_and_wait(total,t_time=1,r_time=1):
    print("stop and wait ARQ")
    for i in range(total):
        frame=Frame(i,f"frame{i}")
        print(f"received frame {frame.x} - data: {frame.data}")
        time.sleep(r_time)
        
        ack=int(input(f"did you receive the ack for the frame {frame.x} ? (1/0): "))
        
        if ack==1:
            print(f"ack for the frame {frame.x} received")
        else:
            print(f"ack for the frame {frame.x} not received. resend if needed ")
            
        time.sleep(t_time)
    print("all data transmitted successfully")
    
def go_back_n(total,window_size,t_time=1,r_time=1):
    print("go back n ARQ ")
    frames=[Frame(i,f"frame{i}")for i in range(total)]
    base=0
    while base<total:
        for i in range(base,min(window_size,total)):
            frame=frames[i]
            print(f"received frame {frame.x} - data: {frame.data}")
            time.sleep(r_time)
        
            ack=int(input(f"did you receive the ack for the frame {frame.x} ? (1/0): "))
        
            if ack==1:
                print(f"ack for the frame {frame.x} received")
            else:
                print(f"ack for the frame {frame.x} not received. resend if needed ")
            
            time.sleep(t_time)
        base+=window_size
    print("all data transmitted successfully")
    
def selective_repeat(total,window_size,t_time=1,r_time=1):
    print("selective repeat ")
    frames=[Frame(i,f"frame{i}") for i in range(total)]
    r_frame=set()
    while len(r_frame)<total:
        for i in range(total):
            if i not in r_frame:
                frame=frames[i]
                print(f"received frames {frame.x} - data {frame.data}")
            time.sleep(r_time)
        
            ack=int(input(f"did you receive ack for the frame {frame.x}? (1/0): "))
        
            if ack==1:
                print(f"ack received for the frame{frame.x}")
            else:
                print(f"ack not received for the frame {frame.x}. resend if needed")
            time.sleep(t_time)
    print("all data transmitted successfully")    
        
window_size=int(input("enter the window size: ")) 
total=window_size
print("choose the ARQ:  1.stop and wait   2. go back n   3.selective repeat")
choice=int(input("enter your choice: "))
if choice==1:
    stop_and_wait(total,t_time=1,r_time=1)
elif choice==2:
    go_back_n(total,window_size,t_time=5,r_time=1)
elif choice==3:
    selective_repeat(total,window_size,t_time=5,r_time=5)
else:
    print("invalid input")
    
if _name=='main_':
    main()