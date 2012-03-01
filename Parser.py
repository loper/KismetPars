class Parser:
    __net = None
    __ssid_node = None
    __sonar = None

    def mainNode(self, file, node):
        main = file.childNodes[1].getElementsByTagName(node)
        return main

    def setNet(self, net):
        self.__net = net
        if self.__net != None:
            return True
        return False

    def getAttr(self, data):
        return self.__net.attributes.getNamedItem(data).value

    def setSSIDnode(self):
        self.__ssid_node = self.__net.getElementsByTagName('SSID')

    def getSonarData(self, data):
        try:
            self.__sonar = self.__net.getElementsByTagName('snr-info')
            datz = self.__sonar[0].getElementsByTagName(data)[0].childNodes[0].data
            return datz
        except:
            return 'err'

    def getData(self, data):
        try:
            elem = self.__ssid_node[0].getElementsByTagName(data)
            if len(elem) == 2:
                return elem[1].childNodes[0].data
            return elem[0].childNodes[0].data
        except:
            return 'err'

    def getNodeData(self, data):
        try:
            datz = self.__net.getElementsByTagName(data)[0].childNodes[0].data
            return datz
        except:
            return 'err'
