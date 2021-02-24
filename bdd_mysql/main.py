import mysql.connector
import json

from management_bdd import *

def main():
    print('Pret!!')
    #liste_videos=[]
    #liste_videos.append(['https://www.youtube.com/watch?v=m6chqKlhpPo','30 Days of Python - Day 15 - Automated Video Processing with Moviepy - Python TUTORIAL','autheur 1', 2020, 'description', 'Python'])
    #INSERT INTO videos(titre, author,lien,anne_video,description,categorie) VALUES('30 Days of Python - Day 15 - Automated Video Processing with Moviepy - Python TUTORIAL','Auttheur1','https://www.youtube.com/watch?v=m6chqKlhpPo', '2020',"description dddd",'Python'),('Déboguer son code JavaScript : RegeneratorRuntime is not defined','auteur2','https://www.youtube.com/watch?v=upfsiT_A33I&list=PLjwdMgw5TTLWWXgsHpfCLHJ1Oq4YnE08e','2020','Javascript') 
    connect_bdd = ManagementBdd()
    connect_bdd.message()
    connect_bdd.create_table_videos()
    print('OK')


if __name__ == "__main__":
    main()