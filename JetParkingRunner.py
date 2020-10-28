
 Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



#Project : Jet Parking                                       ***

import datetime
import networkx as nx
import dwave_networkx as dnx

import matplotlib.pyplot as plt
from dwave.system.samplers import DWaveSampler

from dwave.system.composites import EmbeddingComposite


sampler = EmbeddingComposite(DWaveSampler())
timestamp = datetime.datetime.now()

#CONSTRAINTS
# 2 x 8 rows. Used generator.

G = nx.Graph()


                                                    
G.add_edges_from([(1, 2 ),(2, 3 ),(3, 4 ),(4, 5 ),(5, 6 ),(6, 7 ),(7, 8 ),(9, 10 ),(10, 11 ),(11, 12 ),(12, 13 ),(13, 14 ),(14, 15 ),(15, 16 ),(1, 9 ),(2, 10 ),(3, 11 ),(4, 12 ),(5, 13 ),(6, 14 ),(7, 15 ),(8, 16 ),(1, 10 ),(2, 11 ),(3, 12 ),(4, 13 ),(5, 14 ),(6, 15 ),(7, 16 ),(2, 9 ),(3, 10 ),(4, 11 ),(5, 12 ),(6, 13 ),(7, 14 ),(8, 15 )])

                
S = dnx.maximum_independent_set(G, sampler=sampler, num_reads = 10)

                  

#   adjust your  printout requirments ---------------REPORT---------***

print(" ")
print("--------------------------------------------------------------")
print("Jet Parking")
print("Run                             ",timestamp)
print("--------------------------------------------------------------")
print("Total avaiable seats - nodes  16 in each section "),
print("Maximum  set size     ", len (S))
print("Missed ", 16 -len(S))
print("Assignments in Nodes this run   ",S)
print("--------------------------------------------------------------")
print(" ")
k =G.subgraph(S)
notS =list(set(G.nodes())-set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G,pos=pos)
nx.draw(k,pos=pos)
nx.draw(othersubgraph,pos=pos,node_color ='b')
plt.show()
