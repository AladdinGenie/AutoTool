package authorize.universal.method;

import java.io.File;
import java.io.IOException;
import java.util.Calendar;

import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;

import com.google.common.io.Files;

public class ScreenShot
{
    static String filepath = createDir.takecreateDir("d:/webdriver/");// 设置目录路径
    
    static Calendar ca = Calendar.getInstance();

    static int day = ca.get(Calendar.DATE);// 获取日

    static int minute = ca.get(Calendar.MINUTE);// 分

    static int hour = ca.get(Calendar.HOUR);// 小时

    static String data = day + "_" + hour + "_" + minute;

    public static void takeScreenShot(String name, WebDriver driver)
    {

        File scrFile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
        try
        {          
            Files.copy(scrFile, new File(filepath + data + "_" + name + ".jpeg"));
            System.out.println(name + " "+"screenshots Successfully...");
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
    }

}
