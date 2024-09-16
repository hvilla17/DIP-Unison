import javax.swing.*;
import java.awt.*;

public class MainWindow extends JFrame {
    private final DrawPanel drawPanel;

    public MainWindow()
    {
        super("ColorChooser Test");

        this.setLayout(new BorderLayout());

        JPanel controlPanel = new JPanel();
        JButton colorBtn = new JButton("Color");
        colorBtn.addActionListener(e -> changeColor());
        controlPanel.add(colorBtn);
        this.add(controlPanel, BorderLayout.WEST);

        drawPanel = new DrawPanel();
        this.add(drawPanel, BorderLayout.CENTER);

        this.setSize(800, 600);
        this.setLocation(400, 20);
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }

    private void changeColor()
    {
        Color color = JColorChooser.showDialog(this, "Select a color", drawPanel.getCurrentColor());
        if (color != null) {
            drawPanel.changeColor(color);
        }
    }
}
