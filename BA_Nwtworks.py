import sys, re, time, string,os
import networkx as nx
import matplotlib.pyplot as plt
import BeautifulSoup
seed = 0.00005
for iter in range(1,100,1):
    n_node = 1000  # number of nodes
    
    RG = nx.random_graphs.barabasi_albert_graph(n_node, iter)
    # pos = nx.spectral_layout(RG)
    path = '/users/chaofeng/Documents/network/'
    file_name = path + 'BA_N%d' % n_node + "_" + 'iter%d' % iter
    edge_file = file(file_name, "w")
    fo = open(file_name, "wb")
    n_edge = 0
    for n, nbrs in RG.adjacency_iter():
        for nbr, eattr in nbrs.items():
            if n < nbr:
                fo.write('%d' % n + "\t" + '%d' % nbr + "\n")
                n_edge = n_edge + 1
                # print('(%d, %d)' %(n, nbr))
    print ('%d %d' % (iter,n_edge))
    fo.close()
    # nx.nodes(RG)
    # nx.draw(RG, pos, with_labels = False, node_size = 30)
    # plt.show()