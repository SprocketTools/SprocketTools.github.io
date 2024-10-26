from js import document
import random, time
guncals = [12, 20, 30, 37, 40, 45, 47, 50, 55, 57, 65, 73, 75, 76, 80, 85, 88, 90, 100, 105, 107, 110, 115, 120, 122, 125, 128, 130, 150, 152, 155, 183, 200, 240]
def update(*ags, **kws):
	# initial declaration
	IsHeavy = 0

	random.seed(time.time())
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
		MinWeight = 12
		MaxWeight = 30
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
		AdditionalNote = "File editing track size is permitted."
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
		AdditionalNote = "Open-top turrets are permitted.  If using an open-top, the turret space of firing compartments can be ignored."
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
		AdditionalNote = "File editing tracks is allowed."
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
		AdditionalNote = "Editing load speed is allowed for autocannons."
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
		Inspiration = "Try using the BMP-2 or T-40 as a reference!  Just don't go looking in Russia for a real one..."
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
		AdditionalNote = "You get bonus points for armoring up a train from the Island of Sodor"
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
		Gun = GunCals[round(RNG * GunListSize) - 1]
		WeaponType = "cannon"
	SecondaryGunCount = round(GunCount / 2)
	PrimaryGunCount = GunCount - SecondaryGunCount
	AmmoMin = round(3 * (1000 / Gun))
	
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
def rerollRNG():
	RNG = random.random()
	   
