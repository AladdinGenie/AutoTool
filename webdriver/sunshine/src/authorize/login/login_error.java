package authorize.login;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;

public class login_error {
	public static void highlightElement(WebDriver wdriver, WebElement welement) {

		JavascriptExecutor js = (JavascriptExecutor) wdriver;
		js.executeScript(
				"element = arguments[0];"
						+ "original_style = element.getAttribute('style');"
						+ "element.setAttribute('style', original_style + \";"
						+ "background: yellow; border: 2px solid red;\");"
						+ "setTimeout(function(){element.setAttribute('style', original_style);}, 1000);",
				welement);
	}

	public static void main(String[] args) throws FileNotFoundException,
			IOException {

		long startTime = System.currentTimeMillis();
		// System.out.println("程序运行时间： "+startTime+"ms");
		Properties prop = new Properties();

		prop.load(new FileInputStream("config.properties"));

		String ip = prop.getProperty("ip");
		String port = prop.getProperty("port");
		String login_name = prop.getProperty("name");
		String login_passwd = prop.getProperty("password");
		int count = Integer.parseInt(prop.getProperty("count"));
		String browser = prop.getProperty("browser");
		String pathToFirefox = prop.getProperty("pathToFirefox");
		int time = Integer.parseInt(prop.getProperty("time"));
		Map<String, Integer> map = new HashMap<String, Integer>();
		map.put("ie", 1);
		map.put("firefox", 2);
		map.put("chrome", 3);
		WebDriver driver = null;

		// 配置服务器
		int result = 0;
		for (int i = 1; i <= count; i++) {
			switch (map.get(browser)) {
			case 1:
				System.out.println("ie");
				System.setProperty("webdriver.ie.driver",
						"Driver\\IEDriverServer.exe");
				driver = new InternetExplorerDriver();
				break;

			case 2:
				System.out.println("firefox");
				System.setProperty("webdriver.firefox.bin", pathToFirefox);
				driver = new FirefoxDriver();
				break;
			case 3:
				System.out.println("chrome");
				System.setProperty("webdriver.chrome.driver",
						"Driver\\chromedriver.exe");
				driver = new ChromeDriver();
				break;
			default:
				System.out.println("browser value is wrong!");
				driver = null;
				break;
			}

			// 访问google
			driver.get("https://"
					+ ip
					+ ":"
					+ port
					+ "/checkin?param=538598d514983zb5d14d59356bbfe6a52c04b104e1d22cfcb7f409f04f3855b83cef4ab21d1c44aec");

			// 为了看效果，我们等待3S钟
			try {
				Thread.sleep(time);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			System.out.println("Page title is: " + driver.getTitle());
			// 找到文本框
			WebElement name = driver.findElement(By.name("name"));
			highlightElement(driver, name);

			try {
				Thread.sleep(time);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			// 输入搜索关键字
			name.sendKeys(login_name);
			WebElement password = driver.findElement(By.name("password"));
			highlightElement(driver, password);

			try {
				Thread.sleep(time);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			// 输入搜索关键字
			password.sendKeys(login_passwd);
			// 提交表单 WebDriver会自动从表单中查找提交按钮并提交
			name.submit();
			// 检查页面title

			try {
				Thread.sleep(time);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			// 找到文本框
			WebElement project_name = driver.findElement(By.name("name"));
			// 输入搜索关键字
			highlightElement(driver, project_name);
			try {
				Thread.sleep(time);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			project_name.sendKeys(login_name);
			WebElement project_password = driver.findElement(By
					.name("password"));
			highlightElement(driver, project_password);
			// 输入搜索关键字

			try {
				Thread.sleep(time);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			project_password.sendKeys(login_passwd);
			// 提交表单 WebDriver会自动从表单中查找提交按钮并提交
			WebElement submit_button = driver
					.findElement(By
							.xpath("/html/body/div/div[2]/div/div/div/div[2]/form/div[5]/button"));
			submit_button.click();

			// 显示查询结果title
			System.out.println("Page title is: " + driver.getTitle());
			result += 1;
			System.out.println("login counts: " + result);
			try {
				Thread.sleep(time);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			// 关闭浏览器
			driver.quit();
		}
		long endTime = System.currentTimeMillis(); // 获取结束时间
		// System.out.println("程序运行时间： "+endTime+"ms");
		System.out.println("程序运行时间： " + (endTime - startTime) / 1000 + "s");
	}
}