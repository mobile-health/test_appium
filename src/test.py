from appium import webdriver
import pathlib
import json

path = str(pathlib.Path(__file__).parent.resolve())

desired_cap_file = path + "/../desired_cap.json"

with open(desired_cap_file) as f:
    desired_cap = json.load(f)

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


print("ToanTK")
