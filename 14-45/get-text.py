#! /usr/bin/env python3

import docx

# Returns a single string value of all text in a Word document:
def getText(filename):
    documentObject = docx.Document(filename)
    fullText = []
    for paragraph in documentObject.paragraphs:
        fullText.append(paragraph.text)
    return '\n'.join(fullText)


print(getText(
    '/Users/bronson/Udemy/automate-the-boring-stuff-with-python/14-45/demo.docx'
))
