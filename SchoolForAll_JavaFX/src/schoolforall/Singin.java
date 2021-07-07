package schoolforall;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.image.Image;
import javafx.scene.image.PixelWriter;
import javafx.scene.image.WritableImage;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

public class Singin implements Initializable {
    @Override
    public void initialize(URL location, ResourceBundle resources) {
    }
    @FXML
    public void close(ActionEvent actionEvent) {
        System.exit(0);
    }

    public void singup(ActionEvent actionEvent) {

    }
}
