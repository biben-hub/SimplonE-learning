import mysql.connector
import json

from management_bdd import *

def main():
    print('Pret!!')
    """ liste_videos=[]
    liste_videos.append('https://www.youtube.com/watch?v=m6chqKlhpPo','30 Days of Python - Day 15 - Automated Video Processing with Moviepy - Python TUTORIAL','autheur 1', 2020, 'description', 'Python') """
    connect_bdd = ManagementBdd()
    connect_bdd.message()
    """ connect_bdd.create_table_videos() """


if __name__ == "__main__":
    main()