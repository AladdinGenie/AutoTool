package gui;

import java.awt.Component;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.ArrayList;

import javax.swing.UIManager;

import assist.PropertyFile;
import main.PortHolder;

public class MyInterface extends Interface {
	
	private static final long serialVersionUID = 1L;
	private static PortHolder[] holders  = null;	
	private String config = "config.ini";
	private String KEY_PORT_START = "port_start";	
	private String KEY_PORT_END = "port_end";
	private String KEY_DISORDER_COUNT = "disorder_count";
	private PropertyFile prop = new PropertyFile(config);

	/**
	 * Disable控制输入，Enable停止
	 * */
	public void disable(){
		jButton1.setEnabled(false);
		jButton2.setEnabled(true);
		jButton3.setEnabled(false);
	}

	/**
	 * Enable控件输入，Disable停止
	 */
	public void enable(){
		jButton1.setEnabled(true);
		jButton2.setEnabled(false);
		jButton3.setEnabled(true);
	}
	
	/**
	 * 初始化端口值
	 * */
	private ArrayList<Integer> initConfig() {		
		
		ArrayList<Integer> portsArray = new ArrayList<Integer>();
		
		String start, end;
		/*有序端口*/
		start = prop.getValue(KEY_PORT_START);
		end = prop.getValue(KEY_PORT_END);
		if(!start.equals("")&& !end.equals("")){
			int portstart  = Integer.parseInt(start);
			int portend = Integer.parseInt(end);
			for(int i=portstart; i<=portend; i++){
				portsArray.add(i);
			}			
		}				
		
		/*无序端口*/
		String value= "";
		
		int disorder_count = Integer.parseInt(prop.getValue(KEY_DISORDER_COUNT));
		for(int i=1; i<=disorder_count; i++){
			value = prop.getValue( "port_"+i ).trim();			
			if(!value.equals("")){
				portsArray.add(Integer.parseInt(value));
			}			
		}	
		
		return portsArray;
	}
	
	
	/**
	 * 日志打印到面板
	 * */
	public static void log(String msg){
		jTextArea1.append(msg+"\n");
	}
	
	public MyInterface(){		
		
		enable(); // 使能控件
		
		/*开始按钮*/
		jButton1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				ArrayList<Integer> portsArray = initConfig(); //初始化端口数据，从配置文件读
				
				/*Disable 其他控件*/
				disable();			
				
				
				holders = new PortHolder[portsArray.size()];
				
				/*根据起始端口，开启线程，占用端口*/
				for(int i=0; i<portsArray.size(); i++){					
					holders[i] = new PortHolder();
					holders[i].setPort(portsArray.get(i));
					holders[i].start();
					log("监听端口"+portsArray.get(i));
				}
				log("********************  完成监听端口   ********************");
			}			
		});
		
		
		
		/*结束按钮*/
		jButton2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				/*根据起始端口号、终止端口号，开启线程，释放端口*/
				for(int i=0; i<holders.length; i++){					
					holders[i].terminal();
					log("释放端口"+holders[i].getPort());
				}				
				log("********************  完成释放端口  ********************");
				holders = null;				
				/*Enable 其他控件*/
				enable();
			}
		});
		
		/*清除日志按钮*/
		jButton3.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				jTextArea1.setText("");				
			}
		});
	}





	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try {			
			UIManager.put("RootPane.setupButtonVisible", false);
			org.jb2011.lnf.beautyeye.BeautyEyeLNFHelper.launchBeautyEyeLNF();
		} catch (Exception ex) {
			java.util.logging.Logger.getLogger(MyInterface.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
		}

		java.awt.EventQueue.invokeLater(new Runnable() {
			public void run() {
				new MyInterface().setVisible(true);
			}
		});

	}

}
