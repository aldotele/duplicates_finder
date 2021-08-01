from dupli_lib.filehash import md5checksum
from dupli_lib.move_duplipairs import move_and_rename_file, path_leaf

import os


def find_duplicates(rootdir='', filext=''):
    """
    @param rootdir is the root directory to start looking from
    @param filext is the file extension to consider (.py, .txt, etc.) 
    if no root directory is provided, the program will start looking from the current one
    if no file extension is provided, the program will consider all files
    """
    if not rootdir:
        rootdir = os.getcwd()
    all_files = []

    # through the walk method, a tree of tuples gets created
    # for each subdirectory, the tuple is composed by a root path, a list of subdirectories, and a list of files
    for root, dirs, files in os.walk(rootdir):
        # each tuple of files gets looped
        for file in files:
            # if no extension is provided, all encountered files will be pushed into the list
            if not filext:
                all_files.append(os.path.join(root, file))
            else:
                # otherwise, the first thing is to calculate how many characters is the extension made of
                fromindex = len(filext)
                # the only files considered are those files whose last n characters equal the provided extension
                if file[-fromindex:] == filext:
                    all_files.append(os.path.join(root, file))

    # a dictionary will store (as keys) the md5sum of all files
    # a list will store a series of tuples with a pair of duplicates
    d_md5 = {}
    duplipairs = []
    
    count = 1
    for file in all_files:
        hashing = md5checksum(file)
        # if the md5 hashing is not in the dictionary, it will be added as a key, with its file as a value
        if hashing not in d_md5:
            d_md5[hashing] = file
        # if the md5 hashing is already a key, it means the file is a duplicate
        # in this case a tuple (duplicate, original) will be added to the duplipairs list
        # the original file is the file stored as a value of the md5 hashing key 
        else:
            original_file = d_md5[hashing]
            duplicate_file = file
            duplipairs.append((file, original_file))
        
            # invoking a function which moves the two files in a new folder 
            #new_folder_path = os.path.join(rootdir, 'move_here')  # NOT MOVING FOR NOW
            original_file_name = path_leaf(original_file)[1]  # extracting the second element of the tuple
            #new_original_file_path = os.path.join(new_folder_path, original_file_name)

            # renaming duplicate file
            duplicate_file_split = path_leaf(file)
            duplicate_folder = duplicate_file_split[0]
            dot_index = original_file_name.index('.')

            new_duplicate_name = original_file_name[:dot_index] + '_DUPLICATE' + original_file_name[dot_index:]
            new_duplicate_dest = os.path.join(duplicate_folder, new_duplicate_name)
            # move and rename
            count = 1
            while True:
                try:
                    os.rename(file, new_duplicate_dest)
                    break
                except(FileExistsError):
                    count += 1
                    change = 'DUPLICATE{}'.format(count)
                    new_duplicate_name = original_file_name[:dot_index] + change +  original_file_name[dot_index:]
                    new_duplicate_dest = os.path.join(duplicate_folder, new_duplicate_name)
            count = 1

    # the output will be the list of (duplicate, original) pairs
    return duplipairs


