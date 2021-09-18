public class ZapatosNacional extends Zapatos {
    // Constantes
    private final static String REGION="Cundinamarca";
    // Atributos
    private String region;
    // Constructores
    public ZapatosNacional(){
        region = REGION;
    }
    public ZapatosNacional(String region){
        this.region = region;
    }
    public ZapatosNacional(String marca, String tipo_material, double precioBase, String region){
        super(marca, tipo_material, precioBase);
        this.region = region;
    }
    // Metodos
    public double calcularPrecio(){
    // Calculos
    double precioFinal = super.calcularPrecio();
    if (region == REGION){
        precioFinal += 10000;
    }
    return precioFinal;
    }
    // getters/setters de ser necesarios
    }
