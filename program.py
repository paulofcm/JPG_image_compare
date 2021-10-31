import dir
import images

flag = True
dir.create_dirs()

while flag:
    print('''
    0 - Exit. 
    1 - Load Images to db.
    2 - Delete Images from db.
    3 - Compare one image to other.
    4 - Find Similar.
    ''')
    menu = int(input("Choice an item:"))
    if menu == 0:
        flag = False
    elif menu == 1:
        images.load_images_to_db()
    elif menu == 2:
        images.del_images_from_db()
    elif menu == 3:
        images.compare_one_to_other()
    elif menu == 4:
        images.find_similar()
    else:
        print("****** Opção invalida ******")