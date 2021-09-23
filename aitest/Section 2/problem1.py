def checker(input_list):
    final_text = input_list[0]
    final_text = list(final_text)

    text_lengths = len(input_list[0])

    
    for i in range( 1, len(input_list) ):
        for j in range(text_lengths):
            

            if final_text[j] != input_list[i][j]:
                final_text[j] = "?"
            
    
    
    

    return "".join( map( str, final_text ))
        








def main():
    input_list = input()
    
    input_list = input_list.split(" ")
    
    

    print( checker(input_list) )


if __name__ == "__main__":
    main()