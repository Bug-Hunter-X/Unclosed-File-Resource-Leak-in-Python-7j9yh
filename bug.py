def function_with_unclosed_file(filename):
    f = open(filename, 'r')
    # ... some code that processes the file ... 
    # forgot to close the file
    return #Missing f.close()

function_with_unclosed_file("data.txt")