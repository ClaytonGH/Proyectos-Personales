public class ZapatosArtesanal extends Zapatos {
    // Constantes
    private final static int TAMAÑO = 40;
    // Atributos
    private int tamaño;
    // Constructores
    public ZapatosArtesanal(){
        tamaño = TAMAÑO;
    }
    public ZapatosArtesanal(int tamaño){
        this.tamaño = tamaño;
    }
    public ZapatosArtesanal(String marca, String tipo_material, double precioBase, Integer tamaño){
        super(marca, tipo_material, precioBase);
        this.tamaño = tamaño;
    }
    // Metodos
    public double calcularPrecio(){
    // Calculos
    double precioFinal = super.calcularPrecio();
    if (tamaño < 40){
        precioFinal += 10000;
    }else{
        precioFinal += 4500;
    }
    return precioFinal;
    }
    // getters/setters de ser necesarios
    }
    // Fin de la solución