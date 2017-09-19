import sys, re, time, string,os
import networkx as nx
import matplotlib.pyplot as plt
import BeautifulSoup
seed = 0.00005
for iter in range(1,202,1):
    n_node = 1000  # number of nodes
    p_edge = seed * iter  # p
    lambda_p = p_edge * (n_node - 1)
    RG = nx.random_graphs.erdos_renyi_graph(n_node, p_edge)
    # pos = nx.spectral_layout(RG)
    a = 0;
    path = '/users/chaofeng/Documents/network/'
    file_name = path + 'ER_N%d' % n_node + "_" + 'lammda%f' % lambda_p
    edge_file = file(file_name, "w")
    fo = open(file_name, "wb")
    n_edge = 0
    for n, nbrs in RG.adjacency_iter():
        for nbr, eattr in nbrs.items():
            if n < nbr:
                fo.write('%d' % n + "\t" + '%d' % nbr + "\n")
                n_edge = n_edge + 1
                # print('(%d, %d)' %(n, nbr))
    print ('%d %d %f' % (iter,n_edge, lambda_p))
    fo.close()
    # nx.nodes(RG)
    # nx.draw(RG, pos, with_labels = False, node_size = 30)
    # plt.show()