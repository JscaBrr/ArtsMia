from database.DB_connect import DBConnect
from model.object import Object

class DAO:

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT DISTINCT * FROM objects"
        cursor.execute(query)
        listobj = []
        for dct in cursor:
            listobj.append(Object(**dct))
        cursor.close()
        conn.close()
        return listobj

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT e1.object_id as o1, e2.object_id as o2, COUNT(*) as count
        FROM exhibition_objects e1, exhibition_objects e2
        WHERE e1.exhibition_id = e2.exhibition_id AND e1.object_id < e2.object_id
        GROUP BY e1.object_id, e2.object_id
        ORDER BY count ASC"""
        cursor.execute(query)
        listobj = []
        for dct in cursor:
            listobj.append((dct['o1'], dct['o2'], dct['count']))
        cursor.close()
        conn.close()
        return listobj


