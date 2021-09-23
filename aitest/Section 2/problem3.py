
def last_locker(num, lockers):

    
    opened = 0
    total = 0
    pass_count = 1
    

    while total < num:
        
        for i in range( 0, len(lockers), 1+pass_count ):
            
            opened = lockers[i]
            
            lockers[i] = -1          

            total+=1
        pass_count += 1
        
        
        lockers = list(filter(lambda a: a!=-1, lockers))
        
    
    return opened

    
        

def main():
    num = int(input())

    lockers = [i for i in range(1, num+1)]
    
    print( last_locker(num, lockers) )
    


if __name__ == "__main__":
    main()