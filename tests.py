from ppalms import *

test_lines = ["#a","b","c","d","#e"]
test_lines_comments = ["b","c","d"]
test_lines_empty = ["#a","b","c","","d","#e",""]

#to conduct test, call the test function in main and try a good case and edge 
#case for each. 

# tests the exlude lines functionality 
def exclude_test():
    exclude_lines(test_lines)
    print_lines(test_lines) 

# tests the group lines functionality 
def group_test(): 
    group_lines(test_lines)
    print_lines(test_lines)

# tests the remove comments functionality 
def comment_test():
    rem_comments(test_lines)
    print_lines(test_lines)
    #rem_comments(test_lines_comments)      # reserved for the no comments in the list case, result in the test report
    #print_lines(test_lines_comments)       # reserved for the no comments in the list case, result in the test report

# tests the remove empty lines functionality 
def empty_test():
    rem_empty_lines(test_lines_empty)
    print_lines(test_lines_empty)

# tests the import file functionality 
def import_test():
    import_file()
        

if __name__ == "__main__":
    exclude_test()
    group_test()
    comment_test()
    empty_test()
    import_test()