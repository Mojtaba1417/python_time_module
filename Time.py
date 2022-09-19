import datetime as dt
class Time:
    def __init__(self,hour=10,minute=12,second=24):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
        
    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self,value):
        if isinstance(value,int) and 0<=value<24:
            self.__hour=value
        else:
            print("Invalid number . ")

    @property
    def minute(self):
        return self.__minute
    @minute.setter
    def minute(self,value):
        if isinstance(value,int) and 0<=value<60:
            self.__minute=value
        else:
            print("Invalid number . ")
     
    def getSecond(self):
        return self.__second
    def setSecond(self,value):
        if isinstance(value,int) and 0<=value<60:
            self.__second=value
        else:
            print("Invalid number . ")
    second=property(getSecond,setSecond)

    # def __str__(self):
    #     return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def __repr__(self):
        if self.hour<12:
            return str(self)+"AM"
        elif self.hour==12:
            return str(self)+"PM"
        else:
            return f"{self.hour-12:02}:{self.minute:02}:{self.second:02} PM"
    def __iter__(self):
        return self
    def atTime(self):
        return not (self.minute or self.second)
    
    def __next__(self):
        self.second=(self.second+1)%60
        if self.second==0:
            self.minute=(self.minute+1)%60
            if self.minute==0:
                self.hour=(self.hour+1)%24
        
        return self
    def set(self ,w):
        
        from winsound import Beep
        if self.hour==w.hour and self.minute==w.minute and self.second==w.second:
            print("wake up")
            for i in range(5):
                Beep(2000,500)    
if __name__=="__main__":
    now=dt.datetime.now()
    d=Time(hour=now.hour,minute=now.minute,second=now.second)
    u=Time(hour=21,minute=58,second=32)
    while True:
        Time.set(d,u)
        print(next(d))
        
        import time  # to use sleep function for 1 second delay
        import os    # to clear terminal and print new object
        
        time.sleep(1)
        os.system('cls')

