import mysql.connector
import logging

logging.basicConfig(filename='logging_bdd.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

#create database e_learning;
class ManagementBdd:
    def __init__(self):
        
        #"Établissement de la connexion - Création du curseur"
        try:
            logging.info("class ManagementBdd, methode: init - Start")
            self.cnx = mysql.connector.connect(user='cary', password='cordoba#1234AA', host='localhost', database='e_learning', use_unicode=True, charset='utf8')
            print('connexion reussi')
            logging.info("connection reussi à la BDD") 
            #self.mycursor = self.cnx.cursor()
            self.echec =0
            logging.info("class ManagementBdd, methode: init - End")
        except mysql.connector.Error as err:
            logging.error("Error de connection "+ err)
            print("Something went wrong, La connexion avec la base de données a échoué : {}".format(err))       
            self.echec =1        
            
    def message(self):
        print('hola')
    
    def create_database(self):
        try:       
            logging.info("class ManagementBdd, methode: create_database - Start")
            var_cursor = self.cnx.cursor()
            
            self.requete=f'CREATE DATABASE IF NOT EXISTS e_learning'

            #logging.info("create_database requete : "+self.requete)
            var_cursor.execute(self.requete)
            print('creation BDD reussi!!!')
            logging.info("creation BDD reussi!!!")
            logging.info("class ManagementBdd, methode: create_database, creation BDD reussi!!! - End")

            return 1

        except Exception as err:
            # afficher la requête et le message d'erreur système :
            print ("Requête SQL incorrecte :\n%s\nErreur détectée :\n%s"\
                % (self.requete, err))
            logging.error("Error - class ManagementBdd, methode: create_database "+self.requete+ ' - '+err)
            return 0   
    
    def create_table_videos(self):
        try:       
            logging.info("class ManagementBdd, methode: create_table_videos - Start")
            var_cursor = self.cnx.cursor()            

            self.requete=f'CREATE TABLE IF NOT EXISTS videos (video_id INTEGER AUTO_INCREMENT PRIMARY KEY, titre VARCHAR(250) NOT NULL, author VARCHAR(250), lien TEXT NOT NULL, anne_video VARCHAR(4), description TEXT, categorie VARCHAR(200)) '
            #logging.info("create_table_videos, requete : "+self.requete)

            var_cursor.execute(self.requete)
            print('creation reussi!!!')
            logging.info("creation reussi!!!")
            logging.info("class ManagementBdd, methode: create_table_videos - End")
            return 1

        except Exception as err:
            logging.error("Error - class ManagementBdd, methode: create_table_videos "+self.requete+ ' - '+err)
            # afficher la requête et le message d'erreur système :
            print ("Requête SQL incorrecte :\n%s\nErreur détectée :\n%s"\
                % (self.requete, err))
            return 0         
    
    def insert_donnes(self, donnes):        

        #donnes sera un dictionnare json envoyé pour le flask
        #print(donnes, type(donnes))#<class 'list'>
        try:
            logging.info("class ManagementBdd, methode: insert_donnes - Start")
            mon_cursor = self.cnx.cursor()
            #print(donnes)           

            #on cree la requete d'insertion            
            sql_insert = ('INSERT INTO videos(titre, author,lien,anne_video,description,categorie) VALUES(%s,%s,%s,%s,%s,%s)')
            
            #logging.info("insert_donnes , requete : "+sql_insert)
            #on execute le methode pour inserer les donnes sur la BDD bd_scrapping)
            mon_cursor.execute(sql_insert, donnes) #execute le curseur avec la methode executemany transmit la requete
            
            self.cnx.commit() #valide la transaction
                
            print(mon_cursor.rowcount, "record inserted.\n")  

            logging.info (str(mon_cursor.rowcount) + " record inserted.\n")   
            logging.info("class ManagementBdd, methode: insert_donnes - End")
            
            return mon_cursor.rowcount

        except mysql.connector.Error as err:
            print("Something went wrong, un erreur se produit : {}".format(err))
            logging.error("Error - class ManagementBdd, methode: insert_donnes "+self.requete+ ' - '+err)
            return 0
    

 




  