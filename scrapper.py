import os
import requests
import urllib.parse
from bs4 import BeautifulSoup

main_url = 'https://wallpapercave.com'  # Website to scrape
nwp = None  # Number of wallpapers to download (-n param)


def set_list(filename):
    """ Set a list of wallpapers """
    if os.path.isfile(filename):
        try:
            with open(filename, 'rb') as f:
                subjects = f.readlines()
                return subjects  # Return a list with all the file lines

        except Exception as e:
            print('An error ', e, ' has ocurred in func set_list, line 37')

    else:
        print('Error, file ' + filename + ' does not exist or is corrupt')
        isList = False  # This prevent to iterate a None type var


def multiple_results_func(soup, dirn, index=1):
    """ Function to handle multiple results for a query """
    tags = soup.find_all('a', class_='albumthumbnail')

    if tags is None:
        # There is no any result
        print('The is no any result for your search :(')
        return

    result = tags[index-1].get('href')
    link = main_url + result
    get_images(link, dirn, nwp)


def get_images(url, dirname, wallpapers):
    """ Get subject wallpapers """

    global nwp
    nwp = wallpapers
    url = str(url.replace('\\', '/'))

    print('url > ' + url)

    try:

        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        wp = soup.find_all('div', class_='wallpaper')
        tf = 0

        if len(wp) > 0:

            for element in wp:
                wplink = element.find('img', class_='wpimg').get('src')
                wpname = wplink[wplink.rfind('/'):]
                wpimage = requests.get(main_url + wplink)

                print('Creating element > ' + wpname)
                print('Link > ' + url + wplink)

                with open(dirname + wpname, 'wb') as imagefile:
                    imagefile.write(wpimage.content)
                    print('File created')

                tf += 1

                if tf == nwp:
                    break

            # Debug
            print('Files downloaded > ', tf)
            print('\n\nDone.')

        else:

            print('Not found')
            print('Executing multiple_results_func function...')
            multiple_results_func(soup, dirname, )

    except FileExistsError as e:
        print('\nFileExistsError: ', e)
        return

    except Exception as e:
        print('An error has occurred > ', e)
