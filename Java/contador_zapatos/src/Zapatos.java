public class Zapatos{
    // Constantes
    private final static String MARCA="Arturo";
    private final static String TIPO_MATERIAL ="Cuero";
    private final static double PRECIO_BASE= 10000;
    // Atributos
    private String marca;
    private String tipo_material;
    private double precioBase;
    // Constructores
    // Metodos
    public Zapatos(){
       marca = MARCA;
       tipo_material = TIPO_MATERIAL;
       precioBase = PRECIO_BASE;
    }
    public Zapatos (String marca){
       this.marca = marca;
       tipo_material = TIPO_MATERIAL;
       precioBase = PRECIO_BASE;
    }
   public Zapatos (String marca, String tipo_material, double precioBase2){
      this.marca = marca;
      this.tipo_material = tipo_material;
      this.precioBase = precioBase2;
   }

    // En caso de ser necesarios metodos adicionales
    public double calcularPrecio(){
       double precioFinal = precioBase;
       if (marca.equals("Arturo")){
          precioFinal = precioFinal + (precioFinal*0.75);
       }else{
          precioFinal = precioFinal + (precioFinal*0.20);
       }
       if (tipo_material.equals("Cuero")){
            precioFinal = precioFinal - 5000;
          }
       else{
            precioFinal = precioFinal - 500;
          }
    // Calculos
    return precioFinal;
    }
    // getters/setters de ser necesarios
    }
