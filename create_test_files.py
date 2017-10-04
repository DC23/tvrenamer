import shutil
from os import mkdir, path

test_dir = "test_files"
test_files = [
    "Peppa Pig - Chloe's Big Friends garbage-16.m4v",
    "Peppa Pig - Daddy Pig's Birthday 7.m4v",
    "Peppa Pig - George's Racing Abc -5.m4v",
    "Peppa Pig - Grandpa's Pig Train 20.m4v",
    "Peppa Pig - Chloe's Big Friends.m4v",
]

shutil.rmtree(test_dir, ignore_errors=True)
mkdir(test_dir)
for f in test_files:
    open(path.join(test_dir, f), 'a').close()
