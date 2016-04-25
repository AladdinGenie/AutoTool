package authorization.Application.testsuite;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

/*
 * 文件名：testsuite_test.java
 * 包名：authorization.Application.testsuite
 * 目的：测试申请授权基本流程
 * 输入参数：
 * 返回结果：
 * 注意事项：
 * 作者：曾昱皓
 * 日期：May 6, 2014 5:18:43 PM
*/
public class testsuite_test
{
    public static void main(String[] args) throws FileNotFoundException, IOException
    {
        Properties prop = new Properties();
        prop.load(new FileInputStream("config.properties"));
        int count = Integer.parseInt(prop.getProperty("count"));
        // 配置服务器
        for (int i = 1; i <= count; i++)
        {
            long startTime = System.currentTimeMillis();
            testsuite_1 testsuite_1 = new testsuite_1();
            testsuite_2 testsuite_2 = new testsuite_2();
            testsuite_3 testsuite_3 = new testsuite_3();
            testsuite_4 testsuite_4 = new testsuite_4();
            testsuite_5 testsuite_5 = new testsuite_5();
            testsuite_6 testsuite_6 = new testsuite_6();
            testsuite_7 testsuite_7 = new testsuite_7();
            testsuite_8 testsuite_8 = new testsuite_8();
            int result = 0;
            result += 1;
            System.out.println("Test counts: " + result);
            long endTime = System.currentTimeMillis(); // 获取结束时间
            System.out.println("程序运行时间： " + (endTime - startTime) / 1000 + "s");
        }
    }
}