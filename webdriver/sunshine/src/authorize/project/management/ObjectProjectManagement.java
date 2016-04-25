package authorize.project.management;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import authorize.universal.method.globalValue;

public class ObjectProjectManagement
{
    private final WebDriver driver;

    // The projectmanagement page contains several HTML elements that will be represented as
    // WebElements.
    // The locators for these elements should only be defined once.
    private By newButtonLocator = By.xpath("/html/body/div/div[2]/div/div[1]/div[1]/button[1]");

    private By modifyButtonLocator = By.xpath("/html/body/div/div[2]/div/div[1]/div[1]/button[2]");

    private By delButtonLocator = By.xpath("/html/body/div/div[2]/div/div[1]/div[1]/button[3]");

    private By licButtonLocator = By.xpath("/html/body/div/div[2]/div/div[1]/div[1]/button[4]");

    private By noLocator = By.cssSelector("#no");

    private By customerFullNameLocator = By.cssSelector("#customer");

    private By orderNoLocator = By.cssSelector("#order");

    private By passwordLocator = By.cssSelector("#password");

    private By confirmPasswordLocator = By.cssSelector("#confirmPassword");

    private By professionRadioLocator = By.xpath("/html/body/div[3]/div/div/div/form/fieldset/div[7]/div[1]/label[1]");

    private By irrigationRadioLocator = By.xpath("/html/body/div[3]/div/div/div/form/fieldset/div[7]/div[1]/label[2]");

    private By overseasLocator = By.xpath("/html/body/div[3]/div/div/div/form/fieldset/div[7]/div[1]/label[3]");

    private By countLocator = By.cssSelector("#boxcount");

    private By salesmanLocator = By.cssSelector("#salesman");

    private By cancelButtonLocator = By.xpath("/html/body/div[3]/div/div/div/form/fieldset/div[11]/div/button[2]");

    private By saveButtonLocator = By.xpath("/html/body/div[3]/div/div/div/form/fieldset/div[11]/div/button[1]");

    public ObjectProjectManagement(WebDriver driver)
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

    public By setlicButtonLocator(String licButtonLocator)
    {
        return this.delButtonLocator = By.xpath(licButtonLocator);
    }

    public WebElement getlicButtonLocator()
    {
        return driver.findElement(licButtonLocator);
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

    public WebElement getirrigationRadioLocator()
    {
        return driver.findElement(irrigationRadioLocator);
    }

    public WebElement getprofessionRadioLocator()
    {
        return driver.findElement(professionRadioLocator);
    }

    public ObjectProjectManagement clickNewButton(WebElement newbutton)
    {
     // This is the only place that "knows" how to click a newbutton
        driver.findElement(newButtonLocator).click();
        return this;
    }

    public ObjectProjectManagement clickModifyButton(WebElement modifybutton)
    {
        // This is the only place that "knows" how to click a modifybutton
        driver.findElement(modifyButtonLocator).click();
        return this;
    }

    public ObjectProjectManagement clickDelButtonLocator(WebElement delbutton)
    {
        // This is the only place that "knows" how to click a delbutton
        driver.findElement(delButtonLocator).click();
        return this;
    }

    public ObjectProjectManagement clicklicButtonLocator(WebElement licbutton)
    {
        // This is the only place that "knows" how to click a licbutton
        driver.findElement(licButtonLocator).click();
        return this;
    }

    public ObjectProjectManagement typeNo(String no)
    {
        // This is the only place that "knows" how to enter a no
        driver.findElement(noLocator).clear();
        driver.findElement(noLocator).sendKeys(no);
        return this;
    }

    public ObjectProjectManagement typeCustomerFullName(String customerFullName)
    {
        // This is the only place that "knows" how to enter a customerFullName
        driver.findElement(customerFullNameLocator).clear();
        driver.findElement(customerFullNameLocator).sendKeys(customerFullName);
        return this;
    }

    public ObjectProjectManagement typeOrderNo(String orderNo)
    {
        // This is the only place that "knows" how to enter a orderNo
        driver.findElement(orderNoLocator).clear();
        driver.findElement(orderNoLocator).sendKeys(orderNo);
        return this;
    }

    public ObjectProjectManagement typePassword(String password)
    {
        // This is the only place that "knows" how to enter a password
        driver.findElement(passwordLocator).clear();
        driver.findElement(passwordLocator).sendKeys(password);
        return this;
    }

    public ObjectProjectManagement typeConfirmPassword(String confirmPassword)
    {
        // This is the only place that "knows" how to enter a confirmPassword
        driver.findElement(confirmPasswordLocator).clear();
        driver.findElement(confirmPasswordLocator).sendKeys(confirmPassword);
        return this;
    }

    public ObjectProjectManagement typeCount(String count)
    {
        // This is the only place that "knows" how to enter a count
        driver.findElement(countLocator).clear();
        driver.findElement(countLocator).sendKeys(count);
        return this;
    }

    public ObjectProjectManagement typeSalesman(String salesman)
    {
        // This is the only place that "knows" how to enter a salesman
        driver.findElement(salesmanLocator).clear();
        driver.findElement(salesmanLocator).sendKeys(salesman);
        return this;
    }


    public ObjectProjectManagement clickSaveButtonLocator()
    {
        // This is the only place that "knows" how to click a saveButton
        driver.findElement(saveButtonLocator).click();
        return this;
    }

    public ObjectProjectManagement clickCancelButtonLocator()
    {
        // This is the only place that "knows" how to click a cancelButton
        driver.findElement(cancelButtonLocator).click();
        return this;
    }

    public ObjectProjectManagement clickSaveButtonLocator(String saveButton)
    {
        // This is the only place that "knows" how to click a customize saveButton
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

    public ObjectProjectManagement clickCancelButtonLocator(String cancelButton)
    {
        // This is the only place that "knows" how to click a customize cancelButton
        By cancelButtonLocator = By.xpath(cancelButton);
        driver.findElement(cancelButtonLocator).click();
        return this;
    }

    public ObjectProjectManagement selectprofessionRadioLocator()
    {
        // This is the only place that "knows" how to select a professionRadio
        driver.findElement(professionRadioLocator).click();
        return this;
    }

    public ObjectProjectManagement selectIrrigationRadioLocator()
    {
        // This is the only place that "knows" how to select a IrrigationRadio
        driver.findElement(irrigationRadioLocator).click();
        return this;
    }

    public ObjectProjectManagement selectoverseasRadioLocator()
    {
        // This is the only place that "knows" how to select a overseasRadio
        driver.findElement(overseasLocator).click();
        return this;
    }

    public ObjectProjectManagement clickSelectxlineButtonLocator(String x)
    {
        String selectlineButton = "/html/body/div/div[2]/div/div[2]/div/div[2]/div/div[x]/div[1]/div[2]/div/input";
        String selectxlineButton = selectlineButton.replaceAll("x", x);
        By selectthefirstlineButtonLocator = By.xpath(selectxlineButton);
        // This is the only place that "knows" how to select the firstline
        driver.findElement(selectthefirstlineButtonLocator).click();
        return this;
    }

    public ObjectProjectManagement clickSelectxlineLocator(String x, String text)
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