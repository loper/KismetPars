import sys
import CSVmaker
import Open
import Parser

if __name__ == "__main__":
    if (len(sys.argv)<2):
        print "uzycie: python run.py <plik_netxml>"
        exit(-1)
    o = Open.Open()
    file = o.openFile(sys.argv[1])
    csv = CSVmaker.CSVmaker('parsed.csv')
    csv.write(['essid', 'bssid', 'type', 'channel', 'encryption', 'power'])
    
    pars = Parser.Parser()
    net = pars.mainNode(file, 'wireless-network')

    for i in range(0, len(net)):
        ok = pars.setNet(net[i])
        if not ok:
            continue
        pars.setSSIDnode()
        encryption = pars.getData('encryption')
        if encryption == "err":
            continue
        essid = pars.getData('essid')
        type = pars.getAttr('type')
        channel = pars.getNodeData('channel')
        bssid = pars.getNodeData('BSSID')
        power = pars.getSonarData('max_signal_dbm')
        if (essid<>'err'):
            csv.write([essid, bssid, type, channel, encryption, power])


        data = {'ESSID':essid, 'type': type, 'encryption':encryption, 'channel':channel, 'power':power, 'bssid':bssid}
        print ", ".join(data.values())
