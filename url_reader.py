import image_downloader
import sys

# Global Variable Section
TXT_FILE_NAME = 1


def read_lines(txt_file):
    """
    This method reads the text file and
    call appropriate function to download the image
    """
    # Using readlines method
    file1 = open(txt_file, 'r')
    lines = file1.readlines()
    # Strips the newline character
    for line in lines:
        image_downloader.download_image(line.strip())


if __name__ == '__main__':
    if len(sys.argv) == 0:
        print("Please specify the url file location")
    else:
        read_lines(sys.argv[TXT_FILE_NAME])
