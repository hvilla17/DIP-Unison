import javax.swing.*;
import java.awt.*;

public class DrawPanel extends JPanel {
    private Color currentColor = Color.red;

    public void paintComponent(Graphics g)
    {
        Graphics2D g2 = (Graphics2D) g;

        RenderingHints hints = g2.getRenderingHints();
        hints.put(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        hints.put(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
        hints.put(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
        g2.addRenderingHints(hints);

        int width = this.getWidth();
        int height = this.getHeight();
        int radius = width / 4;

        Color background = g2.getBackground();
        g2.setPaint(background);
        g2.fillRect(0, 0, width, height);

        g2.setPaint(currentColor);
        g2.fillOval(width / 2 - radius, height / 2 - radius,
                2 * radius, 2 * radius);
    }

    public void changeColor(Color color)
    {
        currentColor = color;
        repaint();
    }

    public Color getCurrentColor()
    {
        return currentColor;
    }
}
