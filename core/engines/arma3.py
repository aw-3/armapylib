import ctypes

api = ctypes.cdll.LoadLibrary("core/engines/arma3.dll")

api.Execute.argtypes = [ctypes.c_char_p]
def execute(s):
	api.Execute(s.encode("utf8"))

def execute_remote(s, server_only):
	if server_only:
		s = "if (isServer) then { " + s + "};"

	execute("""rereported = {'C_man_1' createUnit [[0, 0, 0], (createGroup west), (_this select 0), 1.0, "MAJOR"];}; ['%s'] call rereported; """ % s)

def execute_remote_player(s, player_name):
	s = ("""if (name player == "%s") then { """  % player_name) + s + "};"
	x = """apl_reported = {'C_man_1' createUnit [[0, 0, 0], (createGroup west), (_this select 0), 1.0, "MAJOR"];}; ['%s'] call apl_reported; """ % s
	execute(x)


api.GetAllVariables.argtypes = None
api.GetAllVariables.restype = ctypes.py_object
def get_mission_variables():
	return api.GetAllVariables()

api.GetAllAddons.argtypes = None
api.GetAllAddons.restype = ctypes.py_object
def get_addons():
	return api.GetAllAddons()

api.GetPlayers.argtypes = None
api.GetPlayers.restype = ctypes.py_object
def get_players():
	return api.GetPlayers()

api.GetRunningScripts.argtypes = None
api.GetRunningScripts.restype = ctypes.py_object
def get_running_scripts():
	return api.GetRunningScripts()


""" current methods
void execute(str)
void execute_remote(str, bool)
void execute_remote_player(str, str)
list get_players()
list get_addons()
list get_running_scripts()
list get_mission_variables()

# future methods?
# is_arma_running
# is_ingame
# get_localplayer
"""