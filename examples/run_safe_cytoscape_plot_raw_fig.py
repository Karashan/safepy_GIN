# Author: Xiang Zhang
# Date created: 06/09/2021

import sys
import os
from os.path import expanduser
from pathlib import Path

# Add path to folder containing safepy
sys.path.append(expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/safepy/')

import safe

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#%matplotlib inline


def get_node_coordinates(graph):

    x = dict(graph.nodes.data('x'))
    y = dict(graph.nodes.data('y'))

    ds = [x, y]
    pos = {}
    for k in x:
        pos[k] = np.array([d[k] for d in ds])

    node_xy = np.vstack(list(pos.values())).astype(float)

    return node_xy

def plot_network_revise1(sf, background_color='#000000', node_list=None, save_fig_path=None):
    ax = plot_network_revise2(sf.graph, background_color=background_color, node_list=node_list, save_fig_path=save_fig_path)
    
def plot_network_revise2(G, ax=None, background_color='#000000', node_list=None, save_fig_path=None):

    foreground_color = '#ffffff'
    if background_color == '#ffffff':
        foreground_color = '#000000'

    node_xy = get_node_coordinates(G)

    if ax is None:
        fig, ax = plt.subplots(figsize=(20, 10), facecolor=background_color, edgecolor=foreground_color)
        fig.set_facecolor(background_color)

    # Randomly sample a fraction of the edges (when network is too big)
    edges = tuple(G.edges())
    if len(edges) > 30000:
        edges = random.sample(edges, int(len(edges)*0.1))

    nx.draw(G, ax=ax, pos=node_xy, edgelist=edges,
            node_color=foreground_color, edge_color=foreground_color, node_size=10, width=1, alpha=0.2)
        
    # Add code for highlighting the genes in the node list
    #for i in range(len(G.node)):
    #    if G.node[i]['gene'] in node_list:
    #        ax.plot(G.node[i]['x'], G.node[i]['y'], 'ro', markersize=5)
        
    ax.set_aspect('equal')
    ax.set_facecolor(background_color)

    ax.grid(False)
    ax.invert_yaxis()
    ax.margins(0.1, 0.1)

    ax.set_title('Network', color=foreground_color)
      
    plt.axis('off')

    try:
        fig.set_facecolor(background_color)
    except NameError:
        pass

    plt.savefig(save_fig_path, bbox_inches='tight', dpi=500, facecolor=fig.get_facecolor())
    plt.close(fig)
    
    return ax

def safe_just_plot(sf, output_dir):
    #sf = safe.SAFE()
    
    #sf.load_network(network_file=input_network_file, node_key_attribute="gene")

    #sf.plot_network()

    #sf.load_attributes(attribute_file=input_attribute_file)
    
    #sf.define_neighborhoods(node_distance_metric=metric, neighborhood_radius=nerbor_radius)

    #sf.compute_pvalues(multiple_testing=multiple_testing_bool) # May visualize right after this point

    #print(sf.pvalues_pos.shape)
    #print(sf.pvalues_pos)

    # build node list for an input attribute file
    
    plot_network_revise1(sf, node_list = [], save_fig_path=output_dir)

    return sf

if __name__ == '__main__':
    #input_network_file = "/Users/zhangxiang/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/new_expanded_Dec2022/expanded_c12rm_no507Var2_041_30_min010.cys"

    # 09082023: switch to the updated coordinates (Perox area rotated)
    '''
    input_network_file = "/Users/zhangxiang/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/new_expanded_Dec2022/rotated perox network_new_coordinates.cys"
    sf = safe.SAFE()
    sf.load_network(network_file=input_network_file, node_key_attribute="shared name")

    output_direc = '/Users/zhangxiang/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/new_expanded_Dec2022/scaffold_expanded_network_perox_rotated.pdf'
    sf_ = safe_just_plot(sf, output_direc)
    '''

    # 09152023: plot the new version for core
    input_network_file = "/Users/zhangxiang/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/new_expanded_Dec2022/mc3_organic_core_centroid_12_rm_no507Var2_041_30_new_coordinates.cys"
    sf = safe.SAFE()
    sf.load_network(network_file=input_network_file, node_key_attribute="shared name")

    output_direc = '/Users/zhangxiang/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/new_expanded_Dec2022/mc3_organic_core_centroid_12_rm_no507Var2_041_30_new_coordinates.pdf'
    sf_ = safe_just_plot(sf, output_direc)

