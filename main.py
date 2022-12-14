import argparse
import pathlib
from pathlib import *
import shutil
import sys
import Parser as parser
from Normalize import normalize

def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / filename.name.replace(filename.suffix, '')
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()

def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Помилка видалення папки {folder}')

def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')

    for file in parser.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')

    for file in parser.DOC_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser.DOCX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser.TXT_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in parser.PDF_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser.XLSX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in parser.PPTX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PPTX')


    for file in parser.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')

    for file in parser.SMTH_OTHER:
        handle_other(file, folder / 'SMTH_OTHER')

    for file in parser.ARCHIVES:
        handle_archive(file, folder / 'archives')


    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)

def start_function():
    try:
        folder = sys.argv[1]
    except IndexError:
        print("Enter valid path to the folder")
    else:
        folder_for_scan = Path(folder)
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())

if __name__ == '__main__':
    start_function()




    #try:
       # a = sys.argv[1]
        #folder_for_scan = Path(a)
        #print(f'Start in folder {folder_for_scan.resolve()}')
        #main(folder_for_scan.resolve())
   # except:
        #print("Error")


