

def read_file(filename)-> list:
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
            file_lines.append(line) 
    return file_lines

def count_task_1(file_content):

    steering_values = {'forward': 0, 'up': 0, 'down': 0}
    for line in file_content:
        values = line.split(' ', maxsplit=1)
        steering_values[values[0]] += int(values[1])
    depth = steering_values['up'] - steering_values['down']
    return abs(depth * steering_values['forward'])

    
def count_task_2(file_content):
    steering_values = {'forward': 0, 'aim': 0, 'depth': 0}
    for line in file_content:
        values = line.split(' ', maxsplit=1)
        if values[0] in 'down':
            steering_values['aim'] += int(values[1])
        elif values[0] in 'up':
            steering_values['aim'] -= int(values[1])
        else:
            steering_values[values[0]]+= int(values[1])
            steering_values['depth'] += int(values[1])*steering_values['aim'] 
    return steering_values['forward']* steering_values['depth']     
    

def main():
    
    steering_values = read_file("input.txt")
    print(count_task_1(steering_values))
    print(count_task_2(steering_values))

if __name__ =='__main__':
    main()