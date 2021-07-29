#!/usr/bin/env python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import pairwise_kernels
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import cosine
import sys
import time
start_time = time.time()


# Script to compute similarity matrices for subregion electrostatics of each PDB. Will need to plot them too. Hmmm -> matrix heatmap.

## Load the data ##

pdbs = []
potentials = {}
a = open('all_spike_strs_regions_pot.csv', 'r')
for line in a:
    mm = line.split(',')
    if len(mm) == 3 and mm[0] != 'PDB ID':
        if mm[1] == 'region_1':
            pdbs.append(mm[0])
            temp_potential = [float(mm[2])]

        elif mm[1] != 'region_1':
            temp_potential.append(float(mm[2]))

        if mm[1] == 'region_21':
            potentials[mm[0]] = np.array(temp_potential)


a.close()


## Compute similarity distances ##
## How do I compute uncertainty? ##

## Sklearn implementation ##


cosine_distances = []
euclidean_distances = []
l2_distances = []
manhattan_distances = []
l1_distances = []
hamming_distances = []
chebyshev_distances = []
jaccard_distances = []

similarity_distances = {}
normalized_similarity_distances = {}
mean_similarity_distances = {}
ci95_similarity_distances = {}

for sys1 in potentials:
    for sys2 in potentials:

        cosine_distances.append(pairwise_distances(potentials[sys1].reshape(
            1, -1), potentials[sys2].reshape(1, -1), metric='cosine')[0][0])
        euclidean_distances.append(pairwise_distances(potentials[sys1].reshape(
            1, -1), potentials[sys2].reshape(1, -1), metric='euclidean')[0][0])
        l2_distances.append(pairwise_distances(potentials[sys1].reshape(
            1, -1), potentials[sys2].reshape(1, -1), metric='l2')[0][0])
        manhattan_distances.append(pairwise_distances(potentials[sys1].reshape(
            1, -1), potentials[sys2].reshape(1, -1), metric='manhattan')[0][0])
        l1_distances.append(pairwise_distances(potentials[sys1].reshape(
            1, -1), potentials[sys2].reshape(1, -1), metric='l1')[0][0])
        hamming_distances.append(pairwise_distances(potentials[sys1].reshape(
            1, -1), potentials[sys2].reshape(1, -1), metric='hamming')[0][0])
        chebyshev_distances.append(pairwise_distances(potentials[sys1].reshape(
            1, -1), potentials[sys2].reshape(1, -1), metric='chebyshev')[0][0])
        jaccard_distances.append(pairwise_distances(potentials[sys1].reshape(
            1, -1), potentials[sys2].reshape(1, -1), metric='jaccard')[0][0])

        similarity_distances[sys1, sys2] = [cosine_distances[-1], euclidean_distances[-1], l2_distances[-1],
                                            manhattan_distances[-1], l1_distances[-1], hamming_distances[-1], chebyshev_distances[-1], jaccard_distances[-1]]


# normalization loop

for sys1 in potentials:
    for sys2 in potentials:

        normalized_similarity_distances[sys1, sys2] = (np.array(similarity_distances[sys1, sys2]) - np.array([min(cosine_distances), min(euclidean_distances), min(l2_distances), min(manhattan_distances), min(l1_distances), min(hamming_distances), min(chebyshev_distances), min(jaccard_distances)])) / (np.array([max(cosine_distances), max(euclidean_distances), max(
            l2_distances), max(manhattan_distances), max(l1_distances), max(hamming_distances), max(chebyshev_distances), max(jaccard_distances)]) - np.array([min(cosine_distances), min(euclidean_distances), min(l2_distances), min(manhattan_distances), min(l1_distances), min(hamming_distances), min(chebyshev_distances), min(jaccard_distances)]))

        mean_similarity_distances[sys1, sys2] = np.mean(
            normalized_similarity_distances[sys1, sys2])
        ci95_similarity_distances[sys1, sys2] = 1.96 * np.std(
            normalized_similarity_distances[sys1, sys2]) / np.sqrt(len(normalized_similarity_distances[sys1, sys2]))


# Plot the data

heatmap_matrix = []
annotations_matrix = []

for sys1 in potentials.keys():
    heatmap_row = []
    annotations_row = []
    for sys2 in potentials.keys():
        heatmap_row.append(mean_similarity_distances[sys1, sys2])
        annotations_row.append('{}\n+/- {}'.format(round(
            mean_similarity_distances[sys1, sys2], 2), round(ci95_similarity_distances[sys1, sys2], 2)))
    
    heatmap_matrix.append(heatmap_row)
    annotations_matrix.append(annotations_row)

labels = np.array(annotations_matrix)
print(labels)

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(heatmap_matrix, dtype=bool))

# Set up the matplotlib figure
matplotlib.rc('xtick', labelsize=16)
matplotlib.rc('ytick', labelsize=16)

fig, ax = plt.subplots()

ax = sns.heatmap(heatmap_matrix, mask=mask, annot=labels, fmt='', annot_kws={
                 "size": 14}, cmap="RdBu_r")  # fmt="0.2f",  cmap="RdBu_r")

row_labels = list(potentials.keys()) #pdbs
column_labels = list(potentials.keys()) #pdbs

# put the major ticks at the middle of each cell
ax.set_yticks(np.arange(len(heatmap_matrix))+0.5, minor=True)
ax.set_xticks(np.arange(len(heatmap_matrix))+0.5, minor=True)

ax.set_xticklabels(column_labels, minor=False, rotation=30,
                   fontsize=16, ha="right", rotation_mode="anchor")  # rotation=-30
ax.set_yticklabels(row_labels, minor=False, rotation=0, fontsize=16)
ax.tick_params(axis='x', which='major')  # , pad=10)
ax.tick_params(axis='y', which='major')  # , pad=10)
ax.set_xlabel('Antibodies', fontsize=20)
# ax.xaxis.tick_top() ## for labels at top

cbar = ax.collections[0].colorbar
cbar.ax.set_ylabel(r'Similarity score (normalized)',
                   rotation=270, fontsize=18, labelpad=25)  # labelpad=25)
cbar.ax.tick_params(labelsize=13)

plt.tight_layout()
plt.savefig('similarity_distances.pdf')
plt.close()


end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))
