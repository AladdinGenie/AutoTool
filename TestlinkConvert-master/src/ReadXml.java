import java.io.*;
import java.util.*;

import org.dom4j.*;
import org.dom4j.io.*;



class ReadXml{

 //private String strFileName="SampleFile\\student.xml";
 private File xmlFile;
 //
 public List<String> gettestsuiteName(String strFileName) throws DocumentException{
	 xmlFile=new File(strFileName);      
 	  SAXReader reader=new SAXReader();     
 	  Document xmlDoc;
		xmlDoc = reader.read(xmlFile);
		Element root=xmlDoc.getRootElement();
		List<String> li = new ArrayList<String>();
		List testsuite=xmlDoc.selectNodes("//testsuite");		
		
		for(Iterator i=testsuite.iterator();i.hasNext();){
			Element ele=(Element)i.next();
			//去除name属性为空的字段
			if (ele.attribute("name").getValue()==""){
				continue;
				}
			System.out.println("Test "+ele.attribute("name").getValue()); 
			li.add(ele.attribute("name").getValue());
		}
	 return li;
 }
 
 //获取name
 public List<String> gettestcaseName(String strFileName) throws DocumentException{
	 xmlFile=new File(strFileName);      
 	  SAXReader reader=new SAXReader();     
 	  Document xmlDoc;
	
		xmlDoc = reader.read(xmlFile);
	 
		Element root=xmlDoc.getRootElement();
		List<String> li = new ArrayList<String>();
		List testcase=xmlDoc.selectNodes("//testcase");
		
		for(Iterator i=testcase.iterator();i.hasNext();){
			Element ele=(Element)i.next();
			System.out.println("Test "+ele.attribute("name").getValue()); 
			li.add(ele.attribute("name").getValue());
		}
	 return li;
 }
 
 //获取关键字
 public List<String> getKey(String strFileName) throws DocumentException{
	  xmlFile=new File(strFileName);      
 	  SAXReader reader=new SAXReader();     
 	  Document xmlDoc;
	
	  xmlDoc = reader.read(xmlFile);
	 
 	  Element root=xmlDoc.getRootElement();
 	  List<String> li = new ArrayList<String>();
 	  List testcase=xmlDoc.selectNodes("//keyword");
 	  
		for(Iterator i=testcase.iterator();i.hasNext();){
			Element ele=(Element)i.next();
//			System.out.println("Test "+ele.attribute("name").getValue()); 
			li.add(ele.attribute("name").getValue());
		}
	 return li;
 }
 
 
 
 //获取步长
 public int[] getTime(String strFileName) throws DocumentException{
	 xmlFile=new File(strFileName);      
	 SAXReader reader=new SAXReader();     
	 Document xmlDoc;
	 
	 xmlDoc = reader.read(xmlFile);
	 	
	  	List step_number = xmlDoc.selectNodes("//step_number");
		String number = "";
		int[] ti = new int[10000];
		
		for(Iterator it = step_number.iterator();it.hasNext();){
			Element ele=(Element)it.next();
			number += ele.getText();
		} 
		
		System.out.println("输出数组"+number);
		String[] num = number.split("1");
		System.out.println("输出数组长度"+num.length);
		
		for(int i=1; i<num.length; i++){
			System.out.println(num[i].length());
			ti[i] = num[i].length()+1;
		} 
		return ti;
			
 }
 
 
 //获取所有数据
 public List[] Read(String strFileName) throws DocumentException{
  
  
	  xmlFile=new File(strFileName);      
  	  SAXReader reader=new SAXReader();     
  	  Document xmlDoc;
	
	  xmlDoc = reader.read(xmlFile);
	 
  	  Element root=xmlDoc.getRootElement();    

	  
  	  
  	  	int add_num = 0;
  	  	
  	  	List step_number = xmlDoc.selectNodes("//step_number");
 		String number = "";
 		
 		for(Iterator it = step_number.iterator();it.hasNext();){
 			Element ele=(Element)it.next();
 			number += ele.getText();
 		} 
 		System.out.println("输出数组"+number);
 		String[] num = number.split("1");
 		int leng = num.length-1;
 		System.out.println("输出数组长度"+num.length);
 		
 		for(String len:num){
 			System.out.println(len.length());
 			add_num = len.length();
 		}
 		
 		//增加testsuite参数
  	  	List testsuite=xmlDoc.selectNodes("//testsuite");
 		
 		List testcase=xmlDoc.selectNodes("//version");
  	  	
  	  	
		List importance=xmlDoc.selectNodes("//importance");

		List execution_type=xmlDoc.selectNodes("//testcase/execution_type");
  	  
		List version=xmlDoc.selectNodes("//version");
			
   		List summary=xmlDoc.selectNodes("//summary");
 
   		List preconditions=xmlDoc.selectNodes("//preconditions");
   		
   		
   		
		List actions=xmlDoc.selectNodes("//actions");
		System.out.println("list长度:"+actions.size());

		List expectedresults=xmlDoc.selectNodes("//expectedresults");

			
		List externalid=xmlDoc.selectNodes("//externalid");
		
			/*for(Iterator i=externalid.iterator();i.hasNext();){
				Element ele=(Element)i.next();
				System.out.println("Test "+ele.getText()); 
			}*/
   
	List[] result = {testsuite,testcase,version,summary,preconditions,importance,step_number,actions,expectedresults,};
 	
	
	return result;   
  	
 }
 /*public static void main(String [] args) throws DocumentException{

    new ReadXml().getTime("SampleFile\\student.xml");

  }*/
}