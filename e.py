import MDAnalysis as mda
from MDAnalysis.analysis import distances
import numpy as np
import matplotlib.pyplot as plt
import sys


def plot_distance_map(universe, output_file):
    protein = universe.select_atoms('protein')
    coords = protein.positions

    dist_matrix = distances.distance_array(coords, coords)

    plt.imshow(dist_matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Distance (Å)')
    plt.title('Distance Map')
    plt.xlabel('Residue Index')
    plt.ylabel('Residue Index')
    plt.savefig(output_file)
    plt.close()

def plot_contact_map(universe, output_file, cutoff=3.5):
    protein = universe.select_atoms('protein')
    coords = protein.positions

    dist_matrix = distances.distance_array(coords, coords)
    contact_map = dist_matrix < cutoff

    plt.imshow(contact_map, cmap='binary', interpolation='nearest')
    plt.title('Contact Map (cutoff = {} Å)'.format(cutoff))
    plt.xlabel('Residue Index')
    plt.ylabel('Residue Index')
    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    pdb_file = f"{sys.argv[1]}" 
    universe = mda.Universe(pdb_file)

    plot_distance_map(universe, "./saida/distance_map.png")
    plot_contact_map(universe, "./saida/contact_map.png")

    print("Os mapas de distâncias e de contato foram salvos.")
