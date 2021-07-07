package schoolforall;


//import java.sql.*;

public class BDConnection {
    private String DBPath = "Chemin aux base de donnée SQLite";
    //private Connection connection = null;
    //private Statement statement = null;

    public BDConnection(String dBPath) {
        DBPath = dBPath;
    }

    public void connect() {
        /*try {
            Class.forName("org.sqlite.JDBC");
            connection = DriverManager.getConnection("jdbc:sqlite:" + getClass().getClassLoader().getResource(DBPath));
            statement = connection.createStatement();
            System.out.println("Connexion a " + DBPath + " avec succès");
        } catch (ClassNotFoundException notFoundException) {
            notFoundException.printStackTrace();
            System.out.println("Erreur de connecxion");
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
            System.out.println("Erreur de connecxion");
        }*/
    }

    /*public void close() {
        try {
            connection.close();
            statement.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public ResultSet query(String requet) {
        ResultSet resultat = null;
        try {
            resultat = statement.executeQuery(requet);
        } catch (SQLException e) {
            e.printStackTrace();
            System.out.println("Erreur dans la requet : " + requet);
        }
        return resultat;

    }*/
/*
    public static void main(String[] args) {
        System.out.println("debut");
        BDConnection connexion = new BDConnection("schoolforallBD.db");
        connexion.connect();
        connexion.close();
        System.out.println("fin");
    }*/
}


