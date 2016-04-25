package authorize.universal.method;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class highlight
{
    public static void Element(WebDriver wdriver, WebElement welement)
    {
        //隐式等待
        if (welement.isDisplayed() == false) {
            wdriver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        } 
        JavascriptExecutor js = (JavascriptExecutor) wdriver;
        js.executeScript("element = arguments[0];" + "original_style = element.getAttribute('style');"
                + "element.setAttribute('style', original_style + \";"
                + "background: yellow; border: 2px solid red;\");"
                + "setTimeout(function(){element.setAttribute('style', original_style);}, 1000);", welement);
    }
}