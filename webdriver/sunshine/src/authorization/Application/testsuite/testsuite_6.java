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
 * 文件名：testsuite_6.java
 * 包名：authorization.Application.testsuite
 * 目的：执行测试用例7.4
 * 输入参数：modifyOrderNo
 * 返回结果：
 * 注意事项：
 * 作者：曾昱皓
 * 日期：May 6, 2014 5:18:00 PM
*/
public class testsuite_6
{
    public testsuite_6(WebDriver driver)
    {
        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public testsuite_6() throws FileNotFoundException, IOException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        int count = Integer.parseInt(prop.getProperty("count"));
        int time = Integer.parseInt(prop.getProperty("time"));
        String Custom_URL = prop.getProperty("Custom_URL");
        String modifyOrderNo = prop.getProperty("modifyOrderNo");

        for (int i = 1; i <= count; i++)
        {
            WebDriver odriver = new openBrowser().run(Custom_URL);
            sleep.wait(time);
            System.out.println("testsuite_6 is starting...");
            odriver.manage().window().maximize();
            sleep.wait(time);
            ObjectGetProject ObjectGetProject = new ObjectGetProject(odriver);
            sleep.wait(time);
            ObjectGetProject.typeOrderNo(modifyOrderNo);
            sleep.wait(time);
            ObjectGetProject.typePassword(modifyOrderNo);
            sleep.wait(time);
            ObjectGetProject.clickConfirmButtonLocator();
            sleep.wait(time);
            String assertText = odriver.findElement(By.cssSelector("#loginModal > div > div > div.modal-body > form > div.form-group.has-error > p.help-block.ng-binding")).getText();
            if (assertText.equals("授权单号不存在"))
            {
                System.out.println(assertText);
            }
            ScreenShot.takeScreenShot("testsuite_6_1", odriver); 
            sleep.wait(time);
            odriver.quit();
        }
    }
}