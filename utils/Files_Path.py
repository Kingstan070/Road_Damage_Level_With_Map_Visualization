from pathlib import Path
from typing import List, Tuple

def list_files_in_folder(folder_path: str) -> List[str]:
    """
    Lists all files in the specified folder.

    Parameters
    ----------
    folder_path : str
        The path to the folder from which to list files.

    Returns
    -------
    List[str]
        A list of file paths as strings contained within the specified folder.

    Raises
    ------
    FileNotFoundError
        If the specified folder does not exist.
    NotADirectoryError
        If the specified path is not a directory.

    Examples
    --------
    >>> files = list_files_in_folder('/path/to/your/folder')
    >>> for file in files:
    ...     print(file)
    /path/to/your/folder/file1.txt
    /path/to/your/folder/file2.jpg
    /path/to/your/folder/document.pdf
    """
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
    if not folder.is_dir():
        raise NotADirectoryError(f"The path '{folder_path}' is not a directory.")

    file_list = [str(file) for file in folder.iterdir() if file.is_file()]
    return file_list

def print_file_structure(folder_path: str, indent: str = '', file_limit: int = 5) -> Tuple[List[str], List[str]]:
    """
    Prints the directory structure of the specified folder in a tree-like format.
    
    If a folder contains more than `file_limit` files, it prints the number of files instead of listing each file.
    Additionally, returns a list of folder paths encountered during the traversal.

    Parameters
    ----------
    folder_path : str
        The path to the folder whose structure is to be printed.
    indent : str, optional
        The indentation string used for formatting the tree structure. Default is an empty string.
    file_limit : int, optional
        The number of files after which only the file count is displayed instead of the full list. Default is 5.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing:
        - A list of folder paths as strings.
        - A list of folder paths with their structure printed.

    Raises
    ------
    FileNotFoundError
        If the specified folder does not exist.
    NotADirectoryError
        If the specified path is not a directory.

    Notes
    -----
    - This function works recursively to display all nested directories and files.
    - The indentation increases with each level of depth in the directory structure.
    """
    
    folder = Path(folder_path)
    folder_paths = []

    if not folder.exists():
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
    if not folder.is_dir():
        raise NotADirectoryError(f"The path '{folder_path}' is not a directory.")

    print(f"{indent}{folder.name}/")
    folder_paths.append(str(folder))

    # Increase indentation for sub-items
    new_indent = indent + '    '

    files = [item for item in folder.iterdir() if item.is_file()]
    directories = [item for item in folder.iterdir() if item.is_dir()]

    # Print files or file count
    if len(files) > file_limit:
        print(f"{new_indent}[{len(files)} files]")
    else:
        for file in files:
            print(f"{new_indent}{file.name}")

    # Recurse into directories and collect paths
    for directory in directories:
        subfolder_paths, _ = print_file_structure(directory, new_indent, file_limit)
        folder_paths.extend(subfolder_paths)

    return folder_paths, [str(folder) + '/' for folder in directories]