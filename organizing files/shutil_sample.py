import shutil, os


os.chdir('D:\\')

# copy the file at the path source to the folder at the path destination
shutil.copy('D:\\example_file.txt', 'D:\\example_folder')

# copies the file at C:\example_file.txt to the folder C:\example_folder but
# gives the copied file the name example_file2.txt
shutil.copy('example_file.txt', 'D:\\example_folder\\example_file2.txt')

# The shutil.copytree() call creates a new folder named example_folder_backup
# with the same content as the original example_folder folder
shutil.copytree('D:\\example_folder', 'D:\\example_folder_backup')

# move the file or folder at the path source to the path destination and will
# return a string of the absolute path of the new location.
shutil.move('D:\\example_file.txt', 'D:\\example_folder')

# The destination path can also specify a filename. In the following example,
# the source file is moved and renamed.
shutil.move('example_file.txt', 'D:\\example_folder\\example_file2.txt')
