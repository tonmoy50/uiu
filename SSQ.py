import random
import numpy as np

def ashar_somoy():
    random.seed(0)
    x = [random.randint(2,5) for i in range(1,10)]
    #x.sort()

    return x

def kajer_somoy():
    random.seed(6)
    y = [random.randint(2,7) for i in range(1,10)]
    #y.sort()

    return y


if __name__ == '__main__':

    serverBusy = 0
    cDelay = 0
    total_c_Delay = 0
    customersServed = 0
    Queue = []
    n = 4

    #a = olot_palot()
    #print(a)

    x = ashar_somoy()
    y = kajer_somoy()
    print(x)
    print(y)

    currentTime = 0
    #random.seed(6)
    #interarrivalTime = random.randint(1, 9);  
    interarrivalTime = x.pop(0)
    arrivalTime = currentTime + interarrivalTime ; 

    departureTime = 999

    while customersServed<n:

        if arrivalTime < departureTime:
            currentTime = arrivalTime
            print("currnet time when arrival:",currentTime)
        else:
            currentTime = departureTime
            print("currnet time when departure:",currentTime)

        if currentTime == arrivalTime:
            currentTime = arrivalTime
            if serverBusy == 0 :
                cDelay = 0
                serverBusy = 1
                #serviceTime = random.randint(1, 5)
                serviceTime = y.pop(0)
                print("service time : ", serviceTime)
                departureTime = currentTime + serviceTime
            else:
                Queue.insert(0,currentTime)
                print("queue : ",Queue)

            #for next customer
            #interarrivalTime = random.randint(1, 9)
            interarrivalTime = x.pop(0)
            arrivalTime  = currentTime + interarrivalTime
            print("arrival time for next customer :",arrivalTime)

        else:
            customersServed = customersServed + 1
            print("customer served : ",customersServed)
            serverBusy = 0

            if len(Queue) != 0:
                jobDeparts = Queue.pop()

                cDelay =   currentTime - jobDeparts
                print(" Delay Current Time : ",currentTime)
                print(" Delay Arrival Time : ",jobDeparts)
                print("delay : ",cDelay)
                total_c_Delay = total_c_Delay + cDelay
                #serviceTime = random.randint(1, 5)
                serviceTime = y.pop()
                print("service time : ", serviceTime)
                departureTime = currentTime + serviceTime 
            else:
                departureTime = 999

    print("total delay : ", total_c_Delay)