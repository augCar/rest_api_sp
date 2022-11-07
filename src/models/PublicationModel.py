from database.db import get_connection
from .entitites.Publication import Publication

class PublicationModel():

    @classmethod
    def get_publications(self):
        try:
            connection = get_connection()
            publications = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, description, priority, stat, usr FROM publication ORDER BY title ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    publication = Publication(row[0], row[1], row[2], row[3], row[4], row[5])
                    publications.append(publication.to_JSON())
            connection.close()
            return publications

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_publication(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, description, priority, stat, usr FROM publication WHERE id = %s", (id,))
                row = cursor.fetchone()

                publication = None

                if row:
                    publication = Publication(row[0], row[1], row[2], row[3], row[4], row[5])
                    publication = publication.to_JSON()

            connection.close()
            return publication

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_publication(self, publication):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO publication (id, title, description, priority, stat, usr) VALUES (%s, %s, %s, %s, %s, %s)""", (publication.id, publication.title, publication.description, publication.priority, publication.stat, publication.usr))                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_publication(self, publication):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE publication SET title = %s, description = %s, priority = %s, stat = %s, usr = %s WHERE id = %s", (publication.title, publication.description, publication.priority, publication.stat, publication.usr, publication.id))                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_publication(self, publication):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM publication WHERE id = %s", (publication.id,))                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
