import hashlib


def md5checksum(inputfile):
    """

    @param inputfile: the file to open
    @return: a unique code which refers to the file being passed
    """
    inf = open(inputfile, 'rb').read()
    md5 = hashlib.md5(inf).hexdigest()
    return md5


if __name__ == '__main__':
    print(md5checksum('sample_files/elements.txt'))




