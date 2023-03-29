class Driver extends Account{

    constructor(id, name, document, email, password){
        super(id, name, document, email, password);
    }     
     printDataDriver(){
        console.log("Id : " + this.id);
        console.log("Name : " + this.name);
        console.log("Document : " + this.document);
        console.log("Mail : " + this.email);
        console.log("Password : " + this.password);
     }  
}