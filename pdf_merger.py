import os
from PyPDF2 import PdfMerger
from pathlib import Path


def concatenate_pdfs(input_folder, output_file_name="combined.pdf"):
    """
    Traverses a folder and concatenates all files in it into one file.
    Args:
        input_folder (path): DPath to the folder containing the PDFs.
        output_file_name (str): Name of the output file, "combined.pdf" by default.
    """

    if not os.path.isdir(input_folder):
        print(f"Error: Folder '{input_folder}' not found.")
        return

    merger = PdfMerger()
    pdf_files = []

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(input_folder, file_name)
            pdf_files.append(file_path)

    pdf_files.sort()

    if not pdf_files:
        print(f"No files found in folder '{input_folder}'.")
        return

    for pdf in pdf_files:
        try:
            merger.append(pdf)
            print(f"'{os.path.basename(pdf)}' added.")
        except Exception as e:
            print(f"Error while adding file '{os.path.basename(pdf)}': {e}.")

    output_path = os.path.join(input_folder, output_file_name)

    try:
        with open(output_path, "wb") as output_file:
            merger.write(output_file)
        print(f"\nAll pdfs successfully combined in '{output_file_name}'.")
    except Exception as e:
        print(f"Error while writing in file: {e}.")
    finally:
        merger.close()


if __name__ == "__main__":
    target_folder = input(f'enter absolute path to folder of files')
    target_folder = Path(target_folder)
    print(f"The target folder is '{target_folder}'.")
    concatenate_pdfs(target_folder)