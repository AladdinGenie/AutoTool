#!/usr/bin/python
# -*- encoding: utf-8 -*-
import xml.sax  
import xml.sax.handler  


class XMLHandler(xml.sax.handler.ContentHandler):
	def __init__(self):
		self.buffer = ""
		self.mapping = {}

	def startElement(self, name, attributes):
		self.buffer = ""

	def characters(self, data):
		self.buffer += data

	def endElement(self, name):
		self.mapping[name] = self.buffer

	def getDict(self):
		return self.mapping

if __name__ == '__main__':    

	buf = open("test.xml").read()

	xh = XMLHandler()
	xml.sax.parseString(buf, xh)
	ret = xh.getDict()

	#print ret
	print ret['Content']
	tmp=ret['Content'][10:]
	print tmp