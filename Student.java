
class TestStudent2 {

	int id;
	String name;

	void insertRecord(int id, String name) {
		this.id = id;
		this.name = name;
	}

	void display() {
		System.out.println("id: " + id + " name: " + name);
	}
}

class Student {

	public static void main(String[] args) {
		TestStudent2 s1 = new TestStudent2();
		s1.insertRecord(1, "satish");
		s1.display();

	}

}
