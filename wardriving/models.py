from django.db import models

# Create your models here.
class WigleWiFiNetwork(models.Model):
	trilat = models.FloatField()
	trilong = models.FloatField()
	ssid = models.TextField()
	qos = models.IntegerField()
	transid	= models.TextField()
	firsttime = models.TextField()
	lasttime = models.TextField()
	lastupdt = models.TextField()
	netid = models.TextField()
	name = models.TextField()
	type = models.TextField()
	comment = models.TextField()
	wep = models.TextField()
	bcninterval = models.IntegerField()
	freenet = models.TextField()
	dhcp = models.TextField()
	paynet = models.TextField()
	userfound = models.BooleanField()
	channel = models.IntegerField()
	encryption = models.TextField()
	country = models.TextField()
	region = models.TextField()
	housenumber = models.TextField()
	road = models.TextField()
	city = models.TextField()
	postalcode = models.TextField()

class WigleNetSearchResponse(models.Model):
	success = models.BooleanField()
	totalResults = models.BigIntegerField()
	first = models.BigIntegerField()
	last = models.BigIntegerField()
	resultCount = models.BigIntegerField()
	results = models.ManyToManyField(WigleWiFiNetwork, on_delete=models.CASCADE)
	searchAfter = models.TextField() # Use this in future searches to get the next page of data
	search_after = models.BigIntegerField() # deprecated, though may still be in use in wigle db?

class WigleGroup(models.Model):
	groupId = models.TextField()
	groupName = models.TextField()
	owner = models.TextField()
	discovered = models.BigIntegerField()
	total = models.BigIntegerField()
	genDisc = models.BigIntegerField()
	authType = models.TextField()
	groupOwner = models.BooleanField()

class WigleGroupMember(models.Model):
	groupId = models.TextField()
	username = models.TextField()
	status = models.TextField()
	discovered = models.BigIntegerField()
	total = models.BigIntegerField()
	genDisc = models.BigIntegerField()
	firstTransid = models.TextField()
	lastTransid = models.TextField()
	monthCount = models.BigIntegerField()
	prevMonthCount = models.BigIntegerField()

class WigleGroupMemberResponse(models.Model):
	success = models.BooleanField()
	users = models.ForeignKey(WigleGroupMember, on_delete=models.CASCADE)
	group = models.ForeignKey(WigleGroup, on_delete=models.CASCADE)

class WigleGroupResponse(models.Model):
	success = models.BooleanField()
	groupId = models.TextField()
	users = models.ManyToManyField(WigleGroupMember, on_delete=models.CASCADE)
	group = models.ForeignKey(WigleGroup, on_delete=models.CASCADE)

class WigleGroupResponse(models.Model):
	success = models.BooleanField()
	groupId = models.TextField()
	users = models.ManyToManyField(WigleGroupMember, on_delete=models.CASCADE)
	group = models.ForeignKey(WigleGroup, on_delete=models.CASCADE)

class WigleGeocodingResponse(models.Model):
	address = models.TextField() #Holds json obj as string
	lat = models.FloatField()
	lon = models.FloatField()
	importance = models.FloatField()
	place_id = models.BigIntegerField()
	licence = models.TextField()
	osm_type = models.TextField()
	display_name = models.TextField()
	boundingbox = models.TextField() #Holds json list of floating numbers as string

class WigleNetworkGeocodingResponse(models.Model):
	success = models.BooleanField()
	results = models.ManyToManyField(WigleGeocodingResponse, on_delete=models.CASCADE)

class WigleWiFiLocation(models.Model):
	alt = models.IntegerField()
	accuracy = models.FloatField()
	lastupdt = models.TextField()
	latitude = models.FloatField()
	longitude = models.FloatField()
	month = models.TextField()
	ssid = models.TextField()
	time = models.TextField()
	signal = models.FloatField()
	name = models.TextField()
	netId = models.TextField()
	noise = models.FloatField()
	snr = models.FloatField()
	wep = models.TextField()
	encryptionValue = models.TextField()

class WigleWiFiNetworkWithLocation(models.Model):
	trilat = models.FloatField()
	trilong = models.FloatField()
	ssid = models.TextField()
	qos = models.IntegerField()
	transid = models.TextField()
	firsttime = models.TextField()
	lasttime = models.TextField()
	lastupdt = models.TextField()
	netid = models.TextField()
	name = models.TextField()
	type = models.TextField()
	comment = models.TextField()
	wep = models.TextField()
	bcninterval = models.IntegerField()
	freenet = models.TextField()
	dhcp = models.TextField()
	paynet = models.TextField()
	userfound = models.BooleanField()
	channel = models.IntegerField()
	locationData = models.ManyToManyField(WigleWiFiLocation, on_delete=models.CASCADE)
	encryption = models.TextField()
	country = models.TextField()
	region = models.TextField()
	housenumber = models.TextField()
	road = models.TextField()
	city = models.TextField()
	postalcode = models.TextField()

class WigleWiFiNetworkDetailResponse(models.Model):
	success = models.BooleanField()
	cdma = models.BooleanField()
	gsm = models.BooleanField()
	lte = models.BooleanField()
	wcdma = models.BooleanField()
	wifi = models.BooleanField()
	addresses = models.ManyToManyField(WigleGeocodingResponse, on_delete=models.CASCADE)
	results = models.ManyToManyField(WigleWiFiNetworkWithLocation, on_delete=models.CASCADE)

class WigleNetCommentResponse(models.Model):
	success = models.BooleanField()
	comment = models.TextField()
	netid = models.TextField()

class WiglePerson(models.Model):
	userid = models.TextField()
	email = models.TextField()
	donate = models.TextField()
	joindate = models.TextField()
	lastlogin = models.TextField()
	session = models.TextField()
	success = models.TextField()

class WigleAuthToken(models.Model):
	authName = models.TextField()
	token = models.TextField()
	status = models.TextField() #Enum:[ STATUS_ACTIVE, STATUS_DISABLED ]
	type = models.TextField() #Enum:[ API, COMMAPI, ANDROID, COOKIE ]
	personId = models.BigIntegerField()

class WigleAuthTokensResponse(models.Model):
	success = models.BooleanField()
	results = models.ManyToManyField(WigleAuthToken, on_delete=models.CASCADE)

class WigleUserStandings(models.Model):
	rank = models.BigIntegerField()
	monthRank = models.BigIntegerField()
	userName = models.TextField()
	discoveredWiFiGPS = models.BigIntegerField()
	discoveredWiFiGPSPercent = models.FloatField()
	discoveredWiFi = models.BigIntegerField()
	discoveredCellGPS = models.BigIntegerField()
	discoveredCell = models.BigIntegerField()
	discoveredBtGPS = models.BigIntegerField()
	discoveredBt = models.BigIntegerField()
	eventMonthCount = models.BigIntegerField()
	eventPrevMonthCount = models.BigIntegerField()
	prevRank = models.BigIntegerField()
	prevMonthRank = models.BigIntegerField()
	totalWiFiLocations = models.BigIntegerField()
	first = models.TextField()
	last = models.TextField()
	self = models.BooleanField()

class WigleUserStandings(models.Model):
	success = models.BooleanField()
	imageBadgeUrl = models.TextField()
	statistics = models.ForeignKey(WigleUserStandings, on_delete=models.CASCADE)
	rank = models.BigIntegerField()
	monthRank = models.BigIntegerField()
	user = models.TextField()

class WigleTransidResponse(models.Model):
	file = models.TextField()
	size = models.BigIntegerField()
	transId = models.TextField()

class WigleUploadResultsResponse(models.Model):
	timeTaken = models.TextField()
	filesize = models.BigIntegerField()
	filename = models.TextField()
	transids = models.ManyToManyField(WigleTransidResponse, on_delete=models.CASCADE)

class WigleUploadResponse(models.Model):
	success = models.BooleanField()
	warning = models.TextField()
	results = models.ManyToManyField(WigleUploadResultsResponse, on_delete=models.CASCADE)
	observer = models.TextField()

class WigleTransLog(models.Model):
	transid = models.TextField()
	username = models.TextField()
	firstTime = models.TextField()
	lastupdt = models.TextField()
	fileName = models.TextField()
	fileSize = models.BigIntegerField()
	fileLines = models.BigIntegerField()
	status = models.TextField()
	discoveredGps = models.BigIntegerField()
	discovered = models.BigIntegerField()
	total = models.BigIntegerField()
	totalGps = models.BigIntegerField()
	totalLocations = models.BigIntegerField()
	percentDone = models.FloatField()
	timeParsing = models.BigIntegerField()
	genDiscovered = models.BigIntegerField()
	genDiscoveredGps = models.BigIntegerField()
	genTotal = models.BigIntegerField()
	genTotalGps = models.BigIntegerField()
	genTotalLocations = models.BigIntegerField()
	btDiscovered = models.BigIntegerField()
	btDiscoveredGps = models.BigIntegerField()
	btTotal = models.BigIntegerField()
	btTotalGps = models.BigIntegerField()
	btTotalLocations = models.BigIntegerField()
	wait = models.BigIntegerField()

class WigleTranslogResponse(models.Model):
	success = models.BooleanField()
	results = models.ManyToManyField(WigleTransLog, on_delete=models.CASCADE)
	processingQueueDepth = models.BigIntegerField()
	geoQueueDepth = models.BigIntegerField()
