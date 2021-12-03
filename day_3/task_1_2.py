def read_file(filename)->list:
    """
        Just reading file nothing special about it

        Parameters
        ----------
        filename : str 
                   directory to a file 


        Returns
        -------
        list: contents of file divided by lines  
    """
    file_lines =[]
    with open(filename, 'r') as file:
        for line in file:
            file_lines.append(str(line)) 
    return file_lines, len(file_lines[0])-1

def count_task_1(file_content, size_of_bits) -> tuple:
    gamma, epsilon ='',''
    for position in range(size_of_bits):
        numb_bits_1 =0
        for number in file_content:
            if "1" in number[position] :
                numb_bits_1+=1
        if numb_bits_1 > len(file_content)/2:
            gamma +="1"
            epsilon +="0"
        else:
            gamma +="0"
            epsilon+="1" 
    
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    return gamma_dec*epsilon_dec
    
def count_task_2(file_content, size_of_bits):
    most_common_list = file_content.copy()
    least_common_list = file_content.copy()
    for position in range(size_of_bits):
        most_common_list = count_air(most_common_list, position)
        least_common_list = count_air(least_common_list, position, False)
    oxygen = int(most_common_list[0],2) 
    CO2 =  int(least_common_list[0], 2) 
    return oxygen * CO2


def count_air(list, position, is_oxygen=True):    
    numb_bits_1=0
    if len(list) >1:
        for number in list:
                if "1" in number[position]:
                    numb_bits_1+=1
        if numb_bits_1 >= len(list)/2 :
            condition = str(int(is_oxygen))
        else:
            condition = str(int(not is_oxygen))
        return [bit_number for bit_number in list if condition in bit_number[position]  ]
    return list




def main():
    binary_numbers, size = read_file("input.txt")
    print(count_task_1(binary_numbers, size))
    print (count_task_2(binary_numbers, size))

if __name__ =='__main__':
    main()