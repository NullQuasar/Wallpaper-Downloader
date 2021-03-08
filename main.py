#import pandas as pd
import sys
from scrapper import *

#from selenium import webdriver
theme = ''


defaultpath_file = 'defaultpath.txt'
defaultpath = open(defaultpath_file, 'r+')

print('Reading default path')
parent_dir = str(defaultpath.readline())
print('File cont > ', parent_dir)

if parent_dir == '':
    defaultpath.write(os.getcwd())

defaultpath.close()



def set_default_folders_path(folder):

    if os.path.exists(folder):
        parent_dir = folder

        # Set new path as default
        with open('defaultpath.txt', 'w') as f:
            f.write(folder)

    else:
        print('Folder ' + folder + ' does not exist')
        return



# Set program as GUI mode
def init_gui_mode():
    # Set theme or list of themes
    
    isList = False # Do not remove
    # themes_list = set_list(f)






if __name__ == '__main__':

    print('Starting...\n\n')
    #fonts = ('poison', 'larry3d', 'isometric1', 'cosmic', 'block', '3-d') good fonts
    themes_list = []
    isList = False

    if len(sys.argv) > 1:

        print('Console mode started\n\n')

        params = ['-l', '-d', '-n']

        if not any([x in params for x in sys.argv]): # If there is any parameter in arguments
            theme = ' '.join(sys.argv[1:])
            
        else:

            # Set a list of wallpapers
            if '-l' in sys.argv:
                pos = sys.argv.index('-l') + 1
                themes_list = set_list(sys.argv[ pos ])
                isList = True

            # Set a default directory
            if '-d' in sys.argv:
                pos = sys.argv.index('-d') + 1
                set_default_folders_path(sys.argv[ pos ])


            if '-n' in sys.argv:
                pos = sys.argv.index('-n') + 1
                nwp = int(sys.argv[ pos ])
            

            """ if '-i' in sys.argv:
                pos = sys.argv.index('-i') + 1
                results_index = int(sys.argv[ pos ]) """

            theme = sys.argv[1]


    else:

        print('UI mode started')

        # File pyqtGUI.py

        init_gui_mode()


    # ----------------- BANNER------------------------

    import pyfiglet

    pyfiglet.print_figlet('WallpaperCave', 'larry3d')

    # ----------------- BANNER------------------------

    # If query is not empty
    if theme.strip() != '':

        url_query = main_url + '/search?q='
        dirname = os.path.join(parent_dir, theme) + '/'
        print('Dir path > ', parent_dir)

        if isList:
            try:
                for wp in themes_list:
                    wp = wp.decode('ascii')[:-2]
                    cfolder = os.path.join(parent_dir, wp)
                    get_images(url_query + urllib.parse.quote(wp), cfolderm, nwp)

            except TypeError as tpe:
                print('Type Error > ', tpe)
            
            except Exception as e:
                print('An exception has occured > ', e)

        else:
            get_images(url_query + urllib.parse.quote(theme), dirname, nwp)

    # If query is an empty string
    else:
        print('Use: main.py [wallpaper] [-n] [-d] [-l]\n')