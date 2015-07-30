package katana;
import java.io.IOException;
public class Katana {
    public static void main(String[] args) throws IOException { 
        System.out.println("\n  [+] Stating Katana framework GUI.");
        KatanaGUI ktn=new KatanaGUI();
        ktn.setTitle("Katana GUI");
        ktn.setVisible(true);
        
    }
    
}
