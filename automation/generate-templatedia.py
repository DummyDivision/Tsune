import re
import sys

def getDigraphString(filename):
    '''Extracts necessary information to draw Digraph from template'''
    with open(filename, 'r') as template:
        content = template.read()
    extends = re.search('{% extends "(.*)" %',content)
    if extends is None:
        return False
    extended = filename[filename.find('templates')+10:]
    return '"'+extended+'"' + ' -> ' + '"'+ extends.group(1) + '"'


def main(filenameList):
    with open('templates.dot', 'w') as templateDiagram:
        templateDiagram.write('digraph G {\n')
        for filename in filenameList:
            result = getDigraphString(filename)
            if result:
                templateDiagram.write(result+'\n')
        templateDiagram.write('}')


main(sys.argv[1:])
