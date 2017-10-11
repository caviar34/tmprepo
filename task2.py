#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def find_sequence_slow(sequence):
    return "".join(str(e) for e in range(1,int(sequence)+1)).find(sequence)+1


def find_sequence(sequence):
    last_index=find_last_index(sequence) 
    # вычисляем крайний справа индекс в который входит строка sequence, представляя бесконечный ряд чисел в виде списка последовательных натуральных чисел [1,2,3,..,10,N]
    (minimal_index,minimal_substr)=make_minimal_substr(sequence,last_index)
    #Вычисляем крайний слева индекс с которым граничит строка sequence , в представлении аналогичному выше, а также строку полученную из списка (minimal_index,last_index]
    #print last_index,minimal_index,minimal_substr
    #Результат есть сумма минимального индекса(в представлении ряда как строка символов),первого вхождения sequence в minimal_substr и 1(пересчет индексов)
    return index2index(minimal_index)+minimal_substr.find(sequence)+1
    
def find_last_index(sequence):
    S=sequence
    stest=""
    for i in xrange(1,len(S)+1):
        stest=S[:i]
        S2=stest
        while S2 in S or S in S2:
            if S in S2: return int(stest)
            stest = str(int(stest)+1)
            S2+=stest
            #print "S2:",S2

def make_minimal_substr(sequence,index):
    minimal_substr=""
    while sequence not in minimal_substr:
        minimal_substr=str(index)+minimal_substr
        index -=1
    return (index+1,minimal_substr)

def index2indexbad(Listindex):
    indexofstr=0
    strListindex=str(Listindex)
    for i in xrange(0,len(strListindex)):
        print i, int(strListindex[::-1][i])
        indexofstr+=(10**i)*9*int(strListindex[::-1][i])
    return indexofstr

def index2index(ind):
    strind=str(ind)
    indofstr=len(strind)*ind
    for i in xrange(0,len(strind)-1):
        indofstr-=9*10**i*(len(strind)-i-1)
        #print indofstr
    return indofstr-len(strind)

if __name__ == "__main__":
    sequence=str(sys.argv[1]) 
    assert(find_sequence_slow(sequence) == find_sequence(sequence))
    print find_sequence(sequence)

