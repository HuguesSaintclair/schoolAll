package schoolforall;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.image.Image;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.FlowPane;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

public class Acceuil implements Initializable{
    @FXML
    private FlowPane moduleCSFA;

    //@FXML
    //private AnchorPane imageEnTete;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        try {
            /*boolean backgroundLoading = true;
            Image image_ = new Image(url, backgroundLoading);
            imageEnTete.setImage(image_);*/
            addModule("La Souris", "souris.jpg", "Dans ce module nous allons vous apprendre a manipuler la souris d'un ordinateur");
            addModule("Le Clavier", "clavier.jpg", "Dans ce module nous allons vous apprendre a manipuler la souris d'un ordinateur");
            addModule("L'ecran", "ecran.jpg", "Dans ce module nous allons vous apprendre a manipuler la souris d'un ordinateur");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void addModule(String titre, String url, String description) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getClassLoader().getResource("moduleSFA.fxml"));
        AnchorPane msfa = fxmlLoader.load();
        ModuleSFA ctrl = fxmlLoader.getController();
        if(!url.equals("none"))
            ctrl.setImage(url);
        ctrl.setTitre(titre);
        ctrl.setDescription(description);
        moduleCSFA.getChildren().add(msfa);
    }
}
