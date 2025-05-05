from database.DB_connect import DBConnect
from model.edge import Edge
from model.object import Object


class DAO():

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * from objects"
        cursor.execute(query, ())
        listobj = []
        for dict in cursor:
            listobj.append(Object(**dict))
        cursor.close()
        conn.close()
        return listobj

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT eo1.object_id as o1, eo2.object_id as o2, COUNT(*) as peso
        FROM exhibition_objects  eo1
        INNER JOIN exhibition_objects  eo2
        ON eo1.exhibition_id = eo2.exhibition_id
        AND eo2.object_id < eo1.object_id
        GROUP BY eo1.object_id, eo2.object_id
        ORDER BY peso DESC
        """
        cursor.execute(query, ())
        listobj = []
        for dict in cursor:
            listobj.append(Edge(**dict))
        cursor.close()
        conn.close()
        return listobj
