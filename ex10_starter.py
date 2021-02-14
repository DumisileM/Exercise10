import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
print(hdir)

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
print(pattern)


# TODO: Use the glob.glob() function to obtain the list of filenames
file_size=glob.glob(pattern)
# TODO: use os.path.getsize to find each file's size

for each in file_size:
    os.path.getsize(each)

# TODO: Add a test to only display files that are not zero length
for each in file_size:
    size=os.path.getsize(each)
    if size > 0:
        print(size, each)
# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

for each in file_size:
    size=os.path.getsize(each)
    if size > 0:
        print(size,os.path.basename(each)) #we removed basename and printed files size more 0

