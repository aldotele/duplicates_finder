import ntpath


def path_leaf(path):
    head, tail = ntpath.split(path)
    return head, tail


if __name__ == '__main__':
    mypath = 'C:/Users/aldot/Desktop/TDevs/Python/repo/duplicates_finder/sample_files/some_duplicates/alice_book.txt'
    print(path_leaf(mypath))
    

