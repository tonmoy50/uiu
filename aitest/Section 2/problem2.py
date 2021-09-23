import re
from datetime import datetime
import datefinder


def finddate(source):
    date_list = []

    match = re.search( r'\d{2}-\d{2}-\d{4}', source )

    while 1:
        
        #print(1)
        match = re.search( r'\d{2}-\d{2}-\d{4}', source )
        if( re.search( r'\d{2}-\d{2}-\d{4}', source ) is None ):
             break
        
        
        date_list.append(match.group())
        temp = match.group()
        temp1 = temp.split("-")
       

        source = source.split(temp, 1)
        source[0] += "----" 
        source[0] += temp1[2]

        source = "".join(source)
        

    
    for i in range( len(date_list) ):
        valid = 1

        day, month, year = date_list[i].split("-")
        day = int(day)
        month = int(month)
        year = int(year)
        
        try:
            datetime(int(year), int(month), int(day))
        except ValueError:
            valid = 0
        
        if valid==0:
            date_list[i] = ""

    
    try:
    
        date_list.remove("")
    except ValueError:
        pass
    

    freq = []

    for ele in date_list:
        freq.append( date_list.count(ele) )
    
    

    return date_list[freq.index( max(freq) )]  




def main():
    source = str(input())
    

    print( finddate(source) )

    


if __name__ == "__main__":
    main()