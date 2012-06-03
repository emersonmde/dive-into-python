#!/usr/bin/python3.2

import os
import glob

def find(pattern, starting_dir = os.getcwd(), levels = 50):
	'''
	Finds all files (matching a glob pattern) recursively

	Params:
		pattern -- A glob pattern to match
		starting_dir -- OPTIONAL = Working Directory -- Directory to start from
		levels -- OPTIONAL = 50 -- The number of directorys to search

	Returns a tuple of filenames or False if no files were found
	'''
	if starting_dir == os.getcwd():
		current_dir = starting_dir
	else:
		current_dir = os.path.join(os.getcwd(), starting_dir)
	file_list = []
	possible_dirs = []
	dir_queue = []
	
	for i in range(0, levels): 
		print('Checking Directory: {0}'.format(current_dir)) 
		del file_list[:]
		file_list = glob.glob(pattern)
		if file_list:
			for file in file_list:
				print('-- Found File: {0}'.format(file)) 
			return tuple(file_list)
		else:
			print('-- No Files Found')
			del possible_dirs[:]
			possible_dirs = [os.path.join(current_dir, d) 
					for d in os.listdir(current_dir) 
					if os.path.isdir(d) and d != '.' and d != '..']
			if possible_dirs:
				for dirs in possible_dirs:
					print('Adding Directory to Queue: {0}'.format(dirs))
				dir_queue.extend(possible_dirs)
			if dir_queue:
				current_dir = os.path.join(current_dir, dir_queue.pop())
				print('Changing Directory: {0}'.format(current_dir))
				os.chdir(current_dir)
			else:
				print('No Directories in Queue')
				return ()

			#print('a')
			#x = False

if __name__ == '__main__':
	output = find('*.py', '../../')
	for i in output:
		print('{0}'.format(i))
	print('\n')
