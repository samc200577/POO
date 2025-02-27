package co.edu.uniquindio.poo;

public class Ninio {

    private String nombres;
    private int edad;
    private String genero;
    private String documento;
    private String alergias;
    private String nombreAcudiente;
    private String numeroContactoAcudiente;
    private String ID;

    public Ninio(String nombres, int edad, String genero, String documento, String alergias, String nombreAcudiente, String numeroContactoAcudiente, String ID) {
        this.nombres = nombres;
        this.edad = edad;
        this.genero = genero;
        this.documento = documento;
        this.alergias = alergias;
        this.nombreAcudiente = nombreAcudiente;
        this.numeroContactoAcudiente = numeroContactoAcudiente;
        this.ID = ID;
    }

    public String getNombres() {
        return nombres;
    }

    public void setNombres(String nombres){
        this.nombres = nombres;
    }

    public int getEdad(){
        return edad;
    }

    public void setEdad(int edad){
        this.edad = edad;
    }

    public String getGenero(){
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public String getDocumento(){
        return documento;
    }

    public void setDocumento(String documento){
        this.documento = documento;
    }

    public String getAlergias(){
        return alergias;
    }

    public void setAlergias(String alergias){
        this.alergias = alergias;
    }

    public String getNombreAcudiente(){
        return nombreAcudiente;
    }

    public void setNombreAcudiente(String nombreAcudiente){
        this.nombreAcudiente = nombreAcudiente;
    }

    public String getNumeroContactoAcudiente(){
        return numeroContactoAcudiente;
    }

    public void setNumeroContactoAcudiente(String numeroContactoAcudiente){
        this.numeroContactoAcudiente = numeroContactoAcudiente;
    }

    public String getID(){
        return ID;
    }

    public void getID(String ID){
        this.ID = ID;
    }

    public String toString(){
        return "Ninio{" +
                "Nombres = " +  nombres + '\'' +
                "Edad = " + edad + '\''+
                "Genero = " + genero + '\''+
                "Documento" + documento + '\''+
                "Alergias del niño = " + alergias + '\''+
                "Nombre del Acudiente = " + nombreAcudiente + '\''+
                "Número de contacto del acudiente = " + numeroContactoAcudiente + '\''+
                "ID = " + ID +'\'' + '}';


    }

}