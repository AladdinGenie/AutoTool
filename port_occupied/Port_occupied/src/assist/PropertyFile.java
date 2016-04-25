package assist;

import gui.MyInterface;

import java.io.FileInputStream;
import java.util.Properties;

public class PropertyFile {

	String path = null;
	
	public PropertyFile(String path){		
		this.path = path;
	}

	public String getValue(String key) {
		String value = null;
		try {
			Properties prop = new Properties();	
			FileInputStream fis = new FileInputStream(path);
			prop.load(fis);
			value = prop.getProperty(key);	
			fis.close();
		} catch (Exception e) {			
			MyInterface.log(e.getMessage());	
		}
		return value;
	}	
}