import os
import sys
import hashlib


def findDup(main_folder):
    dups = {}
    for dirName, subdirs, fileList in os.walk(main_folder):
        for filename in fileList:
            if filename[0] != '.' and filename[0] != '~':
                path = os.path.join(dirName, filename)
                file_hash = hash_file(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
    return dups


def join_dicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hash_file(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def print_files(dict_with_files):
    results = list(filter(lambda x: len(x) > 1, dict_with_files.values()))
    if len(results) > 0:
        for result in results:
            for fileName in result:
                print(fileName, end=':')
            print('\n')
    else:
        print('No files find')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for i in folders:
            if os.path.exists(i):
                join_dicts(dups, findDup(i))
            else:
                print('Wrong path')
                sys.exit()
        print_files(dups)
    else:
        print('No path')
