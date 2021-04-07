from xml.dom import minidom
import os

directory = r'[*/DIRECTORY/TO/ALL/IMAGE/IMAGES/SOURCE/HERE*]'

positive = 0
negative = 0
for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        doc = os.path.join(directory, filename)
        mydoc = minidom.parse(doc)
        
        items = mydoc.getElementsByTagName('name')
        label = items[0].firstChild.data
        images = mydoc.getElementsByTagName('filename')
        image = images[0].firstChild.data
        print(image, label)
        
        if label == 'OnPhone':
            positive += 1
        elif label == 'NotOnPhone':
            negative += 1
    else:
        continue

print()
print('Postive count:\t', positive)
print('Negative count:\t', negative)