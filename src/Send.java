import java.net.*;
import java.io.*;

public class Send extends Thread
{
	Socket ac;
	DataInputStream in;
	DataOutputStream out;
	Send(String ip,int port)throws Exception{
		ac=new Socket(ip,port);
	}
	public void run(){
		try{
			out=new DataOutputStream(ac.getOutputStream());
			in=new DataInputStream(new BufferedInputStream(System.in));
		
			String msg="";

			while(!msg.equals("Over")){
				
				msg=in.readLine();
				out.writeUTF(msg);
				System.out.print("\n");
				
			}

			ac.close();
			in.close();
			out.close();
		}
		catch(Exception ex){}
	}
}
