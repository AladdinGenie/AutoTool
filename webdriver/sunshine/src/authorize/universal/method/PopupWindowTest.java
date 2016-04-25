package authorize.universal.method;

import java.util.Iterator;
import java.util.Set;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

 

public class PopupWindowTest {

 

 

         /**

          * @author gongjf

          */

         public static void main(String[] args) {

             System.setProperty("webdriver.chrome.driver",
                     "Driver\\chromedriver.exe");
             ChromeDriver dr = new ChromeDriver();

                   String url = "http://www.51.com/";

                   dr.get(url);        

                   dr.findElement(By.id("51")).click();

                   //得到当前窗口的句柄

                   String currentWindow = dr.getWindowHandle();

                   //得到所有窗口的句柄

                   Set<String>handles = dr.getWindowHandles();

                   Iterator<String>it = handles.iterator();

                   while(it.hasNext()){

                            if(currentWindow== it.next())  continue;

                            dr.switchTo().window(it.next());

                            

                   }

         }

 

}

