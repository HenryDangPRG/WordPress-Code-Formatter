import sys

def fixFormat(file_name):

    original = open(file_name, 'r')
    fixed_copy = open("fixed_" + file_name, 'w')
    
    for line in original:
        line = line.replace('&lt;', '<')
        line = line.replace('&gt;', '>')
        line = line.replace("&quot;", '"')
        fixed_copy.write(line)

    original.close()
    fixed_copy.close()

file_name = sys.argv[1]
fixFormat(file_name)
