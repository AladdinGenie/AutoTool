package authorize.user.management;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import authorize.universal.method.globalValue;

public class ObjectUserManagement
{
    private final WebDriver driver;

    // The projectmanagement page contains several HTML elements that will be
    // represented as
    // WebElements.
    // The locators for these elements should only be defined once.
    private By newButtonLocator = By.xpath("/html/body/div/div[2]/div/div[1]/div[1]/button[1]");

    private By modifyButtonLocator = By.xpath("/html/body/div/div[2]/div/div[1]/div[1]/button[2]");

    private By delButtonLocator = By.xpath("/html/body/div/div[2]/div/div[1]/div[1]/button[3]");

    private By cancelButtonLocator = By.xpath("/html/body/div[3]/div/div/div/form/fieldset/div[7]/div/button[2]");

    private By saveButtonLocator = By.xpath("/html/body/div[3]/div/div/div/form/fieldset/div[7]/div/button[1]");

    private By usernameLocator = By.cssSelector("#name");

    private By fullNameLocator = By.cssSelector("#fn");

    private By passwordLocator = By.cssSelector("#password");

    private By confirmPasswordLocator = By.cssSelector("#confirmPassword");

    private By generaluserRadioLocator = By.xpath("/html/body/div[3]/div/div/div/form/fieldset/div[5]/div[1]/label[1]");

    private By administratorRadioLocator = By
            .xpath("/html/body/div[3]/div/div/div/form/fieldset/div[5]/div[1]/label[2]");

    public ObjectUserManagement(WebDriver driver)
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

    public By setnewButtonLocator(String newButtonLocator)
    {
        return this.newButtonLocator = By.xpath(newButtonLocator);
    }

    public WebElement getnewButtonLocator()
    {
        return driver.findElement(newButtonLocator);
    }

    public By setmodifyButtonLocator(String modifyButtonLocator)
    {
        return this.modifyButtonLocator = By.xpath(modifyButtonLocator);
    }

    public WebElement getmodifyButtonLocator()
    {
        return driver.findElement(modifyButtonLocator);
    }

    public By setdelButtonLocator(String delButtonLocator)
    {
        return this.delButtonLocator = By.xpath(delButtonLocator);
    }

    public WebElement getdelButtonLocator()
    {
        return driver.findElement(delButtonLocator);
    }

    public By setsaveButtonLocator(String saveButtonLocator)
    {
        return this.saveButtonLocator = By.xpath(saveButtonLocator);
    }

    public WebElement getsaveButtonLocator()
    {
        return driver.findElement(saveButtonLocator);
    }

    public By setcancelButtonLocator(String cancelButtonLocator)
    {
        return this.cancelButtonLocator = By.xpath(cancelButtonLocator);
    }

    public WebElement getcancelButtonLocator()
    {
        return driver.findElement(cancelButtonLocator);
    }

    public WebElement getadministratorradioLocator()
    {
        return driver.findElement(administratorRadioLocator);
    }

    public WebElement getgeneraluserRadioLocator()
    {
        return driver.findElement(generaluserRadioLocator);
    }

    public ObjectUserManagement clickNewButton(WebElement newbutton)
    {
        // This is the only place that "knows" how to click a newbutton
        driver.findElement(newButtonLocator).click();
        return this;
    }

    public ObjectUserManagement clickModifyButton(WebElement modifybutton)
    {
        // This is the only place that "knows" how to click a modifybutton
        driver.findElement(modifyButtonLocator).click();
        return this;
    }

    public ObjectUserManagement clickDelButtonLocator(WebElement delbutton)
    {
        // This is the only place that "knows" how to click a delbutton
        driver.findElement(delButtonLocator).click();
        return this;
    }

    public ObjectUserManagement clickSaveButtonLocator()
    {
        // This is the only place that "knows" how to click a saveButton
        driver.findElement(saveButtonLocator).click();
        return this;
    }

    public ObjectUserManagement clickCancelButtonLocator()
    {
        // This is the only place that "knows" how to click a cancelButton
        driver.findElement(cancelButtonLocator).click();
        return this;
    }

    public ObjectUserManagement clickSaveButtonLocator(String saveButton)
    {
        // This is the only place that "knows" how to click a customize
        // saveButton
        try
        {
            By saveButtonLocator = By.xpath(saveButton);
            driver.findElement(saveButtonLocator).click();
            return this;
        }
        catch(org.openqa.selenium.NoSuchElementException e)
        {
            return this;
        }
    }

    public ObjectUserManagement clickCancelButtonLocator(String cancelButton)
    {
        // This is the only place that "knows" how to click a customize
        // cancelButton
        By cancelButtonLocator = By.xpath(cancelButton);
        driver.findElement(cancelButtonLocator).click();
        return this;
    }

    public ObjectUserManagement typeUsername(String username)
    {
        // This is the only place that "knows" how to enter a username
        driver.findElement(usernameLocator).clear();
        driver.findElement(usernameLocator).sendKeys(username);
        return this;
    }

    public ObjectUserManagement typeFullName(String fullName)
    {
        // This is the only place that "knows" how to enter a fullName
        driver.findElement(fullNameLocator).clear();
        driver.findElement(fullNameLocator).sendKeys(fullName);
        return this;
    }

    public ObjectUserManagement typePassword(String password)
    {
        // This is the only place that "knows" how to enter a password
        driver.findElement(passwordLocator).clear();
        driver.findElement(passwordLocator).sendKeys(password);
        return this;
    }

    public ObjectUserManagement typeConfirmPassword(String confirmPassword)
    {
        // This is the only place that "knows" how to enter a confirmPassword
        driver.findElement(confirmPasswordLocator).clear();
        driver.findElement(confirmPasswordLocator).sendKeys(confirmPassword);
        return this;
    }

    public ObjectUserManagement selectGeneraluserRadioLocator(WebElement generaluserradio)
    {
        // This is the only place that "knows" how to select a generaluserradio
        driver.findElement(generaluserRadioLocator).click();
        return this;
    }

    public ObjectUserManagement selectAdministratorRadioLocator(WebElement administratorradio)
    {
        // This is the only place that "knows" how to select a
        // administratorradio
        driver.findElement(administratorRadioLocator).click();
        return this;
    }

    public ObjectUserManagement clickSelectxlineButtonLocator(String x)
    {
        String selectlineButton = "/html/body/div/div[2]/div/div[2]/div/div[2]/div/div[x]/div[1]/div[2]/div/input";
        String selectxlineButton = selectlineButton.replaceAll("x", x);
        By selectthefirstlineButtonLocator = By.xpath(selectxlineButton);
        // This is the only place that "knows" how to select the firstline
        driver.findElement(selectthefirstlineButtonLocator).click();
        return this;
    }

    public ObjectUserManagement clickSelectxlineLocator(String x, String text)
    {
        String selectlineButton = "/html/body/div/div[2]/div/div[2]/div/div[2]/div/div[x]/div[2]/div[2]/div/span";
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