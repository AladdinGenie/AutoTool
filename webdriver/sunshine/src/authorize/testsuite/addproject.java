package authorize.testsuite;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

import org.openqa.selenium.WebDriver;

import authorize.login.LoginPage;
import authorize.project.management.ObjectProjectManagement;
import authorize.universal.method.ScreenShot;
import authorize.universal.method.globalValue;
import authorize.universal.method.highlight;
import authorize.universal.method.openBrowser;
import authorize.universal.method.sleep;

/*
 * 文件名：addproject.java
 * 包名：authorize.testsuite
 * 目的：执行测试用例4. 新增项目
 * 输入参数：typOrderNo,count
 * 返回结果：
 * 注意事项：使用admin_name账号测试
 * 作者：曾昱皓
 * 日期：May 6, 2014 2:04:46 PM
 */
public class addproject
{
    public addproject(WebDriver driver)
    {
        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public addproject() throws FileNotFoundException, IOException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String login_name = prop.getProperty("admin_name");
        String login_passwd = prop.getProperty("password");
        int count = Integer.parseInt(prop.getProperty("count"));
        int time = Integer.parseInt(prop.getProperty("time"));
        String typeOrderNo = prop.getProperty("typeOrderNo");

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
            LoginPage.clickprojectPage();
            sleep.wait(time);
            ScreenShot.takeScreenShot("addproject_projectPage", odriver);
            ObjectProjectManagement ObjectProjectManagement = new ObjectProjectManagement(odriver);
            highlight.Element(odriver, ObjectProjectManagement.getnewButtonLocator());
            sleep.wait(time);
            ObjectProjectManagement.clickNewButton(ObjectProjectManagement.getnewButtonLocator());
            sleep.wait(time);
            ObjectProjectManagement.typeNo(typeOrderNo);
            sleep.wait(time);
            ObjectProjectManagement.typeCustomerFullName(typeOrderNo);
            sleep.wait(time);
            ObjectProjectManagement.typeOrderNo(typeOrderNo);
            sleep.wait(time);
            ObjectProjectManagement.typePassword(login_passwd);
            sleep.wait(time);
            ObjectProjectManagement.typeConfirmPassword(login_passwd);
            sleep.wait(time);
            ObjectProjectManagement.selectprofessionRadioLocator();
            sleep.wait(time);
            ObjectProjectManagement.typeCount(String.valueOf(count));
            sleep.wait(time);
            ObjectProjectManagement.typeSalesman(typeOrderNo);
            sleep.wait(time);
            ObjectProjectManagement.clickSaveButtonLocator();
            sleep.wait(time * 5);
            LoginPage.clickoperationPage();
            sleep.wait(time * 3);
            ScreenShot.takeScreenShot("addproject_operationPage", odriver);
            sleep.wait(time);
            odriver.quit();
        }
    }
}