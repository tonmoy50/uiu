import numpy as np 
import random as rnd 



def demand():
    
    random_digit = rnd.randint(1, 100)
    daily_demand = 0
    

    if ( random_digit >= 1 and random_digit <= 10 ):
        daily_demand = 0
    elif ( random_digit >= 11 and random_digit <= 35 ):
        daily_demand = 1
    elif ( random_digit >= 36 and random_digit <= 70 ):
        daily_demand = 2
    elif ( random_digit >= 71 and random_digit <= 91 ):
        daily_demand = 3
    else:
        daily_demand = 4
    
    return [daily_demand, random_digit]
    

def lead_time():
    random_lead = rnd.randint(0, 9)

    if (random_lead >= 1 and random_lead <= 6):
        lead = 1
    elif (random_lead >= 7 and random_lead <= 9):
        lead = 2
    else:
        lead = 3
    
    return [lead, random_lead]

def orders(m, end_inv):
    order_unit = m - end_inv
    return order_unit

def main():

    #n = 5
    #m = 11
    #inventory = 3
    #order_unit = 8
    #order_arrives = 1

    n,m,inventory,order_unit,order_arrives = input("Enter N, M, Begining_Inventory, Order_Unit, Order_Arrival Sequentially with comma: ").split(',')
    n = int(n)
    m = int(m)
    inventory = int(inventory)
    order_unit = int(order_unit)
    order_arrives = int(order_arrives)

    ending_inventory = []
    shortage_quantity = []

    print( "Cycle", "Days", "Beg'n_Inventory", "Rand_Demand", "Demand", "End_Inventory", "Shortage", "Order_number", "Rand_Lead", "Order_Arrives" )

    for i in range(1, n+1):
        lead = lead_time()
        
        for j in range(1, n+1):
            
            temp_order = order_arrives
            if temp_order == -1:
                temp_order = '_'

           

            if order_arrives == -1: #check krchi j order arrive koreche kina krle inventory te order amount add korechi
                inventory = inventory + order_unit - (shortage_quantity[-1] if shortage_quantity[-1] != '_' else 0)
                order_arrives = '_'
            else:
                if order_arrives != '_':
                    order_arrives = order_arrives - 1
            
            
            
            
            demands = demand()



            if (inventory-demands[0]) >= 0:
                shortage_quantity.append('_')
                ending_inventory.append(inventory-demands[0])
            else:
                temp_val = demands[0] - inventory
                shortage_quantity.append(temp_val)
                ending_inventory.append(0)
            
            
            
            
            
            
            print("  {}\t{}\t {}\t\t{}\t{}\t{}\t\t{}\t{}\t   {}\t\t   {}".format(i if j==1 else ' ', j, inventory, demands[1], demands[0], ending_inventory[-1], shortage_quantity[-1], orders(m, ending_inventory[-1]) if j==n else '_',  lead[1] if j==n else '_', temp_order)  )
            #print('\n')
            inventory = ending_inventory[-1]
        
        #order_unit = m - ending_inventory[-1]
        order_arrives = lead[0]
        print('\n')


    print("Average Number of Ending Inventory: {}".format( (sum(ending_inventory)/len(ending_inventory)) ) )

    
    print("Average Number of Shortage in Days: {}".format( sum( i!='_' for i in shortage_quantity )/(n*n) ) )
        
                


            

    


if __name__ == "__main__":
    main()



