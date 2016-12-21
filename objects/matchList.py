from objects import match
from objects import glob
from constants import serverPackets
from common.log import logUtils as log

class matchList:
	def __init__(self):
		"""Initialize a matchList object"""
		self.matches = {}
		self.lastID = 1

	def createMatch(self, matchName, matchPassword, beatmapID, beatmapName, beatmapMD5, gameMode, hostUserID):
		"""
		Add a new match to matches list

		:param matchName: match name, string
		:param matchPassword: match md5 password. Leave empty for no password
		:param beatmapID: beatmap ID
		:param beatmapName: beatmap name, string
		:param beatmapMD5: beatmap md5 hash, string
		:param gameMode: game mode ID. See gameModes.py
		:param hostUserID: user id of who created the match
		:return: match ID
		"""
		# Add a new match to matches list and create its stream
		matchID = self.lastID
		self.lastID+=1
		self.matches[matchID] = match.match(matchID, matchName, matchPassword, beatmapID, beatmapName, beatmapMD5, gameMode, hostUserID)
		return matchID

	def disposeMatch(self, matchID):
		"""
		Destroy match object with id = matchID

		:param matchID: ID of match to dispose
		:return:
		"""
		# Make sure the match exists
		if matchID not in self.matches:
			return

		# Remove match object and stream
		match = self.matches.pop(matchID)
		glob.streams.dispose(match.streamName)
		glob.streams.dispose(match.playingStreamName)
		glob.streams.remove(match.streamName)
		glob.streams.remove(match.playingStreamName)

		# Send match dispose packet to everyone in lobby
		glob.streams.broadcast("lobby", serverPackets.disposeMatch(matchID))