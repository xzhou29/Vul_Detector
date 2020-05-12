import os
import subprocess

# return a list of files under this path
def get_files(this_path):
    results = []
    arr = os.listdir(this_path)
    for a in arr:
        temp_path = this_path + "/" + a
        final_path = os.path.abspath(temp_path)
        results.append(final_path)

    return results
''
def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)