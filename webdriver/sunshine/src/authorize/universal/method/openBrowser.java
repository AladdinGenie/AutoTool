package authorize.universal.method;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;

public class openBrowser
{
    public WebDriver run() throws FileNotFoundException, IOException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String ip = prop.getProperty("ip");
        String port = prop.getProperty("port");
        String browser = prop.getProperty("browser");
        String pathToFirefox = prop.getProperty("pathToFirefox");
        Map<String, Integer> map = new HashMap<String, Integer>();
        map.put("ie", 1);
        map.put("firefox", 2);
        map.put("chrome", 3);
        WebDriver odriver = null;

        // 配置服务器
        switch (map.get(browser))
        {
        case 1:
            System.out.println("ie");
            System.setProperty("webdriver.ie.driver", "Driver\\IEDriverServer.exe");
            DesiredCapabilities capabilities_ie = new DesiredCapabilities();
            capabilities_ie.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true);
            odriver = new InternetExplorerDriver(capabilities_ie);
            break;

        case 2:
            System.out.println("firefox");
            System.setProperty("webdriver.firefox.bin", pathToFirefox);
            // No need of custom profiles to deal with "Untrusted connection" on WebDriver
            DesiredCapabilities capabilities = new DesiredCapabilities();
            capabilities.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true);
            odriver = new FirefoxDriver(capabilities);

            break;
        case 3:
            System.out.println("chrome");
            System.setProperty("webdriver.chrome.driver", "Driver\\chromedriver.exe");
            DesiredCapabilities capabilities_chrome = new DesiredCapabilities();
            capabilities_chrome.setCapability(CapabilityType.ACCEPT_SSL_CERTS, true);
            odriver = new ChromeDriver(capabilities_chrome);
            break;
        default:
            System.out.println("browser value is wrong!");
            odriver = null;
            break;
        }

        // 访问google
        odriver.get("https://" + ip + ":" + port);
        return odriver;
    }

    public WebDriver run(String url) throws FileNotFoundException, IOException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        String ip = prop.getProperty("ip");
        String port = prop.getProperty("port");
        String browser = prop.getProperty("browser");
        String pathToFirefox = prop.getProperty("pathToFirefox");
        Map<String, Integer> map = new HashMap<String, Integer>();
        map.put("ie", 1);
        map.put("firefox", 2);
        map.put("chrome", 3);
        WebDriver odriver = null;

        // 配置服务器
        switch (map.get(browser))
        {
        case 1:
            System.out.println("ie");
            System.setProperty("webdriver.ie.driver", "Driver\\IEDriverServer.exe");
            odriver = new InternetExplorerDriver();
            break;

        case 2:
            System.out.println("firefox");
            System.setProperty("webdriver.firefox.bin", pathToFirefox);
            odriver = new FirefoxDriver();
            break;
        case 3:
            System.out.println("chrome");
            System.setProperty("webdriver.chrome.driver", "Driver\\chromedriver.exe");
            odriver = new ChromeDriver();
            break;
        default:
            System.out.println("browser value is wrong!");
            odriver = null;
            break;
        }

        // 访问google
        odriver.get("https://" + ip + ":" + port + "/" + url);
        return odriver;
    }
}