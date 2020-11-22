from dupli_lib.dupli_finder import find_duplicates


# choosing the root directory. If empty, the root directy will be the current working directory
rd = input('enter a root directory (leave empty for current directory): ')

# choosing file extension. If empty, the program will consider all files
# note: file extensions have to be written starting from the DOT: e.g. ".py", ".png", ".txt" etc.
while True:
    file_extension = input('enter a file extension (leave empty for all extensions): ')
    if file_extension[0] == '.':
        break
    else:
        print('NOT VALID. Your file extension has to start with a DOT (".txt", ".png", etc.): ')

# the following will store the list of (original-duplicate) pairs
duplicate_pairs = find_duplicates(rd, file_extension)

print()
print('Detailed results of the analysis: ')
# showing a sequence of duplicates-original pairs
for duplicate, original in duplicate_pairs:
    print(duplicate, '__ DUPLICATE OF __', original)

# Storing only the duplicates for later use (by extracting the first element of each tuple)
# the original files will not be in the duplicates list
duplicates = []
for pair in duplicate_pairs:
    duplicate = pair[0]
    duplicates.append(duplicate)

print()

print('In total, {} DUPLICATES were found'.format(len(duplicates)))
# showing only the sequence of duplicates
print('here is the list of DUPLICATES that were found:')
for file in duplicates:
    print(file)