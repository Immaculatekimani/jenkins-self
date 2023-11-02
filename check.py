import os.path


def checking(path):
   

    check_file = os.path.isfile(path)
    return check_file
    
my_path = './remi.sh'
print (checking(my_path))
