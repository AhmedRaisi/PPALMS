# PPALMS ver 0.1

from os.path import exists

def import_file():
    filename = input("enter filename: ")
    straight_line()

    # check if file exists
    file_exists = exists(filename)
    if not file_exists:
        print("file name does not exist")
        return -1

    # open file and read lines
    print("file imported")
    file = open(filename, 'r')

    lines = []
    myline = file.readline()
    while myline:
        lines.append(myline[:-1]) # append line and remove /n at the end of line
        myline = file.readline()

    file.close()
    return lines

def rem_empty_lines(lines):
    # remove empty lines
    i = 0
    while i < len(lines):
        if(lines[i] == ""):
            lines.remove(lines[i])
            i -= 1 # reduce array by 1
        i += 1

    return lines

def rem_comments(lines):
    # remove comments functionality
    prompt = input("remove comments? (yes/no): ")
    straight_line()
    if(prompt == "yes"):
        i = 0
        while i < len(lines):
            if(lines[i][0] == "#"): # if line is comment
                lines.pop(i)
                i -= 1
            i += 1

    return lines

def print_lines(lines):
    # print lines by number
    for i in range(len(lines)):
        if isinstance(lines[i], list): # if grouped lines exist
            for j in range(len(lines[i])):
                num = str(i) + "." + str(j)
                print(num, ": ", lines[i][j])
        else:
            print(i, ": ", lines[i])

    straight_line()
        
def exclude_lines(lines):
    # code to exclude lines
    exclude = list(map(int, input("Enter val of lines to exclude with space between vals or press enter for no exclusion: ").split()))
    straight_line()
    exclude.sort(reverse=True) # sort descending order

    for i in range(len(exclude)):
        if(exclude[i] < len(lines) and exclude[i] >= 0): # if line num between bounds
            lines.pop(exclude[i])
        else:
            print("val of lines out of index bounds")
    
    return lines

def group_lines(lines):
    prompt = input("group lines? (yes/no): ")
    straight_line()
    while(prompt == "yes"):
        lower = 0
        upper = 0
        while True: # catch non integer val inputted
            try:
                lower = int(input("enter num of start of line to group: "))
                straight_line()
                upper = int(input("enter num of end of line to group: "))
                straight_line()
            except ValueError:
                print("--please enter a valid integer--")
                straight_line()
                continue
            else:
                break

        if(upper<=lower or upper >= len(lines) or upper < 1 or lower < 0 or lower >= (len(lines)-1)): # if out of bounds
            print("--bounds error--")
            straight_line()
        else:
            create_inner_list(upper, lower, lines)

        print_lines(lines)

        prompt = input("group more lines? (yes/no): ")
        straight_line()

    return lines

def create_inner_list(upper, lower, lines):
    inner_list = []
    for i in range(upper, lower - 1, -1): # check if line already in group
        if(isinstance(lines[i], list)): 
            print("--line already in a group--")
            straight_line()
            return -1

    for i in range(upper, lower - 1, -1): # group lines into a list
        element = lines.pop(i)
        inner_list.append(element)

    inner_list.reverse()

    # add grouped lines to main lines
    lines.insert(lower, inner_list)
    return 1

def straight_line():
    print("------------------------")

# main ppalms function
def ppalms():
    lines = import_file()
    if(lines == -1): # if file don't exist
        straight_line()
        return -1

    lines = rem_empty_lines(lines)
    lines = rem_comments(lines)
    
    print_lines(lines)

    lines = exclude_lines(lines)
    
    print_lines(lines)

    lines = group_lines(lines)

    print_lines(lines)

    return 1

if __name__ == "__main__":
    ppalms()
