import sys
import urllib.request
from urllib import error
from urllib.parse import urlparse


def get_jpg_image(url, file_path, file_name):
    """
    This method use urllib library to download the image
    @param url : url of the image
           file_path: path of the image to be stored
           file_name: name of the image file
    """
    full_path = file_path + file_name
    try:
        urllib.request.urlretrieve(url, full_path)
    except (error.HTTPError, error.URLError) as err:
        print(url)
        print("HTTP Error {} ".format(str(err)))


def get_image_name(url):
    """
    This method is responsible to validate the url
    and return the appropriate image name
    @param: url : url of the image
    @return : image name
    """
    # Parse the URL
    parse_url = urlparse(url)
    # Split the url by '/'
    split_url = str.split(parse_url.path, sep="/")
    # file name generation from url
    file_name = split_url[-1].strip(' \t\n\r')
    # Check if it is .PNG or .JPG file
    if file_name[-4:] == ".jpg" or file_name[-4:] == ".jpeg" or \
            file_name[-4:] == ".png":
        return file_name
    # url validator failed
    return ""


def download_image(url):
    """
    This method is resposnible to call functions to downalod the
    image from url
    @param url : url of the image
           file_name: file name of the image

    """
    # Statically specifying the folder name
    # Where image to be stored
    file_path = 'images/'
    file_name = get_image_name(url)
    if file_name != "":
        get_jpg_image(url, file_path, file_name)
    else:
        print("Url is not valid or no JPG, PNG found")

