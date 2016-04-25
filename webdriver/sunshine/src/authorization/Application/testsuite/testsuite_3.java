package authorization.Application.testsuite;


import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import authorize.getproject.ObjectGetProject;
import authorize.universal.method.ScreenShot;
import authorize.universal.method.globalValue;
import authorize.universal.method.openBrowser;
import authorize.universal.method.sleep;

/*
 * 文件名：testsuite_3.java
 * 包名：authorization.Application.testsuite
 * 目的：执行测试用例7.2
 * 输入参数：typeOrderNo
 * 返回结果：
 * 注意事项：
 * 作者：曾昱皓
 * 日期：May 6, 2014 5:17:31 PM
*/
public class testsuite_3
{
    public testsuite_3(WebDriver driver)
    {
        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public testsuite_3()throws FileNotFoundException, IOException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String login_passwd = prop.getProperty("password");
        int count = Integer.parseInt(prop.getProperty("count"));
        int time = Integer.parseInt(prop.getProperty("time"));
        String Custom_URL = prop.getProperty("Custom_URL");
        String typeOrderNo = prop.getProperty("typeOrderNo");

        for (int i = 1; i <= count; i++)
        {
            WebDriver odriver = new openBrowser().run(Custom_URL);
            sleep.wait(time);
            System.out.println("testsuite_3 is starting...");
            odriver.manage().window().maximize();
            sleep.wait(time);
            ObjectGetProject ObjectGetProject = new ObjectGetProject(odriver);
            sleep.wait(time);
            ObjectGetProject.typeOrderNo(typeOrderNo);
            sleep.wait(time);
            ObjectGetProject.typePassword(login_passwd);
            sleep.wait(time);
            ObjectGetProject.clickConfirmButtonLocator();
            sleep.wait(time);
            String assertText = odriver.findElement(By.cssSelector("body > div > div.box.ng-scope > div:nth-child(2) > h4")).getText();
            String selectxlineButton = "授权单orderno：总点数total，已使用点数i，剩余点数spare";
            int total = count;
            int used = i;
            int spare = total - used;
            String orderno = selectxlineButton.replaceAll("orderno", typeOrderNo);
            String totalcount = orderno.replaceAll("total", String.valueOf(total));
            String usedcount = totalcount.replaceAll("i", String.valueOf(used));
            String sparecount = usedcount.replaceAll("spare", String.valueOf(spare));
            if (assertText.equals(sparecount))
            {
                System.out.println(assertText);
            }
            else
            {
                System.out.println("第" + String.valueOf(i) + "次" + " Failed..");
            }
            ScreenShot.takeScreenShot("testsuite_3_1", odriver); 
            sleep.wait(time);
            odriver.quit();
        }
    }
}