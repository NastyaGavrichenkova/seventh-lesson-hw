import pypdf
import os
from conftest import RESOURCES_DIR
# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_pdf():
    reader = pypdf.PdfReader(os.path.join(RESOURCES_DIR, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    img_counter = 0
    for image_file in first_page.images:
        with open(os.path.join(RESOURCES_DIR, str(img_counter) + image_file.name), 'wb') as fp:
            fp.write(image_file.data)
            img_counter += 1

    assert number_of_pages == 412
    assert text == ('pytest Documentation\n'
                    'Release 0.1\n'
                    'holger krekel, trainer and consultant, https://merlinux.eu/\n'
                    'Jul 14, 2022')
    assert img_counter == 1

    os.remove(os.path.join(RESOURCES_DIR, '0Im1.png'))