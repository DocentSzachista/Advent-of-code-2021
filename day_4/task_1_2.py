
def read_file(filename)-> list:
    """ Read numbers list and bingo tables from a file

        
        Returns
        -------
        list : list of bingo moves
        list : list of bingo tables 
    """
    moves_list = ''
    bingo_tables=[]
    bingo_table =[]
    counter = 0
    with open(filename, 'r') as file:
        moves_list = [int(numb) for numb in file.readline().split(',')]
        for line in file:
            if len(line)>1:
                
                column = [int(x)for x in line.split()]
                bingo_table.append(column)
                counter +=1
                if counter > 4:
                    bingo_tables.append(bingo_table.copy())
                    bingo_table = []
                    counter = 0
    return moves_list, bingo_tables               


def count_task_1(moves_list, bingo_tables):
    """
        Count task one - find first bingo that wins

        -----------
        Description
        -----------
        For every move check every bingo table for considered number
        if it contains sign this place with -1 and count this up to lists
        If any of the rows or columns will be equal 5, return the table and move

        -------
        Returns
        -------
        list : bingo_table that wins
        move : move in which table was chosen
    """
    for move in moves_list:
        for bingo_table in bingo_tables:
            # helper lists to count up if we have found bingo
            rows = [0, 0, 0, 0, 0]
            columns = [0, 0, 0, 0, 0]
            for x in range(len(bingo_table)):
                for y in range(len(bingo_table)):
                    # found move  
                    if move ==bingo_table[x][y]:
                         bingo_table[x][y] = -1
                    # check if the certain index was already visited 
                    # and add it to count    
                    if bingo_table[x][y] ==-1:
                         rows[x]+=1
                         columns[y]+=1
                    # if found bingo 
                    if rows[x] == 5 or columns[y] == 5:
                        return bingo_table , move

def count_task_2(moves_list, bingo_tables):
    """
        Count task two - find the last bingo_table that wins

        -----------
        Description
        -----------
        Function does the same thing as the count_task_1 but with difference that when the bingo table 
        that wins is found, it is being discarded if it isn't the last one  
        -------
        Returns
        -------
        list : last bingo_table that wins
        move : move in which table was chosen


    """
    table_to_delete =[]
    to_delete = False 
    for move in moves_list:
        # clean the bingo tables list of the ones in which bing has been found
        # Or return if it is the last bingo 
        for to_remove in table_to_delete:
            if len(bingo_tables) > 1:
                    bingo_tables.remove(to_remove)
            else: 
                    return to_remove, move
            table_to_delete = []
        for bingo_table in bingo_tables:
            to_delete = False
            rows = [0, 0, 0, 0, 0]
            columns = [0, 0, 0, 0, 0]
            for x in range(len(bingo_table)):
                
                for y in range(len(bingo_table)):
                    if move ==bingo_table[x][y]:
                         bingo_table[x][y] = -1  
                    if bingo_table[x][y] ==-1:
                         rows[x]+=1
                         columns[y]+=1
                    # check if we have found bingo     
                    if rows[x] == 5 or columns[y] == 5:
                        if len(bingo_tables) > 1:
                            to_delete= True
                        else:
                            return bingo_table , move
            # add table to delete to list 
            if to_delete:
                table_to_delete.append(bingo_table)
       
def count_sum(table, move)-> None:
    bingo_sum =0
    for x in range(len(table)):
        for y in range(len(table)):
            if table[x][y] != -1:
                bingo_sum+=table[x][y]
    print(bingo_sum*move)

def main ():
    move_list, bingo_tables = read_file('input.txt')
    table, move = count_task_2(move_list, bingo_tables)#count_task_1(move_list, bingo_tables)
    count_sum(table, move)

if __name__ == '__main__':
    main()