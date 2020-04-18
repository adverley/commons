import fnmatch
import os
import shutil
from os.path import isdir, join

def is_file(file_path):
    return os.path.isfile(file_path)

def create_dirs_if_not_exists(*dirs):
    for d in dirs:
        make_dir_if_not_exist(d)

    return dirs


def make_dir_if_not_exist(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

    return dir


def all_directories_in(path):
    return sorted([f for f in os.listdir(path) if isdir(join(path, f))])


def n_dirs_in_path(output_path):
    dirs = all_directories_in(output_path)
    return len(dirs)


def walk_files(data_path, extension):
    fragment_files = []
    for root, dirnames, filenames in os.walk(data_path):
        for filename in fnmatch.filter(filenames, '*.{}'.format(extension)):
            fragment_files.append(os.path.join(root, filename))

    return sorted(fragment_files)


def rename_all_files_in_subdirs_to(source_name, target_name, parent_dir):
    for root, dirnames, filenames in os.walk(parent_dir):
        for filename in fnmatch.filter(filenames, '{}'.format(source_name)):
            source_fp = os.path.join(root, filename)
            target_fp = os.path.join(root, target_name)
            os.rename(source_fp, target_fp)


def remove_all_files_in_subdirs(target_name, parent_dir):
    for root, dirnames, filenames in os.walk(parent_dir):
        for filename in fnmatch.filter(filenames, '{}'.format(target_name)):
            fp = os.path.join(root, filename)
            os.remove(fp)


def remove_all_subdirs_with_name(parent_dir, target_name_to_remove):
    for root, dirnames, filenames in os.walk(parent_dir):
        for dirname in fnmatch.filter(dirnames, '{}'.format(target_name_to_remove)):
            fp = os.path.join(root, dirname)
            shutil.rmtree(fp)

