package katana;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Machine {
    public static void start (String d[]){
        try {
            System.out.println("        [!] Make Tab.");
            String module=d[9];
            KatanaGUI.PanelContenedor.addTab("Console", new Console(module));
            KatanaGUI.PanelContenedor.validate();
            KatanaGUI.PanelContenedor.repaint();
            KatanaGUI.PanelContenedor.grabFocus();
            KatanaGUI.PanelContenedor.setSelectedIndex(KatanaGUI.PanelContenedor.getTabCount()-1);
            KatanaGUI.PanelContenedor.getSelectedIndex();
        } catch (IOException ex) {
            Logger.getLogger(Machine.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}