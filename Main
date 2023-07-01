import os
import time
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Language codes for OCR
ocr_languages = {
    'german': 'deu',
    'french': 'fra',
    'dutch': 'nld',
    'czech': 'ces',
    'hungarian': 'hun',
    'polish': 'pol',
    'slovak': 'slk',
    'romanian': 'ron'
}

# Function to convert PDF to text
def convert_pdf_to_text(pdf_file):
    # Convert PDF to images
    images = convert_from_path(pdf_file, 200)

    # Initialize a string to store the text
    text = ""

    # Process each image
    for image in images:
        # Convert image to grayscale
        image = image.convert('L')

        # Extract text from the image using OCR
        page_text = pytesseract.image_to_string(image)

        # Append the page text to the overall text
        text += page_text + '\n'

    return text

# Watchdog event handler
class PDFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_extension = os.path.splitext(event.src_path)[1].lower()
        if file_extension == '.pdf':
            print(f"New PDF file added: {event.src_path}")
            text = convert_pdf_to_text(event.src_path)
            text_file = os.path.splitext(event.src_path)[0] + '.txt'
            with open(text_file, 'w') as f:
                f.write(text)
            print(f"Converted PDF to text: {text_file}")


# Directory to monitor for new PDF files
directory_to_watch = '/home/abdaff/Documents/Thesiscode001/Thesiscode/Path'



# Start the watchdog observer
event_handler = PDFHandler()
observer = Observer()
observer.schedule(event_handler, directory_to_watch, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
