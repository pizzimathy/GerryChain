
from networkx import set_node_attributes, check_planarity
from networkx.algorithms.planarity import PlanarEmbedding
import numpy as np


def shared(G, L):
    """
    Computes weights for the line graph of G.
    """
    _, F = check_planarity(G)
    faces = { }

    for edge in F.edges():
        face = F.traverse_face(*edge)
        faces[edge] = [face] if not faces.get(edge, False) else faces[edge].append(face)

    return faces