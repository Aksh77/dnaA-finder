def hammingDist(pat1, pat2):
    hDist = 0
    for i in range(len(pat1)):
        if pat1[i] != pat2[i]:
            hDist += 1
    return hDist

def generateNeighbours(kmer, d):
    bases = ['A','C','G','T']
    k = len(kmer)
    nKmers = [kmer]
    for mismatch in range(d):
        nKmers_temp = nKmers[:]
        for approxKmer in nKmers_temp:
            for i in range(k):
                mutations = bases[:]
                mutations.remove(approxKmer[i])
                for b in mutations:
                    nKmer = approxKmer[:i]+b+approxKmer[i+1:]
                    if nKmer not in nKmers:
                        nKmers.append(nKmer)
    return nKmers

def getKmers(text, k, d):
    neighbourKmers = []
    l = len(text)-k+1
    neighbourKmers = []
    for i in range(l):
        kmer = text[i:i+k]
        nKmers = generateNeighbours(kmer, d)
        for j in nKmers:
            if j not in neighbourKmers:
                neighbourKmers.append(j)
    return neighbourKmers

def reverseComplement(s):
    r = []
    for i in s:
        if i=='A':
            r.append('T')
        elif i=='T':
            r.append('A')
        elif i=='C':
            r.append('G')
        else:
            r.append('C')
    r.reverse()
    return ''.join(r)

def approxPatternCount(text, pattern, d):
    lp = len(pattern)
    l = len(text)-lp+1
    c = 0
    for i in range(l):
        kmer = text[i:i+lp]
        if hammingDist(kmer, pattern) <= d:
            c += 1
        if hammingDist(reverseComplement(kmer), pattern) <= d:
            c += 1
    return c

def getFreqKmer(text, k, d):
    kmers = getKmers(text, k, d)
    kmerCount = {}
    for kmer in kmers:
        kmerCount[kmer] = approxPatternCount(text, kmer, d)
    max_count = 0
    freqKmers = []
    for k, v in kmerCount.items():
        if v>max_count:
            freqKmers = [k]
            max_count = v
        elif v==max_count:
            freqKmers.append(k)
    return (freqKmers, v)
