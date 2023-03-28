class Main {
    public static void main(String[] args) {
        System.out.println("hola mundo");
        
        Car car = new Car("ABC123", new Account("Andres Herrera", 0001));
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car("DEF456",new Account("Andrea Herrera", 0002));
        car2.passenger = 3;
        car2.printDataCar();
    }
}