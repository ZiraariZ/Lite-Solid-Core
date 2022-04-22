import time
import os
import sys
import formuls
import constants
import os.path
os.chdir(sys.path[0])

clears = lambda:os.system("cls")
def Help_checker(check):
	check = check.lower(); check = check.title()
	while True:
		if "  " in check:
			check = check.replace("  "," ")
		else:
			break
	if check == "/Back":
		return check
	elif check.isspace() or len(check) < 6:
		return "Error"
	else:
		check = check[6:]; check = check.rstrip()
		if check.isalpha():
			print(check)
			return check
		else:
			return "Error"
def Helper():
	while True:
		print("Helper:Помошник по командам")
		print("[/Info Commands]")
		user = input("Поиск: ")
		user = Help_checker(user)
		if os.path.exists("Assets/Commands/"+user+".txt"):
			with open("Assets/Commands/"+user+".txt", "r", encoding="utf-8") as file:
				clears()
				print(file.read())
		elif os.path.exists("Assets/Langs/"+user+".txt"):
			with open("Assets/Langs/"+user+".txt", "r", encoding="utf-8") as file:
				clears()
				print(file.read())
		elif os.path.exists("Assets/Races/"+user+".txt"):
			with open("Assets/Races/"+user+".txt", "r", encoding="utf-8") as file:
				clears()
				print(file.read())
		elif os.path.exists("Assets/Rangs/"+user+".txt"):
			with open("Assets/Rangs/"+user+".txt", "r", encoding="utf-8") as file:
				clears()
				print(file.read())
		elif os.path.exists("Assets/Religions/"+user+".txt"):
			with open("Assets/Religions/"+user+".txt", "r", encoding="utf-8") as file:
				clears()
				print(file.read())
		elif os.path.exists("Assets/Skills/"+user+".txt"):
			with open("Assets/Skills/"+user+".txt", "r", encoding="utf-8") as file:
				clears()
				print(file.read())
		elif user == "/Back":
			break
		else:
			clears()
			print("Error!""\n""Помошник не нашёл информацию об этом элементе или его не существует!")
def Action():
	while True:
		print("Action:Функция обработки действий персонажа")
		act = input("Действие: "); act = act.lower(); act = act.title(); act = act.strip()
		if act == "/Learn":
			if "Мудрость" in PlayerSkills["Skills"]:
				print(formuls.Learn(PlayerInfo["Class"], PlayerChar["Мудрость"], constants.SkillsBonus["Мудрость"]))
			else:
				print(formuls.Learn(PlayerInfo["Class"], 0, 0))
		elif act == "/Sell":
			if "Торговля" in PlayerSkills["Skills"]:
				print(formuls.Sell(3600,1200,PlayerChar["Торговля"], constants.SkillsBonus["Торговля"]["Продажа"]))
			else:
				print(formuls.Sell(3600, 1200, 0, 0))
		elif act == "/Buy":
			if "Торговля" in PlayerSkills["Skills"]:
				print(formuls.Buy(3600, 1200, PlayerChar["Торговля"], constants.SkillsBonus["Торговля"]["Покупка"]))
			else:
				print(formuls.Buy(3600, 1200, 0, 0))
		elif act == "/Proof":
			if "Социальность" in PlayerSkills["Skills"]:
				print(formuls.Proof(PlayerChar["Социальность"], constants.SkillsBonus["Социальность"]))
			else:
				print(formuls.Proof(0, 0))
		elif act == "/Check":
			if "Внимательность" in PlayerSkills["Skills"]:
				print(formuls.Check(PlayerChar["Внимательность"], constants.SkillsBonus["Внимательность"]))
			else:
				print(formuls.Check(0, 0))
		elif act == "/Hack":
			if "Взлом" in PlayerSkills["Skills"]:
				print(formuls.Hack(PlayerChar["Взлом"], constants.SkillsBonus["Взлом"]))
			else:
				print(formuls.Hack(0, 0))
		elif act == "/Steal":
			if "Воровство" in PlayerSkills["Skills"]:
				print(formuls.Steal(PlayerChar["Воровство"], constants.SkillsBonus["Воровство"]))
			else:
				print(formuls.Steal(0, 0))
		elif act == "/Dodge":
			if "Ловкость" in PlayerSkills["Skills"]:
				print(formuls.Dodge(PlayerChar["Ловкость"], constants.SkillsBonus["Ловкость"]))
			else:
				print(formuls.Dodge(0, 0))
		elif act == "/Craft":
			if "Изобритательность" in PlayerSkills["Skills"]:
				print(formuls.Craft(PlayerChar["Изобритательность"], constants.SkillsBonus["Изобритательность"]))
			else:
				print(formuls.Craft(0, 0))
		elif act == "/Block":
			if "Сила" in PlayerSkills["Skills"]:
				print(formuls.Craft(PlayerChar["Сила"], constants.SkillsBonus["Сила"]))
			else:
				print(formuls.Craft(0, 0))
		elif act == "/Back":
			break
		else:
			print("Error: Action не способен обработать такой запрос ["+act+"]")
def Requests(searh):
	r"""Обрабатывает основные команды, такие как /Create,/Load,/Sace,/Esc,/Help,/Ver"""
	searh = searh.lower(); searh = searh.title();  searh = searh.strip()
	if searh == "/Help":
		clears()
		Helper()
	elif searh == "/Create":
		clears()
		print("Эта функция не работает")
	elif searh == "/Load":
		clears()
		print("Эта функция не работает")
	elif searh == "/Save":
		clears()
		print("Эта функция не работает")
	elif searh == "/Action":
		clears()
		Action()
	elif searh =="/Ver":
		print("LSC-Public-Version-3.0-Beta")
	elif searh =="/Esc":
		return "Break"
	else:
		print("Error: Requests не способен обработать такой запрос["+searh+"]")


PlayerInfo = {"Name": "Clyoucker", "Race": "Человек", "Class": "Никто", "Prof": "Паладин", "Spec": "Авангард", "Religion": "Сихритизм"}
PlayerSkills = {"Skills":["Мудрость", "Мастерство", "Сила", "Телосложение", "Адаптивность", "Воля", "Разведка", "Внимательность", "Ресурсы"]}
PlayerStats = {PlayerInfo["Race"]: constants.Races[PlayerInfo["Race"]],
			PlayerInfo["Class"]: constants.Class[PlayerInfo["Class"]],
			PlayerInfo["Prof"]: constants.Profs[PlayerInfo["Prof"]],
			PlayerInfo["Spec"]: constants.Specs[PlayerInfo["Spec"]]}
PlayerChar = {PlayerSkills["Skills"][0]: 4,
			PlayerSkills["Skills"][1]: 3,
			PlayerSkills["Skills"][2]: 3,
			PlayerSkills["Skills"][3]: 2,
			PlayerSkills["Skills"][4]: 2,
			PlayerSkills["Skills"][5]: 2,
			PlayerSkills["Skills"][6]: 1,
			PlayerSkills["Skills"][7]: 1,
			PlayerSkills["Skills"][8]: 1}
startTime = time.time()



while True:
	clears()
	print("Requests:Функция обработки основных запросов")
	print("[/Help][/Create][/Load][/Save][/Action][/Ver][/Esc]")
	x = Requests(str(input("Введите команду: ")))
	if x =="Break":
		print("Программа завершена и данные обновлены")
		break

endTime = time.time()
totalTime = endTime - startTime
print("Время, затраченное на выполнение данного кода = ", totalTime)

r"""
def inputs():
	user_info = dict()
	user_info_skills = dict()

	user_info["Name"] = (str(input("Введите имя персонажа")))
	user_info["Race"] = (str(input("Введите расу персонажа")))
	user_info["Class"] = (str(input("Введите класс персонажа")))
	user_info["Profession"] = (str(input("Введите профессию персонажа")))
	user_info["Specialization"] = (str(input("Введите специализацию персонажа")))
	user_info["Religion"] = (str(input("Введите религию персонажа")))

	skills = input("Введите 9 навыков через пробел")
	if "  " in skills:
		skills = skills.replace("  "," ")
	skills = skills.split()
	user_info_skills["Skills"] = skills

	return user_info

print(inputs())
"""