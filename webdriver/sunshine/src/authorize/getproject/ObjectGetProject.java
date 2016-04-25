package authorize.getproject;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import authorize.universal.method.globalValue;

public class ObjectGetProject
{
    private final WebDriver driver;
    // The getproject page contains several HTML elements that will be represented as
    // WebElements.
    // The locators for these elements should only be defined once.

    private By orderNoLocator = By
            .cssSelector("#loginModal > div > div > div.modal-body > form > div:nth-child(1) > input");

    private By passwordLocator = By
            .cssSelector("#loginModal > div > div > div.modal-body > form > div:nth-child(2) > input");

    private By confirmButtonLocator = By
            .cssSelector("#loginModal > div > div > div.modal-body > form > div:nth-child(4) > button");

    public ObjectGetProject(WebDriver driver)
    {
        this.driver = driver;
        
        if (driver.getTitle().equals("证书错误: 导航已阻止"))
        {       
            System.out.println(driver.getTitle());
            driver.get("javascript:document.getElementById('overridelink').click();");
        }

        // Check that we're on the right page.
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    public ObjectGetProject typeOrderNo(String orderNo)
    {
        // This is the only place that "knows" how to enter a orderNo
        driver.findElement(orderNoLocator).sendKeys(orderNo);
        return this;
    }

    public ObjectGetProject typePassword(String password)
    {
        // This is the only place that "knows" how to enter a password
        driver.findElement(passwordLocator).clear();
        driver.findElement(passwordLocator).sendKeys(password);
        return this;
    }

    public ObjectGetProject clickConfirmButtonLocator()
    {
        // This is the only place that "knows" how to click a confirmButton
        driver.findElement(confirmButtonLocator).click();
        return this;
    }

}