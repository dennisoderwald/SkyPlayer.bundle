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

####################################################################################################

channels = { 
    "106": { 
        'url': SKY_ONE, 
        'title': L('Sky1Title'), 
        'subtitle': L('Sky1Subtitle'), 
        'summary': L('Sky1Summary'),
        'thumb': "icon-sky1.png" },
    "107": {
        'url': SKY_LIVING, 
        'title': L('SkyLivingTitle'), 
        'subtitle': L('SkyLivingSubtitle'), 
        'summary': L('SkyLivingSummary'),
        'thumb': "icon-skyliving.png" },
    "108": {
        'url': SKY_ATLANTIC, 
        'title': L('SkyAtlanticTitle'), 
        'subtitle': L('SkyAtlanticSubtitle'), 
        'summary': L('SkyAtlanticSummary'),
        'thumb': "icon-skyatlantic.png" },
    "110": {
        'url': GOLD, 
        'title': L('GoldTitle'), 
        'subtitle': L('GoldSubtitle'), 
        'summary': L('GoldSummary'),
        'thumb': "icon-gold.png" },
    "126": {
        'url': MTV, 
        'title': L('MTVTitle'), 
        'subtitle': L('MTVSubtitle'), 
        'summary': L('MTVSummary'),
        'thumb': "icon-mtv.png" },
    "243": {
        'url': SKY_ARTS_ONE, 
        'title': L('SkyArts1Title'), 
        'subtitle': L('SkyArts1Subtitle'), 
        'summary': L('SkyArts1Summary'),
        'thumb': "icon-skyarts1.png" },
    "301": {
        'url': SKY_PREMIERE, 
        'title': L('SkyPremiereTitle'), 
        'subtitle': L('SkyPremiereSubtitle'), 
        'summary': L('SkyPremiereSummary'),
        'thumb': "icon-skypremiere.png" },
    "303": {
        'url': SKY_SHOWCASE, 
        'title': L('SkyMoviesShowcaseTitle'), 
        'subtitle': L('SkyMoviesShowcaseSubtitle'), 
        'summary': L('SkyMoviesShowcaseSummary'),
        'thumb': "icon-skymoviesshowcase.png" },
    "305": {
        'url': SKY_ACTION, 
        'title': L('SkyMoviesActionAdventureTitle'), 
        'subtitle': L('SkyMoviesActionAdventureSubtitle'), 
        'summary': L('SkyMoviesActionAdventureSummary'),
        'thumb': "icon-skymoviesactionadventure.png" },
    "306": {
        'url': SKY_FAMILY, 
        'title': L('SkyMoviesFamilyTitle'), 
        'subtitle': L('SkyMoviesFamilySubtitle'), 
        'summary': L('SkyMoviesFamilySummary'),
        'thumb': "icon-skymoviesfamily.png" },
    "401": {
        'url': SKY_SPORTS_ONE, 
        'title': L('SkySports1Title'), 
        'subtitle': L('SkySports1Subtitle'), 
        'summary': L('SkySports1Summary'),
        'thumb': "icon-skysports1.png" },
    "402": {
        'url': SKY_SPORTS_TWO, 
        'title': L('SkySports2Title'), 
        'subtitle': L('SkySports2Subtitle'), 
        'summary': L('SkySports2Summary'),
        'thumb': "icon-skysports2.png" },
    "403": {
        'url': SKY_SPORTS_THREE, 
        'title': L('SkySports3Title'), 
        'subtitle': L('SkySports3Subtitle'), 
        'summary': L('SkySports3Summary'),
        'thumb': "icon-skysports3.png" },
    "404": {
        'url': SKY_SPORTS_FOUR, 
        'title': L('SkySports4Title'), 
        'subtitle': L('SkySports4Subtitle'), 
        'summary': L('SkySports4Summary'),
        'thumb': "icon-skysports4.png" },
    "405": {
        'url': SKY_SPORTS_NEWS, 
        'title': L('SkySportsNewsTitle'), 
        'subtitle': L('SkySportsNewsSubtitle'), 
        'summary': L('SkySportsNewsSummary'),
        'thumb': "icon-skysportsnews.png" },
    "405": {
        'url': EURO_SPORT, 
        'title': L('EurosportTitle'), 
        'subtitle': L('EurosportSubtitle'), 
        'summary': L('EurosportSummary'),
        'thumb': "icon-eurosport.png" },
    "501": {
        'url': SKY_NEWS, 
        'title': L('SkyNewsTitle'), 
        'subtitle': L('SkyNewsSubtitle'), 
        'summary': L('SkyNewsSummary'),
        'thumb': "icon-skynews.png" },
    "526": {
        'url': NAT_GEO, 
        'title': L('NatGeoTitle'), 
        'subtitle': L('NatGeoSubtitle'), 
        'summary': L('NatGeoSummary'),
        'thumb': "icon-natgeo.png" },
    "528": {
        'url': NAT_GEO_WILD, 
        'title': L('NatGeoWildTitle'), 
        'subtitle': L('NatGeoWildSubtitle'), 
        'summary': L('NatGeoWildSummary'),
        'thumb': "icon-natgeowild.png" },
    "601": {
        'url': CARTOON_NETWORK, 
        'title': L('CartoonNetworkTitle'), 
        'subtitle': L('CartoonNetworkSubtitle'), 
        'summary': L('CartoonNetworkSummary'),
        'thumb': "icon-cartoonnetwork.png" },
    "603": {
        'url': BOOMERANG, 
        'title': L('BoomerangTitle'), 
        'subtitle': L('BoomerangSubtitle'), 
        'summary': L('BoomerangSummary'),
        'thumb': "icon-boomerang.png" },
    "604": {
        'url': NICKELODEON, 
        'title': L('NickelodeonTitle'), 
        'subtitle': L('NickelodeonSubtitle'), 
        'summary': L('NickelodeonSummary'),
        'thumb': "icon-nickelodeon.png" },
    "607": {
        'url': DISNEY_XD, 
        'title': L('DisneyXDTitle'), 
        'subtitle': L('DisneyXDSubtitle'), 
        'summary': L('DisneyXDSummary'),
        'thumb': "icon-disneyxd.png" },
    "609": {
        'url': DISNEY_CHANNEL, 
        'title': L('DisneyChannelTitle'), 
        'subtitle': L('DisneyChannelSubtitle'), 
        'summary': L('DisneyChannelSummary'),
        'thumb': "icon-disneychannel.png" },
    "615": {
        'url': NICKELODEON_JR, 
        'title': L('NickelodeonJrTitle'), 
        'subtitle': L('NickelodeonJrSubtitle'), 
        'summary': L('NickelodeonJrSummary'),
        'thumb': "icon-nickjr.png" }}

group_names = [ 
    str(L('Entertainment')), 
    str(L('Lifestyle')), 
    str(L('Movies')), 
    str(L('Sports')), 
    str(L('News')), 
    str(L('Documentaries')), 
    str(L('Kids'))]

groups = {
    str(L('Entertainment')): [ "106", "107", "108", "110", "126" ],
    str(L('Lifestyle')): [ "243" ],
    str(L('Movies')): [ "301", "303", "305", "306" ],
    str(L('Sports')): [ "401", "402", "403", "404", "405" ],
    str(L('News')): [ "501" ],
    str(L('Documentaries')): [ "526", "528" ],
    str(L('Kids')): [ "601", "603", "604", "607", "609", "615" ]}

####################################################################################################

# This function is initially called by the PMS framework to initialize the plugin. This includes
# setting up the Plugin static instance along with the displayed artwork.
def Start():

    # Initialize the plugin
    Plugin.AddPrefixHandler(VIDEO_PREFIX, MainMenu, NAME, ICON, ART)
    Plugin.AddViewGroup("List", viewMode = "List", mediaType = "items")
    Plugin.AddViewGroup("InfoList", viewMode = "InfoList", mediaType = "items")

    # Setup the artwork associated with the plugin
    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "InfoList"
    DirectoryItem.thumb = R(ICON)

# This main function will setup the displayed items. This will depend if the user is currently 
# logged in.
def MainMenu():
    dir = MediaContainer(viewMode="List")
    
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
    dir = MediaContainer(title2 = group_name)

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