import os
import sys
import hashlib
import collections


def hash_file(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as afile:
        hasher.update(afile.read())
    return hasher.hexdigest()


def find_dups(main_folder):
    dups = collections.defaultdict(list)
    for dir_name, _, file_list in os.walk(main_folder):
        for file_name in file_list:
            path = os.path.join(dir_name, file_name)
            if not file_name.startswith(('.', '~')):
                if not os.path.islink(path):
                    file_hash = hash_file(path)
                    dups[file_hash].append(os.path.abspath(path))
    return dups


if __name__ == '__main__':
    dict_with_files = find_dups(sys.argv[1])
    for file_names in dict_with_files.values():
        if len(file_names) > 1:
            print(":".join(file_names))
