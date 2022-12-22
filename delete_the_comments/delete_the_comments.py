"""Delete the comments.

A function called deleteComments() which can read and parse a txt file."""

import os


def delete_comments(file_path):
    """The function takes the path to the file as a string parameter and
        removes the single line comments from the content.
        It writes the comment-free code to file named: ./clean-<filename.extension>.
        Filename should be followed by the extension
    Argument: file_path - string - path to the file
    Returns: the number of the single line comments
        Single line comments are the lines that starts with #
    If there is a problem with reading or writing the file the method
    Catches the error / exception and throws a new one with the following message:
        'An error occurred with accessing the files'
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except IOError:
        raise IOError("An error occurred with accessing the files")
    count_comments = 0
    cleaned_lines = []
    for line in lines:
        if line.strip().startswith("#"):
            count_comments += 1
        else:
            cleaned_lines.append(line)

    file_name, file_ext = os.path.splitext(file_path)
    new_file_path = f"clean-{file_name}{file_ext}"
    try:
        with open(new_file_path, 'w', encoding="utf-8") as file:
            file.writelines(cleaned_lines)
    except IOError:
        raise IOError("An error occurred with accessing the file.")

    return count_comments
