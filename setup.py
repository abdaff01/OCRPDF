from cx_Freeze import setup, Executable
import shutil
import os

base = None

# Specify the path to your icon file
icon_path = "C:\\Users\\abdaf\\PycharmProjects\\pythonOCR\\icon.ico"


executables = [Executable("PDF2WORD.py", base="Win32GUI", icon=icon_path)]  # Set base to "Win32GUI" and add icon parameter

packages = ["idna", "watchdog", "docx", "subprocess", "cv2", "numpy", "pytesseract", "os", "sys", "tkinter"]

# Add the tessdata directory to include_files
options = {
    'build_exe': {
        'packages': packages,
        'include_files': [
            ('Tesseract-OCR', 'Tesseract-OCR'),
            ('OCRPDF/tessdata', 'OCRPDF/tessdata')
        ]
    },
}

setup(
    name="<PDF2WORD>",
    options=options,
    version="1.0",
    description='<Converting PDF to Word _a.affoun>',
    executables=executables
)
