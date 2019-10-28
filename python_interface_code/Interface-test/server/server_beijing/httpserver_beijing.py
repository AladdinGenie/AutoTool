#coding:gbk
#!/usr/bin/python
import BaseHTTPServer
import codecs
import sys
import glob
import xml.sax  
import xml.sax.handler  
import urlparse
from my_xml import XMLHandler
reload(sys)
sys.setdefaultencoding( "utf-8" )
 
def build_file_path(url_path,url_qs):  
	print (url_path)
	print (url_qs)
	
	if  (url_path.endswith("customer") ) :

		idcard=url_qs['idcard'][0]
		if(glob.glob("../data/beijing/customer/"+idcard+".json")):
			file_path="../data/beijing/customer/"+idcard+".json"
		else:
			file_path="../data/beijing/customer/no_find_idcard.json"

	elif(url_path.endswith("customerlist") ):

		name=url_qs['name'][0]
		if(glob.glob("../data/beijing/customerlist/"+name+".json")):
			file_path="../data/beijing/customerlist/"+name+".json"
		else:
			file_path="../data/beijing/customerlist/no_find_name.json"


	elif(url_path.endswith("tellerpolicy") ):
		
		if(glob.glob("../data/beijing/tellerpolicy/"+url_qs['sellerno'][0]+"*")):
			if(glob.glob("../data/beijing/tellerpolicy/"+url_qs['sellerno'][0]+"_"+url_qs['sdate'][0]+"_"+url_qs['edate'][0]+".json")):
				file_path="../data/beijing/tellerpolicy/"+url_qs['sellerno'][0]+"_"+url_qs['sdate'][0]+"_"+url_qs['edate'][0]+".json"
			else:
				file_path="../data/beijing/tellerpolicy/no_find_date.json"
		else:
			file_path="../data/beijing/tellerpolicy/no_find_sellerno.json"
			
	elif(url_path.endswith("tellerapplypolicy") ):
		
		if(glob.glob("../data/beijing/tellerapplypolicy/"+url_qs['sellerno'][0]+"*")):
			if(glob.glob("../data/beijing/tellerapplypolicy/"+url_qs['sellerno'][0]+"_"+url_qs['sdate'][0]+"_"+url_qs['edate'][0]+".json")):
				file_path="../data/beijing/tellerapplypolicy/"+url_qs['sellerno'][0]+"_"+url_qs['sdate'][0]+"_"+url_qs['edate'][0]+".json"
			else:
				file_path="../data/beijing/tellerapplypolicy/no_find_date.json"
		else:
			file_path="../data/beijing/tellerapplypolicy/no_find_sellerno.json"
		
	elif(url_path.endswith("tellercus") ):
		
		sellerno=url_qs['sellerno'][0]
		if(glob.glob("../data/beijing/tellercus/"+sellerno+".json")):
			file_path="../data/beijing/tellercus/"+sellerno+".json"
		else:
			file_path="../data/beijing/tellercus/no_find_sellerno.json"
		
	elif(url_path.endswith("policy") ):
		
		policyno=url_qs['policyno'][0] 
		if(glob.glob("../data/beijing/policy/"+policyno+".json")):
			file_path=glob.glob("../data/beijing/policy/"+policyno+".json")[0]
		
		else:
			file_path="../data/beijing/policy/no_find.json"
		
	else :
		file_path="../data/beijing/unknow.json"
	
	return file_path
	



class TestHTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):  

	def do_GET(self): 	
		#self.path：get请求的整个路径
		path_parsed = urlparse.urlparse(self.path)   #解析url，其中path为路径部分，query为参数部分
		path_qs = urlparse.parse_qs(path_parsed.query,True) #解析参数，返回参数字典
		
		
		
		buf = open(build_file_path(path_parsed.path , path_qs )).read() #生成数据文件所在路径并读取
		tmp = buf.decode("gbk").encode("utf8")
		if tmp[:3] == codecs.BOM_UTF8:
 			tmp = tmp[3:]
		
		self.send_response(200)
		self.send_header("Content-type","text/html;charset=\"utf-8\"")
		self.send_header("Content-Length",str(len(tmp)))
		self.end_headers()

		self.wfile.write(tmp)


if __name__ == "__main__" :
	
	server_ip=sys.argv[1]
	server_port=sys.argv[2]
	
	http_server =  BaseHTTPServer.HTTPServer((server_ip, int(server_port)), TestHTTPHandler)  
	http_server.serve_forever()
