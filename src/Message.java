import java.io.*;

class Message {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String ip = args[0];

		int receivePort = Integer.parseInt(args[2]);
		Recieve b = new Recieve(receivePort, args[3]);
		Thread t1 = new Thread(b);
		t1.start();

		System.out.println("Press Enter key to continue. When you partner is also in tha same step...");
		br.readLine();
		int sendPort = Integer.parseInt(args[1]);
		Send a = new Send(ip, sendPort);
		Thread t2 = new Thread(a);
		t2.start();

		System.out.print("\nYou are Connected and Ready to Recieve....\n");

	}
}
