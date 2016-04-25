import java.io.FileInputStream;  
import java.io.InputStream;  
import java.util.ArrayList;  
import java.util.List;  
import java.util.regex.Pattern;

import jxl.Cell;  
import jxl.Sheet;  
import jxl.Workbook;  
import jxl.WorkbookSettings;  
  
/** 
 * Jxl目前只支持Excel 2003版本 
 * 支持Excel的多表读数据 
 */  
public class ReadXls {  
      
	
	/*public static void main(String args[]) throws Exception{
		readExcel("SampleFile\\testsuites.xls");
	}*/
	public static String HtmlsText(String inputString) {
		String htmlStr = inputString; // 含html标签的字符串
		String textStr = "";
		java.util.regex.Pattern p_script;
		java.util.regex.Matcher m_script;
		java.util.regex.Pattern p_style;
		java.util.regex.Matcher m_style;
		java.util.regex.Pattern p_html;
		java.util.regex.Matcher m_html;

		try {
			String regEx_script = "<[\\s]*?script[^>]*?>[\\s\\S]*?<[\\s]*?\\/[\\s]*?script[\\s]*?>"; // 定义script的正则表达式{或<script[^>]*?>[\\s\\S]*?<\\/script>
			// }
			String regEx_style = "<[\\s]*?style[^>]*?>[\\s\\S]*?<[\\s]*?\\/[\\s]*?style[\\s]*?>"; // 定义style的正则表达式{或<style[^>]*?>[\\s\\S]*?<\\/style>
			// }
			String regEx_html = "<[^>]+>"; // 定义HTML标签的正则表达式
			p_script = Pattern.compile(regEx_script, Pattern.CASE_INSENSITIVE);
			m_script = p_script.matcher(htmlStr);
			htmlStr = m_script.replaceAll(""); // 过滤script标签
			p_style = Pattern.compile(regEx_style, Pattern.CASE_INSENSITIVE);
			m_style = p_style.matcher(htmlStr);
			htmlStr = m_style.replaceAll(""); // 过滤style标签
			p_html = Pattern.compile(regEx_html, Pattern.CASE_INSENSITIVE);
			m_html = p_html.matcher(htmlStr);
			htmlStr = m_html.replaceAll(""); // 过滤html标签
			htmlStr = htmlStr.replaceAll("\\s*|\t|\r|\n", "");// 去除字符串中的空格,回车,换行符,制表符
			htmlStr = htmlStr.replaceAll("&nbsp;", "");// 去除字符串中的空格,回车,换行符,制表符
			textStr = htmlStr;

		} catch (Exception e) {
			System.err.println("Html2Text: " + e.getMessage());
		}
		return textStr;// 返回文本字符串
	}
	
 
    public static List<String> readExcel(String excelfilePath) throws Exception {  
        String data="";
        InputStream ins = new FileInputStream(excelfilePath); //读取xls文件  
        WorkbookSettings setEncode = new WorkbookSettings(); //设置读文件编码  
        setEncode.setEncoding("GBK");  
        Workbook rwb = Workbook.getWorkbook(ins, setEncode);  
        List<String> alldata = new ArrayList<String>();  
        alldata.clear();  
        Sheet[] sheets=rwb.getSheets();//获得当前Excel表共有几个sheet  
        int pages = sheets.length; //获得表数  
          
        //将excel表中的数据读取出来  
        //在从Excel中读取数据的时候不需要知道每个sheet有几行，有那多少列  
        for(int i=0; i<pages; i++) {  
            Sheet sheet = rwb.getSheet(i);             
           
            //循环读取每一行的全部列数目的内容  
            int rows = sheet.getRows();		//列
            int cols = sheet.getColumns();  //行  
            	for(int r=1; r<rows; r++){
            		for(int c=0; c<cols; c++) {  //行循环,Excel的行列是从（0，0）开始  
                                      
            			Cell excelRows = sheet.getCell(c, r);  
            			String strRow = excelRows.getContents();  
            			data+=(strRow+",");
                    
            		}
            		String data1=HtmlsText(data);
            		alldata.add(data1);
            		data="";
            	}
              
        }  
                                ins.close();  

        System.out.println(alldata);

        return alldata;  
    } 
}