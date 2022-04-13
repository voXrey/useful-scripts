from PyPDF2 import PdfFileMerger

from scripts.commons import extension_is


def merge_pdf(files_path:str, new_file_path:str) -> None:
    """
    Merge a list of pdf

    Args:
        files_path (str): list of files's path
        new_file_path (str): path to save new pdf
    """
    merger = PdfFileMerger()

    for file_path in files_path:
        if extension_is(file_path, 'pdf'):
            merger.append(open(file_path, 'rb'))
            print(f'File "{file_path}" has been add to merge!')

        else:
            print(f'[ERROR]: File "{file_path}" has not "pdf" extension!')
    
    with open(new_file_path, 'wb') as result_file:
        merger.write(result_file)
    
    print(f'Merged pdf has been saved to "{new_file_path}"!')
