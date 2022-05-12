import json
import math
import time
import ast
import requests
from os import name
import threading
from kivymd.app import MDApp
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivymd.theming import ThemeManager
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.config import Config
from kivy.core.window import Window

#Config.set('graphics', 'width', '1200')
#Config.set('graphics', 'height', '800')
#Config.write()
ItemNamesList = []
ItemList = []
txtlist = []
ddd=-1000000
h=[]
with open('babes.json', encoding="utf-8") as f:
    h = json.load(f)
    f.close()
jow= "none" 
jowe= "none"
ruwans = ["Saved Items"]
biwans= ["Saved Items"]
jiwanshe = ["Items we found"]
biwanshee= ["Items we found"]
bababe = False
secopa = False
fircha = False
seccha = False
cienz = 0
yberi = 1
bassherre= 1
reqlvla = "My Level"
reqlvlmin = 1
reqduraa = 1
reqstra = 0
reqdexa = 0
reqinta = 0
reqdefa = 0
reqagila = 0
reqlowa = 0
reqchaa = 0
filterinb = "What Item do you want to make?".upper()
filterina = "What Item do you want to make?".upper()
biltera = "What Identification do you want to optimize for?".upper()
bilterba = "What Identification do you want to optimize foras well?".upper()
cilteraa = "Check for unwanted ID #1".upper()
cilterba = "Check for unwanted ID #2".upper()
id_filter_twoa = 0
id_check_onea = 0
id_check_twoa = 0
rar1a = 0
rar2a = 0
chichia = False
chuchua = False
chachaa = False
your_moms_lock = threading.Lock()
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    def shisha(self):
        global ItemNamesList
        response = requests.get("https://api.wynncraft.com/v2/ingredient/list")
        ItemNamesList = response.json()["data"]
        print(len(ItemNamesList))
        self.bartender()
    def bartender(self):
        t = threading.Thread(target=self.bababui, args=())
        t.daemon = True
        t.start()
    def bababui(self):
        global ItemList
        sua=[]
        uaiieieie = 0
        for i in ItemNamesList:
            print("in loops")
            soe = "https://api.wynncraft.com/v2/ingredient/get/" + i
            if i == "Old Treasure":
                soe ="https://api.wynncraft.com/v2/ingredient/get/" + "Old Treasure\u058e"
            bsbs = requests.get(soe)
            print(bsbs.json())
            if "code" in bsbs.json():
                huai = bsbs.json()["data"]
                print(bsbs)
                uaiieieie +=1
                ItemList.append(huai[0])
            else:
                print("bsbs")
                time.sleep(30)
                soe = "https://api.wynncraft.com/v2/ingredient/get/" + i
                bsbs = requests.get(soe)
                print(bsbs.json())
                if "code" in bsbs.json():
                    huai = bsbs.json()["data"]
                    ItemList.append(huai[0])
                    print("resloved")
                else:
                    print("oo stinkyy")
                    break
        print(uaiieieie)
        print(sua)
        with open('babes.json', 'w', encoding="utf-8") as de:
            json.dump(ItemList, de) 
        global h
        h = ItemList
        print("done")
class ScreenNav(Screen):
    pass
class BoxLayoutExample(Screen):
    screen_manager = ObjectProperty()
    def durabmod(self, *args):
        global chichia
        chichia = args[1]
    def skillmod(self, *args):
        global chuchua
        chuchua = args[1]
    def negatmod(self, *args):
        global chachaa
        chachaa = args[1]
    def flippedmod(self, *args):
        global bababe
        bababe = args[1]
    def lirroo(self, *args):
        rrre = str(int(pow(1.3,args[1])))
        self.yore.text = rrre
        self.callmyname(rrre)
    def rarityonechanger(self, text):
        global rar1a
        rar1a = int(text)
    def raritytwochanger(self, text):
        global rar2a
        rar2a = int(text)
    def callmyname(self, easier):
        global reqlowa
        reqlowa = int(easier)
    def callmynametxt(self, *args):
        global reqlowa
        try:
            boks = int(args[0].text)
            if boks > 10000:
                args[0].text = "10000"
                boks = 10000
            elif boks < 0:
                boks = 0
                args[0].text = "0"
            else:
                args[0].text = str(boks)
        except:
            boks = 0
            args[0].text = "0"
        reqlowa = boks
    def justdoit(self, *args):
        global biltera
        biltera = args[1].upper()
    def changeingr(self, *args):
        listo=["What Item do you want to make?", "Helmet", "Chestplate", "Boots", "Leggings", "Ring", "Bracelet", "Necklace", "Spear", "Dagger", "Relik", "Bow", "Wand", "Food", "Potion", "Scroll"]
        listering=["What Item do you want to make?", "armouring", "armouring", "tailoring", "tailoring", "jeweling", "jeweling", "jeweling", "weaponsmithing", "weaponsmithing", "woodworking", "woodworking", "woodworking", "cooking", "alchemism", "scribing"]
        listreee=["Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum durability:", "Minmum duration:", "Minmum duration:", "Minmum duration:"]
        liststone=["Choose what you want to craft first:", "Ingots:", "Ingots:", "Ingots:", "Ingots:", "Oil:", "Oil:", "Oil:", "Ingots:", "Ingots:", "Oil:", "Sring:", "Sring:", "Meat:", "Grains:", "Paper:"]
        listtwo=["Choose what you want to craft first:", "Paper:", "Paper:", "Sring:", "Sring:", "Gems:", "Gems:", "Gems:", "Wood:", "Wood:", "Wood:", "Wood:", "Wood:", "Grains:", "Oil:", "Oil:"]
        self.bes.text = liststone[listo.index(args[1])]
        self.tes.text = listtwo[listo.index(args[1])]
        global filterina
        global filterinb
        filterinb = args[1]
        filterina = listering[listo.index(args[1])].upper()
    
class SecondSpinner(BoxLayout):
    def powerforathing(self, *args):
        rrre = str(int(pow(2,args[1])))
        self.expo.text = rrre
        self.powerforabing(rrre)
    def sec_optim_bool(self, *args):
        global secopa
        secopa = args[1]
    def secopdili(self, *args):
        global bilterba
        bilterba = args[1].upper()
    def powerforabing(self, easi):
        global id_filter_twoa
        id_filter_twoa = int(easi)
    def powerforabingtxt(self, *args):
        global id_filter_twoa
        try:
            boks = int(args[0].text)
            if boks > 10000:
                args[0].text = "10000"
                boks = 10000
            elif boks < 0:
                boks = 0
                args[0].text = "0"
            else:
                args[0].text = str(boks)
        except:
            boks = 0
            args[0].text = "0"
        id_filter_twoa = int(boks)
class FirstSpinnerCheck(BoxLayout):
    def powerfortwothing(self, *args):
        rrre = str(int(-pow(2,args[1])))
        self.rego.text = rrre
        self.powerfortwobing(rrre)
    def fir_check_bool(self, *args):
        global fircha
        fircha = args[1]
    def firchdili(self, *args):
        global cilteraa
        cilteraa = args[1].upper()
    def powerfortwobing(self, easi):
        global id_check_onea
        id_check_onea = int(easi)
    def powerfortwobingtxt(self, *args):
        global id_check_onea
        try:
            boks = int(args[0].text)
            if boks > 10000:
                args[0].text = "10000"
                boks = 10000
            elif boks <= -10000:
                boks = -9999
                args[0].text = "-9999"
            else:
                args[0].text = str(boks)
        except:
            boks = 0
            args[0].text = "0"
        id_check_onea = int(boks)

class SecondSpinnerCheck(BoxLayout):
    def powerforthreething(self, *args):
        rrre = str(int(-pow(2,args[1])))
        self.bergo.text = rrre
        self.powerfortwobing(rrre)
    def sec_check_bool(self, *args):
        global seccha
        seccha = args[1]
    def secchdili(self, *args):
        global cilterba
        cilterba = args[1].upper()
    def powerforthreebing(self, easi):
        global id_check_twoa
        id_check_twoa = int(easi)
    def powerforthreebingtxt(self, *args):
        global id_check_twoa
        try:
            boks = int(args[0].text)
            if boks > 10000:
                args[0].text = "10000"
                boks = 10000
            elif boks <= -10000:
                boks = -9999
                args[0].text = "-9999"
            else:
                args[0].text = str(boks)
        except:
            boks = 0
            args[0].text = "0"
        id_check_twoa = int(boks)
    def powerforthreething(self, *args):
        self.bergo.text = str(int(-pow(2,args[1])))
class OutputScreen(Screen):
    screen_manager = ObjectProperty()
    def save_item(self):
        global ruwans
        global biwans
        if jow != "none":
            with open('saved_items.txt', 'a', encoding="utf-8") as k:
                k.write(jow + '\ns\n')
                k.write(jowe + '\nr\n')
                ruwans.append(jow)
                biwans.append(jowe)
        else:
            content = Button(text="OK")
            popup = Popup(title='Choose Item First', content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
            content.bind(on_press=popup.dismiss)
            popup.open()
            self.screen_manager.current = "input"
    def printjiw(self):
        asa = int((len(jiwanshe)-1)/1000)+1
        if(asa == yberi):
            eb = yberi*1000-1000
            self.kokokei.values = biwanshee[eb:]
        else:
            eb = yberi*1000-1000
            kb = yberi*1000
            self.kokokei.values = biwanshee[eb:kb]
    def changeyourlife(self, *args):
        global bassherre
        global jow
        global jowe
        bassherre = 1
        bre = ast.literal_eval(jiwanshe[biwanshee.index(args[1])])
        if biwanshee.index(args[1])==0 and args[1]=="Items we found":
            self.ithinkso.text = "Choose an Item"
            jow = "none"
            jowe = "none"
        else:
            jow = args[1]
            a={}
            b={}
            c={}
            d={}
            e={}
            f={}
            soos = {"name": "Empty Slot", "tier": 0, "level": 1, "skills": ["WEAPONSMITHING", "ARMOURING", "WOODWORKING"], "sprite": {"id": 888888, "damage": 0}, "identifications":{}, "itemOnlyIDs": {"durabilityModifier": 0, "strengthRequirement": 0, "dexterityRequirement": 0, "intelligenceRequirement": 0, "defenceRequirement": 0, "agilityRequirement": 0}, "consumableOnlyIDs": {"duration": 0, "charges": 0}, "ingredientPositionModifiers": {"left": 0, "right": 0, "above": 0, "under": 0, "touching": 0, "notTouching": 0}}
            for i in h:
                if i["name"] == bre['firstSlot']:
                    a=i
                if i["name"] == bre['secondSlot']:
                    b=i 
                if i["name"] == bre['thirdSlot']:
                    c=i
                if i["name"] == bre['fourthSlot']:
                    d=i
                if i["name"] == bre['fifthSlot']:
                    e=i
                if i["name"] == bre['sixthSlot']:
                    f=i
            if soos["name"] == bre['firstSlot']:
                a=soos
            if soos["name"] == bre['secondSlot']:
                b=soos 
            if soos["name"] == bre['thirdSlot']:
                c=soos
            if soos["name"] == bre['fourthSlot']:
                d=soos
            if soos["name"] == bre['fifthSlot']:
                e=soos
            if soos["name"] == bre['sixthSlot']:
                f=soos
            fir = 0 + b['ingredientPositionModifiers']['touching'] + c['ingredientPositionModifiers']['touching'] + d['ingredientPositionModifiers']['notTouching'] + e['ingredientPositionModifiers']['notTouching'] + f['ingredientPositionModifiers']['notTouching'] + c['ingredientPositionModifiers']['above'] + e['ingredientPositionModifiers']['above'] + b['ingredientPositionModifiers']['left']
            sec = 0 + a['ingredientPositionModifiers']['touching'] + c['ingredientPositionModifiers']['notTouching'] + d['ingredientPositionModifiers']['touching'] + e['ingredientPositionModifiers']['notTouching'] + f['ingredientPositionModifiers']['notTouching'] + d['ingredientPositionModifiers']['above'] + f['ingredientPositionModifiers']['above'] + a['ingredientPositionModifiers']['right']
            thir = 0 + a['ingredientPositionModifiers']['touching'] + b['ingredientPositionModifiers']['notTouching'] + d['ingredientPositionModifiers']['touching'] + e['ingredientPositionModifiers']['touching'] + f['ingredientPositionModifiers']['notTouching'] + a['ingredientPositionModifiers']['under'] + e['ingredientPositionModifiers']['above'] + d['ingredientPositionModifiers']['left']
            four = 0 + a['ingredientPositionModifiers']['notTouching'] + b['ingredientPositionModifiers']['touching'] + c['ingredientPositionModifiers']['touching'] + e['ingredientPositionModifiers']['notTouching'] + f['ingredientPositionModifiers']['touching'] + b['ingredientPositionModifiers']['under'] + f['ingredientPositionModifiers']['above'] + c['ingredientPositionModifiers']['right']
            fif = 0 + a['ingredientPositionModifiers']['notTouching'] + b['ingredientPositionModifiers']['notTouching'] + c['ingredientPositionModifiers']['touching'] + d['ingredientPositionModifiers']['notTouching'] + f['ingredientPositionModifiers']['touching'] + a['ingredientPositionModifiers']['under'] + c['ingredientPositionModifiers']['under'] + f['ingredientPositionModifiers']['left']
            six = 0 + a['ingredientPositionModifiers']['notTouching'] + b['ingredientPositionModifiers']['notTouching'] + c['ingredientPositionModifiers']['notTouching'] + d['ingredientPositionModifiers']['touching'] + e['ingredientPositionModifiers']['touching'] + b['ingredientPositionModifiers']['under'] + d['ingredientPositionModifiers']['under'] + e['ingredientPositionModifiers']['right']
            identsheesh=[]
            for i in a["identifications"]:
                if i not in identsheesh:
                    identsheesh.append(i)
            for j in b["identifications"]:
                if j not in identsheesh:
                    identsheesh.append(j)
            for k in c["identifications"]:
                if k not in identsheesh:
                    identsheesh.append(k)
            for l in d["identifications"]:
                if l not in identsheesh:
                    identsheesh.append(l)
            for m in e["identifications"]:
                if m not in identsheesh:
                    identsheesh.append(m)
            for n in f["identifications"]:
                if n not in identsheesh:
                    identsheesh.append(n)
            zorte = (bre["what"] + "-"+bre["lvl"]+": "+"dura: " + str(bre["durability"]) + " chance: "
            + str(bre["chance"])+ "%" + "\n" + str(biltera).lower().capitalize()+": " + str(bre["low"])+"->"+str(bre[biltera]) + " ")
            for i in identsheesh:
                if i!=biltera:
                    if i not in a['identifications']:
                        a['identifications'][i] = {"minimum": 0, "maximum": 0} 
                    if i not in b['identifications']:
                        b['identifications'][i] = {"minimum": 0, "maximum": 0}
                    if i not in c['identifications']:
                        c['identifications'][i] = {"minimum": 0, "maximum": 0}
                    if i not in d['identifications']:
                        d['identifications'][i] = {"minimum": 0, "maximum": 0}
                    if i not in e['identifications']:
                        e['identifications'][i] = {"minimum": 0, "maximum": 0}
                    if i not in f['identifications']:
                        f['identifications'][i] = {"minimum": 0, "maximum": 0}
                    op=math.floor(a['identifications'][i]['maximum']*(1+fir/100)) + math.floor(b['identifications'][i]['maximum']*(1+sec/100)) + math.floor(c['identifications'][i]['maximum']*(1+thir/100)) + math.floor(d['identifications'][i]['maximum']*(1+four/100)) + math.floor(e['identifications'][i]['maximum']*(1+fif/100)) + math.floor(f['identifications'][i]['maximum']*(1+six/100))
                    dop=math.floor(a['identifications'][i]['minimum']*(1+fir/100)) + math.floor(b['identifications'][i]['minimum']*(1+sec/100)) + math.floor(c['identifications'][i]['minimum']*(1+thir/100)) + math.floor(d['identifications'][i]['minimum']*(1+four/100)) + math.floor(e['identifications'][i]['minimum']*(1+fif/100)) + math.floor(f['identifications'][i]['minimum']*(1+six/100))
                    if (op >= dop) and (op != 0  or dop !=0):
                        zorte+=i.lower().capitalize() + ": "
                        zorte+=str(dop) + "->"
                        zorte+=str(op) + " "
                        if(bassherre==0):
                            bassherre += 1
                        else:
                            zorte += "\n"
                            bassherre = 0
                    elif (op != 0  or dop !=0):
                        zorte+=i.lower().capitalize() + ": "
                        zorte+=str(op) + "-"
                        zorte+=str(dop) + " "
                        if(bassherre==0):
                            bassherre += 1
                        else:
                            zorte += "\n"
                            bassherre = 0
            if(bassherre == 0):
                pass
            elif(bassherre == 1):
                zorte += "\n"
            zorte+=("Skillrequirements:"+ "\n" + "Strength Requirement: " + str(bre["strengthRequirement"])
            + " Dexterity Requirement: " + str(bre["dexterityRequirement"])+"\n"
            + "Intelligence Requirement: " + str(bre["intelligenceRequirement"])
            + " Defence Requirement: " + str(bre["defenceRequirement"])+"\n"
            + "Agility Requirement: " + str(bre["agilityRequirement"])+ "\n" )
            zorte+= "Ingredients:\n"
            lorte = zorte 
            zorte+= (    bre['firstSlot'] + "   " + bre['secondSlot'] + "\n" + 
                bre['thirdSlot'] + "   " + bre['fourthSlot'] + "\n" + 
                bre['fifthSlot'] + "   " + bre['sixthSlot'])
            shorte = bre['firstSlot']+"\n" +"\n"+ bre['thirdSlot']+"\n" +"\n"+ bre['fifthSlot']
            shirte = bre['secondSlot']+"\n"+"\n" + bre['fourthSlot']+"\n" +"\n"+ bre['sixthSlot']
            jowe = zorte
            self.ithinkso.text = lorte
            self.idonot.text = shorte
            self.idonte.text = shirte
    def changethousand(self, *args):
        global yberi
        yberi = int(args[1])
    def thousanddivider(self):
        global jiwanshe
        op = int((len(jiwanshe)-1)/1000)+1
        lsel = []
        for i in range(op):
            lsel.append(str(i+1))
        self.reesaa.values = lsel
class SavedItemsScreen(Screen):
    screen_manager = ObjectProperty()
    global ruwans
    global biwans
    global txtlist
    hiser = ""
    with open('saved_items.txt', encoding="utf-8") as we:
        loien = we.readlines()
    for i in loien:
        if i == 's\n':
            if hiser != "":
                hiser = "\n"+hiser
                ruwans.append(hiser)
                txtlist.append(hiser)
                txtlist.append('s\n')
                hiser = ""
        elif i == 'r\n':
            if hiser != "":
                biwans.append(hiser)
                hiser = ""
                txtlist.append(hiser)
            txtlist.append('r\n')
        else:
            hiser+=i
    def delete_item(self):
        global txtlist
        global ruwans
        global biwans
        if len(txtlist) >4:
            ruwans.remove(ruwans[len(ruwans)-1])
            biwans.remove(biwans[len(biwans)-1])
            self.savebute.text = "Saved Items"
            self.leftrow.text = "Saved Items"
            self.rightrow.text = "Saved Items"
            self.savedite.text = "Saved Items"
            txtlist.remove(txtlist[len(txtlist)-1])
            txtlist.remove(txtlist[len(txtlist)-1])
            txtlist.remove(txtlist[len(txtlist)-1])
            txtlist.remove(txtlist[len(txtlist)-1])
            with open('saved_items.txt', 'w', encoding="utf-8") as we:
                for i in txtlist: 
                    we.write(i)
        else:
            ruwans = ["Saved Items"]
            biwans= ["Saved Items"]
            self.savebute.text = "Saved Items"
            self.leftrow.text = "Saved Items"
            self.rightrow.text = "Saved Items"
            self.savedite.text = "Saved Items"
            txtlist = ['r\n']
            with open('saved_items.txt', 'w', encoding="utf-8") as we:
                for i in txtlist: 
                    we.write('r\n')
    def printrow(self):
        self.savedite.values = ruwans
    def changeyourkief(self, *args):
        if args[1] == "Saved Items":
            self.savebute.text = "Saved Items"
            self.leftrow.text = "Saved Items"
            self.rightrow.text = "Saved Items"
        else:
            kkrree = biwans[ruwans.index(args[1])]
            print(*args)
            print(kkrree)
            sirreie = kkrree.split("Ingredients:")
            print(sirreie)
            burree = sirreie[1].split("   ")
            kkeeww = []
            kkeeww.append(burree[0].split("\n"))
            kkeeww.append(burree[1].split("\n"))
            kkeeww.append(burree[2].split("\n"))
            kkeeww.append(burree[3].split("\n"))
            print(kkeeww)
            self.savebute.text = sirreie[0] + "Ingredients:"
            self.leftrow.text = kkeeww[0][1] + "\n" + kkeeww[1][1] + "\n" + kkeeww[2][1]
            self.rightrow.text = kkeeww[1][0] + "\n" + kkeeww[2][0] + "\n" + kkeeww[3][0]

class SettingsScreen(Screen):
    screen_manager = ObjectProperty()
class TheLabApp(MDApp):
    fontse = "akashi/akashi.ttf"
    fontbi = "akashi/akashi.ttf"
    lamba = NumericProperty(0.5)
    myvalue = NumericProperty(0)
    amountlive = NumericProperty(0)
    amountlivestr = StringProperty(str("0"))
    def changetheme(self, *args):
        self.lamba = args[1]
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Window.size = (1200, 800)
    def adddlvl(self, *args):
        global reqlvla
        print(*args)
        reqlvla=str(args[1])
    def addddura(self, *args):
        global reqduraa
        reqduraa=int(args[1])
    def adddduratxt(self, *args):
        try:
            boks = int(args[0].text)
            if boks > 1000:
                args[0].text = "1000"
                boks = 1000
            elif boks < 1:
                boks = 1
                args[0].text = "1"
            else:
                args[0].text = str(boks)
        except:
            boks = 1
            args[0].text = "1"
        global reqduraa
        reqduraa=boks
    def adddcha(self, okose):
        global reqchaa
        reqchaa=okose/100
    def adddchatxt(self, okose):
        global reqchaa
        reqchaa=okose/100
    def adddstr(self, *args):
        global reqstra
        reqstra=int(args[1])
    def adddstrtxt(self, *args):
        try:
            boks = int(args[0].text)
            if boks > 1000:
                args[0].text = "1000"
                boks = 1000
            elif boks < 0:
                boks = 0
                args[0].text = "0"
            else:
                args[0].text = str(boks)
        except:
            boks = 0
            args[0].text = "0"
        global reqstra
        reqstra=boks
    def addddex(self, *args):
        global reqdexa
        reqdexa=int(args[1])
    def addddextxt(self, *args):
        try:
            boks = int(args[0].text)
            if boks > 1000:
                args[0].text = "1000"
                boks = 1000
            elif boks < 0:
                boks = 0
                args[0].text = "0"
            else:
                args[0].text = str(boks)
        except:
            boks = 0
            args[0].text = "0"
        global reqdexa
        reqdexa=boks
    def adddint(self, *args):
        global reqinta
        reqinta=int(args[1])
    def adddinttxt(self, *args):
        try:
            boks = int(args[0].text)
            if boks > 1000:
                args[0].text = "1000"
                boks = 1000
            elif boks < 0:
                boks = 0
                args[0].text = "0"
            else:
                args[0].text = str(boks)
        except:
            boks = 0
            args[0].text = "0"
        global reqinta
        reqinta=boks
    def addddef(self, *args):
        global reqdefa
        reqdefa=int(args[1])
    def addddeftxt(self, *args):
        try:
            boks = int(args[0].text)
            if boks > 1000:
                args[0].text = "1000"
                boks = 1000
            elif boks < 0:
                boks = 0
                args[0].text = "0"
            else:
                args[0].text = str(boks)
        except:
            boks = 0
            args[0].text = "0"
        global reqdefa
        reqdefa=boks
    def adddagi(self, *args):
        global reqagila
        reqagila=int(args[1])
    def adddagitxt(self, *args):
        try:
            boks = int(args[0].text)
            if boks > 1000:
                args[0].text = "1000"
                boks = 1000
            elif boks < 0:
                boks = 0
                args[0].text = "0"
            else:
                args[0].text = str(boks)
        except:
            boks = 0
            args[0].text = "0"
        global reqagila
        reqagila=boks
    def call_api(self):
        sseee=["Helmet", "Chestplate", "Boots", "Leggings", "Ring", "Bracelet", "Necklace", "Spear", "Dagger", "Relik", "Bow", "Wand", "Food", "Potion", "Scroll"]
        for i in sseee:
            ooo = "https://api.wynncraft.com/v2/recipe/get/" + i + "-103-105"
            response = requests.get(ooo)
            see = response.json()
            print(see)
    def calculate(self):
        self.myvalue = 0
        self.amountlive = 0
        self.amountlivestr = "0"
        global jiwanshe
        global biwanshee
        jiwanshe = ["Items we found"]
        biwanshee = ["Items we found"]
        if(filterina == "What Item do you want to make?".upper()):
            content = Button(text="OK")
            popup = Popup(title='Choose what you want to craft', content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
            content.bind(on_press=popup.dismiss)
            popup.open()
            return
        if(biltera == "What Identification do you want to optimize for?".upper()):
            content = Button(text="OK")
            popup = Popup(title='Choose what you want to optimize for', content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
            content.bind(on_press=popup.dismiss)
            popup.open()
            return
        if(rar1a == 0 or rar2a == 0):
            content = Button(text="OK")
            popup = Popup(title='Choose the rarity of your materials', content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
            content.bind(on_press=popup.dismiss)
            popup.open()
            return
        if(reqlvla == "My Level"):
            content = Button(text="OK")
            popup = Popup(title='Choose your lvl first', content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
            content.bind(on_press=popup.dismiss)
            popup.open()
            return
        if(reqduraa == 1 and reqstra == 0 and reqdexa == 0 and reqinta == 0 and reqdefa == 0 and reqagila == 0 and reqlowa == 0 and reqchaa == 0):
            content = Button(text="Yes")
            popup = Popup(title='Did you really want to test for that??', content=content, auto_dismiss=False, size_hint=(None, None), size=(400, 400))
            content.bind(on_press=popup.dismiss)
            popup.open()
            return
        if(reqlowa==0):
            print("are you sure you are ready for what is about to come?")
            return
        t = threading.Thread(target=self.calcWynn, args=(reqlvla, reqduraa, reqstra, reqdexa, reqinta, reqdefa, reqagila, reqlowa, reqchaa, filterina, filterinb, biltera, rar1a, rar2a, chichia, chuchua, chachaa, secopa, fircha, seccha, bilterba, cilteraa, cilterba, id_filter_twoa, id_check_onea, id_check_twoa, bababe))
        t.daemon = True
        t.start()
        #self.calcWynn(reqlvla, reqduraa, reqstra, reqdexa, reqinta, reqdefa, reqagila, reqlowa, reqchaa, filterina, biltera, rar1a, rar2a)
    def calcWynn(self, reqlvl, reqdura, reqstr, reqdex, reqint, reqdef, reqagil, reqlow, reqcha, filter, filterb, bilter, rar1, rar2, chichi, chuchu, chacha, secop, firch, secch, bilterb, ciltera, cilterb, id_filter_two, id_check_one, id_check_two, babab):
        global jiwanshe
        global biwanshee
        is_dura_or_duraa = "itemOnlyIDs"
        is_dura_or_durab = "durabilityModifier"
        if filterb in ["Food", "Potion", "Scroll"]:
            is_dura_or_duraa = "consumableOnlyIDs"
            is_dura_or_durab = "duration"
        else:
            is_dura_or_duraa = "itemOnlyIDs"
            is_dura_or_durab = "durabilityModifier"
        jiwanshe = ["Items we found"]
        biwanshee = ["Items we found"]
        buiid = "https://api.wynncraft.com/v2/recipe/get/" + filterb + "-" + reqlvl
        kuka = requests.get(buiid).json()
        print(kuka)
        kuki = kuka["data"][0]
        print(kuki["level"]["minimum"])
        reqlvllow = kuki["level"]["minimum"]
        dural=735
        durah=738
        if "duration" in kuki:
            durah = kuki["duration"]["maximum"]
            dural = kuki["duration"]["minimum"]
        elif "durability" in kuki:
            durah = kuki["durability"]["maximum"]
            dural = kuki["durability"]["minimum"]
        #here comes the other code, now think how you want to print out and design the thing
        self.myvalue = 0
        res = []
        #a = json.load('tier0ing.json')
        #b = json.load('tier1ing.json')
        #c = json.load('tier2ing.json')
        #d = json.load('tier3ing.json')
        durab = {1:182,3:189,5:196,7:203,10:217,13:224,15:231,17:238,20:252,23:259,25:266,27:273,30:287,33:294,35:301,37:308,40:322,43:329,45:336,47:343,50:357,53:364,55:371,57:378,60:392,63:399,65:406,67:413,70:427,73:434,75:441,77:448,80:462,83:469,85:476,87:483,90:497,93:504,95:511,97:518,100:525,103:527}
        duraa = {1:182,3:189,5:196,7:203,10:217,13:224,15:231,17:238,20:252,23:259,25:266,27:273,30:287,33:294,35:301,37:308,40:322,43:329,45:336,47:343,50:357,53:364,55:371,57:378,60:392,63:399,65:406,67:413,70:427,73:434,75:441,77:448,80:462,83:469,85:476,87:483,90:497,93:504,95:511,97:518,100:525,103:527}
        hmap={}
        duracool = {}
        duramul={1:{1:1.0,2:1.0833,3:1.1333},2:{1:1.1666,2:1.25,3:1.3},3:{1:1.2666,2:1.35,3:1.4}}
        flippedduramul={1:{1:1.0,2:1.1666,3:1.2666},2:{1:1.0833,2:1.25,3:1.35},3:{1:1.1333,2:1.3,3:1.4}}
        equalduramul={1:{1:1.0,2:1.125,3:1.2},2:{1:1.125,2:1.25,3:1.325},3:{1:1.2,2:1.325,3:1.4}}
        doubleduramul={1:{1:1.0,2:1.0625,3:1.1},2:{1:1.1875,2:1.25,3:1.2875},3:{1:1.3,2:1.3625,3:1.4}}
        if filterb in ["Chestplate", "Leggings", "Bracelet", "Dagger", "Relik", "Bow", "Food", "Potion"]:
            duracool = duramul
        elif filterb in ["Helmet", "Boots", "Spear", "Wand"]:
            duracool = flippedduramul
        elif filterb in ["Ring", "Scroll"]:
            duracool = equalduramul
        elif filterb in ["Necklace"]:
            duracool = doubleduramul
        """
        equalduramul={1:{1:1.0,2:1.1666,3:1.2666},2:{1:1.0833,2:1.25,3:1.35},3:{1:1.1333,2:1.3,3:1.4}}
        neclaceduramul={1:{1:1.0,2:1.1666,3:1.2666},2:{1:1.0833,2:1.25,3:1.35},3:{1:1.1333,2:1.3,3:1.4}}
        """
        sorted = []
        borted = []
        #addlost='THUNDERDAMAGEBONUS'
        kks = 0
        for i in h:
            kks+=1
            print(kks)
            if filter in i['skills'] and i['level'] <= reqlvllow:
                sorted.append(i)
            #if i["name"] == "Ancient Currency":
                #print(i)
        """
        if reqlvl in durab:
            reqlvl = reqlvl
        else:
            if reqlvl-1 in durab:
                reqlvl = reqlvl-1
            else:
                if reqlvl-2 in durab:
                    reqlvl = reqlvl-2
                else:
                    reqlvl = reqlvl-3
        """
        if rar1 == 1:
            if rar2 == 1:
                durah = round(durah*duracool[1][1])
                dural = round(durah*duracool[1][1])
            if rar2 == 2:
                durah = round(durah*duracool[1][2])
                dural = round(durah*duracool[1][2])
            if rar2 == 3:
                durah = round(durah*duracool[1][3])
                dural = round(durah*duracool[1][3])
        if rar1 == 2:
            if rar2 == 1:
                durah = round(durah*duracool[2][1])
                dural = round(durah*duracool[2][1])
            if rar2 == 2:
                durah = round(durah*duracool[2][2])
                dural = round(durah*duracool[2][2])
            if rar2 == 3:
                durah = round(durah*duracool[2][3])
                dural = round(durah*duracool[2][3])
        if rar1 == 3:
            if rar2 == 1:
                durah = round(durah*duracool[3][1])
                dural = round(durah*duracool[3][1])
            if rar2 == 2:
                durah = round(durah*duracool[3][2])
                dural = round(durah*duracool[3][2])
            if rar2 == 3:
                durah = round(durah*duracool[3][3])
                dural = round(durah*duracool[3][3])
        
        incr = 0
        if not babab:
            for i in sorted:
                if (bilter in i['identifications'] and chacha) or (bilter in i['identifications'] and not chacha and i['identifications'][bilter]["maximum"]>0):
                    #if addlost not in i['identifications']:
                        #i['identifications'][addlost] = {"minimum": 0, "maximum": 0}
                    hmap[i['name']] = incr
                    incr+=1
                    borted.append(i)
                    if secop and (bilterb not in i['identifications']):
                        i['identifications'][bilterb] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                if (secop and bilterb in i['identifications'] and chacha) or (secop and bilterb in i['identifications'] and not chacha and i['identifications'][bilterb]["maximum"]>0):
                    hmap[i['name']] = incr
                    incr+=1
                    borted.append(i)
                    if bilter not in i['identifications']:
                        i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                #if (firch and ciltera in i['identifications'] and chacha) or (firch and ciltera in i['identifications'] and not chacha and i['identifications'][ciltera]["maximum"]>0):
                    #pass
                #if (secch and cilterb in i['identifications'] and chacha) or (secch and cilterb in i['identifications'] and not chacha and i['identifications'][cilterb]["maximum"]>0):
                    #ypass
                #elif addlost in i['identifications']:
                    #if bilter not in i['identifications']:
                        #i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    #borted.append(i)
                elif  i[is_dura_or_duraa][is_dura_or_durab]>0 and chichi and i not in borted:
                    if bilter not in i['identifications']:
                        i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    if secop and (bilterb not in i['identifications']):
                        i['identifications'][bilterb] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                    hmap[i['name']] = incr
                    incr+=1
                    borted.append(i)
                elif  ((i['itemOnlyIDs']['strengthRequirement']>0 or i['itemOnlyIDs']['dexterityRequirement']>0 or i['itemOnlyIDs']['intelligenceRequirement']>0 or i['itemOnlyIDs']['defenceRequirement']>0 or i['itemOnlyIDs']['agilityRequirement']>0) and chuchu and i not in borted and not chacha) or ((i['itemOnlyIDs']['strengthRequirement']!=0 or i['itemOnlyIDs']['dexterityRequirement']!=0 or i['itemOnlyIDs']['intelligenceRequirement']!=0 or i['itemOnlyIDs']['defenceRequirement']!=0 or i['itemOnlyIDs']['agilityRequirement']!=0) and chuchu and i not in borted and chacha):
                    if bilter not in i['identifications']:
                        i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    if secop and (bilterb not in i['identifications']):
                        i['identifications'][bilterb] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                    hmap[i['name']] = incr
                    incr+=1
                    borted.append(i)
                elif ((i['ingredientPositionModifiers']['touching'] != 0 or i['ingredientPositionModifiers']['notTouching'] != 0 or i['ingredientPositionModifiers']['above'] != 0 or i['ingredientPositionModifiers']['under'] != 0 or i['ingredientPositionModifiers']['left'] != 0 or i['ingredientPositionModifiers']['right'] != 0) and chacha) or ((i['ingredientPositionModifiers']['touching'] > 0 or i['ingredientPositionModifiers']['notTouching'] > 0 or i['ingredientPositionModifiers']['above'] > 0 or i['ingredientPositionModifiers']['under'] > 0 or i['ingredientPositionModifiers']['left'] > 0 or i['ingredientPositionModifiers']['right'] > 0) and not chacha):
                    if bilter not in i['identifications']:
                        i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    if secop and (bilterb not in i['identifications']):
                        i['identifications'][bilterb] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                    #if addlost not in i['identifications']:
                        #i['identifications'][addlost] = {"minimum": 0, "maximum": 0}
                    borted.append(i)
        else:
            for i in sorted:
                if bilter in i['identifications'] and i['identifications'][bilter]["maximum"]<0:
                    #if addlost not in i['identifications']:
                        #i['identifications'][addlost] = {"minimum": 0, "maximum": 0}
                    hmap[i['name']] = incr
                    incr+=1
                    borted.append(i)
                    if secop and (bilterb not in i['identifications']):
                        i['identifications'][bilterb] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                if secop and bilterb in i['identifications'] and i['identifications'][bilterb]["maximum"]<0:
                    hmap[i['name']] = incr
                    incr+=1
                    borted.append(i)
                    if bilter not in i['identifications']:
                        i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                #if (firch and ciltera in i['identifications'] and chacha) or (firch and ciltera in i['identifications'] and not chacha and i['identifications'][ciltera]["maximum"]>0):
                    #pass
                #if (secch and cilterb in i['identifications'] and chacha) or (secch and cilterb in i['identifications'] and not chacha and i['identifications'][cilterb]["maximum"]>0):
                    #ypass
                #elif addlost in i['identifications']:
                    #if bilter not in i['identifications']:
                        #i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    #borted.append(i)
                elif  i[is_dura_or_duraa][is_dura_or_durab]>0 and chichi and i not in borted:
                    if bilter not in i['identifications']:
                        i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    if secop and (bilterb not in i['identifications']):
                        i['identifications'][bilterb] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                    hmap[i['name']] = incr
                    incr+=1
                    borted.append(i)
                elif  (i['itemOnlyIDs']['strengthRequirement']<0 or i['itemOnlyIDs']['dexterityRequirement']<0 or i['itemOnlyIDs']['intelligenceRequirement']<0 or i['itemOnlyIDs']['defenceRequirement']<0 or i['itemOnlyIDs']['agilityRequirement']<0) and chuchu and i not in borted:
                    if bilter not in i['identifications']:
                        i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    if secop and (bilterb not in i['identifications']):
                        i['identifications'][bilterb] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                    hmap[i['name']] = incr
                    incr+=1
                    borted.append(i)
                elif (i['ingredientPositionModifiers']['touching'] < 0 or i['ingredientPositionModifiers']['notTouching'] < 0 or i['ingredientPositionModifiers']['above'] < 0 or i['ingredientPositionModifiers']['under'] < 0 or i['ingredientPositionModifiers']['left'] < 0 or i['ingredientPositionModifiers']['right'] < 0):
                    if bilter not in i['identifications']:
                        i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                    if secop and (bilterb not in i['identifications']):
                        i['identifications'][bilterb] = {"minimum": 0, "maximum": 0}
                    if firch and (ciltera not in i['identifications']):
                        i['identifications'][ciltera] = {"minimum": 0, "maximum": 0}
                    if secch and (cilterb not in i['identifications']):
                        i['identifications'][cilterb] = {"minimum": 0, "maximum": 0}
                    #if addlost not in i['identifications']:
                        #i['identifications'][addlost] = {"minimum": 0, "maximum": 0}
                    borted.append(i)
        soos = {"name": "Empty Slot", "tier": 0, "level": 1, "skills": ["WEAPONSMITHING", "ARMOURING", "WOODWORKING"], "sprite": {"id": 888888, "damage": 0}, "identifications":{"LOOT_QUALITY":{"minimum":0, "maximum":0}, "TEST":{"minimum":0, "maximum":0}, "AIRDEFENSE":{"minimum":0, "maximum":0}, "EARTHDEFENSE":{"minimum":0, "maximum":0}, "FIREDEFENSE":{"minimum":0, "maximum":0}, "THUNDERDEFENSE":{"minimum":0, "maximum":0}, "WATERDEFENSE":{"minimum":0, "maximum":0}, "DAMAGEBONUS":{"minimum":0, "maximum":0}, "DAMAGEBONUSRAW":{"minimum":0, "maximum":0}, "AIRDAMAGEBONUS":{"minimum":0, "maximum":0}, "EARTHDAMAGEBONUS":{"minimum":0, "maximum":0}, "FIREDAMAGEBONUS":{"minimum":0, "maximum":0}, "THUNDERDAMAGEBONUS":{"minimum":0, "maximum":0}, "WATERDAMAGEBONUS":{"minimum":0, "maximum":0}, "AGILITYPOINTS":{"minimum":0, "maximum":0}, "DEFENSEPOINTS":{"minimum":0, "maximum":0}, "DEXTERITYPOINTS":{"minimum":0, "maximum":0}, "INTELLIGENCEPOINTS":{"minimum":0, "maximum":0}, "STRENGTHPOINTS":{"minimum":0, "maximum":0}, "POISON":{"minimum":0, "maximum":0}, "MANASTEAL":{"minimum":0, "maximum":0}, "MANAREGEN":{"minimum":0, "maximum":0}, "SPEED":{"minimum":0, "maximum":0}, "HEALTHBONUS":{"minimum":0, "maximum":0}, "SPELLDAMAGE":{"minimum":0, "maximum":0}, "SPELLDAMAGERAW":{"minimum":0, "maximum":0}, "ATTACKSPEED":{"minimum":0, "maximum":0}, "LIFESTEAL":{"minimum":0, "maximum":0}, "HEALTHREGEN":{"minimum":0, "maximum":0}, "HEALTHREGENRAW":{"minimum":0, "maximum":0}, "REFLECTION":{"minimum":0, "maximum":0}, "THORNS":{"minimum":0, "maximum":0}, "EXPLODING":{"minimum":0, "maximum":0}, "LOOTBONUS":{"minimum":0, "maximum":0}, "XPBONUS":{"minimum":0, "maximum":0}, "EMERALDSTEALING":{"minimum":0, "maximum":0}, "SOULPOINTS":{"minimum":0, "maximum":0}, 'GATHER_XP_BONUS': {'minimum': 0, 'maximum': 0}}, "itemOnlyIDs": {"durabilityModifier": 0, "strengthRequirement": 0, "dexterityRequirement": 0, "intelligenceRequirement": 0, "defenceRequirement": 0, "agilityRequirement": 0}, "consumableOnlyIDs": {"duration": 0, "charges": 0}, "ingredientPositionModifiers": {"left": 0, "right": 0, "above": 0, "under": 0, "touching": 0, "notTouching": 0}}
        #bosoos = {"name": "Ktrorro", "tier": 3, "level": 80, "skills": ["ARMOURING"], "sprite": {"id": 8888898, "damage": 0}, "identifications":{"TEST":{"minimum":0, "maximum":0}}, "itemOnlyIDs": {"durabilityModifier": -150, "strengthRequirement": -25, "dexterityRequirement": -25, "intelligenceRequirement": -25, "defenceRequirement": -25, "agilityRequirement": -25}, "ingredientPositionModifiers": {"left": 0, "right": 0, "above": 0, "under": 0, "touching": -25, "notTouching": -25}}
        borted.append(soos)
        #print(borted)
        #borted.append(bosoos)
        kiki = 100/len(borted)/len(borted)
        #print(borted)
        dd=-1000000
        boi={}
        for i in borted:
            for j in borted:
                for k in borted:
                    for l in borted:
                        for m in borted:
                            for n in borted:
                                #calculating all the different combinations 
                                #their dura with lvl and their max boost
                                durability = durah + i[is_dura_or_duraa][is_dura_or_durab] + j[is_dura_or_duraa][is_dura_or_durab] + k[is_dura_or_duraa][is_dura_or_durab] + l[is_dura_or_duraa][is_dura_or_durab] + m[is_dura_or_duraa][is_dura_or_durab] + n[is_dura_or_duraa][is_dura_or_durab]
                                durabilitylow = dural + i[is_dura_or_duraa][is_dura_or_durab] + j[is_dura_or_duraa][is_dura_or_durab] + k[is_dura_or_duraa][is_dura_or_durab] + l[is_dura_or_duraa][is_dura_or_durab] + m[is_dura_or_duraa][is_dura_or_durab] + n[is_dura_or_duraa][is_dura_or_durab]
                                if durability < 1:
                                    durability = 1
                                    durabilitylow = 1
                                if durabilitylow < 1:
                                    durabilitylow = 1
                                #if durability >= reqdura and not((i['name'] in hmap and j['name'] in hmap and k['name'] in hmap and l['name'] in hmap and m['name'] in hmap and n['name'] in hmap) and (hmap[i['name']]>hmap[j['name']] or hmap[j['name']]>hmap[k['name']] or hmap[k['name']]>hmap[l['name']] or hmap[l['name']]>hmap[m['name']] or hmap[m['name']]>hmap[n['name']])):
                                if durability >= reqdura:
                                #if durability >= reqdura:
                                    calc ={}
                                    a=i['ingredientPositionModifiers']
                                    b=j['ingredientPositionModifiers']
                                    c=k['ingredientPositionModifiers']
                                    d=l['ingredientPositionModifiers']
                                    e=m['ingredientPositionModifiers']
                                    f=n['ingredientPositionModifiers']
                                    fir = 0 + b['touching'] + c['touching'] + d['notTouching'] + e['notTouching'] + f['notTouching'] + c['above'] + e['above'] + b['left']
                                    sec = 0 + a['touching'] + c['notTouching'] + d['touching'] + e['notTouching'] + f['notTouching'] + d['above'] + f['above'] + a['right']
                                    thir = 0 + a['touching'] + b['notTouching'] + d['touching'] + e['touching'] + f['notTouching'] + a['under'] + e['above'] + d['left']
                                    four = 0 + a['notTouching'] + b['touching'] + c['touching'] + e['notTouching'] + f['touching'] + b['under'] + f['above'] + c['right']
                                    fif = 0 + a['notTouching'] + b['notTouching'] + c['touching'] + d['notTouching'] + f['touching'] + a['under'] + c['under'] + f['left']
                                    six = 0 + a['notTouching'] + b['notTouching'] + c['notTouching'] + d['touching'] + e['touching'] + b['under'] + d['under'] + e['right']
                                    calc['what'] = filterb
                                    calc['lvl'] = reqlvl
                                    #if "duration" in kuki:
                                        #if kuki["level"]["minimum"]<30:
                                            #calc['charges'] = 1 + a["consumableOnlyIDs"]["duration"] + b["consumableOnlyIDs"]["duration"] + c["consumableOnlyIDs"]["duration"] + d["consumableOnlyIDs"]["duration"] + e["consumableOnlyIDs"]["duration"] + f["consumableOnlyIDs"]["duration"]
                                        #elif kuki["level"]["minimum"]<70:
                                            #calc['charges'] = 2 + a["consumableOnlyIDs"]["duration"] + b["consumableOnlyIDs"]["duration"] + c["consumableOnlyIDs"]["duration"] + d["consumableOnlyIDs"]["duration"] + e["consumableOnlyIDs"]["duration"] + f["consumableOnlyIDs"]["duration"]
                                        #else:
                                            #calc['charges'] = 3 + a["consumableOnlyIDs"]["duration"] + b["consumableOnlyIDs"]["duration"] + c["consumableOnlyIDs"]["duration"] + d["consumableOnlyIDs"]["duration"] + e["consumableOnlyIDs"]["duration"] + f["consumableOnlyIDs"]["duration"]
                                    calc['firstSlot'] = i['name']
                                    calc['secondSlot'] = j['name']
                                    calc['thirdSlot'] = k['name']
                                    calc['fourthSlot'] = l['name']
                                    calc['fifthSlot'] = m['name']
                                    calc['sixthSlot'] = n['name']
                                    calc['strengthRequirement'] = math.floor(i['itemOnlyIDs']['strengthRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['strengthRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['strengthRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['strengthRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['strengthRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['strengthRequirement']*(1+six/100))
                                    calc['dexterityRequirement'] = math.floor(i['itemOnlyIDs']['dexterityRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['dexterityRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['dexterityRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['dexterityRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['dexterityRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['dexterityRequirement']*(1+six/100))
                                    calc['intelligenceRequirement'] = math.floor(i['itemOnlyIDs']['intelligenceRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['intelligenceRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['intelligenceRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['intelligenceRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['intelligenceRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['intelligenceRequirement']*(1+six/100))
                                    calc['defenceRequirement'] = math.floor(i['itemOnlyIDs']['defenceRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['defenceRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['defenceRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['defenceRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['defenceRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['defenceRequirement']*(1+six/100))
                                    calc['agilityRequirement'] = math.floor(i['itemOnlyIDs']['agilityRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['agilityRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['agilityRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['agilityRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['agilityRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['agilityRequirement']*(1+six/100))
                                    calc['durability'] = durability
                                    calc['durabilitylow'] = durabilitylow
                                    op=math.floor(i['identifications'][bilter]['maximum']*(1+fir/100)) + math.floor(j['identifications'][bilter]['maximum']*(1+sec/100)) + math.floor(k['identifications'][bilter]['maximum']*(1+thir/100)) + math.floor(l['identifications'][bilter]['maximum']*(1+four/100)) + math.floor(m['identifications'][bilter]['maximum']*(1+fif/100)) + math.floor(n['identifications'][bilter]['maximum']*(1+six/100))
                                    dop=math.floor(i['identifications'][bilter]['minimum']*(1+fir/100)) + math.floor(j['identifications'][bilter]['minimum']*(1+sec/100)) + math.floor(k['identifications'][bilter]['minimum']*(1+thir/100)) + math.floor(l['identifications'][bilter]['minimum']*(1+four/100)) + math.floor(m['identifications'][bilter]['minimum']*(1+fif/100)) + math.floor(n['identifications'][bilter]['minimum']*(1+six/100))
                                    if op >= dop:
                                        calc[bilter] = op
                                        calc['low'] = dop
                                    else:
                                        calc[bilter] = dop
                                        calc['low'] = op
                                    if secop:
                                        bop=math.floor(i['identifications'][bilterb]['maximum']*(1+fir/100)) + math.floor(j['identifications'][bilterb]['maximum']*(1+sec/100)) + math.floor(k['identifications'][bilterb]['maximum']*(1+thir/100)) + math.floor(l['identifications'][bilterb]['maximum']*(1+four/100)) + math.floor(m['identifications'][bilterb]['maximum']*(1+fif/100)) + math.floor(n['identifications'][bilterb]['maximum']*(1+six/100))
                                        bdop=math.floor(i['identifications'][bilterb]['minimum']*(1+fir/100)) + math.floor(j['identifications'][bilterb]['minimum']*(1+sec/100)) + math.floor(k['identifications'][bilterb]['minimum']*(1+thir/100)) + math.floor(l['identifications'][bilterb]['minimum']*(1+four/100)) + math.floor(m['identifications'][bilterb]['minimum']*(1+fif/100)) + math.floor(n['identifications'][bilterb]['minimum']*(1+six/100))
                                        if bop >= bdop:
                                            calc[bilterb] = bop
                                            calc['alow'] = bdop
                                        else:
                                            calc[bilterb] = bdop
                                            calc['alow'] = bop
                                    if firch:
                                        cop=math.floor(i['identifications'][ciltera]['maximum']*(1+fir/100)) + math.floor(j['identifications'][ciltera]['maximum']*(1+sec/100)) + math.floor(k['identifications'][ciltera]['maximum']*(1+thir/100)) + math.floor(l['identifications'][ciltera]['maximum']*(1+four/100)) + math.floor(m['identifications'][ciltera]['maximum']*(1+fif/100)) + math.floor(n['identifications'][ciltera]['maximum']*(1+six/100))
                                        cdop=math.floor(i['identifications'][ciltera]['minimum']*(1+fir/100)) + math.floor(j['identifications'][ciltera]['minimum']*(1+sec/100)) + math.floor(k['identifications'][ciltera]['minimum']*(1+thir/100)) + math.floor(l['identifications'][ciltera]['minimum']*(1+four/100)) + math.floor(m['identifications'][ciltera]['minimum']*(1+fif/100)) + math.floor(n['identifications'][ciltera]['minimum']*(1+six/100))
                                        if cop >= cdop:
                                            calc[ciltera] = cop
                                            calc['blow'] = cdop
                                        else:
                                            calc[ciltera] = cdop
                                            calc['blow'] = cop
                                    if secch:
                                        eop=math.floor(i['identifications'][cilterb]['maximum']*(1+fir/100)) + math.floor(j['identifications'][cilterb]['maximum']*(1+sec/100)) + math.floor(k['identifications'][cilterb]['maximum']*(1+thir/100)) + math.floor(l['identifications'][cilterb]['maximum']*(1+four/100)) + math.floor(m['identifications'][cilterb]['maximum']*(1+fif/100)) + math.floor(n['identifications'][cilterb]['maximum']*(1+six/100))
                                        edop=math.floor(i['identifications'][cilterb]['minimum']*(1+fir/100)) + math.floor(j['identifications'][cilterb]['minimum']*(1+sec/100)) + math.floor(k['identifications'][cilterb]['minimum']*(1+thir/100)) + math.floor(l['identifications'][cilterb]['minimum']*(1+four/100)) + math.floor(m['identifications'][cilterb]['minimum']*(1+fif/100)) + math.floor(n['identifications'][cilterb]['minimum']*(1+six/100))
                                        if eop >= edop:
                                            calc[cilterb] = eop
                                            calc['clow'] = edop
                                        else:
                                            calc[cilterb] = edop
                                            calc['clow'] = eop
                                    #if(i['name'] == 'Decaying Heart' and j['name'] == "Bob's Tear" and k['name'] == 'Elephelk Trunk' and l['name'] == 'Ancient Currency' and m['name'] == 'Ancient Currency' and n['name'] == 'Ancient Currency'): print(str(calc[bilter]))
                                    #calc[addlost] = math.floor(i['identifications'][addlost]['maximum']*(1+fir/100)) + math.floor(j['identifications'][addlost]['maximum']*(1+sec/100)) + math.floor(k['identifications'][addlost]['maximum']*(1+thir/100)) + math.floor(l['identifications'][addlost]['maximum']*(1+four/100)) + math.floor(m['identifications'][addlost]['maximum']*(1+fif/100)) + math.floor(n['identifications'][addlost]['maximum']*(1+six/100))
                                    #calc['lowtlost'] = math.floor(i['identifications'][addlost]['minimum']*(1+fir/100)) + math.floor(j['identifications'][addlost]['minimum']*(1+sec/100)) + math.floor(k['identifications'][addlost]['minimum']*(1+thir/100)) + math.floor(l['identifications'][addlost]['minimum']*(1+four/100)) + math.floor(m['identifications'][addlost]['minimum']*(1+fif/100)) + math.floor(n['identifications'][addlost]['minimum']*(1+six/100))
                                    calc['chance'] = (1/(1+i['identifications'][bilter]['maximum']-i['identifications'][bilter]['minimum']))*(1/(1+j['identifications'][bilter]['maximum']-j['identifications'][bilter]['minimum']))*(1/(1+k['identifications'][bilter]['maximum']-k['identifications'][bilter]['minimum']))*(1/(1+l['identifications'][bilter]['maximum']-l['identifications'][bilter]['minimum']))*(1/(1+m['identifications'][bilter]['maximum']-m['identifications'][bilter]['minimum']))*(1/(1+n['identifications'][bilter]['maximum']-n['identifications'][bilter]['minimum']))
                                    #res.append(calc)
                                    #if calc['strengthRequirement'] < 55 and calc['dexterityRequirement'] < 121 and calc['intelligenceRequirement'] < 41 and calc['defenceRequirement'] < 5 and calc['agilityRequirement'] < 5 and calc['durability']>40 and calc[bilter] >70 and calc[addlost]> 20:
                                    #if calc['durability']>40 and calc[bilter] >20 and calc[addlost]> 20:
                                    if calc['strengthRequirement'] <= reqstr and calc['dexterityRequirement'] <= reqdex and calc['intelligenceRequirement'] <= reqint and calc['defenceRequirement'] <= reqdef and calc['agilityRequirement'] <= reqagil and calc["chance"]>=reqcha and calc[bilter] >=reqlow and ((not secop) or (secop and calc[bilterb]>=id_filter_two)) and ((not firch) or (firch and calc[ciltera]>=id_check_one)) and ((not secch) or (secch and calc[cilterb]>=id_check_two)):
                                        #if(i['name'] == 'Decaying Heart' and j['name'] == "Bob's Tear" and k['name'] == 'Elephelk Trunk' and l['name'] == 'Ancient Currency' and m['name'] == 'Ancient Currency' and n['name'] == 'Ancient Currency'): print("fire")
                                        jiwanshe.append(str(calc))
                                        stringbuild = (filterb + "-" + reqlvl + ": " +"dura: " + str(calc["durabilitylow"])+"-"+str(calc["durability"]) + " chance: "
                                            + str(calc["chance"])+ "%" + " " + str(bilter).lower().capitalize()+": " + str(calc["low"])+"->"+str(calc[bilter]) + " ")
                                        if secop:
                                            stringbuild += str(bilterb).lower().capitalize()+": " + str(calc["alow"])+"->"+str(calc[bilterb]) + " "
                                        if firch:
                                            stringbuild += str(ciltera).lower().capitalize()+": " + str(calc["blow"])+"->"+str(calc[ciltera]) + " "
                                        if secch:
                                            stringbuild += str(cilterb).lower().capitalize()+": " + str(calc["clow"])+"->"+str(calc[cilterb]) + " "
                                        stringbuild += ("Skillrequirements:"+ " " + "Str: " + str(calc["strengthRequirement"])
                                            + " Dex: " + str(calc["dexterityRequirement"])+" "
                                            + "Intel: " + str(calc["intelligenceRequirement"])
                                            + " Def: " + str(calc["defenceRequirement"])+" "
                                            + "Agil: " + str(calc["agilityRequirement"]))
                                        biwanshee.append(stringbuild)
                                        self.amountlive += 1
                                        self.amountlivestr = str(self.amountlive)
                                        if(i['name'] == 'Decaying Heart' and j['name'] == "Bob's Tear" and k['name'] == 'Elephelk Trunk' and l['name'] == 'Ancient Currency' and m['name'] == 'Ancient Currency' and n['name'] == 'Ancient Currency'): print(jiwanshe)
                                        if(i['name'] == 'Decaying Heart' and j['name'] == "Bob's Tear" and k['name'] == 'Elephelk Trunk' and l['name'] == 'Ancient Currency' and m['name'] == 'Ancient Currency' and n['name'] == 'Ancient Currency'): print(biwanshee)
                                        #print(calc)
                                    #if calc['strengthRequirement'] < 55 and calc['dexterityRequirement'] < 121 and calc['intelligenceRequirement'] < 41 and calc['defenceRequirement'] < 5 and calc['agilityRequirement'] < 5 and calc['durability']>40 and calc[bilter] >dd and calc[addlost]> 20:
                                    if calc['strengthRequirement'] <= reqstr and calc['dexterityRequirement'] <= reqdex and calc['intelligenceRequirement'] <= reqint and calc['defenceRequirement'] <= reqdef and calc['agilityRequirement'] <= reqagil and calc["chance"]>=reqcha and calc[bilter] >dd and ((not secop) or (secop and calc[bilterb]>=id_filter_two)) and ((not firch) or (firch and calc[ciltera]>=id_check_one)) and ((not secch) or (secch and calc[cilterb]>=id_check_two)):
                                        #if(i['name'] == 'Decaying Heart' and j['name'] == "Bob's Tear" and k['name'] == 'Elephelk Trunk' and l['name'] == 'Ancient Currency' and m['name'] == 'Ancient Currency' and n['name'] == 'Ancient Currency'): print("fireee")
                                        dd = calc[bilter]
                                        boi[dd] = calc
                                        jiwanshe.append(str(calc))
                                        stringbuild = (filterb + "-" + reqlvl + "dura: " + str(calc["durabilitylow"])+"-"+str(calc["durability"]) + " chance: "
                                            + str(calc["chance"])+ "%" + " " + str(bilter).lower().capitalize()+": " + str(calc["low"])+"->"+str(calc[bilter]) + " ")
                                        if secop:
                                            stringbuild += str(bilterb).lower().capitalize()+": " + str(calc["alow"])+"->"+str(calc[bilterb]) + " "
                                        if firch:
                                            stringbuild += str(ciltera).lower().capitalize()+": " + str(calc["blow"])+"->"+str(calc[ciltera]) + " "
                                        if secch:
                                            stringbuild += str(cilterb).lower().capitalize()+": " + str(calc["clow"])+"->"+str(calc[cilterb]) + " "
                                        stringbuild += ("Skillrequirements:"+ " " + "Str: " + str(calc["strengthRequirement"])
                                            + " Dex: " + str(calc["dexterityRequirement"])+" "
                                            + "Intel: " + str(calc["intelligenceRequirement"])
                                            + " Def: " + str(calc["defenceRequirement"])+" "
                                            + "Agil: " + str(calc["agilityRequirement"]))
                                        biwanshee.append(stringbuild)
                                        self.amountlive += 1
                                        self.amountlivestr = str(self.amountlive)
                                        #print(calc)
                                    #elif calc['strengthRequirement'] < 55 and calc['dexterityRequirement'] < 121 and calc['intelligenceRequirement'] < 41 and calc['defenceRequirement'] < 5 and calc['agilityRequirement'] < 5 and calc[addlost]> 20 and calc[bilter] == dd and calc['durability']>boi[dd]['durability']:
                                    elif calc['strengthRequirement'] <= reqstr and calc['dexterityRequirement'] <= reqdex and calc['intelligenceRequirement'] <= reqint and calc['defenceRequirement'] <= reqdef and calc['agilityRequirement'] <= reqagil and calc["chance"]>=reqcha and calc[bilter] == dd and calc['durability']>boi[dd]['durability'] and ((not secop) or (secop and (calc[bilterb]>=id_filter_two))) and ((not firch) or (firch and (calc[ciltera]>=id_check_one))) and ((not secch) or (secch and (calc[cilterb]>=id_check_two))):
                                        #if(i['name'] == 'Decaying Heart' and j['name'] == "Bob's Tear" and k['name'] == 'Elephelk Trunk' and l['name'] == 'Ancient Currency' and m['name'] == 'Ancient Currency' and n['name'] == 'Ancient Currency'): print("fireooo")
                                        dd = calc[bilter]
                                        boi[dd] = calc
                                        jiwanshe.append(str(calc))
                                        stringbuild = (filterb + "-" + reqlvl + "dura: " + str(calc["durabilitylow"])+"-"+str(calc["durability"]) + " chance: "
                                            + str(calc["chance"])+ "%" + " " + str(bilter).lower().capitalize()+": " + str(calc["low"])+"->"+str(calc[bilter]) + " ")
                                        if secop:
                                            stringbuild += str(bilterb).lower().capitalize()+": " + str(calc["alow"])+"->"+str(calc[bilterb]) + " "
                                        if firch:
                                            stringbuild += str(ciltera).lower().capitalize()+": " + str(calc["blow"])+"->"+str(calc[ciltera]) + " "
                                        if secch:
                                            stringbuild += str(cilterb).lower().capitalize()+": " + str(calc["clow"])+"->"+str(calc[cilterb]) + " "
                                        stringbuild += ("Skillrequirements:"+ " " + "Str: " + str(calc["strengthRequirement"])
                                            + " Dex: " + str(calc["dexterityRequirement"])+" "
                                            + "Intel: " + str(calc["intelligenceRequirement"])
                                            + " Def: " + str(calc["defenceRequirement"])+" "
                                            + "Agil: " + str(calc["agilityRequirement"]))
                                        biwanshee.append(stringbuild)
                                        self.amountlive += 1
                                        self.amountlivestr = str(self.amountlive)
                                        #print(calc)                 
                self.myvalue+=kiki
        #for i in res:
            #if i['strengthRequirement'] < 150 and i['dexterityRequirement'] < 150 and i['intelligenceRequirement'] < 150 and i['defenceRequirement'] < 150 and i['agilityRequirement'] < 150 and i['durability']>50 and i[bilter] >70 and i[addlost]> 20:
            #if i['durability']>40 and i[bilter] >57:
                #print(i)
            #if i['strengthRequirement'] < 55 and i['dexterityRequirement'] < 121 and i['intelligenceRequirement'] < 41 and i['defenceRequirement'] < 5 and i['agilityRequirement'] < 5 and i['durability']>40 and i[bilter] >dd and i[addlost]> 20:
            #if i['durability']>40 and i[bilter] >dd:
                #dd = i[bilter]
                #boi[dd] = i
            #elif i['strengthRequirement'] < 55 and i['dexterityRequirement'] < 121 and i['intelligenceRequirement'] < 41 and i['defenceRequirement'] < 5 and i['agilityRequirement'] < 5 and i[addlost]> 20 and i[bilter] == dd and i['durability']>boi[dd]['durability']:
            #elif i['durability']>40 and i[bilter] == dd and i['durability']>boi[dd]['durability']:
                #dd = i[bilter]
                #boi[dd] = i
        #print(jiwanshe)
        #print(biwanshee)   
        print(dd)
        print (boi[dd])
        stringbuild = (filterb + "-" + reqlvl + "dura: " + str(calc["durabilitylow"])+"-"+ str(boi[dd]["durability"]) + " chance: "
            + str(boi[dd]["chance"])+ "%" + " " + str(biltera).lower().capitalize()+": " + str(boi[dd]["low"])+"->"+str(boi[dd][biltera]) + " "
            + "Skillrequirements:"+ " " + "Str: " + str(boi[dd]["strengthRequirement"])
            + " Dex: " + str(boi[dd]["dexterityRequirement"])+" "
            + "Intel: " + str(boi[dd]["intelligenceRequirement"])
            + " Def: " + str(boi[dd]["defenceRequirement"])+" "
            + "Agil: " + str(boi[dd]["agilityRequirement"]))
        biwanshee[0] = stringbuild
        jiwanshe[0] = str(boi[dd])
        self.amountlive += 1
        self.amountlivestr = str(self.amountlive)
    def calcWynnParallel(self, reqlvl, reqdura, reqstr, reqdex, reqint, reqdef, reqagil, reqlow, reqcha, filter, bilter, rar1, rar2, chichi, chuchu, chacha):
        global ddd
        global jiwanshe
        global biwanshee
        ddd = -1000000
        jiwanshe = ["Items we found"]
        biwanshee = ["Items we found"]
        #here comes the other code, now think how you want to print out and design the thing
        self.myvalue = 0
        res = []
        #a = json.load('tier0ing.json')
        #b = json.load('tier1ing.json')
        #c = json.load('tier2ing.json')
        #d = json.load('tier3ing.json')
        durab = {1:182,3:189,5:196,7:203,10:217,13:224,15:231,17:238,20:252,23:259,25:266,27:273,30:287,33:294,35:301,37:308,40:322,43:329,45:336,47:343,50:357,53:364,55:371,57:378,60:392,63:399,65:406,67:413,70:427,73:434,75:441,77:448,80:462,83:469,85:476,87:483,90:497,93:504,95:511,97:518,100:525,103:527}
        duraa = {1:182,3:189,5:196,7:203,10:217,13:224,15:231,17:238,20:252,23:259,25:266,27:273,30:287,33:294,35:301,37:308,40:322,43:329,45:336,47:343,50:357,53:364,55:371,57:378,60:392,63:399,65:406,67:413,70:427,73:434,75:441,77:448,80:462,83:469,85:476,87:483,90:497,93:504,95:511,97:518,100:525,103:527}
        hmap={}
        duramul={1:{1:1.0,2:1.0833,3:1.1333},2:{1:1.1666,2:1.25,3:1.3},3:{1:1.2666,2:1.35,3:1.4}}
        flippedduramul={1:{1:1.0,2:1.1666,3:1.2666},2:{1:1.0833,2:1.25,3:1.35},3:{1:1.1333,2:1.3,3:1.4}}
        """
        equalduramul={1:{1:1.0,2:1.1666,3:1.2666},2:{1:1.0833,2:1.25,3:1.35},3:{1:1.1333,2:1.3,3:1.4}}
        neclaceduramul={1:{1:1.0,2:1.1666,3:1.2666},2:{1:1.0833,2:1.25,3:1.35},3:{1:1.1333,2:1.3,3:1.4}}
        """
        sorted = []
        borted = []
        #addlost='THUNDERDAMAGEBONUS'
        for i in h:
            if filter in i['skills'] and i['level'] <= reqlvl:
                sorted.append(i)
            #if i["name"] == "Ancient Currency":
                #print(i)
        dural=735
        durah=738
        if reqlvl in durab:
            reqlvl = reqlvl
        else:
            if reqlvl-1 in durab:
                reqlvl = reqlvl-1
            else:
                if reqlvl-2 in durab:
                    reqlvl = reqlvl-2
                else:
                    reqlvl = reqlvl-3
        if rar1 == 1:
            if rar2 == 1:
                durah = round(durab[reqlvl]*duramul[1][1])
            if rar2 == 2:
                durah = round(durab[reqlvl]*duramul[1][2])
            if rar2 == 3:
                durah = round(durab[reqlvl]*duramul[1][3])
        if rar1 == 2:
            if rar2 == 1:
                durah = round(durab[reqlvl]*duramul[2][1])
            if rar2 == 2:
                durah = round(durab[reqlvl]*duramul[2][2])
            if rar2 == 3:
                durah = round(durab[reqlvl]*duramul[2][3])
        if rar1 == 3:
            if rar2 == 1:
                durah = round(durab[reqlvl]*duramul[3][1])
            if rar2 == 2:
                durah = round(durab[reqlvl]*duramul[3][2])
            if rar2 == 3:
                durah = round(durab[reqlvl]*duramul[3][3])
        incr = 0
        for i in sorted:
            if bilter in i['identifications']:
                #if addlost not in i['identifications']:
                    #i['identifications'][addlost] = {"minimum": 0, "maximum": 0}
                hmap[i['name']] = incr
                incr+=1
                borted.append(i)
            #elif addlost in i['identifications']:
                #if bilter not in i['identifications']:
                    #i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                #borted.append(i)
            elif  i['itemOnlyIDs']['durabilityModifier']>0 and chichi and i not in borted:
                if bilter not in i['identifications']:
                    i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                hmap[i['name']] = incr
                incr+=1
                borted.append(i)
            elif  (i['itemOnlyIDs']['strengthRequirement']>0 or i['itemOnlyIDs']['dexterityRequirement']>0 or i['itemOnlyIDs']['intelligenceRequirement']>0 or i['itemOnlyIDs']['defenceRequirement']>0 or i['itemOnlyIDs']['agilityRequirement']>0) and chuchu and i not in borted:
                if bilter not in i['identifications']:
                    i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                hmap[i['name']] = incr
                incr+=1
                borted.append(i)
            elif i['ingredientPositionModifiers']['touching'] != 0 or i['ingredientPositionModifiers']['notTouching'] != 0 or i['ingredientPositionModifiers']['above'] != 0 or i['ingredientPositionModifiers']['above'] != 0 or i['ingredientPositionModifiers']['left'] != 0 or i['ingredientPositionModifiers']['right'] != 0:
                if bilter not in i['identifications']:
                    i['identifications'][bilter] = {"minimum": 0, "maximum": 0}
                #if addlost not in i['identifications']:
                    #i['identifications'][addlost] = {"minimum": 0, "maximum": 0}
                borted.append(i)
        soos = {"name": "Empty Slot", "tier": 0, "level": 1, "skills": ["WEAPONSMITHING", "ARMOURING", "WOODWORKING"], "sprite": {"id": 888888, "damage": 0}, "identifications":{"LOOT_QUALITY":{"minimum":0, "maximum":0}, "TEST":{"minimum":0, "maximum":0}, "AIRDEFENSE":{"minimum":0, "maximum":0}, "EARTHDEFENSE":{"minimum":0, "maximum":0}, "FIREDEFENSE":{"minimum":0, "maximum":0}, "THUNDERDEFENSE":{"minimum":0, "maximum":0}, "WATERDEFENSE":{"minimum":0, "maximum":0}, "DAMAGEBONUS":{"minimum":0, "maximum":0}, "DAMAGEBONUSRAW":{"minimum":0, "maximum":0}, "AIRDAMAGEBONUS":{"minimum":0, "maximum":0}, "EARTHDAMAGEBONUS":{"minimum":0, "maximum":0}, "FIREDAMAGEBONUS":{"minimum":0, "maximum":0}, "THUNDERDAMAGEBONUS":{"minimum":0, "maximum":0}, "WATERDAMAGEBONUS":{"minimum":0, "maximum":0}, "AGILITYPOINTS":{"minimum":0, "maximum":0}, "DEFENSEPOINTS":{"minimum":0, "maximum":0}, "DEXTERITYPOINTS":{"minimum":0, "maximum":0}, "INTELLIGENCEPOINTS":{"minimum":0, "maximum":0}, "STRENGTHPOINTS":{"minimum":0, "maximum":0}, "POISON":{"minimum":0, "maximum":0}, "MANASTEAL":{"minimum":0, "maximum":0}, "MANAREGEN":{"minimum":0, "maximum":0}, "SPEED":{"minimum":0, "maximum":0}, "HEALTHBONUS":{"minimum":0, "maximum":0}, "SPELLDAMAGE":{"minimum":0, "maximum":0}, "SPELLDAMAGERAW":{"minimum":0, "maximum":0}, "ATTACKSPEED":{"minimum":0, "maximum":0}, "LIFESTEAL":{"minimum":0, "maximum":0}, "HEALTHREGEN":{"minimum":0, "maximum":0}, "HEALTHREGENRAW":{"minimum":0, "maximum":0}, "REFLECTION":{"minimum":0, "maximum":0}, "THORNS":{"minimum":0, "maximum":0}, "EXPLODING":{"minimum":0, "maximum":0}, "LOOTBONUS":{"minimum":0, "maximum":0}, "XPBONUS":{"minimum":0, "maximum":0}, "EMERALDSTEALING":{"minimum":0, "maximum":0}, "SOULPOINTS":{"minimum":0, "maximum":0}, 'GATHER_XP_BONUS': {'minimum': 0, 'maximum': 0}}, "itemOnlyIDs": {"durabilityModifier": 0, "strengthRequirement": 0, "dexterityRequirement": 0, "intelligenceRequirement": 0, "defenceRequirement": 0, "agilityRequirement": 0}, "ingredientPositionModifiers": {"left": 0, "right": 0, "above": 0, "under": 0, "touching": 0, "notTouching": 0}}
        #bosoos = {"name": "Ktrorro", "tier": 3, "level": 80, "skills": ["ARMOURING"], "sprite": {"id": 8888898, "damage": 0}, "identifications":{"TEST":{"minimum":0, "maximum":0}}, "itemOnlyIDs": {"durabilityModifier": -150, "strengthRequirement": -25, "dexterityRequirement": -25, "intelligenceRequirement": -25, "defenceRequirement": -25, "agilityRequirement": -25}, "ingredientPositionModifiers": {"left": 0, "right": 0, "above": 0, "under": 0, "touching": -25, "notTouching": -25}}
        borted.append(soos)
        #borted.append(bosoos)
        kiki = 100/len(borted)/len(borted)/len(borted)/len(borted)
        dd=-1000000
        boi={}
        threads = []
        for i in borted:
            for j in borted:
                for k in borted:
                    for l in borted:
                        ereke = threading.Thread(target=self.exportcalc_v2, args=(hmap, durah, reqdura, reqcha, i, j, k, l, bilter, boi, reqstr, reqdex, reqint, reqdef, reqagil, reqlow, borted, kiki))
                        ereke.daemon = True
                        threads.append(ereke)
        for ue in threads:
            ue.start()
        for ue in threads:
            ue.join()
        """
        for i in borted:
            for j in borted:
                for k in borted:
                    for l in borted:
                        for m in borted:
                            for n in borted:
                                ereke = threading.Thread(target=self.exportcalc, args=(hmap, durah, reqdura, reqcha, i, j, k, l, m, n, bilter, boi, reqstr, reqdex, reqint, reqdef, reqagil, reqlow))
                                ereke.daemon = True
                                ereke.start()
                self.myvalue+=kiki
        """
        #for i in res:
            #if i['strengthRequirement'] < 150 and i['dexterityRequirement'] < 150 and i['intelligenceRequirement'] < 150 and i['defenceRequirement'] < 150 and i['agilityRequirement'] < 150 and i['durability']>50 and i[bilter] >70 and i[addlost]> 20:
            #if i['durability']>40 and i[bilter] >57:
                #print(i)
            #if i['strengthRequirement'] < 55 and i['dexterityRequirement'] < 121 and i['intelligenceRequirement'] < 41 and i['defenceRequirement'] < 5 and i['agilityRequirement'] < 5 and i['durability']>40 and i[bilter] >dd and i[addlost]> 20:
            #if i['durability']>40 and i[bilter] >dd:
                #dd = i[bilter]
                #boi[dd] = i
            #elif i['strengthRequirement'] < 55 and i['dexterityRequirement'] < 121 and i['intelligenceRequirement'] < 41 and i['defenceRequirement'] < 5 and i['agilityRequirement'] < 5 and i[addlost]> 20 and i[bilter] == dd and i['durability']>boi[dd]['durability']:
            #elif i['durability']>40 and i[bilter] == dd and i['durability']>boi[dd]['durability']:
                #dd = i[bilter]
                #boi[dd] = i
        print(ddd)
        print (boi[ddd])
        stringbuild = ("dura: " + str(boi[ddd]["durability"]) + " chance: "
            + str(boi[ddd]["chance"])+ "%" + " " + str(biltera).lower().capitalize()+": " + str(boi[ddd]["low"])+"->"+str(boi[ddd][biltera]) + " "
            + "Skillrequirements:"+ " " + "Str: " + str(boi[ddd]["strengthRequirement"])
            + " Dex: " + str(boi[ddd]["dexterityRequirement"])+" "
            + "Intel: " + str(boi[ddd]["intelligenceRequirement"])
            + " Def: " + str(boi[ddd]["defenceRequirement"])+" "
            + "Agil: " + str(boi[ddd]["agilityRequirement"]))
        biwanshee[0] = stringbuild
        jiwanshe[0] = str(boi[ddd])
        self.amountlive += 1
        self.amountlivestr = str(self.amountlive)
    def exportcalc(self, hmap, durah, reqdura, reqcha, i, j, k, l, m, n, bilter, boi, reqstr, reqdex, reqint, reqdef, reqagil, reqlow):
        global jiwanshe
        global biwanshee
        global ddd
        #calculating all the different combinations 
        #their dura with lvl and their max boost
        durability = durah + i['itemOnlyIDs']['durabilityModifier'] + j['itemOnlyIDs']['durabilityModifier'] + k['itemOnlyIDs']['durabilityModifier'] + l['itemOnlyIDs']['durabilityModifier'] + m['itemOnlyIDs']['durabilityModifier'] + n['itemOnlyIDs']['durabilityModifier']
        if durability < 1:
            durability = 1
        if durability >= reqdura and not((i['name'] in hmap and j['name'] in hmap and k['name'] in hmap and l['name'] in hmap and m['name'] in hmap and n['name'] in hmap) and (hmap[i['name']]>hmap[j['name']] or hmap[j['name']]>hmap[k['name']] or hmap[k['name']]>hmap[l['name']] or hmap[l['name']]>hmap[m['name']] or hmap[m['name']]>hmap[n['name']])):
        #if durability >= reqdura:
            calc ={}
            a=i['ingredientPositionModifiers']
            b=j['ingredientPositionModifiers']
            c=k['ingredientPositionModifiers']
            d=l['ingredientPositionModifiers']
            e=m['ingredientPositionModifiers']
            f=n['ingredientPositionModifiers']
            fir = 0 + b['touching'] + c['touching'] + d['notTouching'] + e['notTouching'] + f['notTouching'] + c['above'] + e['above'] + b['left']
            sec = 0 + a['touching'] + c['notTouching'] + d['touching'] + e['notTouching'] + f['notTouching'] + d['above'] + f['above'] + a['right']
            thir = 0 + a['touching'] + b['notTouching'] + d['touching'] + e['touching'] + f['notTouching'] + a['under'] + e['above'] + d['left']
            four = 0 + a['notTouching'] + b['touching'] + c['touching'] + e['notTouching'] + f['touching'] + b['under'] + f['above'] + c['right']
            fif = 0 + a['notTouching'] + b['notTouching'] + c['touching'] + d['notTouching'] + f['touching'] + a['under'] + c['under'] + f['left']
            six = 0 + a['notTouching'] + b['notTouching'] + c['notTouching'] + d['touching'] + e['touching'] + b['under'] + d['under'] + e['right']
            calc['firstSlot'] = i['name']
            calc['secondSlot'] = j['name']
            calc['thirdSlot'] = k['name']
            calc['fourthSlot'] = l['name']
            calc['fifthSlot'] = m['name']
            calc['sixthSlot'] = n['name']
            calc['strengthRequirement'] = math.floor(i['itemOnlyIDs']['strengthRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['strengthRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['strengthRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['strengthRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['strengthRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['strengthRequirement']*(1+six/100))
            calc['dexterityRequirement'] = math.floor(i['itemOnlyIDs']['dexterityRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['dexterityRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['dexterityRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['dexterityRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['dexterityRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['dexterityRequirement']*(1+six/100))
            calc['intelligenceRequirement'] = math.floor(i['itemOnlyIDs']['intelligenceRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['intelligenceRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['intelligenceRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['intelligenceRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['intelligenceRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['intelligenceRequirement']*(1+six/100))
            calc['defenceRequirement'] = math.floor(i['itemOnlyIDs']['defenceRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['defenceRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['defenceRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['defenceRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['defenceRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['defenceRequirement']*(1+six/100))
            calc['agilityRequirement'] = math.floor(i['itemOnlyIDs']['agilityRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['agilityRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['agilityRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['agilityRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['agilityRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['agilityRequirement']*(1+six/100))
            calc['durability'] = durability
            op=math.floor(i['identifications'][bilter]['maximum']*(1+fir/100)) + math.floor(j['identifications'][bilter]['maximum']*(1+sec/100)) + math.floor(k['identifications'][bilter]['maximum']*(1+thir/100)) + math.floor(l['identifications'][bilter]['maximum']*(1+four/100)) + math.floor(m['identifications'][bilter]['maximum']*(1+fif/100)) + math.floor(n['identifications'][bilter]['maximum']*(1+six/100))
            dop=math.floor(i['identifications'][bilter]['minimum']*(1+fir/100)) + math.floor(j['identifications'][bilter]['minimum']*(1+sec/100)) + math.floor(k['identifications'][bilter]['minimum']*(1+thir/100)) + math.floor(l['identifications'][bilter]['minimum']*(1+four/100)) + math.floor(m['identifications'][bilter]['minimum']*(1+fif/100)) + math.floor(n['identifications'][bilter]['minimum']*(1+six/100))
            if op >= dop:
                calc[bilter] = op
                calc['low'] = dop
            else:
                calc[bilter] = dop
                calc['low'] = op
            #calc[addlost] = math.floor(i['identifications'][addlost]['maximum']*(1+fir/100)) + math.floor(j['identifications'][addlost]['maximum']*(1+sec/100)) + math.floor(k['identifications'][addlost]['maximum']*(1+thir/100)) + math.floor(l['identifications'][addlost]['maximum']*(1+four/100)) + math.floor(m['identifications'][addlost]['maximum']*(1+fif/100)) + math.floor(n['identifications'][addlost]['maximum']*(1+six/100))
            #calc['lowtlost'] = math.floor(i['identifications'][addlost]['minimum']*(1+fir/100)) + math.floor(j['identifications'][addlost]['minimum']*(1+sec/100)) + math.floor(k['identifications'][addlost]['minimum']*(1+thir/100)) + math.floor(l['identifications'][addlost]['minimum']*(1+four/100)) + math.floor(m['identifications'][addlost]['minimum']*(1+fif/100)) + math.floor(n['identifications'][addlost]['minimum']*(1+six/100))
            calc['chance'] = (1/(1+i['identifications'][bilter]['maximum']-i['identifications'][bilter]['minimum']))*(1/(1+j['identifications'][bilter]['maximum']-j['identifications'][bilter]['minimum']))*(1/(1+k['identifications'][bilter]['maximum']-k['identifications'][bilter]['minimum']))*(1/(1+l['identifications'][bilter]['maximum']-l['identifications'][bilter]['minimum']))*(1/(1+m['identifications'][bilter]['maximum']-m['identifications'][bilter]['minimum']))*(1/(1+n['identifications'][bilter]['maximum']-n['identifications'][bilter]['minimum']))
            with your_moms_lock:
                #res.append(calc)
                #if calc['strengthRequirement'] < 55 and calc['dexterityRequirement'] < 121 and calc['intelligenceRequirement'] < 41 and calc['defenceRequirement'] < 5 and calc['agilityRequirement'] < 5 and calc['durability']>40 and calc[bilter] >70 and calc[addlost]> 20:
                #if calc['durability']>40 and calc[bilter] >20 and calc[addlost]> 20:
                if calc['strengthRequirement'] <= reqstr and calc['dexterityRequirement'] <= reqdex and calc['intelligenceRequirement'] <= reqint and calc['defenceRequirement'] <= reqdef and calc['agilityRequirement'] <= reqagil and calc[bilter] >=reqlow:
                    jiwanshe.append(str(calc))
                    stringbuild = ("dura: " + str(calc["durability"]) + " chance: "
                        + str(calc["chance"])+ "%" + " " + str(biltera).lower().capitalize()+": " + str(calc["low"])+"->"+str(calc[biltera]) + " "
                        + "Skillrequirements:"+ " " + "Str: " + str(calc["strengthRequirement"])
                        + " Dex: " + str(calc["dexterityRequirement"])+" "
                        + "Intel: " + str(calc["intelligenceRequirement"])
                        + " Def: " + str(calc["defenceRequirement"])+" "
                        + "Agil: " + str(calc["agilityRequirement"]))
                    biwanshee.append(stringbuild)
                    self.amountlive += 1
                    self.amountlivestr = str(self.amountlive)
                    print(calc)
                #if calc['strengthRequirement'] < 55 and calc['dexterityRequirement'] < 121 and calc['intelligenceRequirement'] < 41 and calc['defenceRequirement'] < 5 and calc['agilityRequirement'] < 5 and calc['durability']>40 and calc[bilter] >dd and calc[addlost]> 20:
                if calc['strengthRequirement'] <= reqstr and calc['dexterityRequirement'] <= reqdex and calc['intelligenceRequirement'] <= reqint and calc['defenceRequirement'] <= reqdef and calc['agilityRequirement'] <= reqagil and calc[bilter] >ddd:
                    ddd = calc[bilter]
                    boi[ddd] = calc
                    jiwanshe.append(str(calc))
                    stringbuild = ("dura: " + str(calc["durability"]) + " chance: "
                        + str(calc["chance"])+ "%" + " " + str(biltera).lower().capitalize()+": " + str(calc["low"])+"->"+str(calc[biltera]) + " "
                        + "Skillrequirements:"+ " " + "Str: " + str(calc["strengthRequirement"])
                        + " Dex: " + str(calc["dexterityRequirement"])+" "
                        + "Intel: " + str(calc["intelligenceRequirement"])
                        + " Def: " + str(calc["defenceRequirement"])+" "
                        + "Agil: " + str(calc["agilityRequirement"]))
                    biwanshee.append(stringbuild)
                    self.amountlive += 1
                    self.amountlivestr = str(self.amountlive)
                    print(calc)
                #elif calc['strengthRequirement'] < 55 and calc['dexterityRequirement'] < 121 and calc['intelligenceRequirement'] < 41 and calc['defenceRequirement'] < 5 and calc['agilityRequirement'] < 5 and calc[addlost]> 20 and calc[bilter] == dd and calc['durability']>boi[dd]['durability']:
                elif calc['strengthRequirement'] <= reqstr and calc['dexterityRequirement'] <= reqdex and calc['intelligenceRequirement'] <= reqint and calc['defenceRequirement'] <= reqdef and calc['agilityRequirement'] <= reqagil and calc[bilter] == ddd and calc['durability']>boi[ddd]['durability']:
                    ddd = calc[bilter]
                    boi[ddd] = calc
                    jiwanshe.append(str(calc))
                    stringbuild = ("dura: " + str(calc["durability"]) + " chance: "
                        + str(calc["chance"])+ "%" + " " + str(biltera).lower().capitalize()+": " + str(calc["low"])+"->"+str(calc[biltera]) + " "
                        + "Skillrequirements:"+ " " + "Str: " + str(calc["strengthRequirement"])
                        + " Dex: " + str(calc["dexterityRequirement"])+" "
                        + "Intel: " + str(calc["intelligenceRequirement"])
                        + " Def: " + str(calc["defenceRequirement"])+" "
                        + "Agil: " + str(calc["agilityRequirement"]))
                    biwanshee.append(stringbuild)
                    self.amountlive += 1
                    self.amountlivestr = str(self.amountlive)
                    print(calc)
    def exportcalc_v2(self, hmap, durah, reqdura, reqcha, i, j, k, l, bilter, boi, reqstr, reqdex, reqint, reqdef, reqagil, reqlow, borted, kiki):
        global jiwanshe
        global biwanshee
        global ddd
        for m in borted:
            for n in borted:
                #calculating all the different combinations 
                #their dura with lvl and their max boost
                durability = durah + i['itemOnlyIDs']['durabilityModifier'] + j['itemOnlyIDs']['durabilityModifier'] + k['itemOnlyIDs']['durabilityModifier'] + l['itemOnlyIDs']['durabilityModifier'] + m['itemOnlyIDs']['durabilityModifier'] + n['itemOnlyIDs']['durabilityModifier']
                if durability < 1:
                    durability = 1
                if durability >= reqdura and not((i['name'] in hmap and j['name'] in hmap and k['name'] in hmap and l['name'] in hmap and m['name'] in hmap and n['name'] in hmap) and (hmap[i['name']]>hmap[j['name']] or hmap[j['name']]>hmap[k['name']] or hmap[k['name']]>hmap[l['name']] or hmap[l['name']]>hmap[m['name']] or hmap[m['name']]>hmap[n['name']])):
                #if durability >= reqdura:
                    calc ={}
                    a=i['ingredientPositionModifiers']
                    b=j['ingredientPositionModifiers']
                    c=k['ingredientPositionModifiers']
                    d=l['ingredientPositionModifiers']
                    e=m['ingredientPositionModifiers']
                    f=n['ingredientPositionModifiers']
                    fir = 0 + b['touching'] + c['touching'] + d['notTouching'] + e['notTouching'] + f['notTouching'] + c['above'] + e['above'] + b['left']
                    sec = 0 + a['touching'] + c['notTouching'] + d['touching'] + e['notTouching'] + f['notTouching'] + d['above'] + f['above'] + a['right']
                    thir = 0 + a['touching'] + b['notTouching'] + d['touching'] + e['touching'] + f['notTouching'] + a['under'] + e['above'] + d['left']
                    four = 0 + a['notTouching'] + b['touching'] + c['touching'] + e['notTouching'] + f['touching'] + b['under'] + f['above'] + c['right']
                    fif = 0 + a['notTouching'] + b['notTouching'] + c['touching'] + d['notTouching'] + f['touching'] + a['under'] + c['under'] + f['left']
                    six = 0 + a['notTouching'] + b['notTouching'] + c['notTouching'] + d['touching'] + e['touching'] + b['under'] + d['under'] + e['right']
                    calc['firstSlot'] = i['name']
                    calc['secondSlot'] = j['name']
                    calc['thirdSlot'] = k['name']
                    calc['fourthSlot'] = l['name']
                    calc['fifthSlot'] = m['name']
                    calc['sixthSlot'] = n['name']
                    calc['strengthRequirement'] = math.floor(i['itemOnlyIDs']['strengthRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['strengthRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['strengthRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['strengthRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['strengthRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['strengthRequirement']*(1+six/100))
                    calc['dexterityRequirement'] = math.floor(i['itemOnlyIDs']['dexterityRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['dexterityRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['dexterityRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['dexterityRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['dexterityRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['dexterityRequirement']*(1+six/100))
                    calc['intelligenceRequirement'] = math.floor(i['itemOnlyIDs']['intelligenceRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['intelligenceRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['intelligenceRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['intelligenceRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['intelligenceRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['intelligenceRequirement']*(1+six/100))
                    calc['defenceRequirement'] = math.floor(i['itemOnlyIDs']['defenceRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['defenceRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['defenceRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['defenceRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['defenceRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['defenceRequirement']*(1+six/100))
                    calc['agilityRequirement'] = math.floor(i['itemOnlyIDs']['agilityRequirement']*(1+fir/100)) + math.floor(j['itemOnlyIDs']['agilityRequirement']*(1+sec/100)) + math.floor(k['itemOnlyIDs']['agilityRequirement']*(1+thir/100)) + math.floor(l['itemOnlyIDs']['agilityRequirement']*(1+four/100)) + math.floor(m['itemOnlyIDs']['agilityRequirement']*(1+fif/100)) + math.floor(n['itemOnlyIDs']['agilityRequirement']*(1+six/100))
                    calc['durability'] = durability
                    op=math.floor(i['identifications'][bilter]['maximum']*(1+fir/100)) + math.floor(j['identifications'][bilter]['maximum']*(1+sec/100)) + math.floor(k['identifications'][bilter]['maximum']*(1+thir/100)) + math.floor(l['identifications'][bilter]['maximum']*(1+four/100)) + math.floor(m['identifications'][bilter]['maximum']*(1+fif/100)) + math.floor(n['identifications'][bilter]['maximum']*(1+six/100))
                    dop=math.floor(i['identifications'][bilter]['minimum']*(1+fir/100)) + math.floor(j['identifications'][bilter]['minimum']*(1+sec/100)) + math.floor(k['identifications'][bilter]['minimum']*(1+thir/100)) + math.floor(l['identifications'][bilter]['minimum']*(1+four/100)) + math.floor(m['identifications'][bilter]['minimum']*(1+fif/100)) + math.floor(n['identifications'][bilter]['minimum']*(1+six/100))
                    if op >= dop:
                        calc[bilter] = op
                        calc['low'] = dop
                    else:
                        calc[bilter] = dop
                        calc['low'] = op
                    #calc[addlost] = math.floor(i['identifications'][addlost]['maximum']*(1+fir/100)) + math.floor(j['identifications'][addlost]['maximum']*(1+sec/100)) + math.floor(k['identifications'][addlost]['maximum']*(1+thir/100)) + math.floor(l['identifications'][addlost]['maximum']*(1+four/100)) + math.floor(m['identifications'][addlost]['maximum']*(1+fif/100)) + math.floor(n['identifications'][addlost]['maximum']*(1+six/100))
                    #calc['lowtlost'] = math.floor(i['identifications'][addlost]['minimum']*(1+fir/100)) + math.floor(j['identifications'][addlost]['minimum']*(1+sec/100)) + math.floor(k['identifications'][addlost]['minimum']*(1+thir/100)) + math.floor(l['identifications'][addlost]['minimum']*(1+four/100)) + math.floor(m['identifications'][addlost]['minimum']*(1+fif/100)) + math.floor(n['identifications'][addlost]['minimum']*(1+six/100))
                    calc['chance'] = (1/(1+i['identifications'][bilter]['maximum']-i['identifications'][bilter]['minimum']))*(1/(1+j['identifications'][bilter]['maximum']-j['identifications'][bilter]['minimum']))*(1/(1+k['identifications'][bilter]['maximum']-k['identifications'][bilter]['minimum']))*(1/(1+l['identifications'][bilter]['maximum']-l['identifications'][bilter]['minimum']))*(1/(1+m['identifications'][bilter]['maximum']-m['identifications'][bilter]['minimum']))*(1/(1+n['identifications'][bilter]['maximum']-n['identifications'][bilter]['minimum']))
                    with your_moms_lock:
                        #res.append(calc)
                        #if calc['strengthRequirement'] < 55 and calc['dexterityRequirement'] < 121 and calc['intelligenceRequirement'] < 41 and calc['defenceRequirement'] < 5 and calc['agilityRequirement'] < 5 and calc['durability']>40 and calc[bilter] >70 and calc[addlost]> 20:
                        #if calc['durability']>40 and calc[bilter] >20 and calc[addlost]> 20:
                        if calc['strengthRequirement'] <= reqstr and calc['dexterityRequirement'] <= reqdex and calc['intelligenceRequirement'] <= reqint and calc['defenceRequirement'] <= reqdef and calc['agilityRequirement'] <= reqagil and calc[bilter] >=reqlow:
                            jiwanshe.append(str(calc))
                            stringbuild = ("dura: " + str(calc["durability"]) + " chance: "
                                + str(calc["chance"])+ "%" + " " + str(biltera).lower().capitalize()+": " + str(calc["low"])+"->"+str(calc[biltera]) + " "
                                + "Skillrequirements:"+ " " + "Str: " + str(calc["strengthRequirement"])
                                + " Dex: " + str(calc["dexterityRequirement"])+" "
                                + "Intel: " + str(calc["intelligenceRequirement"])
                                + " Def: " + str(calc["defenceRequirement"])+" "
                                + "Agil: " + str(calc["agilityRequirement"]))
                            biwanshee.append(stringbuild)
                            self.amountlive += 1
                            self.amountlivestr = str(self.amountlive) 
                        #if calc['strengthRequirement'] < 55 and calc['dexterityRequirement'] < 121 and calc['intelligenceRequirement'] < 41 and calc['defenceRequirement'] < 5 and calc['agilityRequirement'] < 5 and calc['durability']>40 and calc[bilter] >dd and calc[addlost]> 20:
                        if calc['strengthRequirement'] <= reqstr and calc['dexterityRequirement'] <= reqdex and calc['intelligenceRequirement'] <= reqint and calc['defenceRequirement'] <= reqdef and calc['agilityRequirement'] <= reqagil and calc[bilter] >ddd:
                            ddd = calc[bilter]
                            boi[ddd] = calc
                            jiwanshe.append(str(calc))
                            stringbuild = ("dura: " + str(calc["durability"]) + " chance: "
                                + str(calc["chance"])+ "%" + " " + str(biltera).lower().capitalize()+": " + str(calc["low"])+"->"+str(calc[biltera]) + " "
                                + "Skillrequirements:"+ " " + "Str: " + str(calc["strengthRequirement"])
                                + " Dex: " + str(calc["dexterityRequirement"])+" "
                                + "Intel: " + str(calc["intelligenceRequirement"])
                                + " Def: " + str(calc["defenceRequirement"])+" "
                                + "Agil: " + str(calc["agilityRequirement"]))
                            biwanshee.append(stringbuild)
                            self.amountlive += 1
                            self.amountlivestr = str(self.amountlive)
                        #elif calc['strengthRequirement'] < 55 and calc['dexterityRequirement'] < 121 and calc['intelligenceRequirement'] < 41 and calc['defenceRequirement'] < 5 and calc['agilityRequirement'] < 5 and calc[addlost]> 20 and calc[bilter] == dd and calc['durability']>boi[dd]['durability']:
                        elif calc['strengthRequirement'] <= reqstr and calc['dexterityRequirement'] <= reqdex and calc['intelligenceRequirement'] <= reqint and calc['defenceRequirement'] <= reqdef and calc['agilityRequirement'] <= reqagil and calc[bilter] == ddd and calc['durability']>boi[ddd]['durability']:
                            ddd = calc[bilter]
                            boi[ddd] = calc
                            jiwanshe.append(str(calc))
                            stringbuild = ("dura: " + str(calc["durability"]) + " chance: "
                                + str(calc["chance"])+ "%" + " " + str(biltera).lower().capitalize()+": " + str(calc["low"])+"->"+str(calc[biltera]) + " "
                                + "Skillrequirements:"+ " " + "Str: " + str(calc["strengthRequirement"])
                                + " Dex: " + str(calc["dexterityRequirement"])+" "
                                + "Intel: " + str(calc["intelligenceRequirement"])
                                + " Def: " + str(calc["defenceRequirement"])+" "
                                + "Agil: " + str(calc["agilityRequirement"]))
                            biwanshee.append(stringbuild)
                            self.amountlive += 1
                            self.amountlivestr = str(self.amountlive)
        self.myvalue+=kiki 
if __name__ == '__main__':
    TheLabApp().run()