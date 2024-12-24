import pandas as pd
import os
import shutil

# # this part is for creating the merged (3rd cloumn) csv file
# # Load the CSV file to see its content and structure
# file_name = 'image_labels_asd.csv'
# asd_df = pd.read_csv(file_name)

# # Add a new column with names in the format 'asd_01.jpg', 'asd_02.jpg', etc.
# asd_df['New Name'] = [f"asd_{i+1:02d}.jpg" for i in range(len(asd_df))]

# # Save the updated dataframe to a new CSV for verification
# output_path = 'image_labels_asd_updated.csv'
# asd_df.to_csv(output_path, index=False)



# # Load the CSV file to see its content and structure
# file_name = 'image_labels_td.csv'
# td_df = pd.read_csv(file_name)

# # Add a new column with names in the format 'asd_01.jpg', 'asd_02.jpg', etc.
# td_df['New Name'] = [f"td_{i+1:02d}.jpg" for i in range(len(td_df))]

# # Save the updated dataframe to a new CSV for verification
# output_path = 'image_labels_td_updated.csv'
# td_df.to_csv(output_path, index=False)


# ************************************************************************

# # this part is for copying the images to a new folder with the new names
# asd_folder = "FADC-Dataset/ASD"  # original asd folder
# asd_folder_copy = "FADC-Dataset/ASD_Copy"  # new copy asd folder

# # load csv file
# csv_path = "image_labels_asd_updated.csv"  
# asd_df = pd.read_csv(csv_path)

# # create the new folder if it does not exist
# if not os.path.exists(asd_folder_copy):
#     os.makedirs(asd_folder_copy)

# # iterate over all images in the folder
# for index, row in asd_df.iterrows():
#     original_name = row.iloc[0]  # take the original name from the first column
#     new_name = row.iloc[2]       # take the new name from the third column

#     original_path = os.path.join(asd_folder, original_name)
#     new_path = os.path.join(asd_folder_copy, new_name)

#     # copy the image with the new name if it exists
#     if os.path.exists(original_path):
#         shutil.copy(original_path, new_path)

# print("Images are moved to the copy of ASD folder with new names.")



# td_folder = "FADC-Dataset/TD"  # original td folder
# td_folder_copy = "FADC-Dataset/TD_Copy"  # new copy td folder

# # load csv file
# csv_path = "image_labels_td_updated.csv"  # name of the csv file
# td_df = pd.read_csv(csv_path)

# # create the new folder if it does not exist
# if not os.path.exists(td_folder_copy):
#     os.makedirs(td_folder_copy)

# # iterate over all images in the folder
# for index, row in td_df.iterrows():
#     original_name = row.iloc[0]  # get the original name from the first column
#     new_name = row.iloc[2]       # get the new name from the third column

#     original_path = os.path.join(td_folder, original_name)
#     new_path = os.path.join(td_folder_copy, new_name)

#     # copy the image with the new name if it exists
#     if os.path.exists(original_path):
#         shutil.copy(original_path, new_path)

# print("Images are moved to the copy of TD folder with new names.")


# ************************************************************************


# # In this part, we will update the csv files with the new names and delete the original names

# # load the csv files
# csv_path = "image_labels_asd_updated.csv"  # name of the csv file
# asd_df = pd.read_csv(csv_path, header=None)  # read the csv file

# # give the column names
# asd_df.columns = ['Original Name', 'Label', 'New Name']

# # move the new name column to the first column, delete the original name column
# asd_df = asd_df[['New Name', 'Label']]
# asd_df.columns = ['Image Name', 'Label']  # new column names

# # save the updated csv file
# output_csv_path = "image_labels_asd_final.csv"
# asd_df.to_csv(output_csv_path, index=False)

# print("ASD CSV file is updated.")

# csv_path = "image_labels_td_updated.csv"  # name of the csv file
# td_df = pd.read_csv(csv_path, header=None)  # read the csv file

# # give the column names
# td_df.columns = ['Original Name', 'Label', 'New Name']

# # move the new name column to the first column, delete the original name column
# td_df = td_df[['New Name', 'Label']]
# td_df.columns = ['Image Name', 'Label']  # new column names

# # save the updated csv file
# output_csv_path = "image_labels_td_final.csv"
# td_df.to_csv(output_csv_path, index=False)

# print("TD CSV file is updated.")

# ************************************************************************

# # merge two csv files

# # load the csv files
# asd_csv_path = "image_labels_asd_final.csv"
# td_csv_path = "image_labels_td_final.csv"

# asd_df = pd.read_csv(asd_csv_path)
# td_df = pd.read_csv(td_csv_path)

# # merge the two dataframes
# merged_df = pd.concat([asd_df, td_df], ignore_index=True)

# # save the merged dataframe to a new csv file
# output_csv_path = "image_labels_merged.csv"
# merged_df.to_csv(output_csv_path, index=False)

# print("Merged CSV file is created.")
