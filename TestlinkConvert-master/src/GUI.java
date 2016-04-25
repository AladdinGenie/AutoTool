import java.awt.Container;
import java.awt.Dialog;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.ButtonGroup;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import javax.swing.event.ChangeListener;
import javax.swing.filechooser.FileNameExtensionFilter;

import jxl.write.WriteException;
import jxl.write.biff.RowsExceededException;

import org.dom4j.DocumentException;

/**
 * 
 * 
 * @author 
 */
public class GUI extends JFrame{
	
	
	// 文件路径
	protected JTextField filename;

	// 小容器
	private JLabel jl1;
	private JLabel jl2;
	private JLabel jl3;

	// 小按钮
	private JButton bu1;
	private JButton bu2;
	
	//单选按钮
	private JRadioButton jb1;
	private JRadioButton jb2;
	private ButtonGroup bg;
	/*
	 * 构造方法
	 */
	public GUI() {
		// 设置窗口标题
		this.setTitle("TestlinkConvert");
		// 窗体组件初始化
		init();
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		// 设置布局方式为绝对定位
		this.setLayout(null);
		
		this.setBounds(0, 0, 355, 150);
		// 设置窗体的标题图标
		Image image = new ImageIcon("F:/logo.jpg").getImage();
		this.setIconImage(image);
		
		// 窗体大小不能改变
		this.setResizable(false);
		
		// 居中显示
		this.setLocationRelativeTo(null);

		// 窗体可见
		this.setVisible(true);
	}

	/*
	 * 初始化方法
	 */
	public void init() {
		// 创建一个容器
		final Container con = this.getContentPane();
		jl1 = new JLabel("File");
		jl1.setBounds(20, 40, 70, 20);
		
		jl2 = new JLabel("Choose file to Convert:");
		jl2.setBounds(15, 5, 300, 20);
		
		jl3 = new JLabel("Done!");
		jl3.setBounds(210, 40, 80, 20);
		jl3.setVisible(false);
		
		// 文件路径输入框
		filename = new JTextField();
		filename.setBounds(50, 40, 150, 20);
		
		//单选按钮
		jb1 = new JRadioButton("xml->xls",true);
		jb1.setBounds(40, 75, 80, 20);
		jb2 = new JRadioButton("xls->xml");
		jb2.setBounds(120, 75, 80, 20);
		bg = new ButtonGroup();
		bg.add(jb1);
		bg.add(jb2);

		// 按钮设定
		bu1 = new JButton("select");
		bu1.setBounds(250, 40, 80, 20);
		bu2 = new JButton("convert");
		bu2.setBounds(250, 75, 80, 20);
		// 给按钮添加事件

		change();
		
		// 所有组件用容器装载
		con.add(jb1);
		con.add(jb2);
		con.add(jl1);
		con.add(jl2);
		con.add(jl3);
		con.add(bu2);
		con.add(bu1);
		con.add(filename);

	}

	public static void main(String[] args) {
		// 实例化对象
		GUI qq = new GUI();
	}

	
	
	public void change(){
	
		bu1.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				
				System.out.println("点击选择");
				JFileChooser chooser = new JFileChooser();
				if(jb1.isSelected()){
				FileNameExtensionFilter filter = new FileNameExtensionFilter("xml", "xml");
				chooser.setFileFilter(filter);
				}
				else
				{FileNameExtensionFilter filter = new FileNameExtensionFilter("xls", "xls");
				chooser.setFileFilter(filter);}
				
				int returnVal = chooser.showOpenDialog(new JPanel());
					if(returnVal == JFileChooser.APPROVE_OPTION){
						System.out.println("你打开的文件是："+chooser.getSelectedFile().getAbsolutePath());
						filename.setText(chooser.getSelectedFile().getAbsolutePath());
					}
			}
		});
		
		
		
		// 给按钮添加事件
		bu2.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				
				if(jb1.isSelected()){
				String path = filename.getText();
				try {
					new CreatExcel().creat(new ReadXml().Read(path), path);
					System.out.println("succeed");
					
					jl3.setVisible(true);
					JOptionPane.showMessageDialog(null, "恭喜您，转换成功");
					
				} catch (RowsExceededException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				} catch (WriteException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				} catch (DocumentException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				
				
			}
				else{
					String path = filename.getText();
					
					new CreatXml().create(path);
					System.out.println("succeed");
					
					jl3.setVisible(true);
					JOptionPane.showMessageDialog(null, "恭喜您，转换成功");
				}	
			}
		});
		}
		
	}


	
	

	