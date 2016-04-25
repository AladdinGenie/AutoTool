package authorize.universal.method;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;

public class WaitForSomthing
{

    /**
     * 
     * @author gongjf
     */

    public static void main(String[] args)
    {

        System.setProperty("webdriver.chrome.driver", "Driver\\chromedriver.exe");
        WebDriver dr = new ChromeDriver();

        String url = "file:///C:/Users/Administrator/Desktop/Wait.html";

        dr.get(url);

/*        WebDriverWait wait = new WebDriverWait(dr, 10);

        wait.until(new ExpectedCondition<WebElement>()
        {

            public WebElement apply(WebDriver d)
            {

                return d.findElement(By.id("b"));

            }
        }).click();
        dr.findElement(By.id("b")).click();

        wait.until(new ExpectedCondition<WebElement>()
                {

                    public WebElement apply(WebDriver d)
                    {

                        return d.findElement(By.cssSelector("body > div"));

                    }
                });
        
        WebElement element = dr.findElement(By.cssSelector("body > div"));

        ((JavascriptExecutor) dr).executeScript("arguments[0].style.border= \"5px solid yellow\"", element);*/
        dr.manage().timeouts().implicitlyWait(5,TimeUnit.SECONDS);
        dr.findElement(By.id("b")).click();

        WebElement element = dr.findElement(By.cssSelector(".red_box"));

        ((JavascriptExecutor)dr).executeScript("arguments[0].style.border= \"5px solid yellow\"",element); 

        long startTime = System.currentTimeMillis();
        sleep.wait(10000);

        long endTime = System.currentTimeMillis(); // 获取结束时间
        System.out.println("程序运行时间： " + (endTime - startTime) / 1000 + "s");
        dr.quit();
    }

}
