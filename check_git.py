import os

def is_git_in(directory=os.getcwd()):
	#print directory
	path_name = os.path.join(directory, '.git')
	if os.path.isdir(path_name):
		return True
	return False

def is_git_in_pwd():
	'''
	Does .git exist in the current directory?
	Yes -> return True
	No  -> return False
	'''
	return is_git_in(os.getcwd())

if __name__ == '__main__':
	print is_git_in()
	print is_git_in_pwd()

