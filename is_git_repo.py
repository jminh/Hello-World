from commands import getoutput

'''
Check
(1) The current dir has a sub dir?
(2) The current dir'name is ended with .git?
(3) The current direcoty is contained in a dir whos name is ended with .git.
'''

def is_git_exist():
    pwd = getoutput('pwd')

    subdir_list = getoutput('find . -maxdepth 1 -type d').split()
    del subdir_list[0] # since subdir_list[0] always equals to '.'

    for sub_dir in subdir_list:
        if sub_dir == './.git':
            print '[Y]',
            print 'In the current direcoty,',
            print 'there is a subdir named .git.'
            return
    print '[N] In the current directory,',
    print 'there is no subdir named .git.'

def is_end_git():
    pwd = getoutput('pwd')
    dir_list = pwd.split('/')

    del dir_list[0]
    
    if dir_list[-1][-4:] == '.git':
        print '[Y] The current directory name is ended with .git'
    else:
        print '[N] The current directory name is NOT ended with .git'

    del dir_list[-1]

    for dir in dir_list:
        if dir[-4:] == '.git':
            print '[N] The current directory in contains in a direcoty whose name is ended with .git'
            return

if __name__ == '__main__':
    is_git_exist()
    is_end_git()
