import os
for x in range(1,21):
        print("Running test case: " + str(x))
        infile = "testcasesUnix/re" + str(x) + "In.txt "
        outfile = "output" + str(x) + ".txt"
        os.system("python automata.py " + infile + outfile)
