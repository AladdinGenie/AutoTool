package authorize.testsuite;

import java.io.FileInputStream;
import java.util.Properties;

/*
 * 文件名：test.java
 * 包名：authorize.testsuite
 * 目的：测试授权平台基本流程
 * 输入参数：
 * 返回结果：
 * 注意事项：
 * 作者：曾昱皓
 * 日期：May 6, 2014 2:39:50 PM
 */
public class test
{

    public static void main(String[] args) throws Exception
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        int count = Integer.parseInt(prop.getProperty("count"));
        // 配置服务器
        for (int i = 1; i <= count; i++)
        {
            long startTime = System.currentTimeMillis();
            adduser adduser = new adduser();
            addproject addproject = new addproject();
            modifyuser modifyuser = new modifyuser();
            modifyproject modifyproject = new modifyproject();
            delproject delproject = new delproject();
            deluser deluser = new deluser();
            int result = 0;
            result += 1;
            System.out.println("Test counts: " + result);
            long endTime = System.currentTimeMillis(); // 获取结束时间
            System.out.println("程序运行时间： " + (endTime - startTime) / 1000 + "s");
        }
    }
}