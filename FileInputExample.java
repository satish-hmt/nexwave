import java.io.FileInputStream;

public class FileInputExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			FileInputStream fin = new FileInputStream("C:\\Users\\lab365\\Desktop\\aaa.txt");
			
			int i = 0;
			while((i = fin.read()) != -1) {
				System.out.print((char) i);
			}
			fin.close();
		}catch (Exception e) {
			e.printStackTrace();
		}

	}

}
