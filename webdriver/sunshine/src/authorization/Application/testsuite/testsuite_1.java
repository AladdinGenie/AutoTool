package authorization.Application.testsuite;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import authorize.login.LoginPage;
import authorize.universal.method.ScreenShot;
import authorize.universal.method.globalValue;
import authorize.universal.method.highlight;
import authorize.universal.method.openBrowser;
import authorize.universal.method.sleep;

/*
 * 文件名：testsuite_1.java
 * 包名：authorization.Application.testsuite
 * 目的：执行测试用例7.1
 * 输入参数：
 * 返回结果：
 * 注意事项：
 * 作者：曾昱皓
 * 日期：May 6, 2014 5:16:36 PM
*/
public class testsuite_1
{

    public testsuite_1(WebDriver driver)
    {
        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public testsuite_1() throws FileNotFoundException, IOException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String login_name = prop.getProperty("admin_name");
        String login_passwd = prop.getProperty("root_password");
        int count = Integer.parseInt(prop.getProperty("count"));
        int time = Integer.parseInt(prop.getProperty("time"));

        for (int i = 1; i <= count; i++)
        {
            WebDriver odriver = new openBrowser().run();
            LoginPage LoginPage = new LoginPage(odriver);
            sleep.wait(time);
            System.out.println("testsuite_1 is starting...");
            odriver.manage().window().maximize();
            sleep.wait(time);
            highlight.Element(odriver, LoginPage.getusernameLocator());
            sleep.wait(time);
            LoginPage.typeUsername(login_name);
            sleep.wait(time);
            highlight.Element(odriver, LoginPage.getpasswordLocator());
            sleep.wait(time);
            LoginPage.typePassword(login_passwd);
            sleep.wait(time);
            highlight.Element(odriver, LoginPage.getloginButtonLocator());
            sleep.wait(time);
            LoginPage.clickLogin();
            sleep.wait(time);
            String assertText = odriver.findElement(By.cssSelector("#loginModal > div > div > div.modal-body > form > div.form-group.has-error > p.help-block.ng-binding")).getText();
            if (assertText.equals("密码错误"))
            {
                System.out.println(assertText);
            }
            ScreenShot.takeScreenShot("testsuite_1_1", odriver);         
            odriver.quit();
        }
    }
}
