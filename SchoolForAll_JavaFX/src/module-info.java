
module Practice {
    requires javafx.controls;
    requires javafx.fxml;
    requires org.kordamp.ikonli.core;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.ikonli.fontawesome;
    requires com.jfoenix;

    opens schoolforall to javafx.fxml;
    exports schoolforall;
}

