import numpy as np
import igraph


def degree_assortativity(A):
    """Compute the degree assortativity

    A: scipy.sparse adjacency matrix of a network

    Return:
    degree assortativity of the network.
    """
    return


def calc_modularity(A, membership):
    """
    Calculate the modularity of a graph given the membership of the nodes.
    A: CSR representation of the adjacency matrix
    membership: 1D array of integers

    Return the modularity value of the given membership
    """
    Q = ...
    return Q


def girvan_newman_algorithm(g):
    """
    Perform the Girvan-Newman algorithm on a graph.
    g: igraph Graph object

    Return the 1D array of membership of the nodes
    """
    membership = ...
    return membership


def generate_SBM_network(n_nodes, membership, P):
    """
    Generate a stochastic block model network
    n_nodes: number of nodes
    membership: 1D array of integers
    P: 2D array of connection probability between groups

    Return:
    net: CSR representation of the adjacency matrix generated by the SBM
    """
    net = ...
    return net
