class Employee{
	float salary = 40000;
}
public class Programmer extends Employee {
	int bonus = 10000;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Programmer p = new Programmer();
		System.out.println("Programming salary is:"+p.salary);
		System.out.println("Bonus is: "+p.bonus);
	}

}
