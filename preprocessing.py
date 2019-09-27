import re
import glob
filelist = glob.glob('/home/rajrajeshwari/Desktop/temp/*.txt')  #change username accordingly
nfiles = len(filelist)
for i in range(0,nfiles):
    instr = open(filelist[i],'r').readlines()
    out = filelist[i].split('.txt')
    outf = "_out.txt".join(out)
    outf = re.sub('temp','temp1',outf)
    outstr = open(outf,'w')
    n  = len(instr)
    for j in range(1,n):
        line = instr[j]
        l1 = line.split(" ")
        for wd in range(0,len(l1)):
            l1[wd] = re.sub(r'\\.*|\\[A-Z][A-Z]*_[A-Z]*|\\[A-Z]*','',l1[wd])
        l1 = " ".join(l1)
        l2 = l1.split("\t")
        l2 = l2[1]
        outstr.write(l2)
    outstr.close()

