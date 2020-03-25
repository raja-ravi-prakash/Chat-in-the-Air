import java.net.*;
import java.io.*;

public class Recieve extends Thread {
	ServerSocket ss;
	Socket s;
	DataInputStream in;
	String name;

	Recieve(int port, String name) throws Exception {
		ss = new ServerSocket(port);
		this.name = name;
	}

	public void run() {
		try {
			s = ss.accept();

			in = new DataInputStream(s.getInputStream());

			String msg = "";
			while (!msg.equals("Over")) {
				msg = in.readUTF();
				System.out.println("\n" + name + ": " + msg);
				System.out.print("You: ");
			}
			ss.close();
			s.close();
			in.close();
		} catch (Exception ae) {
		}
	}
}
