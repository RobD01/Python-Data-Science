# minesweeper. 1st argument: array of bomb locations (row, column). 2nd argument: size of the board (row,column)

def minesweeper (bomb, row, column):

    board = [[0 for i in range(column)] for j in range(row)]
    
    for bomb_loc in bomb:
        (bomb_row, bomb_col) = bomb_loc
        board[bomb_row][bomb_col] = -1
        
        row_range = range (bomb_row -1 , bomb_row + 2)
        col_range = range (bomb_col -1 , bomb_col + 2)
        
        for i in row_range:
            current_i = i
            for j in col_range:
                current_j = j
                
                if (0 <= i < row and 0 <= j < column and board [i][j] != -1):
                    board[i][j] += 1
    

    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in board]))



bomberman= """ Here's bomberman:
                                                                                
                      ,                                                         
             ,      .,,                                                         
               , ,,,, ,,                                                        
                .,        ,,,                                                   
               ,,      ,                                                        
                  , ,  ,,,                                                      
                  ,@.                                                           
              ((#%&%#((#           //*** ,                                      
             (&&&&%%%%%%         ,#(((/////                                     
            /#&&&&%%%%%###(      .%%##(,.((                                     
          /##%%%%%%###(*   ((.     &&&&        .........                         
        .(##%%%%%%%###(((((((#/                @@&..../* ......                       
        /#%%%%%%%%%%%########%%,       .     *,...%@@&      .*                  
        (%%%%%&%%%%%%%%%%%%%%%%(    ........,,...&%%..    .,@@((&               
        %%&%%%&&&&&&&%%%%%%%%%%/   ........*,,...&&&....  .&&&.                 
         &&&&&&&&&&&&&&&&&&&&%(    ,,,...  *,,,.&%%.......,&&,.                 
          &&&&&&&&&&&&&&&&&%##/*// /***,.. /**,,##........%%%.  .***,,          
             &&&&&&&&&&%%#&&%(((((  ////*,...///****,,,,,,%#,. #(((//*/*        
                         @@%##((#(...((/////*,, (/////////*, .   ##((((*        
                            *(     ((../#  (////****,,,,,,, .   (&&&%%          
                                        *.,(&%%#####%/*,                        
                                         &%###((////(                           
                                 ./*,,, @@%#((((///(/                           
                                %(((/** ,*@@&&&/.  /&                           
                                %####(((/***(#%#*/#.                            
                                 ########((/**    (,.                           
                                  %########(//,      #,                         
                                   /########((          /.       (///****       
                                      %##%%#              %,. (((((((((((       
                                                            ##(((((((((((       
                                                           %##(((((((((*        
                                                           ,%%#((((((#          
                                                             ,%%####            
                                                                                

"""
    
minesweeper ( [[0,0],[1,2]] , 5,4 )
print(bomberman)