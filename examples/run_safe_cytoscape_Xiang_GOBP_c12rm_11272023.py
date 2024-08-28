# Author: Xiang Zhang
# Date created: 06/09/2021
# Date : last modified:03/25/2022

import sys
import os
from os.path import expanduser
from pathlib import Path

# Add path to folder containing safepy
sys.path.append(expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/safepy/')

import safe

#%matplotlib inline

def safe_test_plot(input_network_file, input_attribute_file, output_dir, metric='shortpath_weighted_layout', neibor_radius=0.15, dist_thre=0.65, min_neighbor=10, enrichment_threshold=0.05, bool_mt=True):
    sf = safe.SAFE()
    
    sf.load_network(network_file=input_network_file, node_key_attribute="shared name")

    #sf.plot_network()

    sf.load_attributes(attribute_file=input_attribute_file)
    
    sf.define_neighborhoods(node_distance_metric=metric, neighborhood_radius=neibor_radius)
    
    sf.enrichment_threshold = enrichment_threshold # May test with different threshold

    sf.compute_pvalues(multiple_testing=bool_mt)

    # Test with different min size
    #sf.attribute_enrichment_min_size = min_neighbor

    sf.define_top_attributes()

    sf.define_domains(attribute_distance_threshold=dist_thre)

    sf.trim_domains()
    

    input_stem = Path(input_network_file).stem
    output_file_dir = os.path.join(output_dir, input_stem)
    if not os.path.exists(output_file_dir):
        os.makedirs(output_file_dir)

    # Prints output
    
    sf.plot_composite_network(show_each_domain=True, save_fig='{output_dir}/{input_file}_viz.pdf'.format(output_dir=output_dir, input_file=input_stem))
    sf.plot_composite_network(show_each_domain=False, save_fig='{output_dir}/top_{input_file}_viz.pdf'.format(output_dir=output_dir, input_file=input_stem))
    sf.print_output_files(output_dir=output_file_dir)
    sf.save_network(output_file=os.path.join(output_file_dir, input_stem + ".gpickle"))
    
    return sf

if __name__ == '__main__':
    #input_file = expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/max_centroid_rm/mc_core_12122022/expanded_c12rm_no245Var3_041_30_min010.cys'
    input_file = expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/max_centroid_rm/mc_core_12122022/expanded_c12rm_no507Var2_041_30_min010.cys'
    #input_file = expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/max_centroid_rm/mc_core_12122022/mc3_organic_core_centroid_12_rm_no507Var2_041_30.cys'

    #input_attribute_file = expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/safe_go_matrix_output/GO_BP_annotation_122021/go_p_matrix_0_500_with_name.txt'
    input_attribute_file = expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/safe_go_matrix_output/GO_BP_annotation_052023/go_p_matrix_0_500_with_description.txt'


    #output_dir = expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/max_centroid_rm/mc_core_12122022/safe_var3/no245Var3_'
    #output_dir = expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/max_centroid_rm/mc_core_12122022/safe_var2/no507Var2_expanded_'
    #output_dir = expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/max_centroid_rm/mc_core_12122022/safe_var2/no507Var2_core_'
    output_dir = expanduser('~') + '/Documents/Research_CB/GIN/safepy_network_annotation/network_generation/max_centroid_rm/mc_core_12122022/safe_c12rm_noVar2_results_11272023/fullBP_no507Var2_expanded_'

    output_dir00 = output_dir + '30_041_GOBP_0_500_shortpath_weighted_layout_radius0_10_distThre0_65_enrichThre0_1_length_over_pcc'
    output_dir11 = output_dir + '30_041_GOBP_0_500_shortpath_weighted_layout_radius0_11_distThre0_65_enrichThre0_1_length_over_pcc'
    output_dir22_1 = output_dir + '30_041_GOBP_0_500_shortpath_weighted_layout_radius0_12_distThre0_65_enrichThre0_1_length_over_pcc'
    output_dir22_2 = output_dir + '30_041_GOBP_0_500_shortpath_weighted_layout_radius0_12_distThre0_65_enrichThre0_2_length_over_pcc'
    output_dir22_3 = output_dir + '30_041_GOBP_0_500_shortpath_weighted_layout_radius0_12_distThre0_65_enrichThre0_3_length_over_pcc'
    output_dir33 = output_dir + '30_041_GOBP_0_500_shortpath_weighted_layout_radius0_13_distThre0_65_enrichThre0_1_length_over_pcc'
    output_dir44 = output_dir + '30_041_GOBP_0_500_shortpath_weighted_layout_radius0_14_distThre0_65_enrichThre0_1_length_over_pcc'
    output_dir55 = output_dir + '30_041_GOBP_0_500_shortpath_weighted_layout_radius0_15_distThre0_65_enrichThre0_1_length_over_pcc'

#sf_bp00 = safe_test_plot(input_file, input_attribute_file, output_dir00, metric='shortpath_weighted_layout', neibor_radius=0.10, dist_thre=0.65, enrichment_threshold=0.1)
#sf_bp11 = safe_test_plot(input_file, input_attribute_file, output_dir11, metric='shortpath_weighted_layout', neibor_radius=0.11, dist_thre=0.65, enrichment_threshold=0.1)
    sf_bp22_1 = safe_test_plot(input_file, input_attribute_file, output_dir22_1, metric='shortpath_weighted_layout', neibor_radius=0.12, dist_thre=0.65, enrichment_threshold=0.1)
    sf_bp22_2 = safe_test_plot(input_file, input_attribute_file, output_dir22_2, metric='shortpath_weighted_layout', neibor_radius=0.12, dist_thre=0.65, enrichment_threshold=0.2)
    sf_bp22_3 = safe_test_plot(input_file, input_attribute_file, output_dir22_3, metric='shortpath_weighted_layout', neibor_radius=0.12, dist_thre=0.65, enrichment_threshold=0.3)
#sf_bp33 = safe_test_plot(input_file, input_attribute_file, output_dir33, metric='shortpath_weighted_layout', neibor_radius=0.13, dist_thre=0.65, enrichment_threshold=0.1)
#sf_bp44 = safe_test_plot(input_file, input_attribute_file, output_dir44, metric='shortpath_weighted_layout', neibor_radius=0.14, dist_thre=0.65, enrichment_threshold=0.1)
#sf_bp55 = safe_test_plot(input_file, input_attribute_file, output_dir55, metric='shortpath_weighted_layout', neibor_radius=0.15, dist_thre=0.65, enrichment_threshold=0.1)

    
