from dupli_lib.filehash import md5checksum

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
                extract_ext = os.path.splitext(file)
                if extract_ext[1]:  # only files with actual extensions will be parsed
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
    idx_dup = 0

    for file in all_files:
        hashing = md5checksum(file)
        # if the md5 hashing is not in the dictionary, it will be added as a key, with its file as a value
        if hashing not in d_md5:
            d_md5[hashing] = file
        # if the md5 hashing is already a key, it means the file is a duplicate
        # in this case a tuple (duplicate, original) will be added to the duplipairs list
        # the original file is the file stored as a value of the md5 hashing key
        else:
            idx_dup += 1
            # renaming the duplicate file as the original file plus _DUP
            name, ext = os.path.splitext(d_md5[hashing])  # this returns
            os.rename(file, name + "_DUP_" + str(idx_dup) + ext)
            duplipairs.append((file, d_md5[hashing]))

    # the output will be the list of (duplicate, original) pairs
    return duplipairs


