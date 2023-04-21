import os

def load_images_from_folder(folder):
    _counter = 1
    for filename in os.listdir(folder):
        _, ending = os.path.splitext(filename)
        if ending == ".jpg":
            os.rename(filename , str(_counter) + ".jpg")
        if ending == ".txt":
            os.rename(filename , str(_counter) + ".txt")
            _counter = _counter + 1 
        


current_dir = os.path.dirname(os.path.abspath(__file__))
load_images_from_folder(current_dir)