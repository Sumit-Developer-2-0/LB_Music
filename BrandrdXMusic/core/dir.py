import os

from ..logging import LOGGER


def dirr():
    """
    This function cleans up image files (.jpg, .jpeg, .png) in the current directory
    and creates 'downloads' and 'cache' directories if they don't already exist.
    """
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("Directories Updated.")