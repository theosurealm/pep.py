"""Contain server and client packet IDs"""
client_changeAction = 0 #osu! wishes to inform bancho about its current state.
client_sendPublicMessage = 1 #osu! sends a chat message to bancho.
client_logout = 2 #osu! is closing.
client_requestStatusUpdate = 3 #osu! wants to get new stats for the local player.
client_pong = 4 #osu! replies to a ping request.
server_userID = 5 #Bancho replies to a login request.
server_commandError = 6 #Bancho warns osu! of an error.
server_sendMessage = 7 #Bancho is proxying an irc message to osu!.
server_ping = 8 #Bancho is requesting a ping from osu!.
server_handleIRCUsernameChange = 9 #Bancho is informing osu! of an IRC username change.
server_handleIRCQuit = 10 #Bancho is informing osu! of an IRC user quitting.
server_userStats = 11 #Bancho is informing osu! of a stat update for another user.
server_userLogout = 12 #Bancho is informing osu! that an osu! user quit.
server_spectatorJoined = 13 #Tells the host that a spectator has joined.
server_spectatorLeft = 14 #Tells the host that a spectator has left.
server_spectateFrames = 15 #Bancho is sending spectator frames (as a bundle) to spectators.
client_startSpectating = 16 #osu! client has requested to spectate someone.
client_stopSpectating = 17 #osu! client wants to stop spectating altogether.
client_spectateFrames = 18 #osu! is sending gameplay frames to be redistributed to spectators.
server_versionUpdate = 19 #Bancho is telling osu! to check for new versions.
client_errorReport = 20 #osu! is sending an error report to be forwarded to peppy... wait... peppy!?
client_cantSpectate = 21 #osu! is informing Bancho that it is unable to spectate the current host.
server_spectatorCantSpectate = 22 #Bancho is informing the host that a spectator can't tune in.
server_getAttention = 23 #Bancho forces osu!'s chat window to surface.
server_notification = 24 #Bancho wants osu! to display an announcement popup.
client_sendPrivateMessage = 25 #Bancho is forwarding a private message from another osu!/IRC client.
server_updateMatch = 26 #Bancho is sending an update for a particular match's details.
server_newMatch = 27 #Bancho is sending a new match entry.
server_disposeMatch = 28 #Bancho is sending notification that a match has been disbanded.
client_partLobby = 29 #osu! has left the multiplayer lobby.
client_joinLobby = 30 #osu! has joined the multiplayer lobby.
client_createMatch = 31 #osu! has created a new multiplayer match.
client_joinMatch = 32 #osu! wants to join a multiplayer match.
client_partMatch = 33 #osikeu! wants to leave the current match.
server_joinLobby_UNUSED = 34 #Bancho informs osu! that a player has joined the lobby.
server_partLobby_UNUSED = 35 #Bancho informs osu! that a player has left the lobby.
server_matchJoinSuccess = 36
server_matchJoinFail = 37
client_matchChangeSlot = 38
client_matchReady = 39
client_matchLock = 40
client_matchChangeSettings = 41
server_fellowSpectatorJoined = 42
server_fellowSpectatorLeft = 43
client_matchStart = 44
allPlayersLoaded = 45
server_matchStart = 46
client_matchScoreUpdate = 47
server_matchScoreUpdate = 48
client_matchComplete = 49
server_matchTransferHost = 50
client_matchChangeMods = 51
client_matchLoadComplete = 52
server_matchAllPlayersLoaded = 53
client_matchNoBeatmap = 54
client_matchNotReady = 55
client_matchFailed = 56
server_matchPlayerFailed = 57
server_matchComplete = 58
client_matchHasBeatmap = 59
client_matchSkipRequest = 60
server_matchSkip = 61
server_unauthorized = 62
client_channelJoin = 63
server_channelJoinSuccess = 64
server_channelInfo = 65
server_channelKicked = 66
server_channelAvailableAutojoin = 67
client_beatmapInfoRequest = 68
server_beatmapInfoReply = 69
client_matchTransferHost = 70
server_supporterGMT = 71
server_friendsList = 72
client_friendAdd = 73
client_friendRemove = 74
server_protocolVersion = 75
server_mainMenuIcon = 76
client_matchChangeTeam = 77
client_channelPart = 78
client_receiveUpdates = 79
server_topBotnet = 80
server_matchPlayerSkipped = 81
client_setAwayMessage = 82
server_userPanel = 83
irc_only = 84
client_userStatsRequest = 85
server_restart = 86
client_invite = 87
server_invite = 88
server_channelInfoEnd = 89
client_matchChangePassword = 90
server_matchChangePassword = 91
server_silenceEnd = 92
client_tournamentMatchInfoRequest = 93
server_userSilenced = 94
server_userPanelSingle = 95
server_userPresenceBundle = 96
client_userPanelRequest = 97
client_userPanelRequestAll = 98
client_userToggleBlockNonFriendPM = 99
server_userPMBlocked = 100
server_targetIsSilenced = 101
server_versionUpdateForced = 102 #Bancho is telling osu! to check for new versions.
server_switchServer = 103 
server_accountRestricted = 104
server_rtx = 105
client_matchAbort = 106
server_matchAbort = 106
server_switchServer = 107 #Bancho is telling osu! to switch to/from tourney server.
client_tournamentJoinMatchChannel = 108 #Tournament client is requesting to join the multiplayer match channel.
client_tournamentLeaveMatchChannel = 109 #Tournament client is requesting to leave the multiplayer match channel.
