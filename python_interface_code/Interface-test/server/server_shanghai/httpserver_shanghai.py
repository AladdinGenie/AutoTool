#coding:gbk
#!/usr/bin/python
import BaseHTTPServer
import codecs
import sys
import glob
import xml.sax  
import xml.sax.handler  
from my_xml import XMLHandler
reload(sys)
sys.setdefaultencoding( "utf-8" )

class TestHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):  
	def do_GET(self):  
		print "do_get"
		buf = open("./QueryPolicyByIdNo.wsdl").read()
		tmp = buf.decode("gbk").encode("utf8")
		
		self.send_response(200)
#		self.send_header("Content-type",'text/plain')
		self.end_headers()
		self.wfile.write(tmp)

	def do_POST(self): 	
		datas = self.rfile.read(int(self.headers['content-length']))
		xh = XMLHandler()
		xml.sax.parseString(datas, xh)
		ret = xh.getDict()
		key_value=ret['ax273:IDNO']
	'''
		if (key_value[0] == "4"):
			print key_value
			buf = open("../data/shanghai/find.xml").read()
		elif glob.glob("../data/shanghai/"+key_value+".xml"):
	'''
		if glob.glob("../data/shanghai/"+key_value+".xml"):
			print "../data/shanghai/"+key_value+".xml"
			buf = open("../data/shanghai/"+key_value+".xml").read()
		else :
			buf = open("../data/shanghai/nofind.xml").read()

		tmp = buf.decode("gbk").encode("utf8")
		self.send_response(200)
#		self.send_header("Content-type",'text/plain')
		self.end_headers()
		self.wfile.write(tmp)



if __name__ == "__main__" :
	server_ip=sys.argv[1]
	server_port=sys.argv[2]
	
	http_server =  BaseHTTPServer.HTTPServer((server_ip, int(server_port)), TestHTTPHandler)  
	http_server.serve_forever()
