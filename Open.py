from xml.dom import minidom

class Open:

    def __init__(self):
        pass
        
    def openFile(self, file):
        try:
            opened = minidom.parse(file)
            return opened
        except:
            return None