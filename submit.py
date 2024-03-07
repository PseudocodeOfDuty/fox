from fox_submission_solver import submit_fox_attempt, end_fox
import configparser

CONFIG_PATH = "fox_config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

TEAM_ID = config["DEFAULT"]["TEAM_ID"]


# submit_fox_attempt(TEAM_ID)
# end_fox(TEAM_ID)
