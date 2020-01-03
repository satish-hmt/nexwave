import java.io.FileNotFoundException;
import java.io.FileOutputStream;
public class FileOutputStreamExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			FileOutputStream fout = new FileOutputStream("C:\\Users\\lab365\\Desktop\\aaa.txt");
			
			String s = "Hello World";
			byte b[] = s.getBytes();
					fout.write(b);
					fout.close();
		System.out.println("Success");
	}
	catch (Exception e) {
		e.printStackTrace();
	}
	}

}
