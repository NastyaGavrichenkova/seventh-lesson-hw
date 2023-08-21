import xlrd
import os
from conftest import RESOURCES_DIR
# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_xls():
    book = xlrd.open_workbook(os.path.join(RESOURCES_DIR, 'file_example_XLS_10.xls'))

    sheets = book.nsheets
    names_sheets = book.sheet_names()
    sheet = book.sheet_by_index(0)
    columns = sheet.ncols
    rows_1 = sheet.nrows
    text_in_cell = sheet.cell_value(rowx=3, colx=2)
    rows_with_data = [sheet.row(rx) for rx in range(sheet.nrows)]

    print(rows_with_data)

    assert sheets == 1
    assert names_sheets == ['Sheet1']
    assert columns == 8
    assert rows_1 == 10
    assert text_in_cell == 'Gent'
    assert str(rows_with_data[1]) == ("[number:1.0, text:'Dulce', "
                                      "text:'Abril', text:'Female', "
                                      "text:'United States', number:32.0, "
                                      "text:'15/10/2017', number:1562.0]")