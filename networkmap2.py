import networkx as nx
import calendar
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from dzcnapyd import dzcnapy_plotlib as dzcnapy
import netmap

#Tree
#lincoln_list = [
## aws logs get-log-events --log-group-name A --log-stream-name a --output text > a.log 
## cat a.log | grep -v REJECT | awk '/ / {print $6, $7}' > a-accept.log
## vi a-accept.log
## type:
## 1,$ s/ /", "/g
## and type:
## 1,$norm I     ("
## and type:
## 1,$norm A"),
## and type:
## :wq
## vi networkmap.py
## and type:
## :set number
## should see line 8 as start or lincoln_list
## go to row 29 and type:
## :.-1read a-accept.log
## that will read in the accepted connection hosts
## and type:
## :wq
#print(str(netmap))
#]
F = nx.DiGraph(netmap)
#F = nx.DiGraph(lincoln_list)

pos = graphviz_layout(F)
nx.draw_networkx(F, pos, **dzcnapy.attrs)
dzcnapy.set_extent(pos, plt)
dzcnapy.plot     ("lincoln")

