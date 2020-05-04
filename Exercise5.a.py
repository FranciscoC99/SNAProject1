import networkx as nx
import matplotlib.pyplot as plt
import csv 
import pandas as pd

G=nx.Graph()
poke = pd.read_csv('RGTE11_CoreDataSet(1).csv', error_bad_lines=False, delimiter = ';')


FIN = poke.loc[poke['COUNTRY'] == "Finland"]
SWE = poke.loc[poke['COUNTRY'] == "Sweden"]
NOR = poke.loc[poke['COUNTRY'] == "Norway"]
DEN = poke.loc[poke['COUNTRY'] == "Denmark"]
ICE = poke.loc[poke['COUNTRY'] == "Iceland"]




for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P1:
                        for W in SWE.P1:
                            for E in DEN.P1:
                                for O in NOR.P1:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P1 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P1 does not preserve the topology of the graph")


for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P2:
                        for W in SWE.P2:
                            for E in DEN.P2:
                                for O in NOR.P2:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P2 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P2 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P3:
                        for W in SWE.P3:
                            for E in DEN.P3:
                                for O in NOR.P3:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P3 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P3 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P4:
                        for W in SWE.P4:
                            for E in DEN.P4:
                                for O in NOR.P4:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P4 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P4 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P5:
                        for W in SWE.P5:
                            for E in DEN.P5:
                                for O in NOR.P5:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P5 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P5 does not preserve the topology of the graph")



for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P6:
                        for W in SWE.P6:
                            for E in DEN.P6:
                                for O in NOR.P6:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P6 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P6 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P7:
                        for W in SWE.P7:
                            for E in DEN.P7:
                                for O in NOR.P7:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P7 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P7 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P8:
                        for W in SWE.P8:
                            for E in DEN.P8:
                                for O in NOR.P8:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P8 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P8 does not preserve the topology of the graph")


for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P9:
                        for W in SWE.P9:
                            for E in DEN.P9:
                                for O in NOR.P9:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P9 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P9 does not preserve the topology of the graph")


for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P10:
                        for W in SWE.P10:
                            for E in DEN.P10:
                                for O in NOR.P10:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P10 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P10 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P11:
                        for W in SWE.P11:
                            for E in DEN.P11:
                                for O in NOR.P11:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P11 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P11 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P12:
                        for W in SWE.P12:
                            for E in DEN.P12:
                                for O in NOR.P12:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P12 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P12 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P13:
                        for W in SWE.P13:
                            for E in DEN.P13:
                                for O in NOR.P13:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P13 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P13 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P14:
                        for W in SWE.P14:
                            for E in DEN.P14:
                                for O in NOR.P14:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P14 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P14 does not preserve the topology of the graph")          
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P15:
                        for W in SWE.P15:
                            for E in DEN.P15:
                                for O in NOR.P15:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P15 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P15 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P16:
                        for W in SWE.P16:
                            for E in DEN.P16:
                                for O in NOR.P16:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P16 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P16 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.P17:
                        for W in SWE.P17:
                            for E in DEN.P17:
                                for O in NOR.P17:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter P17 preserves the topology of the graph")
                                    else:
                                        print ("The parameter P17 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.C2:
                        for W in SWE.C2:
                            for E in DEN.C2:
                                for O in NOR.C2:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter C2 preserves the topology of the graph")
                                    else:
                                        print ("The parameter C2 does not preserve the topology of the graph") 
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.C3:
                        for W in SWE.C3:
                            for E in DEN.C3:
                                for O in NOR.C3:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter C3 preserves the topology of the graph")
                                    else:
                                        print ("The parameter C3 does not preserve the topology of the graph") 
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.C4:
                        for W in SWE.C4:
                            for E in DEN.C4:
                                for O in NOR.C4:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter C4 preserves the topology of the graph")
                                    else:
                                        print ("The parameter C4 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O1:
                        for W in SWE.O1:
                            for E in DEN.O1:
                                for O in NOR.O1:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O1 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O1 does not preserve the topology of the graph")


for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O2:
                        for W in SWE.O2:
                            for E in DEN.O2:
                                for O in NOR.O2:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O2 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O2 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O3:
                        for W in SWE.O3:
                            for E in DEN.O3:
                                for O in NOR.O3:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O3 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O3 does not preserve the topology of the graph")







for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O6:
                        for W in SWE.O6:
                            for E in DEN.O6:
                                for O in NOR.O6:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O6 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O6 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O7:
                        for W in SWE.O7:
                            for E in DEN.O7:
                                for O in NOR.O7:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O7 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O7 does not preserve the topology of the graph")




for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O9:
                        for W in SWE.O9:
                            for E in DEN.O9:
                                for O in NOR.O9:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O9 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O9 does not preserve the topology of the graph")


for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O10:
                        for W in SWE.O10:
                            for E in DEN.O10:
                                for O in NOR.O10:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O10 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O10 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O12:
                        for W in SWE.O12:
                            for E in DEN.O12:
                                for O in NOR.O12:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O12 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O12 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O13:
                        for W in SWE.O13:
                            for E in DEN.O13:
                                for O in NOR.O13:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O13 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O13 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O14:
                        for W in SWE.O14:
                            for E in DEN.O14:
                                for O in NOR.O14:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O14 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O14 does not preserve the topology of the graph")          
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O15:
                        for W in SWE.O15:
                            for E in DEN.O15:
                                for O in NOR.O15:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O15 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O15 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.O16:
                        for W in SWE.O16:
                            for E in DEN.O16:
                                for O in NOR.O16:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter O16 preserves the topology of the graph")
                                    else:
                                        print ("The parameter O16 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W1A:
                        for W in SWE.W1A:
                            for E in DEN.W1A:
                                for O in NOR.W1A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W1A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W1A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W2A:
                        for W in SWE.W2A:
                            for E in DEN.W2A:
                                for O in NOR.W2A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W2A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W2A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W3A:
                        for W in SWE.W3A:
                            for E in DEN.W3A:
                                for O in NOR.W3A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W3A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W3A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W4A:
                        for W in SWE.W4A:
                            for E in DEN.W4A:
                                for O in NOR.W4A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W4A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W4A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W5A:
                        for W in SWE.W5A:
                            for E in DEN.W5A:
                                for O in NOR.W5A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W5A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W2A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W6A:
                        for W in SWE.W6A:
                            for E in DEN.W6A:
                                for O in NOR.W6A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W6A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W6A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W7A:
                        for W in SWE.W7A:
                            for E in DEN.W7A:
                                for O in NOR.W7A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W7A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W7A does not preserve the topology of the graph")                                                                                                                                                                                                         
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W8A:
                        for W in SWE.W8A:
                            for E in DEN.W8A:
                                for O in NOR.W8A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W8A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W8A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W9A:
                        for W in SWE.W9A:
                            for E in DEN.W9A:
                                for O in NOR.W9A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W9A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W9A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W10A:
                        for W in SWE.W10A:
                            for E in DEN.W10A:
                                for O in NOR.W10A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W10A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W10A does not preserve the topology of the graph")                                    
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W11A:
                        for W in SWE.W11A:
                            for E in DEN.W11A:
                                for O in NOR.W11A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W11A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W11A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W12A:
                        for W in SWE.W12A:
                            for E in DEN.W12A:
                                for O in NOR.W12A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W12A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W12A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W13A:
                        for W in SWE.W13A:
                            for E in DEN.W13A:
                                for O in NOR.W13A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W13A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W13A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W14A:
                        for W in SWE.W14A:
                            for E in DEN.W14A:
                                for O in NOR.W14A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W14A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W14A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W15A:
                        for W in SWE.W15A:
                            for E in DEN.W15A:
                                for O in NOR.W15A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W15A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W15A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W16A:
                        for W in SWE.W16A:
                            for E in DEN.W16A:
                                for O in NOR.W16A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W16A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W16A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W17A:
                        for W in SWE.W17A:
                            for E in DEN.W17A:
                                for O in NOR.W17A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W17A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W17A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W18A:
                        for W in SWE.W18A:
                            for E in DEN.W18A:
                                for O in NOR.W18A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W18A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W18A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W19A:
                        for W in SWE.W19A:
                            for E in DEN.W19A:
                                for O in NOR.W19A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W19A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W19A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W20A:
                        for W in SWE.W20A:
                            for E in DEN.W20A:
                                for O in NOR.W20A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W20A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W20A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W21A:
                        for W in SWE.W21A:
                            for E in DEN.W21A:
                                for O in NOR.W21A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W21A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W21A does not preserve the topology of the graph")
                                        

                                        


                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W25A:
                        for W in SWE.W25A:
                            for E in DEN.W25A:
                                for O in NOR.W25A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W25A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W25A does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W26A:
                        for W in SWE.W26A:
                            for E in DEN.W26A:
                                for O in NOR.W26A:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W26A preserves the topology of the graph")
                                    else:
                                        print ("The parameter W26A does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W1C:
                        for W in SWE.W1C:
                            for E in DEN.W1C:
                                for O in NOR.W1C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W1C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W1C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W2C:
                        for W in SWE.W2C:
                            for E in DEN.W2C:
                                for O in NOR.W2C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W2C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W2C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W3C:
                        for W in SWE.W3C:
                            for E in DEN.W3C:
                                for O in NOR.W3C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W3C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W3C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W4C:
                        for W in SWE.W4C:
                            for E in DEN.W4C:
                                for O in NOR.W4C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W4C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W4C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W5C:
                        for W in SWE.W5C:
                            for E in DEN.W5C:
                                for O in NOR.W5C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W5C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W5C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W6C:
                        for W in SWE.W6C:
                            for E in DEN.W6C:
                                for O in NOR.W6C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W6C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W6C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W7C:
                        for W in SWE.W7C:
                            for E in DEN.W7C:
                                for O in NOR.W7C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W7C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W7C does not preserve the topology of the graph")                                                                                                                                                                                                         
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W8C:
                        for W in SWE.W8C:
                            for E in DEN.W8C:
                                for O in NOR.W8C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W8C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W8C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W9C:
                        for W in SWE.W9C:
                            for E in DEN.W9C:
                                for O in NOR.W9C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W9C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W9C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W10C:
                        for W in SWE.W10C:
                            for E in DEN.W10C:
                                for O in NOR.W10C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W10C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W10C does not preserve the topology of the graph")                                    
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W11C:
                        for W in SWE.W11C:
                            for E in DEN.W11C:
                                for O in NOR.W11C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W11C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W11C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W12C:
                        for W in SWE.W12C:
                            for E in DEN.W12C:
                                for O in NOR.W12C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W12C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W12C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W13C:
                        for W in SWE.W13C:
                            for E in DEN.W13C:
                                for O in NOR.W13C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W13C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W13C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W14C:
                        for W in SWE.W14C:
                            for E in DEN.W14C:
                                for O in NOR.W14C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W14C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W14C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W15C:
                        for W in SWE.W15C:
                            for E in DEN.W15C:
                                for O in NOR.W15C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W15C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W15C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W16C:
                        for W in SWE.W16C:
                            for E in DEN.W16C:
                                for O in NOR.W16C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W16C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W16C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W17C:
                        for W in SWE.W17C:
                            for E in DEN.W17C:
                                for O in NOR.W17C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W17C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W17C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W18C:
                        for W in SWE.W18C:
                            for E in DEN.W18C:
                                for O in NOR.W18C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W18C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W18C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W19C:
                        for W in SWE.W19C:
                            for E in DEN.W19C:
                                for O in NOR.W19C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W19C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W19C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W20C:
                        for W in SWE.W20C:
                            for E in DEN.W20C:
                                for O in NOR.W20C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W20C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W20C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W21C:
                        for W in SWE.W21C:
                            for E in DEN.W21C:
                                for O in NOR.W21C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W21C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W21C does not preserve the topology of the graph")
 
                                        


                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W25C:
                        for W in SWE.W25C:
                            for E in DEN.W25C:
                                for O in NOR.W25C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W25C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W25C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.W26C:
                        for W in SWE.W26C:
                            for E in DEN.W26C:
                                for O in NOR.W26C:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter W26C preserves the topology of the graph")
                                    else:
                                        print ("The parameter W26C does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.MM1:
                        for W in SWE.MM1:
                            for E in DEN.MM1:
                                for O in NOR.MM1:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter MM1 preserves the topology of the graph")
                                    else:
                                        print ("The parameter MM1 does not preserve the topology of the graph")
                                        
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.MM2:
                        for W in SWE.MM2:
                            for E in DEN.MM2:
                                for O in NOR.MM2:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter MM2 preserves the topology of the graph")
                                    else:
                                        print ("The parameter MM2 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.MM3:
                        for W in SWE.MM3:
                            for E in DEN.MM3:
                                for O in NOR.MM3:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter MM3 preserves the topology of the graph")
                                    else:
                                        print ("The parameter MM3 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.MM4:
                        for W in SWE.MM4:
                            for E in DEN.MM4:
                                for O in NOR.MM4:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter MM4 preserves the topology of the graph")
                                    else:
                                        print ("The parameter MM4 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.MM5:
                        for W in SWE.MM5:
                            for E in DEN.MM5:
                                for O in NOR.MM5:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter MM5 preserves the topology of the graph")
                                    else:
                                        print ("The parameter MM5 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.MM6:
                        for W in SWE.MM6:
                            for E in DEN.MM6:
                                for O in NOR.MM6:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter MM6 preserves the topology of the graph")
                                    else:
                                        print ("The parameter MM6 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.MM7:
                        for W in SWE.MM7:
                            for E in DEN.MM7:
                                for O in NOR.MM7:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter MM7 preserves the topology of the graph")
                                    else:
                                        print ("The parameter MM7 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.MM8:
                        for W in SWE.MM8:
                            for E in DEN.MM8:
                                for O in NOR.MM8:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter MM8 preserves the topology of the graph")
                                    else:
                                        print ("The parameter MM8 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E1:
                        for W in SWE.E1:
                            for E in DEN.E1:
                                for O in NOR.E1:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E1 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E1 does not preserve the topology of the graph")


for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E2:
                        for W in SWE.E2:
                            for E in DEN.E2:
                                for O in NOR.E2:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E2 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E2 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E3:
                        for W in SWE.E3:
                            for E in DEN.E3:
                                for O in NOR.E3:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E3 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E3 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E4:
                        for W in SWE.E4:
                            for E in DEN.E4:
                                for O in NOR.E4:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E4 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E4 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E5:
                        for W in SWE.E5:
                            for E in DEN.E5:
                                for O in NOR.E5:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E5 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E5 does not preserve the topology of the graph")



for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E6:
                        for W in SWE.E6:
                            for E in DEN.E6:
                                for O in NOR.E6:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E6 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E6 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E7:
                        for W in SWE.E7:
                            for E in DEN.E7:
                                for O in NOR.E7:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E7 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E7 does not preserve the topology of the graph")



for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E9:
                        for W in SWE.E9:
                            for E in DEN.E9:
                                for O in NOR.E9:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E9 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E9 does not preserve the topology of the graph")


for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E10:
                        for W in SWE.E10:
                            for E in DEN.E10:
                                for O in NOR.E10:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E10 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E10 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E11:
                        for W in SWE.E11:
                            for E in DEN.E11:
                                for O in NOR.E11:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E11 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E11 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E12:
                        for W in SWE.E12:
                            for E in DEN.E12:
                                for O in NOR.E12:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E12 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E12 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E13:
                        for W in SWE.E13:
                            for E in DEN.E13:
                                for O in NOR.E13:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E13 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E13 does not preserve the topology of the graph")
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E14:
                        for W in SWE.E14:
                            for E in DEN.E14:
                                for O in NOR.E14:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E14 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E14 does not preserve the topology of the graph")          
for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E15:
                        for W in SWE.E15:
                            for E in DEN.E15:
                                for O in NOR.E15:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E15 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E15 does not preserve the topology of the graph")

for F in FIN.COUNTRY:
    for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway":
                    for I in FIN.E17:
                        for W in SWE.E17:
                            for E in DEN.E17:
                                for O in NOR.E17:
                                    if I == W and W == E and W == O and E == O:
                                        print("The parameter E17 preserves the topology of the graph")
                                    else:
                                        print ("The parameter E17 does not preserve the topology of the graph")
