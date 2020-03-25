import java.io.*;

class Message {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.print("Enter the Partner IP : ");
		String ip = br.readLine();

		System.out.print("\nEnter Receiving Port : ");
		int receivePort = Integer.parseInt(br.readLine());
		Recieve b = new Recieve(receivePort);
		Thread t1 = new Thread(b);
		t1.start();

		System.out.print("Enter Sending Port : ");
		int sendPort = Integer.parseInt(br.readLine());
		Send a = new Send(ip, sendPort);
		Thread t2 = new Thread(a);
		t2.start();

		System.out.print("\nYou are Connected and Ready to Recieve....\n");

	}
}
