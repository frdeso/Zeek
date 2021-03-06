import Queue

CONFIG = 0
INFO = 1
URL = 2


class Packet:
    def __init__(self, type, payload):
        self.type = type
        self.payload = payload

    def setPayload(self, payload):
        self.payload = payload


class ConfigurationPayload():
    STATIC_CRAWLING = 0
    DYNAMIC_CRAWLING = 1
    def __init__(self, crawlingType):
        self.crawlingType = crawlingType


class InfoPayload():
    CLIENT_ACK = 0
    SERVER_ACK = 1

    def __init__(self, info):
        self.info = info


class URLPayload():
    def __init__(self, urlList):
        self.urlList = urlList


def deQueue(queueArray):
    packetArray = []
    for queue in queueArray:
        try:
            packet = queue.get(block=False)
            packetArray.append(packet)
        except Queue.Empty:
            pass
    return packetArray