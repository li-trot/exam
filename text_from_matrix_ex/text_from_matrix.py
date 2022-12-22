"""Text from matrix.

A method which takes a 2D array / matrix containing letters and returns a text.
"""


def text_from_matrix(two_d_matrix):
    """The method creates the text from the letters found in the matrix.
    Argument: two_d_matrix - 2D array matrix containing letters.
    Returns: text.
    Which letters to select:
    From every even row, select the letter found in the even columns
    From every odd row, select the letter found in the odd columns.
    The letters will be concatenated in this order: from left-top to right-bottom.
"""

    text = ""
    if not all(len(row) == len(two_d_matrix[0]) for row in two_d_matrix):
        raise AttributeError(
            "Input should be a 2D matrix with equal number of columns in each row.")
    for num, row in enumerate(two_d_matrix):
        for letter in row:
            if not letter.isalpha():
                raise AttributeError(
                    "Input should be a 2D matrix that contains letters only.")
        if num % 2 == 0:
            letters = row[::2]
        else:
            letters = row[1::2]
        text += "".join(letters)
    return text


if __name__ == "__main__":
    print(text_from_matrix([
        ["n", "x"],
        ["m", "o"]
    ]))

    print(text_from_matrix([
        ["h", "p", "e"],
        ["k", "l", "a"],
        ["l", "m", "o"]
    ]))
