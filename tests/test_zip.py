import zipfile
import os
from conftest import RESOURCES_DIR

files_to_zip = os.listdir(RESOURCES_DIR)


def test_zip_file():
    with zipfile.ZipFile(os.path.join(RESOURCES_DIR, 'resourses.zip'), 'w') as zip_folder:
        for file_to_zip in files_to_zip:
            file_path = os.path.join(RESOURCES_DIR, file_to_zip)
            zip_folder.write(file_path, file_to_zip)
        name_list = zip_folder.namelist()

    assert name_list == files_to_zip

    os.remove(os.path.join(RESOURCES_DIR, 'resourses.zip'))