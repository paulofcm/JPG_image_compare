import imghdr
import pickle
from tkinter import messagebox, filedialog
import PIL
from imagehash import phash
import dir


def select_images(str1, str2):
    messagebox.showinfo(str1, str2)
    images = filedialog.askopenfiles()
    return images


def select_image(str1, str2):
    messagebox.showinfo(str1, str2)
    image = filedialog.askopenfile()
    return image


def select_images_and_path_to_load():
    images = select_images("SELECT", "Select one or more files")
    path = dir.dir_image()
    return images, path


def read_db_image_hash():
    path = dir.dir_db()
    file_pkl_file = path + "//DBImageHash.pkl"
    file = open(file_pkl_file, "rb")
    dic_hash = pickle.load(file)
    file.close()
    image_select = select_image("SELECT", "Select 1 file to compare")
    image_to_hash = PIL.Image.open(image_select.name)
    image_hash = phash(image_to_hash)
    return dic_hash, image_hash, image_select


def select_file_create_hash(str1, str2):
    image_select = select_image(str1,str2)
    image_to_hash = PIL.Image.open(image_select.name)
    image_hash = phash(image_to_hash)
    return image_hash, image_select


def verify_jpg(path):
    file_extension = imghdr.what(path)
    if file_extension != 'jpg' and file_extension != 'jpeg':
        return False
    else:
        return True


def verify_image(path_file_name):
    try:
        PIL.Image.open(path_file_name)
        return True
    except PIL.UnidentifiedImageError:
        return False
