import os


def extension_is(file_name:str, extension:str) -> bool:
    """
    Check if a file has a certain extension

    Args:
        file_name (str): file's name (with extension)
        extension (str): extension required

    Returns:
        bool: `True` if the file has the extension required
    """
    return file_name.endswith('.' + extension)

def get_file_name(file_path:str, with_extension:bool=False) -> str:
    """
    Get file's name from file's path (with extension or not)

    Args:
        file_path (str): file's path
        with_extension (bool, optional): choice if you want name with extension. Defaults to False.

    Returns:
        str: file's path
    """
    file_name = os.path.basename(file_path)
    if with_extension: return file_name
    return file_name.split('.')[-2]

def list_files(directory:str, extension:str=None) -> list[str]:
    """
    Get all files path with a certain extension

    Args:
        directory (str): directory's name
        extension (str, optional): files's extension (without point). Default `None`, no condition.

    Returns:
        list[str]: list of all files's paths
    """
    list_of_files = os.listdir(directory)
    all_files = []
    for entry in list_of_files:
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            all_files += list_files(full_path, extension)
        else:
            if extension is None or extension_is(entry, extension):
                all_files.append(full_path)
                
    return all_files
