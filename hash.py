import os
import sys
import hashlib
import collections


def hash_file(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as afile:
        hasher.update(afile.read())
    return hasher.hexdigest()


def findDup(main_folder):
    dups = collections.defaultdict(list)
    for dir_name, _, fileList in os.walk(main_folder):
        for filename in fileList:
            path = os.path.join(dir_name, filename)
            if not filename.startswith(('.', '~')) and not os.path.islink(path):
                file_hash = hash_file(path)
                dups.setdefault(file_hash, []).append(path)
    return dups


def print_files(dict_with_files):
    for _, lst in dict_with_files.items():
        if (len(lst) > 1):
            print(":".join(lst))


if __name__ == '__main__':
    print_files(findDup(sys.argv[1]))
