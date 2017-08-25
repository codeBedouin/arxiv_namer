import glob
import os
import PyPDF2


class arxivNamer(object):
    def __init__(self, paper_folder):
        self.folder_name = paper_folder

    def get_file_name(self):
        files_to_read = glob.glob('*.pdf')
        for f in files_to_read:
            ftr = open(f)
            pdfreader = PyPDF2.PdfFileReader(ftr)
            pdf_pointer = pdfreader.getPage(0)
            first_line = pdf_pointer.extractText().split('\n')[0]
            new_file_name = os.path.join(os.path.basename(f), (first_line +
                                                               '.pdf'))
            os.rename(f, new_file_name)


