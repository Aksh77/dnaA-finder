def findOri(genome):
    skew = [0] #difference between 'G' and 'C' count (#G-#C)
    for i in range(len(genome)):
        if genome[i]=='G':
            skew.append(skew[i]+1)
        elif genome[i]=='C':
            skew.append(skew[i]-1)
        else:
            skew.append(skew[i])
    minSkew = min(skew)
    oriPos = [i for i, x in enumerate(skew) if x == minSkew]
    return oriPos
