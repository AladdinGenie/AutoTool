package authorize.login;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import authorize.universal.method.globalValue;

public class LoginPage
{
    private final WebDriver driver;

    public LoginPage(WebDriver driver)
    {
        this.driver = driver;
        
        // Check that we're on the right page. 
        if (driver.getTitle().equals("证书错误: 导航已阻止"))
        {       
            System.out.println(driver.getTitle());
            driver.get("javascript:document.getElementById('overridelink').click();");
        }
        
        if (!globalValue.title.equals(driver.getTitle()))
        {
            // // Alternatively, we could navigate to the login page, perhaps
            // logging out first
            throw new IllegalStateException("This is not the login page");
        }
    }

    // The login page contains several HTML elements that will be represented as
    // WebElements.
    // The locators for these elements should only be defined once.
    public By usernameLocator = By.name("name");

    public By passwordLocator = By.name("password");

    public By loginButtonLocator = By
            .cssSelector("#loginModal > div > div > div.modal-body > form > div:nth-child(4) > button");

    public By usermanagementPage = By.cssSelector("#navbar-main > ul:nth-child(1) > li.active > a");

    public By projectPage = By.cssSelector("#navbar-main > ul:nth-child(1) > li:nth-child(2) > a");

    public By operationPage = By.cssSelector("#navbar-main > ul:nth-child(1) > li:nth-child(3) > a");

    public By setusernameLocator(String usernameLocator)
    {
        return this.usernameLocator = By.xpath(usernameLocator);
    }

    public WebElement getusernameLocator()
    {
        return driver.findElement(usernameLocator);
    }

    public By setpasswordLocator(String passwordLocator)
    {
        return this.passwordLocator = By.xpath(passwordLocator);
    }

    public WebElement getpasswordLocator()
    {
        return driver.findElement(passwordLocator);
    }

    public By setloginButtonLocator(String loginButtonLocator)
    {
        return this.loginButtonLocator = By.xpath(loginButtonLocator);
    }

    public WebElement getloginButtonLocator()
    {
        return driver.findElement(loginButtonLocator);
    }

    public LoginPage typeUsername(String username)
    {
        // This is the only place that "knows" how to enter a username
        driver.findElement(usernameLocator).clear();
        driver.findElement(usernameLocator).sendKeys(username);
        return this;
    }

    // The login page allows the user to type their password into the password
    // field
    public LoginPage typePassword(String password)
    {
        // This is the only place that "knows" how to enter a password
        driver.findElement(passwordLocator).clear();
        driver.findElement(passwordLocator).sendKeys(password);
        return this;
    }

    public LoginPage clickLogin()
    {
        // This is the only place that "knows" how to click a loginButton
        driver.findElement(loginButtonLocator).click();
        return new LoginPage(driver);
    }

    public LoginPage clickusermanagementPage()
    {
        // This is the only place that "knows" how to click a usermanagementPage
        driver.findElement(usermanagementPage).click();
        return this;
    }

    public LoginPage clickprojectPage()
    {
        // This is the only place that "knows" how to click a projectPage
        driver.findElement(projectPage).click();
        return this;
    }

    public LoginPage clickoperationPage()
    {
        // This is the only place that "knows" how to click a operationPage
        driver.findElement(operationPage).click();
        return this;
    }

}