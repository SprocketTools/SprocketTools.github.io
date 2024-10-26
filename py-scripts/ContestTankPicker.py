from js import document, alert
import random, time
guncals = [12, 20, 30, 37, 40, 45, 47, 50, 55, 57, 65, 73, 75, 76, 80, 85, 88, 90, 100, 105, 107, 110, 115, 120, 122, 125, 128, 130, 150, 152, 155, 183, 200, 240]

def update(*ags, **kws):
	# initial declaration
	IsHeavy = 0

	ID = document.getElementById('inputbox').value
	offsetRNG = document.getElementById('offsetRNG').value
	try:
		random.seed(int(ID + offsetRNG) + 69)
	except ValueError:
		ID = ID
	guncals = [12, 20, 30, 37, 40, 45, 47, 50, 55, 57, 65, 73, 75, 76, 80, 85, 88, 90, 100, 105, 107, 110, 115, 120, 122, 125, 128, 130, 150, 152, 155, 183, 200, 240]
	VehicleName = "error"
	CannonSuffix = ""
	VehGroup = round(1000*random.random())/10
	if VehGroup < 10:
		VehicleName = "Semi-Turreted Tank Destroyer"
		MinWeight = 7
		MaxWeight = 50
		WeightTol = 1
		HeavyWeightAdj = 30
		HeavyChance = 40
		GunCals = [57, 65, 73, 75, 76, 80, 85, 88, 90, 100, 105, 107, 110, 115, 120, 122, 125, 128, 130]
		HowitzerCals = [105, 155, 183, 240]
		HowitzerChance = 25
		MaxGuns = 2
		MultiGunChance = 25
		MinCylCount = 6
		MaxCylCount = 13
		AdditionalNote = "Cannons need to be restricted to 60 degrees of horizontal traverse in either direction."
		Inspiration = "Check out the T28 Concept!"
		NeedsPlural = 0

	elif VehGroup < 19:
		VehicleName = "Light Tank"
		MinWeight = 10
		MaxWeight = 22
		WeightTol = 1
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [37, 40, 45, 47, 50, 57, 65, 73, 75, 76, 80, 85, 88, 90]
		HowitzerCals = [105, 155, 183, 240]
		HowitzerChance = 0
		MaxGuns = 2
		MultiGunChance = 12
		MinCylCount = 6
		MaxCylCount = 8
		AdditionalNote = ""
		Inspiration = ""
		NeedsPlural = 0
		
	elif VehGroup < 28:
		VehicleName = "Heavy Tank"
		MinWeight = 38
		MaxWeight = 47
		WeightTol = 1
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [75, 76, 80, 85, 88, 90, 94, 105]
		HowitzerCals = [105, 155, 183, 240]
		HowitzerChance = 38
		MaxGuns = 2
		MultiGunChance = 35
		MinCylCount = 8
		MaxCylCount = 12
		AdditionalNote = ""
		Inspiration = ""
		NeedsPlural = 0
		
	elif VehGroup < 37:
		VehicleName = "Medium Tank"
		MinWeight = 14
		MaxWeight = 31
		WeightTol = 1
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [57, 65, 73, 75, 76, 80, 85, 88, 90]
		HowitzerCals = [105, 152]
		HowitzerChance = 25
		MaxGuns = 2
		MultiGunChance = 25
		MinCylCount = 6
		MaxCylCount = 12
		AdditionalNote = ""
		Inspiration = ""
		NeedsPlural = 0
		
	elif VehGroup < 45:
		VehicleName = "Armored car"
		MinWeight = 12
		MaxWeight = 26
		WeightTol = 1
		HeavyWeightAdj = 10
		HeavyChance = 30
		GunCals = [20, 30, 37, 40, 45, 47, 50, 55, 57]
		HowitzerCals = [105]
		HowitzerChance = 17
		MaxGuns = 2
		MultiGunChance = 20
		MinCylCount = 6
		MaxCylCount = 8
		AdditionalNote = "File editing track size is permitted, should you wish to use wheels."
		Inspiration = "Just think back to your worst enemy when playing WOT or WT, and make it even worse to fight against!"
		NeedsPlural = 1

	elif VehGroup < 53:
		VehicleName = "MBT"
		MinWeight = 35
		MaxWeight = 75
		WeightTol = 1
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [100, 105, 107, 110, 115, 120, 122, 125, 128, 130, 150, 152, 155]
		HowitzerCals = [105]
		HowitzerChance = 0
		MaxGuns = 1
		MultiGunChance = 0
		MinCylCount = 10
		MaxCylCount = 16
		AdditionalNote = ""
		Inspiration = "Leopard 2 is a good place to start."
		NeedsPlural = 0
		
	elif VehGroup < 61:
		VehicleName = "Superheavy"
		MinWeight = 70
		MaxWeight = 90
		WeightTol = 1
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [105, 120, 122, 125, 128, 130, 150, 152, 155, 183, 200, 240]
		HowitzerCals = [105]
		HowitzerChance = 0
		MaxGuns = 2
		MultiGunChance = 0
		MinCylCount = 8
		MaxCylCount = 15
		AdditionalNote = ""
		Inspiration = "Just downsize the Maus a bit!  Surely nothing will go wrong..."
		NeedsPlural = 0
		
	elif VehGroup < 67:
		VehicleName = "Artillery"
		MinWeight = 14
		MaxWeight = 20
		WeightTol = 2
		HeavyWeightAdj = 20
		HeavyChance = 40
		GunCals = [57, 65, 73, 75, 76, 80, 85, 88, 90, 100, 105, 107, 110, 115, 120, 122, 125, 128, 130, 150, 152, 155, 183, 200, 240]
		HowitzerCals = [105]
		HowitzerChance = 0
		MaxGuns = 2
		MultiGunChance = 12
		MinCylCount = 6
		MaxCylCount = 10
		AdditionalNote = "Open-top turrets are permitted.  If using an open-top, the turret space of firing compartments can be ignored."
		Inspiration = "Try building a knockoff M41 tank."
		NeedsPlural = 1

	elif VehGroup < 72:
		VehicleName = "Turreted tankette"
		MinWeight = 7
		MaxWeight = 10
		WeightTol = 1
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [20, 30, 37, 40, 45, 47, 50, 55, 57]
		HowitzerCals = [105]
		HowitzerChance = 15
		MaxGuns = 1
		MultiGunChance = 0
		MinCylCount = 4
		MaxCylCount = 8
		AdditionalNote = "Open-top turrets are permitted.  If using an open-top, the internal space of the rotating turret and the gun mantlet can be ignored."
		Inspiration = "The T-26 is a good example tank."
		NeedsPlural = 0

	elif VehGroup < 77:
		VehicleName = "Landship"
		MinWeight = 20
		MaxWeight = 40
		WeightTol = 1
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [57, 65, 73, 75, 76, 80, 85, 88, 90, 100, 105, 107, 110, 115, 120]
		HowitzerCals = [105, 155, 183, 200]
		HowitzerChance = 28
		MaxGuns = 3
		MultiGunChance = 30
		MinCylCount = 6
		MaxCylCount = 8
		AdditionalNote = ""
		Inspiration = "The T-35 is a good example.  Just not with that many turrets..."
		NeedsPlural = 0

	elif VehGroup < 81:
		VehicleName = "Toyota Hilux SPG"
		MinWeight = 12
		MaxWeight = 22
		WeightTol = 2
		HeavyWeightAdj = 12
		HeavyChance = 24
		GunCals = [37, 40, 45, 47, 50, 55, 57, 65, 73, 75, 76, 80, 85, 88, 90]
		HowitzerCals = [105, 155, 183, 200]
		HowitzerChance = 0
		MaxGuns = 1
		MultiGunChance = 0
		MinCylCount = 6
		MaxCylCount = 6
		AdditionalNote = "File editing tracks and building the vehicle as an open-top is permitted.  Additionally, if using an open-top, the internal space of the gun compartment and its horizontal swivel can be ignored."
		NeedsPlural = 0
		Inspiration = ""

	elif VehGroup < 84:
		VehicleName = "Armored Recovery Vehicle"
		MinWeight = 25
		MaxWeight = 40
		WeightTol = 1
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [37, 40, 45, 47, 50, 55, 57, 65, 73, 75, 76, 80, 85, 88]
		HowitzerCals = [105, 155, 183, 200]
		HowitzerChance = 0
		MaxGuns = 1
		MultiGunChance = 0
		MinCylCount = 6
		MaxCylCount = 12
		AdditionalNote = ""
		Inspiration = "Using a common tank chassis, such as the Sherman chassis, is a good start."
		NeedsPlural = 1

	elif VehGroup < 87:
		VehicleName = "Modernized WWI Tank"
		MinWeight = 10
		MaxWeight = 24
		WeightTol = 1
		HeavyWeightAdj = 20
		HeavyChance = 30
		GunCals = [30, 37, 40, 45, 47, 50, 55, 57, 65, 73, 75, 76, 80, 85, 88, 90]
		HowitzerCals = [105, 152]
		HowitzerChance = 15
		MaxGuns = 2
		MultiGunChance = 30
		MinCylCount = 6
		MaxCylCount = 12
		AdditionalNote = ""
		Inspiration = "ARL 44 is a fairly good example tank."
		NeedsPlural = 0
		
	elif VehGroup < 90:
		VehicleName = "Bunker Buster"
		MinWeight = 30
		MaxWeight = 50
		WeightTol = 2
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [88, 90, 100, 105, 107, 110, 115, 120, 130]
		HowitzerCals = [183, 250, 280, 300, 320, 380]
		HowitzerChance = 35
		MaxGuns = 1
		MultiGunChance = 30
		MinCylCount = 6
		MaxCylCount = 12
		AdditionalNote = ""
		Inspiration = "The T28 is a good example of a siege tank."
		NeedsPlural = 0

	elif VehGroup < 93:
		VehicleName = "Infantry Fighting Vehicle"
		MinWeight = 12
		MaxWeight = 30
		WeightTol = 1
		HeavyWeightAdj = 10
		HeavyChance = 20
		GunCals = [57, 65, 73, 75, 76, 80, 85, 88]
		HowitzerCals = [152, 155, 183, 250]
		HowitzerChance = 0
		MaxGuns = 1
		MultiGunChance = 0
		MinCylCount = 8
		MaxCylCount = 10
		AdditionalNote = "File editing track size is allowed, should you wish to use wheels."
		Inspiration = "Check out PatchBits' IFV from our previous contest: https://www.youtube.com/watch?v=z1ohzRBdhq4"
		NeedsPlural = 0

	elif VehGroup < 95:
		VehicleName = "Amphibious Tank"
		MinWeight = 16
		MaxWeight = 28
		WeightTol = 1
		HeavyWeightAdj = 10
		HeavyChance = 20
		GunCals = [37, 40, 45, 47, 50, 55, 57, 65, 73, 75, 76]
		HowitzerCals = [152, 155, 183, 250]
		HowitzerChance = 0
		MaxGuns = 1
		MultiGunChance = 0
		MinCylCount = 6
		MaxCylCount = 12
		AdditionalNote = ""
		Inspiration = "Try using the BMP-2 as a reference!  Just don't go looking in Russia for a real one..."
		NeedsPlural = 1
		
	elif VehGroup < 97:
		VehicleName = "SPAA"
		MinWeight = 13
		MaxWeight = 26
		WeightTol = 1
		HeavyWeightAdj = 20
		HeavyChance = 20
		GunCals = [20, 30, 37, 40, 45, 47, 50, 55, 57, 65, 73, 75, 76, 80, 85, 88, 90]
		HowitzerCals = [152, 155, 183, 250]
		HowitzerChance = 0
		MaxGuns = 4
		MultiGunChance = 100
		MinCylCount = 6
		MaxCylCount = 12
		AdditionalNote = ""
		Inspiration = "The Flakpanzer Gepard is a good example of a SPAA."
		NeedsPlural = 0

	elif VehGroup < 99.5:
		VehicleName = "Armored Train"
		MinWeight = 30
		MaxWeight = 40
		WeightTol = 2
		HeavyWeightAdj = 10
		HeavyChance = 50
		GunCals = [57, 65, 73, 75, 76, 80, 85, 88, 90]
		HowitzerCals = [152, 155, 183, 240]
		HowitzerChance = 35
		MaxGuns = 2
		MultiGunChance = 50
		MinCylCount = 10
		MaxCylCount = 14
		AdditionalNote = "File editing tracks to be invisible is permitted.  Note that you get bonus points for armoring up a train from the Island of Sodor."
		Inspiration = "Check out Nirrti's armored train: https://streamable.com/rxqncl"
		NeedsPlural = 1

	elif VehGroup < 100:
		VehicleName = "Amogus-Piloted Tank"
		MinWeight = 20
		MaxWeight = 40
		WeightTol = 1
		HeavyWeightAdj = 0
		HeavyChance = 0
		GunCals = [37, 40, 45, 47, 50, 55, 57, 65, 73, 75, 76, 80, 85, 88, 90, 94, 100, 105]
		HowitzerCals = [105, 152]
		HowitzerChance = 15
		MaxGuns = 2
		MultiGunChance = 25
		MinCylCount = 8
		MaxCylCount = 12
		AdditionalNote = "Your vehicle must appear to have an Among Us crewmate as the driver or commander.  Otherwise, any vehicle type is permitted.  Congrats on getting a wild card!"
		Inspiration = ""
		NeedsPlural = 1

	#establishing new variables
	Gun = 57
	GunListSize = len(GunCals)
	HowitzerListSize = len(HowitzerCals)
	RNG = random.random()

	#determine if it is a "heavy" variant or not
	if (random.random() < HeavyChance/100.0):
		IsHeavy = 1
		VehicleName = "Heavy " + VehicleName
		print("Build a heavy " + VehicleName + "!")
	else:
		print("Build a " + VehicleName + "!")


	ActWeight = MinWeight + round(random.random()*(MaxWeight -MinWeight)) + HeavyWeightAdj*IsHeavy
	MinWeightVar = ActWeight - WeightTol
	MaxWeightVar = ActWeight + WeightTol
	print("Minimum vehicle weight: " + str(MinWeightVar) + ".0T")
	print("Maximum vehicle weight: " + str(MaxWeightVar) + ".0T")
	
	#next we pick the amount of guns in the vehicle
	rerollRNG()
	GunCount = 1
	i = 2
	while i < 20 and i <= MaxGuns:
		if RNG < (MultiGunChance/((i-1)*100)):
			GunCount = i
		i += 1
		if GunCount > 1:
			CannonSuffix = "s"
	print("Gun count: " + str(GunCount))
	
	# here we pick the caliber of the main gun
	Gun = 0
	GunSec = 0
	
	rerollRNG()
	if (random.random() < HowitzerChance/100.0):
		Gun = HowitzerCals[round(RNG*HowitzerListSize)-1]
		WeaponType = "howitzer"
	else:
		Gun = GunCals[round(RNG*GunListSize)-1]
		WeaponType = "cannon"
	SecondaryGunCount = round(GunCount/2)
	PrimaryGunCount = GunCount - SecondaryGunCount		
	AmmoMin = round(1000/(Gun))

	
	# here we pick the caliber of the secondary gun
	rerollRNG()
	i = 0
	if GunCount > 1:
		GunSec = GunCals[0]
		WeaponTypeSec = "cannon"
		
		if Gun < GunCals[2] and WeaponType == "cannon":
			Gun = GunCals[round((RNG)*(GunListSize-3)) + 2]
		
		if VehicleName == "SPAA" or VehicleName == "Heavy SPAA":
			ActWeight = ActWeight + (round(((Gun*0.0115)**3)*SecondaryGunCount/2))
		if VehicleName != "SPAA" and VehicleName != "Heavy SPAA":
			ActWeight = ActWeight + (round(((GunSec*0.0115)**3)*SecondaryGunCount/2))
		
	else:
		PrimaryGunCount = GunCount
		SecondaryGunCount = 0
		GunSec = 0
	if VehicleName == "SPAA" or VehicleName == "Heavy SPAA":
		PrimaryGunCount = GunCount
		SecondaryGunCount = 0
		GunSec = 0
	
	ActWeight = ActWeight + (round(((Gun*0.0115)**3)*PrimaryGunCount/2))

	#next we set the engine requirements
	rerollRNG()
	CylCount = MinCylCount + round(RNG*(MaxCylCount - MinCylCount))
	rerollRNG()
	if RNG < 0.5:
		CylCount = round(CylCount/2)*2
	print("Engine: " + str(CylCount) + " cylinders")


	#weight adjustment for gun calibers (currently only does one-half of the correct adjustment)
	ActWeight = ActWeight + round(((CylCount*0.2)**3)/2)
	print(ActWeight)
	
	if NeedsPlural == 1 and IsHeavy == 0:
		promptname = "Build an " + VehicleName + "!"
	else:
		promptname = "Build a " + VehicleName + "!"
	
	if SecondaryGunCount == 0:
		cannon_text = " and a " + str(Gun) + "mm " + WeaponType + CannonSuffix
	if SecondaryGunCount > 0:
		cannon_text = ", " + str(PrimaryGunCount) + "x " + str(Gun) + "mm " + WeaponType + ", and " + str(SecondaryGunCount) + "x " + str(GunSec) + "mm " + WeaponTypeSec
	if VehicleName == "SPAA" or VehicleName == "Heavy SPAA":
		cannon_text = " and " + str(GunCount) + "x " + str(Gun) + "mm cannon" + CannonSuffix
	
	weight_text = "Your vehicle needs to weigh between " + str(ActWeight - WeightTol) + " and " +  str(ActWeight + WeightTol) + " tons."
	engine_text = "Power your vehicle using a " + str(CylCount) + "-cylinder engine!"
	ammo_text = "Lastly, don't forget to have at least " + str(AmmoMin) + " rounds of ammo!"
	inspiration_text = "Need Inspiration?  " + Inspiration
	combined_text = "Equip a " + str(CylCount)  + "-cylinder engine" + cannon_text + "!"
	
	pyscript.write("promptname", promptname)
	pyscript.write("weight", weight_text)
	pyscript.write("cannon", combined_text)
	#pyscript.write("engine", engine_text)
	pyscript.write("minimum_ammo", ammo_text)
	pyscript.write("additional_note", AdditionalNote)
	if Inspiration:
		pyscript.write("inspiration", inspiration_text)
	else:
		pyscript.write("inspiration", "")
	ID = document.getElementById('inputbox').value
	ID = ID.lower()
	if ID == "sus" or ID == "among us" or ID == "amogus"  or ID == "hamish dunn":
		pyscript.write("promptname", "Yo what is up you guys right now we’re at mcdonalds, and it is currently 3 in the morning and we just found out when you come to mcdonalds at 3 in the morning, you can order the among us happy meal you guys, that’s right, you heard, me, the among us happy meal, and there’s a toy inside of among us- you can either be a crewmate, or it can be an impostor and if you guys do not know what among us is, you must be living under a rock you guys, this game is insane, ok? so you can play with a bunch of friends ok? like 8, i- i- i think it’s up to 10 people you can play with, and there’s impostors, and there’s crewmates, and pretty much the impostor is trying to sabotage the whole game and trying to win. it’s insane you guys, once again, this- this video is not sponsored at all, but this game is insane. so we got so excited guys we love the game and we found that the mcdonalds is offering an among us happy meal, AND there’s a toy inside, but supposedly, when you get this happy meal you guys, something scary and weird with the impostor. now i don’t really believe it, but these videos i’ve been seeing on youtube have been insane, so that’s why we’re here right now, we’re gonna go through the drive through, and we’re gonna order the among us happy meal. But i need EVERYONE to like this video if you’re excited, ok? like this video with your knuckles right now, just smash, hit the like button, SUPER HARD you guys, on the count of 3 seconds i wanna see what you guys can do cuz i can’t do it, and if cole can’t do it, no one could like this video with their knuckles so let’s see if you guys can do it in 3 seconds. 3, 2, 1. OH HO!")
		pyscript.write("weight", " ")
		pyscript.write("cannon", " ")
		#pyscript.write("engine", " ")
		pyscript.write("minimum_ammo", " ")
		pyscript.write("additional_note", " ")
		pyscript.write("inspiration", "When the impostor is sus!")

	elif ID == "colson":
		pyscript.write("promptname", "Yo what is up you guys right now we’re at mcdonalds, and it is currently 3 in the morning and we just found out when you come to mcdonalds at 3 in the morning, you can order the among us happy meal you guys, that’s right, you heard, me, the among us happy meal, and there’s a toy inside of among us- you can either be a crewmate, or it can be an impostor and if you guys do not know what among us is, you must be living under a rock you guys, this game is insane, ok? so you can play with a bunch of friends ok? like 8, i- i- i think it’s up to 10 people you can play with, and there’s impostors, and there’s crewmates, and pretty much the impostor is trying to sabotage the whole game and trying to win. it’s insane you guys, once again, this- this video is not sponsored at all, but this game is insane. so we got so excited guys we love the game and we found that the mcdonalds is offering an among us happy meal, AND there’s a toy inside, but supposedly, when you get this happy meal you guys, something scary and weird with the impostor. now i don’t really believe it, but these videos i’ve been seeing on youtube have been insane, so that’s why we’re here right now, we’re gonna go through the drive through, and we’re gonna order the among us happy meal. But i need EVERYONE to like this video if you’re excited, ok? like this video with your knuckles right now, just smash, hit the like button, SUPER HARD you guys, on the count of 3 seconds i wanna see what you guys can do cuz i can’t do it, and if cole can’t do it, no one could like this video with their knuckles so let’s see if you guys can do it in 3 seconds. 3, 2, 1. OH HO!")
		pyscript.write("weight", " ")
		pyscript.write("cannon", " ")
		#pyscript.write("engine", " ")
		pyscript.write("minimum_ammo", " ")
		pyscript.write("additional_note", " ")
		pyscript.write("inspiration", "Correct, I am the developer of this website!")
	elif ID == "258242333693181952":
		pyscript.write("inspiration", "Your determination to build contest tanks, despite the endless crashes you're dealing with, is honorable.  We can't wait to see your entry to the contest!")
	elif ID == "863131206798934067":
		pyscript.write("inspiration", "Amogus.")
	elif "u/" in ID:
		pyscript.write("promptname", "Invalid ID.  Remove the u/ from your ID, then try again.")
		pyscript.write("weight", " ")
		pyscript.write("cannon", " ")
		#pyscript.write("engine", " ")
		pyscript.write("minimum_ammo", " ")
		pyscript.write("additional_note", " ")
	elif ID == "hamish dunn":
		pyscript.write("inspiration", "Fun fact: Sprocket Ship Design was filmed in a modified Sandbox map!")
	elif ID == "243299062164619265" or ID == "1032502622965469194" or ID == "1126112072099450922" or ID == "1102877006586200124" or ID == "963833157566734346" or ID == "433617207734304778" or ID == "1062212240830369903" or ID == "651228440422252555" or ID == "1102879910768418876" or ID == "1110660875632787537" or ID == "1114307088403922974" or ID == "1106699028982398997" or ID == "1120759016302313493" or ID == "" or ID == "1120759016302313493" or ID == "1097905019069677568" or ID == "606700678966018058" or ID == "606700678966018058" or ID == "604417737258827797" or ID == "842052491700731934":
		pyscript.write("promptname", "This user ID is not eligible to participate in the Youtube Community Clash")
		pyscript.write("weight", " ")
		pyscript.write("cannon", " ")
		#pyscript.write("engine", " ")
		pyscript.write("minimum_ammo", " ")
		pyscript.write("additional_note", " ")
		pyscript.write("inspiration", " ")
	else:
		if ID.isdigit():
			ID = ID
	
def rerollRNG():
	RNG = random.random()
	   
