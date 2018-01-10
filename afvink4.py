import re
import time




def promoter(line):
    try:
        print(re.search("(TTGACA)(.{15,25})(TATA)(.{5,15})(ATG)(.+)(TAG|TAA|TGA)", line))
    except Exception:
        print("None")
    

def ecoli():
    ecoli = open("ecoli.fasta", 'r')
    for line in ecoli:
        if not line.startswith(">"):
            line = line.strip()
            line += line
    print(line[:100])
    return line

def zuiver(file2):
    seq = ""
    for line in file2:
        if not line.startswith(">"):
            line = line.strip()
            seq += line
    print(seq)

    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")

    print(a+t+c+g)
    print(len(seq))
    if len(seq) == a+t+c+g:
        print("Dit is zuiver DNA")
    else:
        print("Dit is geen zuiver DNA")


def isDNA(file2):
    pattern = "^[ATCG]+$"
    for line in file2:
        if not line.startswith(">"):
            line = line.strip()
        if not line.startswith(">"):
            DNA = re.search(pattern, line)
    if DNA:
        print("This is DNA")
    else:
        print("This is not DNA")
    #print("This is DNA")

        
    

def openfile2():
    file2 = open("protein.fasta", "r")
    file2 = file2.readlines()
    return file2


def aantonen(p53_lijst):
    pattern = "[BJOUZ]+"
    for sequentie in p53_lijst:
        no_aminoacids = re.search(pattern, sequentie)
        if no_aminoacids:
            print(sequentie, "There are letters in this sequence that do not code for an amino acid")
        else:
            print("All the letters in this sequence code for an amino acid")
    
    
        

def herkennen(sequentielijst):
    zoeken = "MCNSSC[MV]GGMNRR"   #"MCNSCC[MV]GGMNRR"
    p53_lijst = []
    try:
        for sequentie in sequentielijst:
            #print(sequentie)
            p53 = re.search(zoeken, sequentie)
            if p53:
                p53_lijst.append(sequentie)
                #print(p53.group(0))
    except Exception as e:
        print("No p53 has been found")
        raise SystemExit
    return p53_lijst
    
          
    
'''def schoonmaken(sequenties):
    sequenties = sequenties.replace("\n", "")
    return sequenties'''


def lists(file):
    accessiecode = []
    sequentie = []
    sequence = ""
    for line in file:
        line = line.strip()
        line = line.replace("\n", "")
        if line.startswith(">"):
            sequentie.append(sequence)
            sequence = ""
            accessiecode.append(line)
        else:
            sequence += line
    return accessiecode, sequentie


'''def dictionary(file):
    keys = {}'''
    


def openfile():
    #accessiecode = []
    #sequentie = []
    file = open("Mus_musculus.GRCm38.pep.all.fa", "r")
    return file
        
    





def main():
    file = openfile()
    accessiecodes, sequentielijst = lists(file)
    print(sequentielijst[5:10])
    #sequentielijst = schoonmaken(sequenties)
    p53_lijst = herkennen(sequentielijst)
    #print(p53_lijst)
    aantonen(p53_lijst)
    file2 = openfile2()

    startTime = time.time()
    isDNA(file2)
    endTime = time.time()
    time1 = endTime - startTime
    startTime2 = time.time()
    zuiver(file2)
    endTime2 = time.time()
    time2 = endTime2 - startTime2
    print("Bij regex duurt het", time1, "seconden")
    print("Bij de iteratieve functie duurt het", time2, "seconden")

    line = ecoli()
    promoter(line)    
    
    

main ()
