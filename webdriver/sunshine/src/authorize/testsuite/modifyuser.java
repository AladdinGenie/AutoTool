package authorize.testsuite;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

import org.openqa.selenium.WebDriver;

import authorize.login.LoginPage;
import authorize.universal.method.ScreenShot;
import authorize.universal.method.globalValue;
import authorize.universal.method.highlight;
import authorize.universal.method.openBrowser;
import authorize.universal.method.sleep;
import authorize.user.management.ObjectUserManagement;

/*
 * 文件名：modifyuser.java
 * 包名：authorize.testsuite
 * 目的：执行测试用例2. 修改用户
 * 输入参数：modify_name,test_name
 * 返回结果：尾部增加zb
 * 注意事项：使用admin_name账号测试
 * 作者：曾昱皓
 * 日期：May 6, 2014 2:36:55 PM
*/
public class modifyuser
{
    public modifyuser(WebDriver driver)
    {
        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }
    public modifyuser() throws FileNotFoundException, IOException, InterruptedException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String login_name = prop.getProperty("admin_name");
        String login_passwd = prop.getProperty("password");
        int count = Integer.parseInt(prop.getProperty("count"));
        int time = Integer.parseInt(prop.getProperty("time"));
        String test_name = prop.getProperty("test_name");
        String modify_name = prop.getProperty("modify_name");  

        for (int i = 1; i <= count; i++)
        {
            WebDriver odriver = new openBrowser().run();
            LoginPage LoginPage = new LoginPage(odriver);
            sleep.wait(time);
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
            LoginPage.clickusermanagementPage();
            sleep.wait(time);
            ScreenShot.takeScreenShot("modifyuser_usermanagementPage", odriver);
            ObjectUserManagement ObjectUserManagement = new ObjectUserManagement(odriver);
            for (int j = 1; j <= 10; j++)
            {
                ObjectUserManagement.clickSelectxlineLocator(String.valueOf(j), test_name);
            }
            sleep.wait(time);
            highlight.Element(odriver, ObjectUserManagement.getmodifyButtonLocator());
            sleep.wait(time);
            ObjectUserManagement.clickModifyButton(ObjectUserManagement.getmodifyButtonLocator());
            sleep.wait(time);
            ObjectUserManagement.typeFullName(modify_name);
            sleep.wait(time);
            ObjectUserManagement.clickSaveButtonLocator("/html/body/div[3]/div/div/div/form/fieldset/div[9]/div/button[1]");
            sleep.wait(time*5);
            LoginPage.clickoperationPage();
            sleep.wait(time*3);
            ScreenShot.takeScreenShot("modify_admin_operationPage", odriver);
            sleep.wait(time);
            odriver.quit();
        }
    }
}