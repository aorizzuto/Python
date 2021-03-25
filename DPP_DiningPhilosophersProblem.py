"""
Dinning philosopher problem.

The dining philosophers problem states that there are 5 philosophers sharing a circular table and they eat and think alternatively. 
There is a bowl of rice for each of the philosophers and 5 chopsticks. 
A philosopher needs both their right and left chopstick to eat. 
A hungry philosopher may only eat if there are both chopsticks available.
Otherwise a philosopher puts down their chopstick and begin thinking again.
"""

import threading
import time
import random

class Philosopher(threading.Thread):
    """Class for philosopher actions."""

    sleepMin = 0                # Min time to sleep between tasks
    sleepMax = 1                # Max time to sleep between tasks
    Eating_Thinking_Time = 4    # Eating/Thiking time
    Loops = 20                  # Number of loops

    def __init__(self, key, leftChopstick, rightChopstick):
        """Initialize the philosopher."""
        super().__init__()
        self.key = key                          # Number of philosopher
        self.leftChopstick = leftChopstick      # Left chopstick
        self.rightChopstick = rightChopstick    # Right chopstick

    def run(self):                                     
        """Actions for the philosopher."""
        spaces = getSpaces(self.key)                    # Spaces to format by column each philosopher
        
        for i in range(self.Loops):                             
            self.stopThinking(spaces)                   # Philosopher go to dinner table
            self.Sleep()                                # Movements cannot be super fast, maybe another philosopher grab the chopstick first
            self.leftChopstick.take(self.key,'LEFT')    # Get left chopstick
            self.Sleep() 
            self.rightChopstick.take(self.key,'RIGHT')  # Get right chopstick
            self.Sleep() 
            self.startEating(spaces)                    # Start eating
            self.Sleep(self.Eating_Thinking_Time) 
            self.stopEating(spaces)                     # Stop eating
            self.Sleep() 
            self.leftChopstick.dropChopstick('LEFT')    # Drop left chopstick
            self.Sleep() 
            self.rightChopstick.dropChopstick('RIGHT')  # Drop right chopstick
            self.Sleep() 
            self.startThinking(spaces)                  # Leave dinner table
            self.Sleep(self.Eating_Thinking_Time) 

    def startEating(self,spaces):
        """Eating action started."""
        print("{}{} philosopher START EATING ...".format(spaces,self.key))

    def stopEating(self,spaces):
        """Eating action stopped."""
        print("{}{} philosopher STOP EATING ...".format(spaces,self.key))

    def startThinking(self,spaces):
        """Thinking action stopped."""
        print("{}{} philosopher START THINKING ...".format(spaces,self.key))

    def stopThinking(self,spaces):
        """Thinking action stopped."""
        print("{}{} philosopher STOP THINKING and want to EAT ... ".format(spaces,self.key))

    def Sleep(self, sl = 0):
        """Sleeping action."""
        if sl == 0:
            time.sleep(random.uniform(0,1))
        else:
            time.sleep(sl)


class Chopstick():
    """Class to handle chopsticks."""

    def __init__(self, key):        
        """Initialize the chopstick."""
        self.philosopher = None     # Ningún filosofo tiene el chopstick
        self.taken = False          # Nadie lo tomó
        self.lock = threading.Condition(threading.Lock())   # Está usándose

    def take(self, phil,side):
        """Take the chopstick."""
        spaces = getSpaces(phil)
        with self.lock:
            while self.taken == True:
                print(f"{spaces}{phil} is waiting for the chopstick ...")
                self.lock.wait()
            self.philosopher = phil
            self.taken = True
            self.lock.notifyAll()   # Le avisa a todos los que quedaron lockeados
            print("{}{} takes {} chopstick.".format(spaces,self.philosopher, side))


    def dropChopstick(self, side):
        """Drop the chopstick."""
        spaces = getSpaces(self.philosopher)
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            print("{}{} drop {} chopstick".format(spaces,self.philosopher, side))
            self.philosopher = None            # Nadie lo tiene
            self.taken = False          # No está tomado
            self.lock.notifyAll()


def getSpaces(key):
    """Get spaces to get philosophers by column."""
    return ''.join(["\t\t\t" for i in range(key)])


def main():
    """Start app."""
    n = 5
    chopsticks   = [Chopstick(i) for i in range(n)]    # Creación de los chopsticks    
    philosophers = [Philosopher(i, chopsticks[i%n],chopsticks[(i+1)%n]) for i in range(n)] # Creación de los filosofos
    
    for i in range(n):
        philosophers[i].start()


if __name__ == "__main__":
    main()