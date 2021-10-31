import os

def create_dirs():
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path_images = dir_path + "\\images"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path_db = dir_path + "\\DBImageHash"
        os.mkdir(dir_path_images)
        os.mkdir(dir_path_db)
    except FileExistsError:
        pass

def dir_image():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path_images = dir_path + "\\images"
    return dir_path_images

def dir_db():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path_db = dir_path + "\\DBImageHash"
    return dir_path_db



