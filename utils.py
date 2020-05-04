import os


# return a list of files under this path
def get_files(this_path):
    results = []
    arr = os.listdir(this_path)
    for a in arr:
        results.append(this_path + "/" + a)
    return results

