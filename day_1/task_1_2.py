

def read_file(file_name) -> list:
    """ read file under given location

        Parameters
        ----------
        filename : str 
                   file locations

        Returns
        -------
        list : list of depth values   

    """

    lines = []
    with open(file_name, 'r') as file:
        for line in  file:
            lines.append(line)
        return lines


# liczenie dla zadania 1
# ciekawe bo dla zadania 1 nie dolicza jednego elementu a dla zadania 2 wszystko pieknie (Mozliwa )xD
def count_dec_increased_ammount(numbers) -> tuple:

    """ 
        Count the number of depth increases / decreases
        Parameters
        ----------
        numbers : list (int)
                  list of depths


        Returns
        -------
        touple (x1 , x2) 
        x1 : number of depth decreases
        x2 : number of depth increases
        -----------       

        Description
        -----------
        Function compares in a loop if i element is smaller than i+1 in a list. If the condition 
        is true local variable     
    
    """
    decreased, increased = 0, 0
    for i in range(0, len(numbers)-1):
        if numbers[i+1] > numbers[i]:
            increased +=1
        elif numbers[i+1] < numbers[i]: 
            decreased +=1
        else:
            pass
# musimy uwzglednic jeszcze ostatnia liczbe czy jest increasedrement czy decrement             
    # if numbers[-1] > numbers[-2]:
    #      increased+=1
    # else:
    #      decreased +=1
    return decreased, increased

# zadanie 2
def count_sliding_window(numbers) -> tuple:
    """ Count the number of times the sum of measurements in sliding window of size 3
        increases

        Parameters
        ----------
        numbers : list (int)
                  list of depths
        

        Returns
        -------
         touple (x1 -> number of decreases, x2 -> number of increasedreases)

        ----------

        Description
        -----------
        Function counts sums of sliding window of size 3 to a  list,

        which is later sent to a function :func:`count_dec_increased_ammount`
    
    """
    decreased, increasedreased = 0, 0
    sums_windows_array = []
    # liczenie sum przesuwajacego sie okna 
    for index in range(0, len(numbers)-2):
            window_sum = 0 
            for window_element in range(0, 3):
                window_sum += int(numbers[index+window_element])
            sums_windows_array.append(window_sum)
    return count_dec_increased_ammount(sums_windows_array)
            

def main():
    
    numbers = read_file("input.txt")
    print(count_dec_increased_ammount(numbers))
    print(count_sliding_window(numbers))

if __name__ =='__main__':
    main()