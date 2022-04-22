import constants

class Player_General:
    def __init__(self):
        self.__Name = "NoName"
        self.__Race = "NoRace"
        self.__Class = "NoClass"
        self.__Prof = "NoProffetion"
        self.__Spec = "NoSpecialization"
        self.__Rank = "NoRank"
        self.__Rel = "NoReligion"
    def __getPlayerStat(self):
        return self.__dict__
    def __setName(self,NewName):
        try:
            if NewName.isalpha():
                self.__Name = NewName
        except AttributeError:
            print("Ваше имя не может состоять из цифр")
    def __getName(self):
        return self.__Name
    def __setRace(self,NewRace):
        if NewRace in constants.Races.keys():
            self.__Race = NewRace
        else:
            print("Вы вписали несуществующую расу")
    def __getRace(self):
        return self.__Race
    def __setClass(self,NewClass):
        if NewClass in constants.Class.keys():
            self.__Class = NewClass
        else:
            print("Вы вписали несуществующий класс")
    def __getClass(self):
        return self.__Class
    def __setProf(self,NewProf):
        if NewProf in constants.Profs.keys():
            self.__Prof = NewProf
        else:
            print("Вы вписали несуществующую професию")
    def __getProf(self):
        return self.__Prof
    def __setSpec(self,NewSpec):
        if NewSpec in constants.Specs.keys():
            self.__Spec = NewSpec
        else:
            print("Вы вписали несуществующую специализацию")
    def __getSpec(self):
        return self.__Spec
    def __setRank(self,NewRank):
        if NewSpec in constants.Ranks:
            self.__Rank = NewRank
        else:
            print("Вы вписали несуществующий ранг")
    def __getRank(self):
        return self.__Rank
    def __setRel(self,NewRel):
        if NewRel in constants.Religions:
            self.__Rel = NewRel
        else:
            print("Вы вписали несуществующую религию")
    def __getRel(self):
        return self.__Rel
    Name = property(__getName,__setName)
    Race = property(__getRace,__setRace)
    Class = property(__getClass,__setClass)
    Prof = property(__getProf,__setProf)
    Spec = property(__getSpec,__setSpec)
    Rank = property(__getRank,__setRank)
    Rel = property(__getRel,__setRel)
    info = property(__getPlayerStat)
class Player_Inventory:
    pass
class Player_Skills:
    pass
player = Player_General()
print(player.info)
player.Name = "Clyoucker"
player.Race = "Человек"
player.Class = "Воин"
player.Prof = "Паладин"
player.Spec = "Авангард"
player.Rel = "Сихритизм"
print(player.info)

PlayerStats = {player.Race: constants.Races[player.Race],
                player.Class: constants.Class[player.Class],
                player.Prof: constants.Profs[player.Prof],
                player.Spec: constants.Specs[player.Spec],}
print(PlayerStats)