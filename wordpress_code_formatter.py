import sys

def fixFormat(file_name):
    
    dict = {
        '&lt;':'<', '&gt;':'>', '&quot;':"'", 
        '&amp;lt;':'<', '&amp;gt;':'>', '&amp;quot;':"'", 
    }

    original = open(file_name, 'r')
    fixed_copy = open("fixed_" + file_name, 'w')
    
    for line in original:
        for key in dict.keys():
            if key in line:
                line = line.replace(key, dict[key])
        fixed_copy.write(line)

    original.close()
    fixed_copy.close()

file_name = sys.argv[1]
fixFormat(file_name)
