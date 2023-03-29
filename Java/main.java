class Main {
    public static void main(String[] args) {
        System.out.println("hola mundo");
        
        Car car = new Car("ABC123", new Account(1111,"Andres Herrera", "0001","correo@dfjs","dasfasd"));
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car("DEF456",new Account(1311,"Ansadres Herrera", "0002","correo2@dfjs","dasfadsd"));
        car2.passenger = 3;
        car2.printDataCar();
    }
}