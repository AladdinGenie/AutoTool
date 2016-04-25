package main;

import java.io.IOException;
import java.net.ServerSocket;

public class PortHolder  extends Thread{

	ServerSocket server = null;
	int port = -1;
	boolean work = false;
	

	public void setPort(int port){
		this.port = port;
	}
	
	
	
	public int getPort(){
		return port;
	}
	

	public void terminal(){
		try {
			work = false;
			server.close();
		} catch (IOException e) {
			e.printStackTrace();
		}finally{
			server = null;
		}
	}

	public void run(){
		try {
			server = new ServerSocket(port);
			work = true;
			while(work){
				Thread.sleep(1000);
			}
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
