public class Main {
    
    public static String kek(String[] titles) {
        String result = "";
        for(int i = 0; i<titles.length; i++) {
            result += " "+titles[i];
        }
        return result;
    }
    public static void main(String[] args) {
        String[] names = {"John", "Doe", "Pidor"};
        System.out.println("Hellow World!");
        System.out.println(kek(names));
        
    }

}