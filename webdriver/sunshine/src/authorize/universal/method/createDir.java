package authorize.universal.method;

import java.io.File;

public class createDir
{

    public static String takecreateDir(String filepath)
    {

        try
        {

            File dirFile = new File(filepath);
            boolean bFile = dirFile.exists();
            if (bFile == true)
            {
                System.out.println("The folder exists.");
            }
            else
            {
                System.out.println("The folder do not exist,now trying to create a one...");
                bFile = dirFile.mkdir();
                if (bFile == true)
                {
                    System.out.println("Create successfully!");
                    // System.out.println("创建文件夹");
                }
                else
                {
                    System.out.println("Disable to make the folder,please check the disk is full or not.");
                    // System.out.println("文件夹创建失败，清确认磁盘没有写保护并且空件足够");
                    // System.exit(1);
                }
            }
        }
        catch(Exception err)
        {
            System.err
                    .println("Create folder is error,because the disk is full or not or the superior folder not exists.");
            err.printStackTrace();
        }
        return filepath;
    }
}