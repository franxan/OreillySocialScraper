from gephistreamer import graph
from gephistreamer import streamer
import random as rn


class ChartStreamer:
    def __init__(self, hostname, port, workspace):

        self.stream = streamer.Streamer(
            streamer.GephiWS(hostname="192.168.10.108",
                             port=8080,
                             workspace="workspace1"))

        self.szfak = 200  # this scales up everything
        self.size_increment = 50
        self.cdfak = 3000

        self.nodedict = {}

    def addfnode(self, fname):
        if (fname in self.nodedict):
            nnode = self.nodedict[fname]
        else:
            nnode = graph.Node(fname,
                               size=self.szfak,
                               x=self.cdfak*rn.random(),
                               y=self.cdfak*rn.random(),
                               color="#8080ff",
                               type="f")
            self.nodedict[fname] = nnode  # new node into the dictionary
        return nnode

    def addnodes(self, pname, fnodenamelist):
        pnode = graph.Node(pname,
                           size=self.szfak + (
                               len(fnodenamelist) * self.size_increment
                           ),
                           x=self.cdfak*rn.random(),
                           y=self.cdfak*rn.random(),
                           color="#ff8080",
                           type="p")
        self.stream.add_node(pnode)
        for fname in fnodenamelist:
            fnode = self.addfnode(fname)
            self.stream.add_node(fnode)
            pfedge = graph.Edge(pnode, fnode, weight=rn.random())
            self.stream.add_edge(pfedge)
