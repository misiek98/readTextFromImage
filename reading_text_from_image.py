"""
pip install pytesseract
pip install opencv-python

polish version
paste to C:\\Program Files\\Tesseract-OCR\\tesseract.exe
download: https://raw.githubusercontent.com/tesseract-ocr/tessdata/4.00/pol.traineddata

tesseract OCR download
https://digi.bib.uni-mannheim.de/tesseract/
"""

from tkinter import *
import pytesseract
import cv2
import os

root = Tk()
root.title("Read text from image")
root.geometry('640x630')

listOfExtensions = ['', '.txt', '.docx']

heading = Label(
    root, text='A script that is used to read text from images. Based on Tesseract OCR software.').pack()

label = Label(root, text='Input path folder').place(x=150, y=125)
label2 = Label(root, text='Input save path').place(
    x=150, y=225)
label3 = Label(root, text='Input file name').place(x=150, y=325)
label4 = Label(root, text='Choose extension of file').place(x=220, y=425)

entryPathFolder = StringVar()
entrySavePath = StringVar()
entryFileName = StringVar()
fileExtension = StringVar()

entry_box1 = Entry(root, textvariable=entryPathFolder,
                   width=50).place(x=150, y=150)
entry_box2 = Entry(root, textvariable=entrySavePath,
                   width=50).place(x=150, y=250)
entry_box3 = Entry(root, textvariable=entryFileName,
                   width=50).place(x=150, y=350)
entry_box4 = OptionMenu(root, fileExtension, *
                        listOfExtensions).place(x=260, y=450)
fileExtension.set(listOfExtensions[1])


def converting_backslash_to_slash_from_entryPathFolder():
    pathFolder = ''

    for character in entryPathFolder.get():
        if character == '\\':
            character = '/'
            pathFolder += character
        else:
            pathFolder += character
    return pathFolder


def converting_backslash_to_slash_from_entrySavePath():
    savePath = ''

    for character in entrySavePath.get():
        if character == '\\':
            character = '/'
            savePath += character
        else:
            savePath += character
    return savePath


def getting_entry_file_name():
    fileName = entryFileName.get()
    return fileName


def creating_list_of_files_from_input_location():
    folder = os.listdir(converting_backslash_to_slash_from_entryPathFolder())
    return folder


def creating_list_of_files():
    listOfPictures = [converting_backslash_to_slash_from_entryPathFolder() + "/" +
                      str(element) for element in creating_list_of_files_from_input_location()]
    return listOfPictures


def reading_and_inputting_text_from_image_to_file():
    position = 0
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    for picture in creating_list_of_files():
        img = cv2.imread(str(picture))
        text = pytesseract.image_to_string(img, lang='pol')

        with open(converting_backslash_to_slash_from_entrySavePath()+'/'+str(getting_entry_file_name())+str(fileExtension.get()), 'a', encoding='UTF-8') as file:
            """
            If file name is the same as file name from list: creating_list_of_files() this condition skipping that name to avoid file naming errors
            """
            if str(creating_list_of_files_from_input_location()[position]) == str(getting_entry_file_name())+str(fileExtension.get()):
                position += 1
                file.write(
                    "Slajd: "+str(creating_list_of_files_from_input_location()[position])+'\n')
                position += 1
                file.write(str(text))
                file.write('\n')

            else:
                file.write(
                    "Slajd: "+str(creating_list_of_files_from_input_location()[position])+'\n')
                position += 1
                file.write(str(text))
                file.write('\n')


def quit():
    root.destroy()

# Function program is connected with Confirm button


def program():
    converting_backslash_to_slash_from_entryPathFolder()
    converting_backslash_to_slash_from_entrySavePath()
    getting_entry_file_name()
    creating_list_of_files_from_input_location()
    creating_list_of_files()
    reading_and_inputting_text_from_image_to_file()
    quit()


workButton = Button(root, text='Confirm', width=20,
                    command=program).place(x=220, y=545)


root.mainloop()
