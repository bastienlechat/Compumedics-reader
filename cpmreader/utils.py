from xml.etree import cElementTree as ElementTree


def lights_is_wrong(lights_off, lights_on):

    if lights_off is not None and lights_on is not None:
        if lights_off>= lights_on:
            return True
        else:
            return False
    else:
        return True

## Forms to deal with XMLs
## This was found in https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary
## and linked here: https://code.activestate.com/recipes/410469-xml-as-dictionary/

class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)