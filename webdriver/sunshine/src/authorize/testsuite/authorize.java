package authorize.testsuite;

import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Row;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import authorize.getproject.ObjectGetProject;
import authorize.login.LoginPage;
import authorize.project.management.ObjectProjectManagement;
import authorize.universal.method.ScreenShot;
import authorize.universal.method.highlight;
import authorize.universal.method.openBrowser;
import authorize.universal.method.sleep;

/*
 * 文件名：authorize.java
 * 包名：authorize.testsuite
 * 目的：申请授权流程请求并发场景测试
 * 输入参数：data.xls
 * 返回结果：
 * 注意事项：运行start_desEntrypt.bat生成data.xls
 * 作者：曾昱皓
 * 日期：May 6, 2014 2:14:04 PM
 */
public class authorize
{
    public static void addproject() throws Exception
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String login_name = prop.getProperty("admin_name");
        String login_passwd = prop.getProperty("password");
        int time = Integer.parseInt(prop.getProperty("time"));
        String typeOrderNo = prop.getProperty("typeOrderNo");
        String inputdir = prop.getProperty("inputdir");
        List<String> dataList = authorize.getValue(inputdir);
        String typeCountNo = String.valueOf(dataList.size());
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
        ObjectProjectManagement.selectoverseasRadioLocator();
        sleep.wait(time);
        ObjectProjectManagement.typeCount(typeCountNo);
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

    public static void delproject() throws Exception
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String login_name = prop.getProperty("admin_name");
        String login_passwd = prop.getProperty("password");
        int time = Integer.parseInt(prop.getProperty("time"));
        String typeOrderNo = prop.getProperty("typeOrderNo");
        int lineNo = 10;

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
        ObjectProjectManagement ObjectProjectManagement = new ObjectProjectManagement(odriver);
        for (int i = 1; i <= lineNo; i++)
        {
            ObjectProjectManagement.clickSelectxlineLocator(String.valueOf(i), typeOrderNo);
        }
        sleep.wait(time);
        highlight.Element(odriver, ObjectProjectManagement.getdelButtonLocator());
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

    public static List<String> getValue(String outDir) throws Exception
    {
        FileInputStream file = new FileInputStream(new File(outDir));
        HSSFWorkbook wb = new HSSFWorkbook(file);// 建立新HSSFWorkbook对象
        HSSFSheet sheet = wb.getSheetAt(0);// 建立新的sheet对象
        int rows = sheet.getPhysicalNumberOfRows(); // 获取总行数
        List<String> dataList = new ArrayList<String>();
        for (int i = 0; i < rows; i++)
        {
            Row row = sheet.getRow(i);
            String entryptData = row.getCell(0).getRichStringCellValue().toString();
            dataList.add(entryptData);
        }
        return dataList;
    }

    public static void main(String[] args) throws Exception
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String typeOrderNo = prop.getProperty("typeOrderNo");
        int time = Integer.parseInt(prop.getProperty("time"));
        String password = prop.getProperty("password");
        authorize.delproject();
        authorize.addproject();
        List<String> dataList = authorize.getValue("data.xls");
        for (int i = 0; i < dataList.size(); i++)
        {
            String url = dataList.get(i);
            WebDriver odriver = new openBrowser().run("checkin?param=" + url);
            sleep.wait(time);
            System.out.println("authorize" + " 第" + String.valueOf(i + 1) + "次" + " starting...");
            odriver.manage().window().maximize();
            sleep.wait(time);
            ObjectGetProject ObjectGetProject = new ObjectGetProject(odriver);
            sleep.wait(time);
            ObjectGetProject.typeOrderNo(typeOrderNo);
            sleep.wait(time);
            ObjectGetProject.typePassword(password);
            sleep.wait(time);
            ObjectGetProject.clickConfirmButtonLocator();
            sleep.wait(time);
            String assertText = odriver.findElement(
                    By.cssSelector("body > div > div.box.ng-scope > div:nth-child(2) > h4")).getText();
            String selectxlineButton = "授权单orderno：总点数total，已使用点数i，剩余点数spare";
            int total = dataList.size();
            int used = i + 1;
            int spare = total - used;
            String orderno = selectxlineButton.replaceAll("orderno", typeOrderNo);
            String totalcount = orderno.replaceAll("total", String.valueOf(total));
            String usedcount = totalcount.replaceAll("i", String.valueOf(used));
            String sparecount = usedcount.replaceAll("spare", String.valueOf(spare));
            if (assertText.equals(sparecount))
            {
                System.out.println(assertText);
                String text = "第" + String.valueOf(i + 1) + "次";
                ScreenShot.takeScreenShot(text, odriver);
            }
            else
            {
                System.out.println("第" + String.valueOf(i + 1) + "次" + " Failed..");
            }
            sleep.wait(time);
            odriver.quit();
        }
        System.out.println("authorize testing finished...");
    }
}