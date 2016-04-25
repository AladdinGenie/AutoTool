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
 * 文件名：deluser.java
 * 包名：authorize.testsuite
 * 目的：执行测试用例3. 删除用户
 * 输入参数：test_name
 * 返回结果：
 * 注意事项：使用admin_name账号测试
 * 作者：曾昱皓
 * 日期：May 6, 2014 2:30:20 PM
*/
public class deluser
{
    public deluser(WebDriver driver)
    {
        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public deluser() throws FileNotFoundException, IOException, InterruptedException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String root_name = prop.getProperty("root_name");
        String root_password = prop.getProperty("root_password");
        String login_name = prop.getProperty("admin_name");
        String login_passwd = prop.getProperty("password");
        int count = Integer.parseInt(prop.getProperty("count"));
        int time = Integer.parseInt(prop.getProperty("time"));
        String admin_name = prop.getProperty("admin_name");
        String guest_name = prop.getProperty("guest_name");
        String modify_name = prop.getProperty("modify_name");

        for (int i = 1; i <= count; i++)
        {

          //删除guest用户
            WebDriver wdriver = new openBrowser().run();
            LoginPage LoginPage_guest = new LoginPage(wdriver);
            sleep.wait(time);
            wdriver.manage().window().maximize();
            sleep.wait(time);
            highlight.Element(wdriver, LoginPage_guest.getusernameLocator());
            sleep.wait(time);
            LoginPage_guest.typeUsername(login_name);
            sleep.wait(time);
            highlight.Element(wdriver, LoginPage_guest.getpasswordLocator());
            sleep.wait(time);
            LoginPage_guest.typePassword(login_passwd);
            sleep.wait(time);
            highlight.Element(wdriver, LoginPage_guest.getloginButtonLocator());
            sleep.wait(time);
            LoginPage_guest.clickLogin();
            sleep.wait(time);
            LoginPage_guest.clickusermanagementPage();
            sleep.wait(time);
            ScreenShot.takeScreenShot("deluser_guest_usermanagementPage", wdriver);
            ObjectUserManagement ObjectUserManagement_guest = new ObjectUserManagement(wdriver);
            for (int j = 1; j <= 10; j++)
            {
                ObjectUserManagement_guest.clickSelectxlineLocator(String.valueOf(j), guest_name);
            }
            sleep.wait(time);
            highlight.Element(wdriver, ObjectUserManagement_guest.getdelButtonLocator());
            sleep.wait(time);
            ObjectUserManagement_guest.clickDelButtonLocator(ObjectUserManagement_guest.getdelButtonLocator());
            sleep.wait(time);
            ObjectUserManagement_guest.clickSaveButtonLocator("/html/body/div[2]/div/div/div[2]/button[2]");
            sleep.wait(time*5);
            LoginPage_guest.clickoperationPage();
            sleep.wait(time*3);
            ScreenShot.takeScreenShot("del_guest_operationPage", wdriver);
            sleep.wait(time);
            wdriver.quit();
            //删除test用户
            WebDriver wd = new openBrowser().run();
            LoginPage LoginPage_test = new LoginPage(wd);
            sleep.wait(time);
            wd.manage().window().maximize();
            sleep.wait(time);
            highlight.Element(wd, LoginPage_test.getusernameLocator());
            sleep.wait(time);
            LoginPage_test.typeUsername(login_name);
            sleep.wait(time);
            highlight.Element(wd, LoginPage_test.getpasswordLocator());
            sleep.wait(time);
            LoginPage_test.typePassword(login_passwd);
            sleep.wait(time);
            highlight.Element(wd, LoginPage_test.getloginButtonLocator());
            sleep.wait(time);
            LoginPage_test.clickLogin();
            sleep.wait(time);
            LoginPage_test.clickusermanagementPage();
            sleep.wait(time);
            ScreenShot.takeScreenShot("deluser_test_usermanagementPage", wd);
            ObjectUserManagement ObjectUserManagement_test = new ObjectUserManagement(wd);
            for (int j = 1; j <= 10; j++)
            {
                ObjectUserManagement_test.clickSelectxlineLocator(String.valueOf(j), modify_name);
            }
            sleep.wait(time);
            highlight.Element(wd, ObjectUserManagement_test.getdelButtonLocator());
            sleep.wait(time);
            ObjectUserManagement_test.clickDelButtonLocator(ObjectUserManagement_test.getdelButtonLocator());
            sleep.wait(time);
            ObjectUserManagement_test.clickSaveButtonLocator("/html/body/div[2]/div/div/div[2]/button[2]");
            sleep.wait(time*5);
            LoginPage_test.clickoperationPage();
            sleep.wait(time*3);
            ScreenShot.takeScreenShot("del_test_operationPage", wd);
            sleep.wait(time);
            wd.quit();
            //删除admin用户
            WebDriver odriver = new openBrowser().run();
            LoginPage LoginPage = new LoginPage(odriver);
            sleep.wait(time);
            odriver.manage().window().maximize();
            sleep.wait(time);
            highlight.Element(odriver, LoginPage.getusernameLocator());
            sleep.wait(time);
            LoginPage.typeUsername(root_name);
            sleep.wait(time);
            highlight.Element(odriver, LoginPage.getpasswordLocator());
            sleep.wait(time);
            LoginPage.typePassword(root_password);
            sleep.wait(time);
            highlight.Element(odriver, LoginPage.getloginButtonLocator());
            sleep.wait(time);
            LoginPage.clickLogin();
            sleep.wait(time);
            LoginPage.clickusermanagementPage();
            sleep.wait(time);
            ScreenShot.takeScreenShot("deluser_admin_usermanagementPage", odriver);
            ObjectUserManagement ObjectUserManagement = new ObjectUserManagement(odriver);
            for (int j = 1; j <= 10; j++)
            {
                ObjectUserManagement.clickSelectxlineLocator(String.valueOf(j), admin_name);
            }
            sleep.wait(time);
            highlight.Element(odriver, ObjectUserManagement.getdelButtonLocator());
            sleep.wait(time);
            ObjectUserManagement.clickDelButtonLocator(ObjectUserManagement.getdelButtonLocator());
            sleep.wait(time);
            ObjectUserManagement.clickSaveButtonLocator("/html/body/div[2]/div/div/div[2]/button[2]");
            sleep.wait(time*5);
            LoginPage.clickoperationPage();
            sleep.wait(time*3);
            ScreenShot.takeScreenShot("del_admin_operationPage", odriver);
            sleep.wait(time);
            odriver.quit();
        }
    }
}