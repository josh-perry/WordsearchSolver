__author__ = "Josh Perry"

def scan_position(wordsearch, x, y, word):
    directions = [["up"], ["down"], ["left"], ["right"], ["up", "left"], ["up", "right"], ["down", "left"], ["down", "right"]]
    for direction in directions:
        res = scan_for_word(wordsearch, x, y, word, direction)

        if res:
            return res

def scan_for_word(wordsearch, x, y, word, direction):
    x_skip, y_skip = 0, 0

    if "right" in direction:
        x_skip = 1
    if "left" in direction:
        x_skip = -1
    if "up" in direction:
        y_skip = -1
    if "down" in direction:
        y_skip = 1

    if x_skip == 0 or y_skip == 0:
        return False

    for i in range(0, len(word)):
        try:
            if wordsearch[y + (i * y_skip)][x + (i * x_skip)]:
                if i == len(word) - 1:
                    return [y, x, y + (i * y_skip),  x + (i * x_skip)]
        except IndexError:
            break

    return False


def solve_wordsearch(wordsearch, find_words):
    width = len(wordsearch[0])
    height = len(wordsearch)

    for word in find_words:
        word = word.upper()
        word_found = False

        for x in range(0, width):
            for y in range(0, height):
                if wordsearch[y][x] != word[0]:
                    continue
                else:
                    res = scan_position(wordsearch, x, y, word)

                    if res:
                        print word + " found! " + str(res)
                        word_found = True
                        break
            if word_found:
                break

        if not word_found:
            print "FAILED TO FIND: " + word


def read_image(path):
    from PIL import Image
    import pytesseract
    import os

    f = open(path)

    print(pytesseract.image_to_string(Image.open(f)))

def main():
    # ws = [["O", "S", "O", "S", "T", "E", "O", "B", "L", "A", "S", "T", "E", "I", "L"],
    #       ["P", "C", "I", "S", "I", "S", "S", "S", "I", "O", "N", "M", "T", "A", "O"],
    #       ["C", "O", "A", "T", "H", "S", "L", "U", "D", "T", "H", "U", "Y", "U", "T"],
    #       ["O", "M", "R", "N", "I", "O", "O", "E", "L", "P", "E", "C", "C", "S", "S"],
    #       ["I", "P", "A", "A", "A", "R", "R", "R", "N", "L", "M", "A", "O", "A", "A"],
    #       ["R", "O", "D", "M", "L", "L", "H", "T", "O", "A", "A", "L", "E", "P", "L"],
    #       ["R", "U", "I", "U", "A", "U", "I", "T", "S", "P", "T", "C", "T", "C", "C"],
    #       ["E", "N", "A", "E", "T", "F", "C", "C", "R", "S", "O", "N", "S", "S", "O"],
    #       ["G", "D", "P", "T", "S", "T", "L", "I", "U", "A", "P", "E", "O", "A", "E"],
    #       ["U", "N", "H", "S", "O", "S", "E", "A", "D", "L", "O", "A", "T", "F", "T"],
    #       ["L", "A", "Y", "O", "C", "F", "H", "M", "T", "N", "I", "E", "O", "S", "S"],
    #       ["A", "S", "S", "I", "T", "I", "L", "E", "Y", "M", "E", "O", "T", "S", "O"],
    #       ["R", "O", "I", "R", "P", "Y", "G", "N", "O", "P", "S", "P", "Y", "S", "I"],
    #       ["S", "O", "S", "E", "P", "I", "P", "H", "Y", "S", "I", "S", "P", "F", "O"],
    #       ["U", "S", "Y", "P", "R", "O", "N", "O", "E", "T", "S", "O", "A", "A", "R"],
    #       ["H", "E", "M", "A", "T", "O", "M", "A", "X", "I", "A", "L", "D", "N", "L"]]
    #
    # words = ["appendicular", "axial", "canaliculi", "compound", "costal", "diaphysis", "epiphysis", "flat", "fontanels",
    #          "hematoma", "callus", "hematopoiesis", "irregular", "lacuna", "osteoarthritis", "osteoblast", "osteoclast",
    #          "osteocyte", "osteon", "osteoporosis", "ostoemyelitis", "periosteum", "short", "spongy"]
    #
    # solve_wordsearch(ws, words)

    read_image("catholic.jpg")


if __name__ == "__main__":
    main()
