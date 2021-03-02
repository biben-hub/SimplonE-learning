import mysql.connector
import json
import logging

from management_bdd import *

logging.basicConfig(filename='logging_bdd.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

def main():
    print('Pret!!')  

    logging.info("initialisation")
    liste_videos=[]
    liste_videos.append(('Comprendre les modèles de Cloud (IaaS, PaaS, SaaS, CaaS, FaaS)', 'Cookie connecté','https://www.youtube.com/watch?v=Al-E4C69UmQ', '2020',"Dans cette vidéo, je vous explique les différents types de cloud :- Qu'est ce que le IaaS  (Infrastructure as a Service) ? - Qu'est ce que le PaaS  (Platform as a Service) ? - Qu'est ce que le SaaS  (Software as a Service) ?","Cloud")) 
    liste_videos.append(('videoTitlePython1', 'Auttheur1Python', 'https://www.youtube.com/embed/psaDHhZ0cPs', '2020',"description 1 python", 'Python'))
    liste_videos.append(('videoTitlePython2','Auttheur2Python','https://www.youtube.com/embed/nvyX8JfoOWY','2020',"description 2 python",'Python'))
    liste_videos.append(('videoTitlePython3','Auttheur3Python','https://www.youtube.com/embed/nvyX8JfoOWY', '2020',"description 3  python",'Python'))
    liste_videos.append(('titleJS1','auteurJS1','https://www.youtube.com/embed/XkvrHQNmigs','2020',"description JS 1  ",'JavaScript'))
    liste_videos.append(('titleJS2', 'auteurJS2','https://www.youtube.com/embed/VZLflMqC6dI', '2020',"description JS 2  ",'JavaScript'))
    liste_videos.append(('titleJS3','auteurJS3','https://www.youtube.com/embed/lDO14MA0C_o', '2020',"description JS 3  ",'JavaScript'))
    liste_videos.append(('30 Days of Python - Day 15 - Automated Video Processing with Moviepy - Python TUTORIAL','Author1','https://www.youtube.com/watch?v=m6chqKlhpPo', '2020',"description dddd",'Python'))
    liste_videos.append(('Déboguer son code JavaScript : RegeneratorRuntime is not defined','auteur2','https://www.youtube.com/watch?v=upfsiT_A33I&list=PLjwdMgw5TTLWWXgsHpfCLHJ1Oq4YnE08e','2020',"description ddddeeeee",'Javascript'))
    
    logging.info("Appel de connection à la classe ManagementBdd - Start")

    connect_bdd = ManagementBdd()
    #connect_bdd.message()
    """ logging.info("create database - Start")
    connect_bdd.create_database()
    logging.info("create database - End") """

    logging.info("create table videos - Start")
    connect_bdd.create_table_videos()
    logging.info("create table videos - End")   

    logging.info("Insertion des donnes - Start")
    connect_bdd.insert_donnes(liste_videos)    
    logging.info("Insertion des donnes - End")

    print('Fin du Script')
    logging.info("Fin du Script")

if __name__ == "__main__":
    main()


# INSERT INTO videos(titre, author,lien,anne_video,description,categorie) VALUES(
#     'videoTitlePython1',
#     'Auttheur1Python',
#     'https://www.youtube.com/embed/psaDHhZ0cPs', 
#     '2020',"description 1 python",
#     'Python'), (
#     'videoTitlePython2',
#     'Auttheur2Python',
#     'https://www.youtube.com/embed/nvyX8JfoOWY', 
#     '2020',"description 2 python",
#     'Python'),(
#     'videoTitlePython3',
#     'Auttheur3Python',
#     'https://www.youtube.com/embed/nvyX8JfoOWY', 
#     '2020',"description 3  python",
#     'Python'),(
#     'titleJS1',
#     'auteurJS1',
#     'https://www.youtube.com/embed/XkvrHQNmigs', 
#     '2020',"description JS 1  ",
#     'JavaScript'
#     ),(
#     'titleJS2',
#     'auteurJS2',
#     'https://www.youtube.com/embed/VZLflMqC6dI', 
#     '2020',"description JS 2  ",
#     'JavaScript'
#     ),(
#     'titleJS3',
#     'auteurJS3',
#     'https://www.youtube.com/embed/lDO14MA0C_o', 
#     '2020',"description JS 3  ",
#     'JavaScript'
#     );
