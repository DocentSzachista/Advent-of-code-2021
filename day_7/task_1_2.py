
def read_file(filename):
    with open(filename) as file:
        return [ int(x) for x in file.readline().split(',')]

def calc_crabs_position(crabs_positions, task_1=False):
    dict_cost = {x : 0 for x in range(0, max(crabs_positions)+1)}
    for element in range(max(crabs_positions)+1):
        sum = 0 
        for element_2 in crabs_positions:
            if element != element_2:
                if not task_1:
                    sum+= count_sum(abs(element_2-element))
                else:
                    sum+= count_cost(abs(element_2-element))
        if dict_cost[element] == 0 or dict_cost[element] > sum:
            dict_cost[element] = sum
    print(sorted(dict_cost.items
    (), key=lambda item:item[1] )[0])

def count_cost(diff):
    return sum(range(1, diff))

def count_sum(diff):
    return  (diff+1)*diff/2


def main():
    horizontal_positions = read_file("input.txt")
    calc_crabs_position(horizontal_positions)

if __name__ == '__main__':
    main()