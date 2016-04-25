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
 * 文件名：modifyproject.java
 * 包名：authorize.testsuite
 * 目的：执行测试用例5. 修改项目
 * 输入参数：typeOrderNo,modifyOrderNo
 * 返回结果：尾部增加zb
 * 注意事项：使用admin_name账号测试
 * 作者：曾昱皓
 * 日期：May 6, 2014 2:31:12 PM
*/
public class modifyproject
{
    public modifyproject(WebDriver driver)
    {
        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public modifyproject() throws FileNotFoundException, IOException, InterruptedException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String login_name = prop.getProperty("admin_name");
        String login_passwd = prop.getProperty("password");
        int count = Integer.parseInt(prop.getProperty("count"));
        int time = Integer.parseInt(prop.getProperty("time"));
        String typeOrderNo = prop.getProperty("typeOrderNo");
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
            ScreenShot.takeScreenShot("modifyproject_projectPage", odriver);
            ObjectProjectManagement ObjectProjectManagement = new ObjectProjectManagement(odriver);
            for (int j = 1; j <= 10; j++)
            {
                ObjectProjectManagement.clickSelectxlineLocator(String.valueOf(j), typeOrderNo);
            }
            sleep.wait(time);
            highlight.Element(odriver, ObjectProjectManagement.getmodifyButtonLocator());
            sleep.wait(time);
            ObjectProjectManagement.clickModifyButton(ObjectProjectManagement.getmodifyButtonLocator());
            sleep.wait(time);
            ObjectProjectManagement.typeNo(modifyOrderNo);
            sleep.wait(time);
            ObjectProjectManagement.typeCustomerFullName(modifyOrderNo);
            sleep.wait(time);
            ObjectProjectManagement.clickSaveButtonLocator("/html/body/div[3]/div/div/div/form/fieldset/div[11]/div/button[1]");
            sleep.wait(time*5);
            LoginPage.clickoperationPage();
            sleep.wait(time*3);
            ScreenShot.takeScreenShot("modifyproject_operationPage", odriver);
            sleep.wait(time);
            odriver.quit();
        }
    }
}