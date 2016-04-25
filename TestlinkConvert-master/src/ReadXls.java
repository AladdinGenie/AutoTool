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
 * JxlĿǰֻ֧��Excel 2003�汾 
 * ֧��Excel�Ķ������� 
 */  
public class ReadXls {  
      
	
	/*public static void main(String args[]) throws Exception{
		readExcel("SampleFile\\testsuites.xls");
	}*/
	public static String HtmlsText(String inputString) {
		String htmlStr = inputString; // ��html��ǩ���ַ���
		String textStr = "";
		java.util.regex.Pattern p_script;
		java.util.regex.Matcher m_script;
		java.util.regex.Pattern p_style;
		java.util.regex.Matcher m_style;
		java.util.regex.Pattern p_html;
		java.util.regex.Matcher m_html;

		try {
			String regEx_script = "<[\\s]*?script[^>]*?>[\\s\\S]*?<[\\s]*?\\/[\\s]*?script[\\s]*?>"; // ����script��������ʽ{��<script[^>]*?>[\\s\\S]*?<\\/script>
			// }
			String regEx_style = "<[\\s]*?style[^>]*?>[\\s\\S]*?<[\\s]*?\\/[\\s]*?style[\\s]*?>"; // ����style��������ʽ{��<style[^>]*?>[\\s\\S]*?<\\/style>
			// }
			String regEx_html = "<[^>]+>"; // ����HTML��ǩ��������ʽ
			p_script = Pattern.compile(regEx_script, Pattern.CASE_INSENSITIVE);
			m_script = p_script.matcher(htmlStr);
			htmlStr = m_script.replaceAll(""); // ����script��ǩ
			p_style = Pattern.compile(regEx_style, Pattern.CASE_INSENSITIVE);
			m_style = p_style.matcher(htmlStr);
			htmlStr = m_style.replaceAll(""); // ����style��ǩ
			p_html = Pattern.compile(regEx_html, Pattern.CASE_INSENSITIVE);
			m_html = p_html.matcher(htmlStr);
			htmlStr = m_html.replaceAll(""); // ����html��ǩ
			htmlStr = htmlStr.replaceAll("\\s*|\t|\r|\n", "");// ȥ���ַ����еĿո�,�س�,���з�,�Ʊ��
			htmlStr = htmlStr.replaceAll("&nbsp;", "");// ȥ���ַ����еĿո�,�س�,���з�,�Ʊ��
			textStr = htmlStr;

		} catch (Exception e) {
			System.err.println("Html2Text: " + e.getMessage());
		}
		return textStr;// �����ı��ַ���
	}
	
 
    public static List<String> readExcel(String excelfilePath) throws Exception {  
        String data="";
        InputStream ins = new FileInputStream(excelfilePath); //��ȡxls�ļ�  
        WorkbookSettings setEncode = new WorkbookSettings(); //���ö��ļ�����  
        setEncode.setEncoding("GBK");  
        Workbook rwb = Workbook.getWorkbook(ins, setEncode);  
        List<String> alldata = new ArrayList<String>();  
        alldata.clear();  
        Sheet[] sheets=rwb.getSheets();//��õ�ǰExcel���м���sheet  
        int pages = sheets.length; //��ñ���  
          
        //��excel���е����ݶ�ȡ����  
        //�ڴ�Excel�ж�ȡ���ݵ�ʱ����Ҫ֪��ÿ��sheet�м��У����Ƕ�����  
        for(int i=0; i<pages; i++) {  
            Sheet sheet = rwb.getSheet(i);             
           
            //ѭ����ȡÿһ�е�ȫ������Ŀ������  
            int rows = sheet.getRows();		//��
            int cols = sheet.getColumns();  //��  
            	for(int r=1; r<rows; r++){
            		for(int c=0; c<cols; c++) {  //��ѭ��,Excel�������Ǵӣ�0��0����ʼ  
                                      
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