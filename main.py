import csv, json, xml.etree.ElementTree as ET, re, os.path as path
def main():
    in_File =   input('Enter the name of the file in the local directory: ')
    if path.exists(in_File):
        while True:
            print('-c CSV format\n'
                  '-j JSON format\n'
                  '-x XML format')
            in_Conv =   input('Enter flag to convert: ')
            if in_Conv.lower() == '-c':
                conv_csv(in_File)
                break
            elif in_Conv.lower() == '-j':
                conv_json(in_File)
                break
            elif in_Conv.lower() == '-x':
                conv_xml(in_File)
                break
            else:
                print('Enter a valid argument, try again.')
    else:
        print('File not found in local directory, please verify file name.')
        main()

def conv_csv (user_file):
    # open source file, create output file
    with open(user_file, 'r') as file, open(user_file.strip('.txt')+'.csv', 'w') as outfile:
        # read in Tab delimited data with instance of DictReader
        read = csv.DictReader(file, delimiter='\t')
        # create DictWriter instance in outfile from DictReader
        outfile = csv.DictWriter(outfile, delimiter='\t', fieldnames=read.fieldnames)
        # write header
        outfile.writeheader()
        # write rows
        outfile.writerows(read)
        print('File written to ' + user_file.strip('.txt')+'.csv')
def conv_json (user_file):
    with open(user_file) as file, open(user_file.strip('.txt')+'.json', 'w') as outfile:
        # read in Tab delimited data with instance of DictReader
        read = csv.DictReader(file, delimiter='\t')
        # write to json output file
        outfile.writelines(json.dumps(list(read)))
        print('File written to ' + user_file.strip('.txt')+'.json')
def conv_xml (user_file):
    with open(user_file) as file:
        read,data = csv.DictReader(file, delimiter='\t'), {}
        root = ET.Element('data')
        for child in read:
            node = ET.Element('input')
            root.append(node)
            for attrib in child.keys():
                attrib_r = attrib
                replace_chars = (('[^A-Za-z0-9]+', ''), ('[0-9]+', ''))
                for element in replace_chars:
                    attrib_r = re.sub(element[0], element[1], attrib_r)
                key = ET.SubElement(node, attrib_r)
                key.text = str(child.get(attrib))

        tree = ET.ElementTree(root)
        tree.write(user_file.strip('.txt')+'.xml')
        print('File written to ' + user_file.strip('.txt')+'.xml')

main()
# conv_xml('stats.txt')
# conv_csv('stats.txt')
# conv_json('stats.txt')