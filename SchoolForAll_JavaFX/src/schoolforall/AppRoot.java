package schoolforall;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.layout.VBox;

import java.net.URL;
import java.util.ResourceBundle;

public class AppRoot implements Initializable {
    @Override
    public void initialize(URL location, ResourceBundle resources) {

    }
    @FXML
    public void close(ActionEvent actionEvent) {
        System.exit(0);
    }
}
