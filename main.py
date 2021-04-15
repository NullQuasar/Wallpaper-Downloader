import sys
from scrapper import *

subject = ''  # The subject to search wallpapers


""" Get default download path or set one """
defaultpath_file = 'defaultpath.txt'
try: 
    defaultpath = open(defaultpath_file, 'r+')
except FileNotFoundError:
    defaultpath = open(defaultpath_file, 'w')

parent_dir = str(defaultpath.readline()).strip()

if parent_dir == '':
    defaultpath.write(os.getcwd())

defaultpath.close()


def set_default_folders_path(folder):
    """ Set a default path to download the wallpapers """

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
    # Set subject or list of subjects

    isList = False  # Do not remove
    # subjects_list = set_list(f)


# Main code
if __name__ == '__main__':
    # fonts = ('poison', 'larry3d', 'isometric1', 'cosmic', 'block', '3-d') good fonts
    subjects_list = []
    isList = False

    if len(sys.argv) > 1:
        """ Check if is there any parameter """

        params = ['-l', '-d', '-n', '-h', '--help']

        # If there is any parameter in arguments
        if not any([x in params for x in sys.argv]):
            subject = ' '.join(sys.argv[1:])

        else:

            # Set a list of wallpapers
            if '-l' in sys.argv:
                pos = sys.argv.index('-l') + 1
                subjects_list = set_list(sys.argv[pos])
                isList = True

            # Set a default directory to download the wallpapers
            if '-d' in sys.argv:
                pos = sys.argv.index('-d') + 1
                set_default_folders_path(sys.argv[pos].replace('\\', '/'))

            # Limit the number of wallpapers to download
            if '-n' in sys.argv:
                pos = sys.argv.index('-n') + 1
                nwp = int(sys.argv[pos])

            # Get help
            elif '-h' or '--help' in sys.argv:
                print("""
                Use:
                -h | --help     Show this help message
                -l              Select a text file as a list to search
                -d              Set default directory to download the wallpapers
                -n              Limit the number of wallpapers to download
                """)
                exit()

            """ if '-i' in sys.argv:
                pos = sys.argv.index('-i') + 1
                results_index = int(sys.argv[ pos ]) """

            subject = sys.argv[1]

        print('Console mode started\n\n')

    # Debug
    print('Starting...\n\n')
    print('Reading default path')
    print('File cont > ', parent_dir)
    # ----------------- BANNER------------------------

    import pyfiglet

    pyfiglet.print_figlet('WallpaperCave', 'larry3d')

    # ----------------- BANNER------------------------

    # If query is not empty
    if subject.strip() != '':

        url_query = main_url + '/search?q='
        dirname = os.path.join(parent_dir, subject) + '/'
        dirname = dirname.strip()
        print('Dir path > ', parent_dir)

        if isList:
            try:
                for wp in subjects_list:
                    wp = wp.decode('ascii')[:-2]
                    cfolder = os.path.join(parent_dir, wp)
                    get_images(url_query + urllib.parse.quote(wp),
                               cfolderm, nwp)

            except TypeError as tpe:
                print('Type Error > ', tpe)

            except Exception as e:
                print('An exception has occured > ', e)

        else:
            get_images(url_query + urllib.parse.quote(subject), dirname, nwp)

    # If query is an empty string
    else:
        print('Use: main.py [wallpaper] [-n] [-d] [-l]\n')
