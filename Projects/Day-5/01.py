def readFile(file):
    try:
        f = open(file,'r')
        i = 0
        while True:
            line = f.readline()
            if not line:
                break
            i += 1
        print(type(line))
        f.close()
        print(f"Number of lines are {i}")
    except FileNotFoundError:
        print(f"The file {file} not found.")

f = 'Projects/Day-5/01.txt'
# f = '01.txt'
readFile(f)