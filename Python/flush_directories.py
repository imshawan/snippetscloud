# Author: @imshawan <hello@imshawan.dev>
# Description: identifies all the directories within the target working directory. 
# Then, it displays the names of these directories. 
# Finally, the code proceeds to delete each of the listed directories along with their contents from the current working directory.

# It deletes only the directories which has lesser size than a supplied size, mostly can be used to flush junk directories 
# that might not have any useful files or is potentially empty

import os
import shutil

def list_directories_in_target_directory(target_dir=os.getcwd()):
    """
        Lists all directories in the target working directory.
    """
    directories = [name for name in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, name))]
    return directories

def get_directory_size(directory):
    """
        Calculates the total size in bytes of the specified directory and all its subdirectories.

        Parameters:
            directory (str): The path to the target directory.

        Returns:
            int: The total size of the directory and its contents in bytes.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def delete_directory(directory):
    """
        Recursively deletes the specified directory and all its contents.

        Parameters:
            directory (str): The path to the target directory to be deleted.

        Raises:
            OSError: If an error occurs during the deletion process.

        Note:
            This function permanently deletes the directory and its contents. Use with caution.
    """
    try:
        shutil.rmtree(directory)
        print(f"Deleted directory: {directory}")
    except OSError as e:
        print(f"Error while deleting directory: {directory}, Error: {e}")

def main(target_directory=os.getcwd(), max_dir_size=500):
    """
        Main function to list and delete directories in the target directory.

        Parameters:
            target_directory (string): The directory path under which the sub-directories is to be deleted.
            max_dir_size (int): Directories having lessar size than which will be deleted
    """
    if os.path.exists(target_directory):
        directories_in_target_directory = list_directories_in_target_directory(target_directory)
        if directories_in_target_directory:
            print("Directories in current directory:")
            for directory in directories_in_target_directory:
                size_in_kb = get_directory_size(directory) / 1024
                if size_in_kb < max_dir_size:
                    delete_directory(directory)
                else:
                    print(f"Directory size is {size_in_kb:.2f} KB, skipping...")
        else:
            print("No directories found in the current directory.")

    else:
        print(f"Directory '{target_directory}' does not exist.")

if __name__ == "__main__":
    main()
