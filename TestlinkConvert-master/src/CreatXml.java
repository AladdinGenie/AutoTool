import java.io.File;
import java.io.FileWriter;
import java.util.List;

import org.dom4j.Document;
import org.dom4j.DocumentHelper;
import org.dom4j.Element;
import org.dom4j.io.OutputFormat;
import org.dom4j.io.XMLWriter;

public class CreatXml {

 
/*    public static void main(String[] args) {
        // TODO Auto-generated method stub
        CreatXml xml = new CreatXml();
        xml.create("");
    }*/
    
	//生成节点
	
    public boolean create(String path) {
        boolean flag = false;
        Document document = null;        //文档
        Element	testsuite = null;		//套件根节点
        //Element testsuite = null;		//用例根节点
        Element node_order = null;
        Element details = null;
        Element testcase = null; 
        Element externalid = null;
        Element version = null;           
        Element summary = null;           
        Element preconditions = null;
        Element execution_type = null;
        Element importance = null;
        Element steps = null;            
        Element step = null;           
        Element step_number = null;            
        Element actions = null;           
        Element expectedresults = null;           
        Element keywords = null;           
        Element keyword = null;            
        OutputFormat format = null;
        XMLWriter writer = null;
        
        try {
            document = DocumentHelper.createDocument();
            String path1 = path.substring(0, path.length()-4);
            testsuite = document.addElement("testsuite");
            testsuite.addComment("注释");
            
            
            ReadXls rx = new ReadXls();
            List li = rx.readExcel(path);            
            
            for(int i=0; i<li.size();i++){
            
            String cdataString = "";	
            String cdataString1 = "1";
            String a = li.get(i).toString();
            testsuite = testsuite.addElement("testsuite");
            node_order = testsuite.addElement("node_order");
            node_order.addCDATA(cdataString);
            details = testsuite.addElement("details");
            details.addCDATA(cdataString);
            testcase = testsuite.addElement("testcase");
            node_order = testcase.addElement("node_order");
            node_order.addCDATA(cdataString);
            externalid = testcase.addElement("externalid");
            externalid.addCDATA(cdataString);
            version = testcase.addElement("version");
            summary = testcase.addElement("summary");
            preconditions = testcase.addElement("preconditions");
            execution_type = testcase.addElement("execution_type");
            execution_type.addCDATA(cdataString1);
            importance = testcase.addElement("importance");
            importance.addCDATA(cdataString);
            steps = testcase.addElement("steps");
            //keywords = testcase.addElement("keywords");
            //keyword = keywords.addElement("keyword");
            
            
            
            
            
           //填充数据
            //String a = "testsuite,testcase,version,summary,preconditions,importance,step_number,actions,expectedresults,";
            String[] b= a.split(",");
           
            for(int j=0; j<b.length; j++){
            
            switch(j){
            case 0:	
            	testsuite.addAttribute("name", b[j]);
         	   break;
            case 1:
            	testcase.addAttribute("name", b[j]);
        	    
        	    break;
            case 2:
            	version.setText(b[j]);
            	
            	break;
            case 3:
            	summary.setText(b[j]);
            	
            break;
            case 4:
            	preconditions.setText(b[j]);
            	
            break;
            case 5:
            	importance.setText(b[j]);
            	
            break;
            case 6:
            	//step_number.setText(b[j]);
            	
            break;
            case 7:
            	String s = b[j];
            	String[] t = s.split("\n");
            		for(int k=0; k<t.length; k++){
            			step = steps.addElement("step");
            			step_number = step.addElement("step_number");
            			step_number.setText(""+(k+1));
            			actions = step.addElement("actions");
            			actions.setText(t[k]);
            			
            			String ss =b[8];
                    	String[] tt = ss.split("\n");
                    	expectedresults = step.addElement("expectedresults");
            			expectedresults.setText(tt[k]);
            		}
            break;
            
            case 8:
            	//keyword.addAttribute("name", b[j]);
            break;
            	
            
            }}}
            //设置字符编码
            format = OutputFormat.createPrettyPrint();
            format.setEncoding("GBK");
            //format.setEncoding("UTF-8");    //用utf-8也不行
            
            System.out.println(document.asXML());
            
            writer = new XMLWriter(new FileWriter(new File(path1+".xml")), format);
            writer.write(document);
            writer.close();
            
            flag = true;
            
            return flag;
        }
        catch(Exception e) {
            e.printStackTrace();
        }
        return flag;
    }

}