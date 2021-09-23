import numpy as np 
import sys 
import  matplotlib.pyplot as plt


pa = 0.2
ps = 0.3


def ssq_lifo_and_sjf(n, arrival_list1, departure_list1, sett):

    #print(arrival_list1)
    #print(departure_list1)
    
    arrival_iter = 0
    departure_iter = 0
    clock = 0
    server_free = 1
    customer_in_queue = []
    customer_served = 0
    departure = sys.maxsize
    item_popped = 0
    
    area_under_qt = [0]
    area_under_bt = [0]
    total_delays = [0]    
    arrival_list = []
    time_of_arrival = []
    departure_list = []
    service_time_list = [ departure_list1[i]-arrival_list1[i] for i in range(len(departure_list1) ) ]
    #print(service_time_list)
    #universal_clock = arrival_list1+departure_list1

    #initialization of first row
    first_arrival = arrival_list1[arrival_iter]
    arrival_iter = arrival_iter+1
    arrival_list.append(first_arrival)
    time_of_arrival.append(arrival_list[-1])
    
    

    while customer_served<n:
        prev_clock = clock

        if arrival_list[-1]<departure:            

            clock = arrival_list[-1]

            if server_free:     #server status checking and relevant operation 
                server_free = 0
                
                customer_served = customer_served + 1
                
                if sett == 1:
                    item_popped = time_of_arrival.pop()
                else:
                    #index_val = departure_list1.index( min(departure_list1) )
                    temp_service_time = sys.maxsize
                    ultimate_index = 0
                    for i in range(len(time_of_arrival) ):
                        index_val = arrival_list1.index(time_of_arrival[i])
                        service_time = service_time_list[index_val]

                        if service_time<temp_service_time:
                            ultimate_index = i
                            temp_service_time = service_time
                
                    item_popped = time_of_arrival.pop(ultimate_index)                
                
                departure = departure_list1[arrival_list1.index(item_popped)]
                #departure_iter = departure_iter+1
                #departure = departure+clock
                departure_list.append(departure)

                temp = clock-item_popped

                total_delays.append( total_delays[-1]+temp )

            customer_in_queue.append(len(time_of_arrival))
            
            
            
            try:

                temp1 = arrival_list1[arrival_iter]
                arrival_iter = arrival_iter+1            
                arrival_list.append(temp1)
            except IndexError:
                arrival_list1.append( np.random.geometric(p=pa)+clock )
                departure_list1.append( np.random.geometric(p=ps)+arrival_list1[-1] )

                temp1 = arrival_list1[arrival_iter]
                arrival_iter = arrival_iter+1            
                arrival_list.append(temp1)
            

            time_of_arrival.append(arrival_list[-1])
            
            
        
        else:
            clock = departure
            server_free = 1
            departure = sys.maxsize
        
        #print("Prev: ", prev_clock)
        #print("Current: ", clock)

        area_under_bt.append( area_under_bt[-1]+(abs(clock-prev_clock))*server_free )
        area_under_qt.append( area_under_qt[-1]+abs((clock-prev_clock))*customer_in_queue[-1] )

        #print("Clock: ", clock)
        #print("Item: ", item_popped)
        #print("Departure: ", departure)
        #print("Arrival List: ", arrival_list)
        #print("Time of arrival: ", time_of_arrival)
        #print("Area under QT: ", area_under_qt)
        #print("Area under BT: ", area_under_bt)

    #print("Delay list;: ", total_delays)
    print("Average Delay: ", total_delays[-1]/n)
    print("Expected Number of Customer in queue: ", (area_under_qt[-1]/clock) )
    print("Utilization of the Server: ", area_under_bt[-1])

    return [total_delays, customer_in_queue, area_under_bt, arrival_list1]


def ssq_fifo(n):
    clock = 0
    server_free = 1
    customer_in_queue = [0]
    customer_served = 0
    departure = sys.maxsize
    item_popped = 0
    
    area_under_qt = [0]
    area_under_bt = [0]
    total_delays = [0]    
    arrival_list = []
    time_of_arrival = []
    departure_list = []
    temp_area = [0]

    #initialization of first row
    first_arrival = np.random.geometric(p=pa)
    arrival_list.append(first_arrival)
    time_of_arrival.append(arrival_list[-1])
    
    

    while customer_served<n:
        prev_clock = clock

        if arrival_list[-1]<departure:
            clock = arrival_list[-1]
            if server_free:     #server status checking and relevant operation 
                server_free = 0
                departure = np.random.geometric(p=ps)
                departure = departure+clock
                departure_list.append(departure)
                customer_served = customer_served + 1
                

                item_popped = time_of_arrival.pop(0)
                
                
                temp = clock-item_popped
                total_delays.append( total_delays[-1]+temp )

            customer_in_queue.append( len(time_of_arrival) )
            temp1 = np.random.geometric(p=pa)
            temp1 = temp1 + clock
            arrival_list.append(temp1)
            time_of_arrival.append(arrival_list[-1])
            
            
        
        else:
            clock = departure
            server_free = 1
            departure = sys.maxsize
        
        
        

        area_under_bt.append( area_under_bt[-1]+(clock-prev_clock)*server_free )
        area_under_qt.append( area_under_qt[-1]+(clock-prev_clock)*customer_in_queue[-1] )

        #print("Clock: ", clock)
        #print("Item: ", item_popped)
        #print("Departure: ", departure)
        #print("Arrival List: ", arrival_list)
        #print("Time of arrival: ", time_of_arrival)
        #print("Area under QT: ", area_under_qt)
        #print("Area under BT: ", area_under_bt)

    #print("Delay list;: ", total_delays)
    print("Average Delay: ", total_delays[-1]/n)
    print("Expected Number of Customer in queue: ", area_under_qt[-1]/clock)
    print("Utilization of the Server: ", area_under_bt[-1])

    #print(arrival_list)
    #print(departure_list)


    return [arrival_list, departure_list, total_delays, customer_in_queue, area_under_bt]


def drawing_here_delay(arrival_list, arrival_list_lifo, arrival_list_sjf, total_delays, total_delays_lifo, total_delays_sjf):
    plt.xlabel("Arrival Time")
    plt.ylabel("Delays")
    
    x1 = np.linspace(0, len(total_delays), len(total_delays))
    x2 = np.linspace(0, len(total_delays_lifo), len(total_delays_lifo))
    x3 = np.linspace(0, len(total_delays_sjf), len(total_delays_sjf))

    plt.plot(x1, total_delays, label="FIFO")
    plt.plot(x2, total_delays_lifo, label="LIFO")
    plt.plot(x3, total_delays_sjf, label="SJF")


    plt.legend()
    plt.show()
    
def drawing_here_customer(arrival_list, arrival_list_lifo, arrival_list_sjf, customer_in_queue, customer_in_queue_lifo, customer_in_queue_sjf):

    plt.xlabel("Arrival")
    plt.ylabel("Customer In Queue")

    x1 = np.linspace(0, len(customer_in_queue), len(customer_in_queue))
    x2 = np.linspace(0, len(customer_in_queue_lifo), len(customer_in_queue_lifo))
    x3 = np.linspace(0, len(customer_in_queue_sjf), len(customer_in_queue_sjf))

    plt.plot(x1, customer_in_queue, label="FIFO")
    plt.plot(x2, customer_in_queue_lifo, label="LIFO")
    plt.plot(x3, customer_in_queue_sjf, label="SJF")
    
    plt.legend()
    plt.show()

def drawing_here_server(arrival_list, arrival_list_lifo, arrival_list_sjf, server_util,  server_util_lifo, server_util_sjf):




    plt.xlabel("Arrival")
    plt.ylabel("Server Utilization")

    x1 = np.linspace(0, len(server_util), len(server_util))
    x2 = np.linspace(0, len(server_util_lifo), len(server_util_lifo))
    x3 = np.linspace(0, len(server_util_sjf), len(server_util_sjf))

    plt.plot(x1, server_util, label="FIFO")
    plt.plot(x2, server_util_lifo, label="LIFO")
    plt.plot(x3, server_util_sjf, label="SJF")
    
    plt.legend()
    plt.show()


def multiple(n):

    print("------------------FIFO--------------------")
    fifo = ssq_fifo(n)
    arrival_list = fifo[0]
    departure_list = fifo[1]
    total_delays = fifo[2]
    customer_in_queue = fifo[3]
    server = fifo[4]
    k = len(departure_list)

    #balancing
    #total_delays.pop(0)
    for i in range( len(arrival_list)-n ):
        departure_list.append( arrival_list[k]+np.random.geometric(p=ps) )
        k = k+1
        
    for i in range( len(arrival_list)-len(total_delays) ):
        total_delays.insert(0, 0)

    #print(arrival_list)
    #print(server)
    #print(departure_list)
    #print(total_delays)
    #print(customer_in_queue)

    

    print("------------------LIFO--------------------")
    lifo = ssq_lifo_and_sjf(n, arrival_list, departure_list, 1)
    total_delays_lifo = lifo[0]
    customer_in_queue_lifo = lifo[1]
    server_lifo = lifo[2]
    arrival_list_lifo = lifo[3]
    #print( len(arrival_list_lifo) )
    #print( len(customer_in_queue_lifo) )
    customer_in_queue_lifo.insert(0, 0)

    for i in range( len(arrival_list)-len(total_delays_lifo) ):
        total_delays_lifo.insert(0, 0)

    print("------------------SJF--------------------")
    sjf = ssq_lifo_and_sjf(n, arrival_list, departure_list, 2)
    total_delays_sjf = sjf[0]
    customer_in_queue_sjf = sjf[1]
    server_sjf = sjf[2]
    arrival_list_sjf = sjf[3]
    #print(customer_in_queue_sjf)
    #print( len(arrival_list_sjf) )
    #print( len(customer_in_queue_sjf) )
    
    for i in range( len(arrival_list)-len(total_delays_sjf) ):
        total_delays_sjf.insert(0, 0)

    if n != 6:
        
        drawing_here_delay(arrival_list, arrival_list_lifo, arrival_list_sjf, total_delays, total_delays_lifo, total_delays_sjf)       
        drawing_here_customer(arrival_list, arrival_list_lifo, arrival_list_sjf, customer_in_queue, customer_in_queue_lifo, customer_in_queue_sjf)
        drawing_here_server(arrival_list, arrival_list_lifo, arrival_list_sjf, server, server_lifo, server_sjf)



def main():
    n = 6
    

    multiple(6)

    multiple(50)
    multiple(100)

    






if __name__ == "__main__":
    main()