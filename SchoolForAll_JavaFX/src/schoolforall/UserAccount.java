package schoolforall;

import javafx.animation.TranslateTransition;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.util.Duration;
import org.kordamp.ikonli.javafx.FontIcon;

import java.io.IOException;
import java.net.URL;
import java.util.EventObject;
import java.util.ResourceBundle;

public class UserAccount implements Initializable {
    private enum SideNav{DOCS, FILES, USER, PLANIF, NONE};
    private SideNav actualSideNave = SideNav.NONE;
    private boolean topSousNavDeroul = true;
    private boolean openNav = false;

    @FXML
    private ToggleGroup side_btn;
    @FXML
    private AnchorPane sousMenuGauche;
    @FXML
    private AnchorPane topSousNav;
    @FXML
    private FontIcon topFleche;
    @FXML
    private ScrollPane centralPane;
    @FXML
    private ScrollPane contentSidNav;

    @FXML
    void subMenuDocs(ActionEvent event) {
        redondAnimateSideSubNav(SideNav.DOCS);
    }

    @FXML
    void subMenuFiles(ActionEvent event) {
        redondAnimateSideSubNav(SideNav.FILES);
    }

    @FXML
    void subMenuPlanif(ActionEvent event) {
        redondAnimateSideSubNav(SideNav.PLANIF);
    }

    @FXML
    void subMenuUser(ActionEvent event) {
        redondAnimateSideSubNav(SideNav.USER);
    }

    @FXML
    void topSousNavDerouler(ActionEvent event) {
        double y = (topSousNavDeroul)?0:-topSousNav.getHeight()-50;
        double yt = (!topSousNavDeroul)?0:-topSousNav.getHeight()-50;
        TranslateTransition side_slide = new TranslateTransition();
        side_slide.setDuration(Duration.seconds(0.3));
        side_slide.setNode(topSousNav);

        side_slide.setToY(y);
        side_slide.play();

        topSousNav.setTranslateY(yt);

        side_slide.setOnFinished((ActionEvent e)->{
            topSousNavDeroul = !topSousNavDeroul;
        });
        if(!topSousNavDeroul)
            topFleche.setIconLiteral("fa-chevron-circle-left");
        else
            topFleche.setIconLiteral("fa-chevron-circle-down");
    }

    @FXML
    void deconnexion(ActionEvent event) {
        Stage stage = (Stage) ((Node)event.getSource()).getScene().getWindow();
        //Stage stageTheLabelBelongs = (Stage) label.getScene().getWindow();
        Parent root = null;
        try {
            root = FXMLLoader.load(getClass().getClassLoader().getResource("app_root.fxml"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        if(root != null)
            stage.setScene(new Scene(root));
    }

    private void animateSideSubNav(double x, double xt, boolean open, boolean style){
        TranslateTransition side_slide = new TranslateTransition();
        side_slide.setDuration(Duration.seconds(0.3));
        side_slide.setNode(sousMenuGauche);

        side_slide.setToX(x);
        side_slide.play();

        sousMenuGauche.setTranslateX(xt);

        side_slide.setOnFinished((ActionEvent e)->{
            if(open){
                openSideMenu(false);
            }else if(style == false){
                contentSidNav.setContent(new VBox());
            }else{
            }
        });
    }
    private void redondAnimateSideSubNav(SideNav type){
        boolean r = false;
        if(actualSideNave != SideNav.NONE){
            if(actualSideNave == type){
                actualSideNave = SideNav.NONE;
                closeSideMenu(false);
                openNav = false;
            }else{
                actualSideNave = type;
                closeSideMenu(true);
                openNav = true;
            }
        }else{
            actualSideNave = type;
            openSideMenu(false);
            openNav = true;
        }
    }

    private void openSideMenu(boolean revers){
        if(actualSideNave == SideNav.FILES){
            openFile(contentSidNav, "listFichier.fxml");
        }else if(actualSideNave == SideNav.DOCS){
            openFile(contentSidNav, "moduleStudie.fxml");
        }
        animateSideSubNav(0, -250, revers, true);
    }

    private void openFile(ScrollPane scroll, String file){
        try {
            VBox pane = FXMLLoader.load(getClass().getClassLoader().getResource(file));
            scroll.setContent(pane);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void closeSideMenu(boolean revers){
        animateSideSubNav(-250, 0, revers, false);
    }

    private void initScroll(ScrollPane scroll, String color){
        scroll.fitToWidthProperty().set(true);
        scroll.fitToHeightProperty().set(true);
        scroll.setStyle(color);
    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        sousMenuGauche.setTranslateX(-250);
        topSousNav.setTranslateY(-250);

        initScroll(centralPane, "-fx-background: #FFF;");
        initScroll(contentSidNav, "-fx-background: #db9d5e;");

        openFile(centralPane, "acceuil.fxml");
    }
}
