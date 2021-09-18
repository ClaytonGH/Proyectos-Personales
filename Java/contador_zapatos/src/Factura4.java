// Inicio de la solución
public class Factura4{
    // Atributos
    Zapatos [] lista;
    // Constructores
    public Factura4(Zapatos lista []){
        this.lista = lista;
    }
    // Metodos
    public void mostrarTotales(){
        double totalZapatos = 0;
        double totalZapatosNacional = 0;
        double totalZapatosArtesanal = 0;
        for (Zapatos zapato : lista){
            double precio = zapato.calcularPrecio();
            totalZapatos += precio;
            if (zapato.getClass() == ZapatosNacional.class){
            totalZapatosNacional += precio;
        }else if (zapato.getClass() == ZapatosArtesanal.class){
            totalZapatosArtesanal += precio;
        }
    }   
    // Calculo de totales
    System.out.println("El precio total de los zapatos es de " + totalZapatos);
    System.out.println("La suma del precio de los ZapatosNacional es de " + totalZapatosNacional);
    System.out.print("La suma del precio de los ZapatosArtesnal es de " + totalZapatosArtesanal);
    }
    
    }
