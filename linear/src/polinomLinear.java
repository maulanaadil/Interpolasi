import java.util.Scanner;

public class polinomLinear {
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        System.out.print("Banyak data : ");
        int N = in.nextInt();
        double dataX[] = new double[N];
        double dataY[] = new double[N];
        //input data x & y
        for(int i=0; i<N; i++){
            System.out.print("X"+(i+1)+" = ");
            dataX[i]=in.nextDouble();
            System.out.print("Y"+(i+1)+" = ");
            dataY[i]=in.nextDouble();
        }
        //mencetak data x & y
        System.out.print("\tX |");
        for(int i=0; i<N; i++){
            System.out.print(" "+dataX[i]+" |");
        }
        System.out.print("\n\tY |");
        for(int i=0; i<N; i++){
            System.out.print(" "+dataY[i]+" |");
        }
        //yang dicari
        System.out.println();
        System.out.print("\nTentukan Nilai X = ");
        double x=in.nextDouble();
        double x1=0,x2=0,y1=0,y2=0;
        //penyeleksian
        for(int i=0; i<N-1; i++){
            if(x>dataX[i] && x<dataX[i+1]){
                x1=dataX[i];
                x2=dataX[i+1];
                y1=dataY[i];
                y2=dataY[i+1];
            }
        }
        System.out.println("x1 = "+x1);
        System.out.println("x2 = "+x2);
        System.out.println("y1 = "+y1);
        System.out.println("y2 = "+y2);
        double y=y1+((y2-y1)/(x2-x1))*(x-x1);
        System.out.println("Titik terbaru adalah P3("+x+","+y+")");
    }
}
