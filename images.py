import os
import pickle
import shutil
import tkinter
from operator import itemgetter
import PIL
import imagehash
from PIL import Image
import dir
import utils

root = tkinter.Tk()
root.wm_withdraw()  # this completely hides the root window


def load_images_to_db():
    # select images file to load
    images, path = utils.select_images_and_path_to_load() #call def to get images and path images
    if images is not None and path is not None:
        for image in images:
            is_jpg = utils.verify_jpg(image.name)# call def to verify extention jpg or jpeg
            is_ok = utils.verify_image(image.name)# call def to check image integridy
            if is_jpg and is_ok:
                image.close()
                shutil.copy(image.name, path)
    # generate db pkl file
    create_db_image_hash()


def del_images_from_db():
    #select image files to delete
    images = utils.select_images("SELECT FILES","Select files to delete")
    if images is not None:
        for image in images:
            image.close()
            os.remove(image.name)
    #generate db pkl file
    create_db_image_hash()


def create_db_image_hash():# def to creat pkl file
    try:
        path_image = dir.dir_image()  # path where are images
        path_pkl = dir.dir_db()  # path of the db pkl file
        dic_image_hash = {}  # dic for key = path image and value = hash file
        file_pkl = path_pkl + "\\DBImageHash.pkl"  # dir pkl + pkl file name
        file = open(file_pkl, "wb")  # open pkl file mode write type bytes
        for name in os.listdir(path_image):  # list all files on dir Images4
            image_path_name = path_image + "\\" + name  # dir files + image file name
            image_to_hash = PIL.Image.open(image_path_name)  # open image
            imagem_hash = imagehash.phash(image_to_hash)  # hash image
            dic_image_hash[image_path_name] = imagem_hash # load dic key = path image file, value = hash image file
        pickle.dump(dic_image_hash, file)#bload dic in pkl file
        file.close()#close file
    except:
        pass



def compare_one_to_other():# select two files to be compare
    percent = 100
    try:
        first_hash, first_image = utils.select_file_create_hash("SELECT","Select the first file")
        second_hash, second_image = utils.select_file_create_hash("SELECT","Select the second file")
        #(first_hash - second_hash) / len(second_hash.hash) ** 2 >> return a 0 < value < 1, how diferent is the hashes files
        #(first_hash - second_hash) / len(second_hash.hash) ** 2 * percent >> tranform value in % of direrence
        #(percent - (first_hash - second_hash) / len(second_hash.hash) ** 2 * percent) >> tranform value in % of similarity
        result = (percent - (first_hash - second_hash) / len(second_hash.hash) ** 2 * percent)
        print("The image ", first_image.name, "\nhas ", result, "% of similarity to the image :\n", second_image.name)
    except AttributeError:
        pass


def find_similar():
    try:
        percent = 100
        list_dic_result = {}
        number_of_result = 3
        dic_hash, image_hash, image_select = utils.read_db_image_hash()# def  to return a dic of images and hash  and the file to be compare
        for image in dic_hash:
            # (first_hash - second_hash) / len(second_hash.hash) ** 2 >> return a 0 < value < 1, how diferent is the hashes files
            # (first_hash - second_hash) / len(second_hash.hash) ** 2 * percent >> tranform value in % of direrence
            # (percent - (first_hash - second_hash) / len(second_hash.hash) ** 2 * percent) >> tranform value in % of similarity
            result = percent - ((image_hash - dic_hash[image]) / len(dic_hash[image].hash) ** 2 * percent)
            list_dic_result[image] = result
            #dict(sorted(list_dic_result.items(), key=itemgetter(1), reverse=True) >>> return dictionary in descending order by value
            #dict(sorted(list_dic_result.items(), key=itemgetter(1), reverse=True)[:number_of_result]) >>> return n higher values of the dic
            dic_maped = dict(sorted(list_dic_result.items(), key=itemgetter(1), reverse=True)[:number_of_result])
        print("\nThe ", number_of_result, " greater similarity with", image_select.name, "is(are):\n")
        for image in dic_maped:
            print(image, " ", dic_maped[image], "%")
    except (AttributeError, FileNotFoundError):
        pass
