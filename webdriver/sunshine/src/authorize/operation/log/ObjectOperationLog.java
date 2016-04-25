package authorize.operation.log;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import authorize.universal.method.globalValue;

public class ObjectOperationLog
{
    private final WebDriver driver;
    
    public ObjectOperationLog(WebDriver driver)
    {
        this.driver = driver;

        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public ObjectOperationLog clickSelectxlineButtonLocator(String x)
    {
        String selectlineButton = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[x]/div[5]/div[2]/div/span";
        String selectxlineButton = selectlineButton.replaceAll("x", x);
        By selectthefirstlineButtonLocator = By.xpath(selectxlineButton);
        // This is the only place that "knows" how to select the firstline
        driver.findElement(selectthefirstlineButtonLocator).click();
        return this;
    }

    public ObjectOperationLog clickSelectxlineLocator(String x, String text)
    {
        String selectlineButton = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[x]/div[5]/div[2]/div/span";
        String selectxlineButton = selectlineButton.replaceAll("x", x);
        By selectthefirstlineButtonLocator = By.xpath(selectxlineButton);
        // This is the only place that "knows" how to select contains the text
        // of the line
        try
        {
            String assertText = driver.findElement(selectthefirstlineButtonLocator).getText();
            if (assertText.equals(text))
            {
                System.out.println(assertText);
                driver.findElement(selectthefirstlineButtonLocator).click();
            }
            return this;
        }
        catch(org.openqa.selenium.NoSuchElementException e)
        {
            return this;

        }
    }
}