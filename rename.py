path = input('Enter path of directory with files that need to be renamed:\n')
input('Instructions: Press enter to skip a file. Otherwise, enter the new name of the file. DO NOT INCLUDE FILE EXTENSION. Press enter to start.')

import os
with os.scandir(rf'{path}') as folder:
	for file in folder:
		old_path = rf'{path}' + '\\' + file.name
		if '.' in file.name:
			file_name, file_extension = file.name.split('.')
			formatted_file_extension = '(.' + file_extension + ')'
			
		else:
			file_name, file_extension = file.name, ''
			formatted_file_extension = ' (directory)'
			
		new_name = input(f'{file_name}{formatted_file_extension} --> ')
		if new_name != '':
			if '.' in file.name:
				new_path = rf'{path}' + '\\' + new_name + "." + file_extension
			else:
				new_path = rf'{path}' + '\\' + new_name
			
			os.rename(old_path, new_path)
