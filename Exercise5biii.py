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
V2FIN= float(FIN.Smk_1_tob_use_M)
V2SWE= float(SWE.Smk_1_tob_use_M)
V2DEN= float(DEN.Smk_1_tob_use_M)
V2NOR= float(NOR.Smk_1_tob_use_M)
V2ICE= float(ICE.Smk_1_tob_use_M)


if ((((VFIN*0.85) < VSWE and (VFIN*1.15) > VSWE) or ((VSWE*0.85) < VFIN and (VSWE*1.15) > VFIN)) and (((V2FIN*0.85) < V2SWE and (V2FIN*1.15) > V2SWE) or ((V2SWE*0.85) < V2FIN and (V2SWE*1.15) > V2FIN))):
    G.add_edge("Finland","Sweden")
if ((((VFIN*0.85) < VDEN and (VFIN*1.15) > VDEN) or ((VDEN*0.85) < VFIN and (VDEN*1.15) > VFIN)) and (((V2FIN*0.85) < V2DEN and (V2FIN*1.15) > V2DEN) or ((V2DEN*0.85) < V2FIN and (V2DEN*1.15) > V2FIN))):
    G.add_edge("Finland","Denmark")
if ((((VFIN*0.85) < VNOR and (VFIN*1.15) > VNOR) or ((VNOR*0.85) < VFIN and (VNOR*1.15) > VFIN)) and (((V2FIN*0.85) < V2NOR and (V2FIN*1.15) > V2NOR) or ((V2NOR*0.85) < V2FIN and (V2NOR*1.15) > V2FIN))):
    G.add_edge("Finland","Norway")
if ((((VFIN*0.85) < VICE and (VFIN*1.15) > VICE) or ((VICE*0.85) < VFIN and (VICE*1.15) > VFIN)) and (((V2FIN*0.85) < V2ICE and (V2FIN*1.15) > V2ICE) or ((V2ICE*0.85) < V2FIN and (V2ICE*1.15) > V2FIN))):
    G.add_edge("Finland","Iceland")
if ((((VNOR*0.85) < VSWE and (VNOR*1.15) > VSWE) or ((VSWE*0.85) < VNOR and (VSWE*1.15) > VNOR)) and (((V2NOR*0.85) < V2SWE and (V2NOR*1.15) > V2SWE) or ((V2SWE*0.85) < V2NOR and (V2SWE*1.15) > V2NOR))):
    G.add_edge("Norway","Sweden")
if ((((VDEN*0.85) < VSWE and (VDEN*1.15) > VSWE) or ((VSWE*0.85) < VDEN and (VSWE*1.15) > VDEN)) and (((V2DEN*0.85) < V2SWE and (V2DEN*1.15) > V2SWE) or ((V2SWE*0.85) < V2DEN and (V2SWE*1.15) > V2DEN))):
    G.add_edge("Denmark","Sweden")
if ((((VICE*0.85) < VSWE and (VICE*1.15) > VSWE) or ((VSWE*0.85) < VICE and (VSWE*1.15) > VICE)) and (((V2ICE*0.85) < V2SWE and (V2ICE*1.15) > V2SWE) or ((V2SWE*0.85) < V2ICE and (V2SWE*1.15) > V2ICE))):
    G.add_edge("Iceland","Sweden")
if ((((VDEN*0.85) < VNOR and (VDEN*1.15) > VNOR) or ((VNOR*0.85) < VDEN and (VNOR*1.15) > VDEN)) and (((V2DEN*0.85) < V2NOR and (V2DEN*1.15) > V2NOR) or ((V2NOR*0.85) < V2DEN and (V2NOR*1.15) > V2DEN))):
    G.add_edge("Denmark","Norway")
if ((((VDEN*0.85) < VICE and (VDEN*1.15) > VICE) or ((VICE*0.85) < VDEN and (VICE*1.15) > VDEN)) and (((V2DEN*0.85) < V2ICE and (V2DEN*1.15) > V2ICE) or ((V2ICE*0.85) < V2DEN and (V2ICE*1.15) > V2DEN))):
    G.add_edge("Denmark","Iceland")
if ((((VNOR*0.85) < VICE and (VNOR*1.15) > VICE) or ((VICE*0.85) < VNOR and (VICE*1.15) > VNOR)) and (((V2NOR*0.85) < V2ICE and (V2NOR*1.15) > V2ICE) or ((V2ICE*0.85) < V2NOR and (V2ICE*1.15) > V2NOR))):
    G.add_edge("Norway","Iceland")


nx.draw(G,with_labels=True)
plt.show()