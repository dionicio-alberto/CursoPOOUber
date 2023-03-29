class Account{
    Integer id;
    String name;    
    String document;    
    String email;    
    String password;    
    
    public Account(Integer id, String name, String document,  String email, String password){
        this.id         = id;
        this.name       = name;
        this.document   = document;
        this.email      = email;
        this.password   = password;
    }

    void printDataAccount(){
        System.out.println("---User Data--");
        System.out.println("id: " + id);
        System.out.println("name: " + name);
        System.out.println("document: " + document);
        System.out.println("email: " + email);
        System.out.println("password: " + password);
        System.out.println("-------------");
    }
}