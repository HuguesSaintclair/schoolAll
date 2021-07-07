package schoolforall;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.text.Text;

import java.net.URL;
import java.util.ResourceBundle;

public class ModuleSFA implements Initializable {
    @FXML
    private Text titre;

    @FXML
    private ImageView image;

    @FXML
    private Text description;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
    }

    public void setImage(String url){
        boolean backgroundLoading = true;
        Image image_ = new Image(url, backgroundLoading);
        image.setImage(image_);
    }
    public void setTitre(String t){
        titre.setText(t);
    }
    public void setDescription(String desc){
        description.setText(desc);
    }
}
