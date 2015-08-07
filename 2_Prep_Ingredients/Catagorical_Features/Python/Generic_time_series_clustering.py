#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Goal is to take time series data and start making meaningful clusters.
#              This is a few to determine seasonal patterns, holiday patterns or promos
#
# Author:      dwoo57
#
# Created:     28/01/2015
# Copyright:   (c) dwoo57 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import helper
import dzwmodel_kit


#--------------------------
# Flow is as follows
# 1. Import data
# 2. Run time series clustering through it
# 3. Visualize results
# 4. Output results
#------------------



# Get me my data or impor tha data

# Working folder
#FOLDER = "C:\\Users\\dwoo57\\Google Drive\\Career\\Data Mining Competitions\\Kaggle\\Walmart - Inventory and weather prediction\Modeling\\Cleaned_Data\\"

#FOLDER = "C:\\Users\\dwoo57\\Google Drive\\Career\\Data Mining Competitions\\Kaggle\\Walmart - Inventory and weather prediction\Experiments\\Alpha\\"
FOLDER = "C:\\Users\\dwoo57\\Google Drive\\Career\\Data Mining Competitions\\Kaggle\\Walmart - Inventory and weather prediction\Experiments\\Alpha\\Input Files\\"


# Data files to import
#INPUTFILE = FOLDER + "1_Store_31_item_9_all_cleaned_no_headers.csv"

#INPUTFILE = FOLDER + "1_Store_31_item_9_all_w_daily_rates_no_headers_2012.csv"
#INPUTFILE = FOLDER + "3_Item9_store31_2014_daily_season_calculated_blanks_partial_weeks_rmv_outliers_rmv.csv"
INPUTFILE = FOLDER + "2_Store_31_item_9_2012_to_2014_all_days_wo_headers_wo_blanks.csv"

#CLUSTER OUTPUT FILES
CLUSTER_OUTPUT = FOLDER + "Cluster_Groups_Output.csv"
CLUSTER_CENTROID_OUTPUT = FOLDER + "Cluster_CENTRIODS_Groups_Output.csv"

def main():
    #1. Sample topics from trending and non trending. Create two partitions, one for training and one for testing (Monday)


    num_clust = 9 # for now has to be less than 10 because of the way that we had plotting the subplots
    sample_size = 0
    tweet_rate_col_idx = 2
    #TODO, allow it to take no headers or put into into a data frame before this which is smart to ignore headers
    #Also for graphing would like it to be smart enough to know what the x-axis should be
    #dzwmodel_kit.KMeansClustBasedOnDynamicTimeWrapping(INPUTFILE,num_clust,sample_size,CLUSTER_OUTPUT,CLUSTER_CENTROID_OUTPUT,tweet_rate_col_idx)

    #num_clust_list =[7,14,21,28,35,42,49]
    #100 = 0.98
    #80 = 0.88
    #70 = 0.77
    num_clust_list =[7]

    # for now try 28 more manageable
    silhouette_score_result_list=[]
    #num_clust = 7
    isDebug = True

    # feature engineering, test/check for autocorrelation


    for num_clust in num_clust_list :

        silhouette_score_result = dzwmodel_kit.KMeansClust(INPUTFILE,num_clust,sample_size,CLUSTER_OUTPUT,CLUSTER_CENTROID_OUTPUT,tweet_rate_col_idx,isDebug)
        silhouette_score_result_list.append([num_clust,silhouette_score_result])

    print silhouette_score_result_list
if __name__ == '__main__':
    main()
