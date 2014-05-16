from zipfile import ZipFile
from sqlite3 import connect
from os.path import dirname
from simplejson import loads

class AnkiCardSourceReader():

    def __init__(self, pathToApkg):
        self.pathToApkg = pathToApkg

    def __enter__(self):
        pathToCollection = self._extractSqlLiteDBFromAnkiArchive(self.pathToApkg)
        self._connectToSqlLiteDB(pathToCollection)
        return self

    def __exit__(self, type, value, traceback):
        self._disconnectFromDb()

    def _connectToSqlLiteDB(self, pathToDb):
        self.connection = connect(pathToDb)

    def _disconnectFromDb(self):
        self.connection.close()

    def _extractSqlLiteDBFromAnkiArchive(self, path):
        apkgFile = ZipFile(path)
        apkgFile.extract("collection.anki2")
        apkgFile.close()
        return dirname(path)+'''/collection.anki2'''

    def _selectOnDb(self, query):
        cur = self.connection.cursor()
        cur.execute(query)
        return cur.fetchall()

    def _fixRawListOfAnkiCards(self, rawAnkiCards):
        # Since this returns tuple such as ('front\x1f\x1fback','') a fix is needed to remove empty element
        # Split at \xf1\xf1 to get back
        #return [htmlParser.unescape(card[0]).split('\x1f',1) for card in rawAnkiCards]
        return [card[0].split('\x1f',1) for card in rawAnkiCards]

    def getRawListOfAnkiCardTuples(self):
        """Returns list of [front, back] lists in anki html format for all cards"""
        listofAnkiCards = self._selectOnDb("SELECT flds from notes")
        return self._fixRawListOfAnkiCards(listofAnkiCards)

    def getAllCardsForDeck(self,deckid):
        """Returns list of [front, back] lists in anki html format for all cards in deck with deckid"""
        listofAnkiCards = self._selectOnDb("SELECT flds from notes,cards WHERE notes.id is cards.nid and cards.did = " + deckid)
        return self._fixRawListOfAnkiCards(listofAnkiCards)

    def getDictOfAllDecks(self):
        """Returns dictionary of all decks in apkg."""
        deckDictJson = self._selectOnDb("SELECT decks from col")[0][0]
        return loads(deckDictJson)



