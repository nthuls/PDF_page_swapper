from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfReader, PdfWriter


# Function to replace a page in a PDF
def replace_page(original_path, replacement_path, target_page_num):
    original_pdf = PdfReader(original_path)
    replacement_pdf = PdfReader(replacement_path)

    writer = PdfWriter()

    for page_num, page in enumerate(original_pdf.pages, 1):
        if page_num != target_page_num:
            writer.add_page(page)
        elif 0 < target_page_num <= len(replacement_pdf.pages):
            target_page = replacement_pdf.pages[target_page_num - 1]
            writer.add_page(target_page)

    with open("Modified_pdf.pdf", "wb") as output_pdf:
        writer.write(output_pdf)


# Create a Tkinter root window (hidden)
root = Tk()
root.withdraw()

# Prompt the user to select the original and replacement PDF files
original_file = askopenfilename(title="Select the original PDF file", filetypes=[("PDF Files", "*.pdf")])
replacement_file = askopenfilename(title="Select the replacement PDF file", filetypes=[("PDF Files", "*.pdf")])

# Prompt the user to enter the page number to replace
target_page_number = int(input("Enter the page number to replace (starting from 1): "))

# Call the function to replace the page
replace_page(original_file, replacement_file, target_page_number)

print("Page replaced successfully. The modified PDF is saved as 'Modified_pdf.pdf'.")
