from collections import defaultdict


def read_coordinates_from_file(filename):
    with open(filename) as file:
        begin_coords = []
        end_coords = []
        
        for line in file:
            line = line.strip("\n")
            coords = line.split(" -> ",1)
            x_begin, y_begin  = coords[0].split(",", 1)
            x_end, y_end = coords[1].split(",", 1)
            begin_coords.append((int(x_begin), int(y_begin)))
            end_coords.append((int(x_end), int(y_end)))
            #print(f"Poczatek {begin_coords[-1]} | Koniec {end_coords[-1]}")

    return begin_coords, end_coords

def count_cover_lines(begin_set, end_set):

    coords_dictionary = {}

    for pair_index in range(len(begin_set)):

        begin_pair = begin_set[pair_index]
        end_pair = end_set[pair_index]

        if begin_pair[0] == end_pair[0]:
            for y in range(min(begin_pair[1], end_pair[1]), max(begin_pair[1], end_pair[1] )+1    ):
                if (begin_pair[0], y) not in coords_dictionary:
                    coords_dictionary[(begin_pair[0], y)] = 1
                else:
                    coords_dictionary[(begin_pair[0], y)] += 1    
        if begin_pair[1] == end_pair[1]:
                for x in range(min(begin_pair[0], end_pair[0]), max(begin_pair[0], end_pair[0] )+1    ):
                    if (x, begin_pair[1]) not in coords_dictionary:
                        coords_dictionary[(x, begin_pair[1])] = 1
                    else:
                        coords_dictionary[(x, begin_pair[1])] += 1 
                       


    print(coords_dictionary)
    print(sum([1 for pair in coords_dictionary if coords_dictionary[pair] > 1]))            


def count_cover_lines_2(begin_set, end_set):

    coords_dictionary = {}

    for pair_index in range(len(begin_set)):

        begin_pair = begin_set[pair_index]
        end_pair = end_set[pair_index]

        if begin_pair[0] == end_pair[0]:
            for y in range(min(begin_pair[1], end_pair[1]), max(begin_pair[1], end_pair[1] )+1    ):
                if (begin_pair[0], y) not in coords_dictionary:
                    coords_dictionary[(begin_pair[0], y)] = 1
                else:
                    coords_dictionary[(begin_pair[0], y)] += 1    
        elif begin_pair[1] == end_pair[1]:
                for x in range(min(begin_pair[0], end_pair[0]), max(begin_pair[0], end_pair[0] )+1    ):
                    if (x, begin_pair[1]) not in coords_dictionary:
                        coords_dictionary[(x, begin_pair[1])] = 1
                    else:
                        coords_dictionary[(x, begin_pair[1])] += 1 
        else:
            dx = 1 if begin_pair[0] < end_pair[0] else -1
            dy = 1 if begin_pair[1] < end_pair[1] else -1
            for x, y  in  zip(range(begin_pair[0], end_pair[0]+dx,dx ), 
                              range(begin_pair[1], end_pair[1]+dy,dy )):

                if ( x, y) in coords_dictionary:
                    coords_dictionary[(x, y)] += 1
                else:
                    coords_dictionary[(x,y)] = 1



    print(sum([1 for pair in coords_dictionary if coords_dictionary[pair] > 1]))  
        


b, e = read_coordinates_from_file("input.txt")
count_cover_lines_2(b, e)
#dicts = generate_maps_for_sets(b, e)
#print(sum([1  for i in dicts if dicts[i] > 1]))
