import zipfile
import os
from conftest import RESOURCES_DIR


def test_zip_file():
    with zipfile.ZipFile(os.path.join(RESOURCES_DIR, 'new_file.zip')) as zip_file:
        name_list = zip_file.namelist()
        zip_file.extract('new_file.txt', path=RESOURCES_DIR)
        text = zip_file.read('new_file.txt')
        print(text)

    assert 'new_file.txt' in name_list
    assert text == b"I'm a new file for test zip"

    os.remove(os.path.join(RESOURCES_DIR, 'new_file.txt'))