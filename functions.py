FILENAME1 = 'applications.txt'
FILENAME2 = 'information.txt'


def get_apply(filepath=FILENAME1):
    with open(filepath, 'r') as file_local:
        apply_local = file_local.readlines()
    return apply_local


def write_apply(apply_arg, filepath=FILENAME1):
    with open(filepath, 'w') as file_local:
        file_local.writelines(apply_arg)


def get_info(filepath=FILENAME2):
    with open(filepath, 'r') as file_local:
        info_local = file_local.readlines()
    return info_local


if __name__ == "__main__":
    print("Done with functions")
