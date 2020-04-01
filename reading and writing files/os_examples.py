import os


# to join directories into path:
os.path.join('C:', 'Users', 'Windows')

# to make directories
# os.makedirs('<direction to create>')

# to get absolute path
os.path.abspath('.')

# to check if path is absolute
os.path.isabs('.')

# to get current working directory:
os.getcwd()

# to get relative path from 'C:\\spam\\eggs' to 'C:\\Windows'
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

path = 'C:\\Windows\\System32\\calc.exe'
# get name of file
os.path.basename(path)
# get name of directories
os.path.dirname(path) 

# to split basename and dirname
calc_file_path = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath) 

# get size of files in bytes
os.path.getsize('C:\\Windows\\System32\\calc.exe')

# get subdirections in directory
os.listdir('C:\\Windows\\System32')

os.path.exists('C:\\Windows')
os.path.exists('C:\\some_made_up_folder')
os.path.isdir('C:\\Windows\\System32')
os.path.isfile('C:\\Windows\\System32')
os.path.isdir('C:\\Windows\\System32\\calc.exe')
os.path.isfile('C:\\Windows\\System32\\calc.exe')
