def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

function_with_closed_file("data.txt") 