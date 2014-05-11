from zipfile import ZipFile
from sqlite3 import connect
from os.path import dirname

class AnkiCardSourceReader():

    def __init__(self,pathToAnkiArchive):
        self.pathToAnkiArchive = pathToAnkiArchive

    def _extractSqlLiteDBFromAnkiArchive(self, path):
        apkgFile = ZipFile(path)
        apkgFile.extract("collection.anki2")
        apkgFile.close()
        return dirname(path)+'''/collection.anki2'''

    def _getListOfAnkiCardStringFromAnkiSqliteDb(self, pathToSqliteDb):
        con = connect(pathToSqliteDb)
        cur = con.cursor()
        cur.execute("SELECT flds from notes")
        listofAnkiCards = cur.fetchall()
        con.close()
        #Since this returns tuple such as ('front\x1f\x1fback','') a fix is needed
        fixedListOFAnkiCards = [card[0] for card in listofAnkiCards]
        return fixedListOFAnkiCards

    def getRawListOfAnkiCardStrings(self, pathToApkg):
        pathToCollection = self._extractSqlLiteDBFromAnkiArchive(pathToApkg)
        list_raw = self._getListOfAnkiCardStringFromAnkiSqliteDb(pathToCollection)
        list_frontback = [card.split('\x1f\x1f') for card in list_raw]
        return list_frontback


