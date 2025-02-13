import markdown
import sys
import os
from spire.doc import *
from spire.doc.common import *

def main():
    if len(sys.argv) < 4:
        sys.exit('system: python markdownToHtmlConverter.py <command> <input_file> <output_file>')
    cmd = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if cmd == 'markdown':
        createHtmlFile(input_file, output_file)
        print('system: End the convert')
    elif cmd == 'jpg':
        createHtmlFile(input_file, output_file)
        createJpgFile(output_file)
        os.remove(output_file)
        print('system: End the convert')
    else:
        sys.exit('system: This command is not available')

def createHtmlFile(input_file, output_file):
    try:
        markdownContents = getMarkdownContents(input_file)
    except Exception as e:
        sys.exit(f"Error reading input file: {e}")
    html = markdown.markdown(markdownContents)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

def getMarkdownContents(input_file):
    contents = ''
    with open(input_file, encoding='utf-8') as f:
        contents = f.read()

    return contents

def createJpgFile(html_file):
    jpgFile = ''
    input_file = html_file
    if input_file.endswith('.html'):
        jpgFile = input_file[:-5] + '.jpg'
    else:
        print('html_file is not endswith .html')
        sys.exit()
    document = Document()
    document.LoadFromFile(input_file, FileFormat.Html, XHTMLValidationType.none)

    imageStream = document.SaveImageToStreams(0, ImageType.Bitmap)
    with open(jpgFile, 'wb') as f:
        f.write(imageStream.ToArray())

    document.Close()

main()