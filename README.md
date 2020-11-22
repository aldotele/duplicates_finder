# Duplicates Finder library
The library can be used to extract all duplicate files
from a starting root directory.<br>

## dupli_lib package
The package includes two scripts:
* *filehash.py*
* *dupli_finder.py*

The *filehash.py* includes a function called `md5checksum` to
which a file is passed, and returns a unique code that will
refer to the **content** of that file, independently from the 
file name.<br>

The *dupli_finder.py* uses the `find_duplicates` function in
order to return a list of duplicate-original file pairs. 
The function's parameter are a **root directory** to start looking
from (by default: the current one), and a **file extension**
(by default: all file extensions).<br>

Note:<br>
The function will search duplicates in all subdirectory inside
the root directory.<br>For example: if a file called "my_file.txt"
is in a folder called "my_folder_a", and a copy of the file called
"whatever.txt" (same content but different name) is inside a folder 
called "my_folder_c", which is a subfolder of a folder called "my_folder_b", 
the program is able to tell that file "whatever.txt" is a DUPLICATE of
file "my_file.txt", and will consider whatever.txt-myfile.txt as a duplicate
pair, where whatever.txt is a duplicate of the original file myfile.txt.



## main script
The *main.py* script performs the analysis by invoking the previous
function and storing the list of **duplicate-original pairs** inside
a `duplicate_pairs` variable.<br>
Such variable will have all the information from which to display the
actual output.<br>


## Output
Starting from the `duplicate_pairs` variable, that is a list of tuples,
the program will:
- show the **sequence of duplicate-original pairs** by indicating which file
is a duplicate of which other file (the original).
- show the **total number of duplicates** that were found.
- extract and display **only the duplicates** in sequence, without indicating
the correspondent original file.