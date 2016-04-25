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
 * 文件名：adduser.java
 * 包名：authorize.testsuite
 * 目的：执行测试用例1. 新增用户
 * 输入参数：admin_name，guest_name，test_name
 * 返回结果：
 * 注意事项：root_name
 * 作者：曾昱皓
 * 日期：May 6, 2014 2:11:07 PM
*/
public class adduser
{
    public adduser(WebDriver driver)
    {
        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public adduser() throws FileNotFoundException, IOException, InterruptedException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String login_name = prop.getProperty("root_name");
        String login_passwd = prop.getProperty("root_password");
        String admin_name = prop.getProperty("admin_name");
        String guest_name = prop.getProperty("guest_name");
        String test_name = prop.getProperty("test_name");
        String password = prop.getProperty("password");
        int count = Integer.parseInt(prop.getProperty("count"));
        int time = Integer.parseInt(prop.getProperty("time"));

        for (int i = 1; i <= count; i++)
        {
            //增加admin用户
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
            ScreenShot.takeScreenShot("adduser_admin_usermanagementPage", odriver);
            ObjectUserManagement ObjectUserManagement = new ObjectUserManagement(odriver);
            highlight.Element(odriver, ObjectUserManagement.getnewButtonLocator());
            sleep.wait(time);
            ObjectUserManagement.clickNewButton(ObjectUserManagement.getnewButtonLocator());
            sleep.wait(time);
            ObjectUserManagement.typeUsername(admin_name);
            sleep.wait(time);
            ObjectUserManagement.typeFullName(admin_name);
            sleep.wait(time);
            ObjectUserManagement.typePassword(password);
            sleep.wait(time);
            ObjectUserManagement.typeConfirmPassword(password);
            sleep.wait(time);
            ObjectUserManagement.selectAdministratorRadioLocator(ObjectUserManagement.getadministratorradioLocator());
            sleep.wait(time);
            ObjectUserManagement.clickSaveButtonLocator();
            sleep.wait(time*5);
            LoginPage.clickoperationPage();
            sleep.wait(time*3);
            ScreenShot.takeScreenShot("add_admin_user_operationPage", odriver);
            sleep.wait(time);
            odriver.quit();
            //增加guest用户
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
            ScreenShot.takeScreenShot("add_guest_usermanagementPage", wdriver);
            ObjectUserManagement ObjectUserManagement_guest = new ObjectUserManagement(wdriver);
            highlight.Element(wdriver, ObjectUserManagement_guest.getnewButtonLocator());
            sleep.wait(time);
            ObjectUserManagement_guest.clickNewButton(ObjectUserManagement_guest.getnewButtonLocator());
            sleep.wait(time);
            ObjectUserManagement_guest.typeUsername(guest_name);
            sleep.wait(time);
            ObjectUserManagement_guest.typeFullName(guest_name);
            sleep.wait(time);
            ObjectUserManagement_guest.typePassword(password);
            sleep.wait(time);
            ObjectUserManagement_guest.typeConfirmPassword(password);
            sleep.wait(time);
            ObjectUserManagement_guest.selectGeneraluserRadioLocator(ObjectUserManagement_guest.getgeneraluserRadioLocator());
            sleep.wait(time);
            ObjectUserManagement_guest.clickSaveButtonLocator();
            sleep.wait(time*5);
            LoginPage_guest.clickoperationPage();
            sleep.wait(time*3);
            ScreenShot.takeScreenShot("add_guest_user_operationPage", wdriver);
            sleep.wait(time);
            wdriver.quit();
            //增加test用户
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
            ScreenShot.takeScreenShot("add_test_usermanagementPage", wd);
            ObjectUserManagement ObjectUserManagement_test = new ObjectUserManagement(wd);
            highlight.Element(wd, ObjectUserManagement_test.getnewButtonLocator());
            sleep.wait(time);
            ObjectUserManagement_test.clickNewButton(ObjectUserManagement_test.getnewButtonLocator());
            sleep.wait(time);
            ObjectUserManagement_test.typeUsername(test_name);
            sleep.wait(time);
            ObjectUserManagement_test.typeFullName(test_name);
            sleep.wait(time);
            ObjectUserManagement_test.typePassword(password);
            sleep.wait(time);
            ObjectUserManagement_test.typeConfirmPassword(password);
            sleep.wait(time);
            ObjectUserManagement_test.selectGeneraluserRadioLocator(ObjectUserManagement_test.getgeneraluserRadioLocator());
            sleep.wait(time);
            ObjectUserManagement_test.clickSaveButtonLocator();
            sleep.wait(time*5);
            LoginPage_test.clickoperationPage();
            sleep.wait(time*3);
            ScreenShot.takeScreenShot("add_test_user_operationPage", wd);
            sleep.wait(time);
            wd.quit();         
        }
    }
}