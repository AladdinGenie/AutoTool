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
 * 文件名：delproject.java
 * 包名：authorize.testsuite
 * 目的：执行测试用例6. 删除项目
 * 输入参数：modifyOrderNo
 * 返回结果：
 * 注意事项：使用admin_name账号测试
 * 作者：曾昱皓
 * 日期：May 6, 2014 2:20:39 PM
*/
public class delproject
{
    public delproject(WebDriver driver)
    {
        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public delproject() throws FileNotFoundException, IOException, InterruptedException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String login_name = prop.getProperty("admin_name");
        String login_passwd = prop.getProperty("password");
        int count = Integer.parseInt(prop.getProperty("count"));
        int time = Integer.parseInt(prop.getProperty("time"));
        String modifyOrderNo = prop.getProperty("modifyOrderNo");

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
            ScreenShot.takeScreenShot("delproject_projectPage", odriver);
            ObjectProjectManagement ObjectProjectManagement = new ObjectProjectManagement(odriver);
            for (int j = 1; j <= 10; j++)
            {
                ObjectProjectManagement.clickSelectxlineLocator(String.valueOf(j), modifyOrderNo);
            }
            sleep.wait(time);
            highlight.Element(odriver,ObjectProjectManagement.getdelButtonLocator());
            sleep.wait(time);
            ObjectProjectManagement.clickDelButtonLocator(ObjectProjectManagement.getdelButtonLocator());
            sleep.wait(time);
            ObjectProjectManagement.clickSaveButtonLocator("/html/body/div[2]/div/div/div[2]/button[2]");
            sleep.wait(time * 5);
            LoginPage.clickoperationPage();
            sleep.wait(time * 3);
            ScreenShot.takeScreenShot("delproject_operationPage", odriver);
            sleep.wait(time);
            odriver.quit();
        }
    }
}