import networkx as nx
import matplotlib.pyplot as plt
import csv 
import pandas as pd

G=nx.Graph()
poke = pd.read_csv('RGTE11_CoreDataSet(1).csv', error_bad_lines=False, delimiter = ';',decimal=",")


FIN = poke.loc[poke['COUNTRY'] == "Finland"]
SWE = poke.loc[poke['COUNTRY'] == "Sweden"]
NOR = poke.loc[poke['COUNTRY'] == "Norway"]
DEN = poke.loc[poke['COUNTRY'] == "Denmark"]
ICE = poke.loc[poke['COUNTRY'] == "Iceland"]
G= nx.Graph()

for F in FIN.COUNTRY:
     for S in SWE.COUNTRY:
        for N in NOR.COUNTRY:
            for D in DEN.COUNTRY:
                for C in ICE.COUNTRY:
                    if F == "Finland" and S == "Sweden" and D == "Denmark" and N == "Norway" and C == "Iceland":
                        G.add_node("Finland")
                        G.add_node("Sweden")
                        G.add_node("Denmark")
                        G.add_node("Iceland")
                        G.add_node("Norway")

VFIN= float(FIN.Smk_1_tob_use_F)
VSWE= float(SWE.Smk_1_tob_use_F)
VDEN= float(DEN.Smk_1_tob_use_F)
VNOR= float(NOR.Smk_1_tob_use_F)
VICE= float(ICE.Smk_1_tob_use_F)



if ((VFIN*0.85) < VSWE and (VFIN*1.15) > VSWE) or ((VSWE*0.85) < VFIN and (VSWE*1.15) > VFIN):
    G.add_edge("Finland","Sweden")
if ((VFIN*0.85) < VDEN and (VFIN*1.15) > VDEN) or ((VDEN*0.85) < VFIN and (VDEN*1.15) > VFIN):
    G.add_edge("Finland","Denmark")
if ((VFIN*0.85) < VNOR and (VFIN*1.15) > VNOR) or ((VNOR*0.85) < VFIN and (VNOR*1.15) > VFIN):
    G.add_edge("Finland","Norway")
if ((VFIN*0.85) < VICE and (VFIN*1.15) > VICE) or ((VICE*0.85) < VFIN and (VICE*1.15) > VFIN):
    G.add_edge("Finland","Iceland")
if ((VNOR*0.85) < VSWE and (VNOR*1.15) > VSWE) or ((VSWE*0.85) < VNOR and (VSWE*1.15) > VNOR):
    G.add_edge("Norway","Sweden")
if ((VDEN*0.85) < VSWE and (VDEN*1.15) > VSWE) or ((VSWE*0.85) < VDEN and (VSWE*1.15) > VDEN):
    G.add_edge("Denmark","Sweden")
if ((VICE*0.85) < VSWE and (VICE*1.15) > VSWE) or ((VSWE*0.85) < VICE and (VSWE*1.15) > VICE):
    G.add_edge("Iceland","Sweden")
if ((VDEN*0.85) < VNOR and (VDEN*1.15) > VNOR) or ((VNOR*0.85) < VDEN and (VNOR*1.15) > VDEN):
    G.add_edge("Denmark","Norway")
if ((VDEN*0.85) < VICE and (VDEN*1.15) > VICE) or ((VICE*0.85) < VDEN and (VICE*1.15) > VDEN):
    G.add_edge("Denmark","Iceland")
if ((VNOR*0.85) < VICE and (VNOR*1.15) > VICE) or ((VICE*0.85) < VNOR and (VICE*1.15) > VNOR):
    G.add_edge("Norway","Iceland")


nx.draw(G,with_labels=True)
plt.show()