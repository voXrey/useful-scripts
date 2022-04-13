import argparse
import os

from scripts.convert import docx_to_pdf
from scripts.merge import merge_pdf
from scripts.commons import list_files


main_parser = argparse.ArgumentParser()
commands_subparsers = main_parser.add_subparsers(title="commands", dest="commands")

merge_parser = commands_subparsers.add_parser("merge", help="merge pdf")
merge_parser.add_argument('directory', help='directory of pdf files to merge')
merge_parser.add_argument('--final-file', help='path of final file (with extension)', required=False)

convert_parser = commands_subparsers.add_parser("convert", help="convert docx files to pdf files")
convert_parser.add_argument('directory', help='directory of docx files to convert')
convert_parser.add_argument('--final-directory', help='path of final directory where save new files', required=False)

args = main_parser.parse_args()
args = args.__dict__
command = args['commands']

if command == 'convert':
    directory = args['directory']

    if 'final-directory' in args: final_directory = args['final-directory']
    else: final_directory = os.path.curdir

    files = list_files(directory=directory, extension='docx')
    docx_to_pdf(files, final_directory)


elif command == 'merge':
    directory = args['directory']

    if 'final-file' in args: final_file = args['final-file']
    else: final_file = 'last_result.pdf'

    files = list_files(directory=directory, extension='pdf')
    merge_pdf(files, final_file)
