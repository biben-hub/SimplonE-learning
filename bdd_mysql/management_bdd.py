import mysql.connector


#create database e_learning;
class ManagementBdd:
    def __init__(self):
        
        #"Établissement de la connexion - Création du curseur"
        try:
            self.cnx = mysql.connector.connect(user='cary', password='cordoba#1234AA', host='localhost', database='e_learning', use_unicode=True, charset='utf8')
            print('connexion reussi') 
            #self.mycursor = self.cnx.cursor()
            self.echec =0

        except mysql.connector.Error as err:
            print("Something went wrong, La connexion avec la base de données a échoué : {}".format(err))       
            self.echec =1        
            
    def message(self):
        print('hola')
    
    def create_database(self):
        try:       

            var_cursor = self.cnx.cursor()
            
            self.requete=f'CREATE DATABASE IF NOT EXISTS e_learning'

            var_cursor.execute(self.requete)
            print('creation BDD reussi!!!')
            return 1

        except Exception as err:
            # afficher la requête et le message d'erreur système :
            print ("Requête SQL incorrecte :\n%s\nErreur détectée :\n%s"\
                % (self.requete, err))
            return 0   
    
    def create_table_videos(self):
        try:       

            var_cursor = self.cnx.cursor()
            

            self.requete=f'CREATE TABLE IF NOT EXISTS videos (video_id INTEGER AUTO_INCREMENT PRIMARY KEY, titre VARCHAR(250) NOT NULL, author VARCHAR(250), lien TEXT NOT NULL, anne_video VARCHAR(4), description TEXT, categorie VARCHAR(200)) '


            var_cursor.execute(self.requete)
            print('creation reussi!!!')
            return 1

        except Exception as err:
            # afficher la requête et le message d'erreur système :
            print ("Requête SQL incorrecte :\n%s\nErreur détectée :\n%s"\
                % (self.requete, err))
            return 0         
    
    def insert_donnes(self, donnes):
        #donnes sera un dictionnare json envoyé pour le flask
        #print(donnes, type(donnes))#<class 'list'>
        try:
            mon_cursor = self.cnx.cursor()
            #print(donnes)           

            #on cree la requete d'insertion
            #['https://www.youtube.com/watch?v=m6chqKlhpPo','30 Days of Python - Day 15 - Automated Video Processing with Moviepy - Python TUTORIAL','autheur 1', 2020, 'description', 'Python']
            sql_insert = ('INSERT INTO videos(titre, author,lien,anne_video,description,categorie) VALUES(%s,%s,%s,%s,%s,%s)')
            
            #on execute le methode pour inserer les donnes sur la BDD bd_scrapping)
            mon_cursor.execute(sql_insert, donnes) #execute le curseur avec la methode executemany transmit la requete
            
            self.cnx.commit() #valide la transaction
                
            print(mon_cursor.rowcount, "record inserted.\n")           
        

        except mysql.connector.Error as err:
            print("Something went wrong, un erreur se produit : {}".format(err))

    

 




  