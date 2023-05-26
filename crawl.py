import json
import os

dictionary = {}
def is_dadada(line):
    return line == "'''\n"
rootdir = "/Users/yf/Documents/LeetcodeRawdata"
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if (not file.endswith(".py")):
            continue
        file_path = os.path.join(subdir, file)
        f = open(file_path, "r")
        count_dadada = 0
        context = ""
        code = ""
        is_ignore = False
        is_context = True
        line_of_codes = 0
        for line in f.readlines():
            if ((count_dadada == 0) & (not is_dadada(line))):
                break
            if is_dadada(line):
                if (count_dadada != 0):
                    context += line
                    is_ignore = False
                    is_context = False
                    continue
                else:
                    count_dadada+=1
            if (is_context & (line == "\n")):
                continue
            if (line.startswith("Example")):
                is_ignore = True
            if (is_ignore):
                continue
            else:
                if (is_context):
                    context += line
                else:
                    code += line
                    line_of_codes +=1
            if (line_of_codes >20):
               context = ""
               code = "" 
               break
        if ((context != "") & (code != "")):
            dictionary[context] = code

json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("context_example.json", "w") as outfile:
    outfile.write(json_object)