import os
import re
import linecache

dir_path = os.path.dirname(os.path.realpath(__file__))
filelist = [f for f in os.listdir(dir_path)
            if os.path.isfile(os.path.join(dir_path, f))]

filelist.remove('pastaMaker.py')

try:
    filelist.remove('.DS_Store')
    filelist.remove('ravioli.fasta')
except Exception:
    pass
# r1 = r'\s{3}[0-9]+\x20[ATGCNatgc]+'
r2 = r'[ATGCNatgc]+'
# expression1 = re.compile(r1)
expression2 = re.compile(r2)

target_string = "ORIGIN\r\n"

target_file = dir_path + "\\" + "ravioli.fasta"
for f in filelist:
    target = ""
    # take all the lines in the file opened
    with open(f, "r") as f_source:
        lines = f_source.readlines()

    for word in lines:
        word.index
    # find the (line number + 1) from the word ORIGIN
    start_of_genes = lines.index(target_string) + 1
    # for element in lines:
    #     if expression1.findall(element):
    #         target.append(element)

    # add all subsequent lines into a string and just keep the regex pattern from it
    for i in lines[start_of_genes:]:
        target += i

    # get a list of all matches - expression2.findall(target)
    # join that list together as the final output
    final_output = "".join(expression2.findall(target))
    # c = expression2.findall(target)
    # c = "".join(c)
    f_target = open('ravioli.fasta', "a")
    f_target.write(">" + os.path.splitext(f)[0] + "\n")
    f_target.write(final_output + "\n")
    f_target.close()

# input("All Done! Press Enter to Exit > ")
    # f_source = open(f, 'r')
    # contents = f_source.read()
    # print f
    # idx = contents.index("ORIGIN")
    # print(contents[idx+6], contents[idx+7], contents[idx+8], contents[idx+9])
    # print ""
