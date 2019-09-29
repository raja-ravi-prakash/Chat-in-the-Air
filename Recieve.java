import java.net.*;
import java.io.*;

public class Recieve extends Thread
{
	ServerSocket ss;
	Socket s;
	DataInputStream in;
	Recieve(int port)throws Exception{
		ss=new ServerSocket(port);
	}
	public void run(){
		try{
			s=ss.accept();
			
			in=new DataInputStream(s.getInputStream());

			String msg="";
			while(!msg.equals("Over")){
				msg=in.readUTF();
				System.out.println("\nUnknown : "+msg);
			}
			ss.close();
			s.close();
			in.close();
		}
		catch(Exception ae){}
	}
}
