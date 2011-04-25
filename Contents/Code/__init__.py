####################################################################################################

VIDEO_PREFIX = "/video/skyplayer"

NAME = L('Title')

ART = 'art-default.jpg'
ICON = 'icon-default.png'

LOGIN_URL = 'https://skyplayer.sky.com/vod/content/Home/Application_Navigation/Sign_in/content/login.do'
PLAYER_URL = 'http://skyplayer.sky.com/vod/page/playLiveTv.do?epgChannelId=%s'

# Entertainment
SKY_ONE = "1402"
SKY_LIVING = "2201"
SKY_ATLANTIC = "1412"
GOLD = "2304"
MTV = "2501"

# Lifestyle
SKY_ARTS_ONE = "1752"

# Movies
SKY_PREMIERE = "1409"
SKY_SHOWCASE = "1814"
SKY_ACTION = "1001"
SKY_FAMILY = "1808"

# Sports
SKY_SPORTS_ONE = "1301"
SKY_SPORTS_TWO = "1302"
SKY_SPORTS_THREE = "1333"
SKY_SPORTS_FOUR = "1322"
SKY_SPORTS_NEWS = "1314"
EURO_SPORT = "1726"

# Children
CARTOON_NETWORK = "5601"
BOOMERANG = "5609"
NICKELODEON = "1846"
NICKELODEON_JR = "1857"
DISNEY_XD = "1843"
DISNEY_CHANNEL = "1881"

# Documentaries
NAT_GEO = "1806"
NAT_GEO_WILD = "1847"

SKY_LIVING_IT = "2207"

SKY_NEWS = "1404"

ERROR = MessageContainer('Network Error','A Network error has occurred')

####################################################################################################

channels = { 
    "106": { 
        'url': SKY_ONE, 
        'title': Locale.LocalString('Sky1Title'), 
        'subtitle': Locale.LocalString('Sky1Subtitle'), 
        'summary': Locale.LocalString('Sky1Summary'),
        'thumb': "icon-sky1.png" },
    "107": {
        'url': SKY_LIVING, 
        'title': Locale.LocalString('SkyLivingTitle'), 
        'subtitle': Locale.LocalString('SkyLivingSubtitle'), 
        'summary': Locale.LocalString('SkyLivingSummary'),
        'thumb': "icon-skyliving.png" },
    "108": {
        'url': SKY_ATLANTIC, 
        'title': Locale.LocalString('SkyAtlanticTitle'), 
        'subtitle': Locale.LocalString('SkyAtlanticSubtitle'), 
        'summary': Locale.LocalString('SkyAtlanticSummary'),
        'thumb': "icon-skyatlantic.png" },
    "110": {
        'url': GOLD, 
        'title': Locale.LocalString('GoldTitle'), 
        'subtitle': Locale.LocalString('GoldSubtitle'), 
        'summary': Locale.LocalString('GoldSummary'),
        'thumb': "icon-gold.png" },
    "126": {
        'url': MTV, 
        'title': Locale.LocalString('MTVTitle'), 
        'subtitle': Locale.LocalString('MTVSubtitle'), 
        'summary': Locale.LocalString('MTVSummary'),
        'thumb': "icon-mtv.png" },
    "243": {
        'url': SKY_ARTS_ONE, 
        'title': Locale.LocalString('SkyArts1Title'), 
        'subtitle': Locale.LocalString('SkyArts1Subtitle'), 
        'summary': Locale.LocalString('SkyArts1Summary'),
        'thumb': "icon-skyarts1.png" },
    "301": {
        'url': SKY_PREMIERE, 
        'title': Locale.LocalString('SkyPremiereTitle'), 
        'subtitle': Locale.LocalString('SkyPremiereSubtitle'), 
        'summary': Locale.LocalString('SkyPremiereSummary'),
        'thumb': "icon-skypremiere.png" },
    "303": {
        'url': SKY_SHOWCASE, 
        'title': Locale.LocalString('SkyMoviesShowcaseTitle'), 
        'subtitle': Locale.LocalString('SkyMoviesShowcaseSubtitle'), 
        'summary': Locale.LocalString('SkyMoviesShowcaseSummary'),
        'thumb': "icon-skymoviesshowcase.png" },
    "305": {
        'url': SKY_ACTION, 
        'title': Locale.LocalString('SkyMoviesActionAdventureTitle'), 
        'subtitle': Locale.LocalString('SkyMoviesActionAdventureSubtitle'), 
        'summary': Locale.LocalString('SkyMoviesActionAdventureSummary'),
        'thumb': "icon-skymoviesactionadventure.png" },
    "306": {
        'url': SKY_FAMILY, 
        'title': Locale.LocalString('SkyMoviesFamilyTitle'), 
        'subtitle': Locale.LocalString('SkyMoviesFamilySubtitle'), 
        'summary': Locale.LocalString('SkyMoviesFamilySummary'),
        'thumb': "icon-skymoviesfamily.png" },
    "401": {
        'url': SKY_SPORTS_ONE, 
        'title': Locale.LocalString('SkySports1Title'), 
        'subtitle': Locale.LocalString('SkySports1Subtitle'), 
        'summary': Locale.LocalString('SkySports1Summary'),
        'thumb': "icon-skysports1.png" },
    "402": {
        'url': SKY_SPORTS_TWO, 
        'title': Locale.LocalString('SkySports2Title'), 
        'subtitle': Locale.LocalString('SkySports2Subtitle'), 
        'summary': Locale.LocalString('SkySports2Summary'),
        'thumb': "icon-skysports2.gif" },
    "403": {
        'url': SKY_SPORTS_THREE, 
        'title': Locale.LocalString('SkySports3Title'), 
        'subtitle': Locale.LocalString('SkySports3Subtitle'), 
        'summary': Locale.LocalString('SkySports3Summary'),
        'thumb': "icon-skysports3.gif" },
    "404": {
        'url': SKY_SPORTS_FOUR, 
        'title': Locale.LocalString('SkySports4Title'), 
        'subtitle': Locale.LocalString('SkySports4Subtitle'), 
        'summary': Locale.LocalString('SkySports4Summary'),
        'thumb': "icon-skysports4.gif" },
    "405": {
        'url': SKY_SPORTS_NEWS, 
        'title': Locale.LocalString('SkySportsNewsTitle'), 
        'subtitle': Locale.LocalString('SkySportsNewsSubtitle'), 
        'summary': Locale.LocalString('SkySportsNewsSummary'),
        'thumb': "icon-skysportsnews.png" },
    "405": {
        'url': EURO_SPORT, 
        'title': Locale.LocalString('EurosportTitle'), 
        'subtitle': Locale.LocalString('EurosportSubtitle'), 
        'summary': Locale.LocalString('EurosportSummary'),
        'thumb': "icon-eurosport.png" },
    "501": {
        'url': SKY_NEWS, 
        'title': Locale.LocalString('SkyNewsTitle'), 
        'subtitle': Locale.LocalString('SkyNewsSubtitle'), 
        'summary': Locale.LocalString('SkyNewsSummary'),
        'thumb': "icon-skynews.png" },
    "526": {
        'url': NAT_GEO, 
        'title': Locale.LocalString('NatGeoTitle'), 
        'subtitle': Locale.LocalString('NatGeoSubtitle'), 
        'summary': Locale.LocalString('NatGeoSummary'),
        'thumb': "icon-natgeo.png" },
    "528": {
        'url': NAT_GEO_WILD, 
        'title': Locale.LocalString('NatGeoWildTitle'), 
        'subtitle': Locale.LocalString('NatGeoWildSubtitle'), 
        'summary': Locale.LocalString('NatGeoWildSummary'),
        'thumb': "icon-natgeowild.png" },
    "601": {
        'url': CARTOON_NETWORK, 
        'title': Locale.LocalString('CartoonNetworkTitle'), 
        'subtitle': Locale.LocalString('CartoonNetworkSubtitle'), 
        'summary': Locale.LocalString('CartoonNetworkSummary'),
        'thumb': "icon-cartoonnetwork.png" },
    "603": {
        'url': BOOMERANG, 
        'title': Locale.LocalString('BoomerangTitle'), 
        'subtitle': Locale.LocalString('BoomerangSubtitle'), 
        'summary': Locale.LocalString('BoomerangSummary'),
        'thumb': "icon-boomerang.png" },
    "604": {
        'url': NICKELODEON, 
        'title': Locale.LocalString('NickelodeonTitle'), 
        'subtitle': Locale.LocalString('NickelodeonSubtitle'), 
        'summary': Locale.LocalString('NickelodeonSummary'),
        'thumb': "icon-nickelodeon.png" },
    "607": {
        'url': DISNEY_XD, 
        'title': Locale.LocalString('DisneyXDTitle'), 
        'subtitle': Locale.LocalString('DisneyXDSubtitle'), 
        'summary': Locale.LocalString('DisneyXDSummary'),
        'thumb': "icon-disneyxd.png" },
    "609": {
        'url': DISNEY_CHANNEL, 
        'title': Locale.LocalString('DisneyChannelTitle'), 
        'subtitle': Locale.LocalString('DisneyChannelSubtitle'), 
        'summary': Locale.LocalString('DisneyChannelSummary'),
        'thumb': "icon-disneychannel.png" },
    "615": {
        'url': NICKELODEON_JR, 
        'title': Locale.LocalString('NickelodeonJrTitle'), 
        'subtitle': Locale.LocalString('NickelodeonJrSubtitle'), 
        'summary': Locale.LocalString('NickelodeonJrSummary'),
        'thumb': "icon-nickjr.png" }}

group_names = [ 
    str(Locale.LocalString('Entertainment')), 
    str(Locale.LocalString('Lifestyle')), 
    str(Locale.LocalString('Movies')), 
    str(Locale.LocalString('Sports')), 
    str(Locale.LocalString('News')), 
    str(Locale.LocalString('Documentaries')), 
    str(Locale.LocalString('Kids'))]

groups = {
    str(Locale.LocalString('Entertainment')): [ "106", "107", "108", "110", "126" ],
    str(Locale.LocalString('Lifestyle')): [ "243" ],
    str(Locale.LocalString('Movies')): [ "301", "303", "305", "306" ],
    str(Locale.LocalString('Sports')): [ "401", "402", "403", "404", "405" ],
    str(Locale.LocalString('News')): [ "501" ],
    str(Locale.LocalString('Documentaries')): [ "526", "528" ],
    str(Locale.LocalString('Kids')): [ "601", "603", "604", "607", "609", "615" ]}

####################################################################################################

# This function is initially called by the PMS framework to initialize the plugin. This includes
# setting up the Plugin static instance along with the displayed artwork.
def Start():

    # Initialize the plugin
    Plugin.AddPrefixHandler(VIDEO_PREFIX, MainMenu, Locale.LocalString('Title'), ICON, ART)
    Plugin.AddViewGroup("Basic", viewMode = "InfoList", mediaType = "items")
    Plugin.AddViewGroup("Basic", viewMode = "List", mediaType = "items")

    # Setup the artwork associated with the plugin
    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    DirectoryItem.thumb = R(ICON)

# This main function will setup the displayed items. This will depend if the user is currently 
# logged in.
def MainMenu():
    dir = MediaContainer(disabledViewModes=["Coverflow"], title1 = Locale.LocalString('Title'))
    
    # List all the different group names
    for group_name in group_names:
    
        dir.Append(Function(
            DirectoryItem(
                GroupMenu,
                group_name),
                group_name = group_name))
    
    # Preferences
    dir.Append(PrefsItem(L('Preferences'), thumb=R('icon-prefs.png')))
    
    return dir

# This function will display a specific group.
def GroupMenu(sender, group_name = ''):
    dir = MediaContainer(disabledViewModes=["Coverflow"], title1 = group_name)

    # Create a new item for every channel
    for channel_number in groups[group_name]:
        
        channel = channels[channel_number]
        
        dir.Append(WebVideoItem(
            GenerateFullUrl(channel['url']),
            title = channel['title'],
            subtitle = channel['subtitle'],
            summary = channel['summary'],
            infoLabel = channel_number,
            thumb = R(channel['thumb'])))
    
    return dir

def GenerateFullUrl(channelUrl):
    if Prefs['quality'] == "Auto":
        return (PLAYER_URL % channelUrl) + "&quality=4"
    elif Prefs['quality'] == "High":
        return (PLAYER_URL % channelUrl) + "&quality=3"
    elif Prefs['quality'] == "Medium":
        return (PLAYER_URL % channelUrl) + "&quality=2"
    else:
        return (PLAYER_URL % channelUrl) + "&quality=1"