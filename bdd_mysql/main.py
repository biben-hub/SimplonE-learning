import mysql.connector
import json

from management_bdd import *

def main():
    print('Pret!!')
    liste_videos= ('Comprendre les modèles de Cloud (IaaS, PaaS, SaaS, CaaS, FaaS)', 'Cookie connecté','https://www.youtube.com/watch?v=Al-E4C69UmQ', '2020',"Dans cette vidéo, je vous explique les différents types de cloud :- Qu'est ce que le IaaS  (Infrastructure as a Service) ? - Qu'est ce que le PaaS  (Platform as a Service) ? - Qu'est ce que le SaaS  (Software as a Service) ?","Cloud")
    
    #INSERT INTO videos(titre, author,lien,anne_video,description,categorie) VALUES('30 Days of Python - Day 15 - Automated Video Processing with Moviepy - Python TUTORIAL','Auttheur1','https://www.youtube.com/watch?v=m6chqKlhpPo', '2020',"description dddd",'Python'),('Déboguer son code JavaScript : RegeneratorRuntime is not defined','auteur2','https://www.youtube.com/watch?v=upfsiT_A33I&list=PLjwdMgw5TTLWWXgsHpfCLHJ1Oq4YnE08e','2020','Javascript') 
    connect_bdd = ManagementBdd()
    #connect_bdd.message()
    connect_bdd.create_database()
    connect_bdd.create_table_videos()
    connect_bdd.insert_donnes(liste_videos)
    print('Fin du Script)


if __name__ == "__main__":
    main()