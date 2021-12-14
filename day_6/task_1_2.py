def read_file(filename):
    with open(filename) as file:
        return [ int(x) for x in file.readline().split(',')]


def count_lanternfish_growth(days, lanternfishes):
    for day in range(days):
        for fish in range(len(lanternfishes)):
            if lanternfishes[fish] == 0:
                lanternfishes[fish] = 6
                lanternfishes.append(8)
            else:
                lanternfishes[fish]-=1
    print(len(lanternfishes))

def count_lanternfish_growth_optimized(days, lanternfishes):
    days_of_reproduction = [0 for x in range(9)]
    old_value = 0
    for index in lanternfishes:
        days_of_reproduction[index]+=1
    for day in range(days):
        old_value = days_of_reproduction[0]
        for left_to_reproduce in  range(1, len(days_of_reproduction)):
            days_of_reproduction[left_to_reproduce-1] = days_of_reproduction[left_to_reproduce]
        days_of_reproduction[8] = old_value
        days_of_reproduction[6]+= old_value
    print(sum(days_of_reproduction))
    
def main():
    lanternfishes = read_file("input.txt")
    #count_lanternfish_growth(256, lanternfishes)
    count_lanternfish_growth_optimized(256, lanternfishes)


main()        