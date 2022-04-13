import os

import comtypes.client

from scripts.commons import extension_is, get_file_name


def docx_to_pdf(files_path:str, directory:str) -> None:
    """
    Convert docx files to pdf format

    Args:
        files_path (str): list of files to convert
        directory (str): directory where save files
    """
    word = comtypes.client.CreateObject('Word.Application')
    wdFormatPDF = 17

    for file_path in files_path:
        if extension_is(file_path, 'docx'):
            file_name = get_file_name(file_path)
            out_file = os.path.join(directory, file_name + ".pdf")
            
            doc = word.Documents.Open(os.path.join(os.getcwd(), file_path))
            doc.SaveAs(os.path.join(os.getcwd(), out_file), FileFormat=wdFormatPDF)
            doc.Close()
            
            print(f'File "{file_path}" has been converted to pdf!')

    word.Quit()
