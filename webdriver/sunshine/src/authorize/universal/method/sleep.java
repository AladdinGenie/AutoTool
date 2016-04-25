package authorize.universal.method;

public class sleep
{
    public static void wait(int time)
    {
        try
        {
            Thread.sleep(time);
        }
        catch(InterruptedException e)
        {
            e.printStackTrace();
        }
        
    }
}