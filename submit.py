from fox_submission_solver import submit_fox_attempt, end_fox,test_submit_fox_attempt
import configparser

CONFIG_PATH = "fox_config.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

TEAM_ID = config["DEFAULT"]["TEAM_ID"]


test_submit_fox_attempt("aaaaaaaaaaaaa")
# end_fox(TEAM_ID)
