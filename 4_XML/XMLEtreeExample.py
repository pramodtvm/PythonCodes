##Below Code Created as a practice for XML parce and Practice 
##Author Pramod Raveendran

import os
import xml.etree.ElementTree as ET
#filename = 'DriverPackCatalog.xml'
filename = 'excercise.xml'
cwd = os.getcwd()
fullFile = os.path.abspath(os.path.join(cwd,filename))
tree = ET.parse(fullFile)
root = tree.getroot()

#Below code will get Child tag and Child attributes
##for child in root:
##    print (child.tag,child.attrib)

#Below Code will go through Child Element  
##for child in root:
##    for element in child:
##        print(element.tag,element.text)

##for child in root:
##    for element in child:
##        if element.tag == "Name":
##            print(element.tag)


for child in root:
    for attr in child:
        if (attr.tag == "sub-branch"):
            print(attr.tag,attr.text,attr.attrib['name'],attr.attrib['drunk'])
