from gephistreamer import graph
from gephistreamer import streamer
import random as rn


class ChartStreamer:
    def __init__(self, hostname, port, workspace):
        self.stream = streamer.Streamer(
            streamer.GephiWS(hostname="192.168.10.108",
                             port=8080,
                             workspace="workspace1"))
        self.node_size = 200  # this scales up everything
        self.size_increment = 50
        self.r_seed = 3000

        self.nodedict = {}

    def addfnode(self, fname):
        if (fname in self.nodedict):
            nnode = self.nodedict[fname]
        else:
            nnode = graph.Node(fname,
                               size=self.node_size,
                               x=self.r_seed*rn.random(),
                               y=self.r_seed*rn.random(),
                               color="#8080ff",
                               type="f")
            self.nodedict[fname] = nnode  # new node into the dictionary
        return nnode

    def addnodes(self, pname, fnodenamelist):
        pnode = graph.Node(pname,
                           size=self.node_size + (
                               len(fnodenamelist) * self.size_increment
                           ),
                           x=self.r_seed*rn.random(),
                           y=self.r_seed*rn.random(),
                           color="#ff8080",
                           type="p")
        self.stream.add_node(pnode)
        for fname in fnodenamelist:
            fnode = self.addfnode(fname)
            self.stream.add_node(fnode)
            pfedge = graph.Edge(pnode, fnode, weight=rn.random())
            self.stream.add_edge(pfedge)
