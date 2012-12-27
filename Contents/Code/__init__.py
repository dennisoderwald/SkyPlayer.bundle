from datetime import datetime as dt

####################################################################################################

NAME = L('Title')

ART = 'art-default.jpg'
ICON = 'icon-default.png'
ICON_SEARCH = 'icon-search.png'

BASE_URL = 'http://go.sky.com'
PLAYER_URL = 'http://go.sky.com/vod/page/detachedLiveTv.do?epgChannelId=%s'
CHANNEL_LOGO_URL = 'http://epgstatic.sky.com/epgdata/1.0/newchanlogos/200/200/skychb%s.png'
EPG_URL = 'http://www.sky.com/tvlistings-proxy/TVListingsProxy/tvlistings.json?detail=2&dur=1440&time=%(time)s&channels=%(channels)s'
ON_DEMAND_URL = 'http://go.sky.com/vod/content/%s/Browse_by_Genre/%s/content/default/promoPage.do'
SEARCH_URL = 'http://go.sky.com/vod/content/Home/Application_Navigation/Search_All/content/default/search.do?searchTerm=%s&searchTypeFilter=titleNameSearch'

# Entertainment
SKY_ONE = "1402"
SKY_LIVING = "2201"
SKY_ATLANTIC = "1412"
GOLD = "2304"
SKY_LIVING_IT = "2207"
MTV = "2501"

# Lifestyle
SKY_ARTS_ONE = "1752"

# Movies
SKY_PREMIERE = "1409"
SKY_SHOWCASE = "1814"
SKY_COMEDY = "1002"
SKY_ACTION = "1001"
SKY_FAMILY = "1808"
SKY_CRIME = "1818"
SKY_DRAMA = "1816"
SKY_SCIFI = "1807"
SKY_MODERN = "1815"
SKY_CLASSICS = "1812"
SKY_INDIE = "1811"

# Sports
SKY_SPORTS_ONE = "1301"
SKY_SPORTS_TWO = "1302"
SKY_SPORTS_THREE = "1333"
SKY_SPORTS_FOUR = "1322"
SKY_SPORTS_NEWS = "1314"
SKY_SPORTS_F1 = "1306"
EURO_SPORT = "1726"
EURO_SPORT_TWO = "1841"
ESPN = "3141"
ESPN_CLASSIC = "3221"

# Children
CARTOON_NETWORK = "5601"
BOOMERANG = "5609"
NICKELODEON = "1846"
NICKELODEON_JR = "1857"
DISNEY_XD = "1843"
DISNEY_CHANNEL = "1881"
DISNEY_JR = "1884"
CARTOON_NITO = "1371"

# Documentaries
NAT_GEO = "1806"
NAT_GEO_WILD = "1847"
HISTORY = "1875"
EDEN = "2302"
CRIME_AND_INVESTIGATION = "1448"

# News
SKY_NEWS = "1404"

####################################################################################################

channels = { 
    "106": { 
        'url': SKY_ONE, 
        'title': L('Sky1Title'), 
        'subtitle': L('Sky1Subtitle'), 
        'summary': L('Sky1Summary')},
    "107": {
        'url': SKY_LIVING, 
        'title': L('SkyLivingTitle'), 
        'subtitle': L('SkyLivingSubtitle'), 
        'summary': L('SkyLivingSummary')},
    "108": {
        'url': SKY_ATLANTIC, 
        'title': L('SkyAtlanticTitle'), 
        'subtitle': L('SkyAtlanticSubtitle'), 
        'summary': L('SkyAtlanticSummary')},
    "110": {
        'url': GOLD, 
        'title': L('GoldTitle'), 
        'subtitle': L('GoldSubtitle'), 
        'summary': L('GoldSummary')},
    "122": {
        'url': SKY_LIVING_IT, 
        'title': L('SkyLivingitTitle'), 
        'subtitle': L('SkyLivingitSubtitle'), 
        'summary': L('SkyLivingitSummary')},
    "126": {
        'url': MTV, 
        'title': L('MTVTitle'), 
        'subtitle': L('MTVSubtitle'), 
        'summary': L('MTVSummary')},
    "243": {
        'url': SKY_ARTS_ONE, 
        'title': L('SkyArts1Title'), 
        'subtitle': L('SkyArts1Subtitle'), 
        'summary': L('SkyArts1Summary')},
    "301": {
        'url': SKY_PREMIERE, 
        'title': L('SkyPremiereTitle'), 
        'subtitle': L('SkyPremiereSubtitle'), 
        'summary': L('SkyPremiereSummary')},
    "303": {
        'url': SKY_SHOWCASE, 
        'title': L('SkyMoviesShowcaseTitle'), 
        'subtitle': L('SkyMoviesShowcaseSubtitle'), 
        'summary': L('SkyMoviesShowcaseSummary')},
    "304": {
        'url': SKY_COMEDY, 
        'title': "Sky Movies Comedy", 
        'subtitle': "Watch Sky Movies Comedy online", 
        'summary': ""},
    "305": {
        'url': SKY_ACTION, 
        'title': L('SkyMoviesActionAdventureTitle'), 
        'subtitle': L('SkyMoviesActionAdventureSubtitle'), 
        'summary': L('SkyMoviesActionAdventureSummary')},
    "306": {
        'url': SKY_FAMILY, 
        'title': L('SkyMoviesFamilyTitle'), 
        'subtitle': L('SkyMoviesFamilySubtitle'), 
        'summary': L('SkyMoviesFamilySummary')},
    "307": {
        'url': SKY_CRIME, 
        'title': "Sky Movies Crime & Thriller", 
        'subtitle': "Watch Sky Movies Crime & Thriller online", 
        'summary': ""},
    "308": {
        'url': SKY_DRAMA, 
        'title': "Sky Movies Drama & Romance", 
        'subtitle': "Watch Sky Movies Drama & Romance online", 
        'summary': ""},
    "309": {
        'url': SKY_SCIFI, 
        'title': "Sky Movies Scifi & Horror", 
        'subtitle': "Watch Sky Movies Scifi & Horror online", 
        'summary': ""},
    "310": {
        'url': SKY_MODERN, 
        'title': "Sky Movies Modern Greats", 
        'subtitle': "Watch Sky Movies Modern Greats online", 
        'summary': ""},
    "311": {
        'url': SKY_CLASSICS, 
        'title': "Sky Movies Classics", 
        'subtitle': "Watch Sky Movies Classics online", 
        'summary': ""},
    "312": {
        'url': SKY_INDIE, 
        'title': "Sky Movies Indie", 
        'subtitle': "Watch Sky Movies Indie online", 
        'summary': ""},
    "401": {
        'url': SKY_SPORTS_ONE, 
        'title': L('SkySports1Title'), 
        'subtitle': L('SkySports1Subtitle'), 
        'summary': L('SkySports1Summary')},
    "402": {
        'url': SKY_SPORTS_TWO, 
        'title': L('SkySports2Title'), 
        'subtitle': L('SkySports2Subtitle'), 
        'summary': L('SkySports2Summary')},
    "403": {
        'url': SKY_SPORTS_THREE, 
        'title': L('SkySports3Title'), 
        'subtitle': L('SkySports3Subtitle'), 
        'summary': L('SkySports3Summary')},
    "404": {
        'url': SKY_SPORTS_FOUR, 
        'title': L('SkySports4Title'), 
        'subtitle': L('SkySports4Subtitle'), 
        'summary': L('SkySports4Summary')},
    "405": {
        'url': SKY_SPORTS_NEWS, 
        'title': L('SkySportsNewsTitle'), 
        'subtitle': L('SkySportsNewsSubtitle'), 
        'summary': L('SkySportsNewsSummary')},
    "408": {
        'url': SKY_SPORTS_F1, 
        'title': L('SkySportsF1Title'), 
        'subtitle': L('SkySportsF1Subtitle'), 
        'summary': L('SkySportsF1Summary')},
    "410": {
        'url': EURO_SPORT, 
        'title': L('EurosportTitle'), 
        'subtitle': L('EurosportSubtitle'), 
        'summary': L('EurosportSummary')},
    "411": {
        'url': EURO_SPORT_TWO, 
        'title': L('Eurosport2Title'), 
        'subtitle': L('Eurosport2Subtitle'), 
        'summary': L('Eurosport2Summary')},
    "417": {
        'url': ESPN,
        'title': L('ESPNTitle'), 
        'subtitle': L('ESPNSubtitle'), 
        'summary': L('ESPNSummary')},
    "442": {
        'url': ESPN_CLASSIC,
        'title': L('ESPNClassicTitle'), 
        'subtitle': L('ESPNClassicSubtitle'), 
        'summary': L('ESPNClassicSummary')},
    "501": {
        'url': SKY_NEWS, 
        'title': L('SkyNewsTitle'), 
        'subtitle': L('SkyNewsSubtitle'), 
        'summary': L('SkyNewsSummary')},
    "526": {
        'url': NAT_GEO, 
        'title': L('NatGeoTitle'), 
        'subtitle': L('NatGeoSubtitle'), 
        'summary': L('NatGeoSummary')},
    "528": {
        'url': NAT_GEO_WILD, 
        'title': L('NatGeoWildTitle'), 
        'subtitle': L('NatGeoWildSubtitle'), 
        'summary': L('NatGeoWildSummary')},
    "529": {
        'url': HISTORY, 
        'title': L('HistoryTitle'), 
        'subtitle': L('HistorySubtitle'), 
        'summary': L('HistorySummary')},
    "532": {
        'url': EDEN, 
        'title': L('EdenTitle'), 
        'subtitle': L('EdenSubtitle'), 
        'summary': L('EdenSummary')},
    "553": {
        'url': CRIME_AND_INVESTIGATION, 
        'title': L('CrimeInvestigationTitle'), 
        'subtitle': L('CrimeInvestigationSubtitle'), 
        'summary': L('CrimeInvestigationSummary')},
    "601": {
        'url': CARTOON_NETWORK, 
        'title': L('CartoonNetworkTitle'), 
        'subtitle': L('CartoonNetworkSubtitle'), 
        'summary': L('CartoonNetworkSummary')},
    "603": {
        'url': BOOMERANG, 
        'title': L('BoomerangTitle'), 
        'subtitle': L('BoomerangSubtitle'), 
        'summary': L('BoomerangSummary')},
    "604": {
        'url': NICKELODEON, 
        'title': L('NickelodeonTitle'), 
        'subtitle': L('NickelodeonSubtitle'), 
        'summary': L('NickelodeonSummary')},
    "607": {
        'url': DISNEY_XD, 
        'title': L('DisneyXDTitle'), 
        'subtitle': L('DisneyXDSubtitle'), 
        'summary': L('DisneyXDSummary')},
    "609": {
        'url': DISNEY_CHANNEL, 
        'title': L('DisneyChannelTitle'), 
        'subtitle': L('DisneyChannelSubtitle'), 
        'summary': L('DisneyChannelSummary')},
    "611": {
        'url': DISNEY_JR, 
        'title': "Disney Junior", 
        'subtitle': "Watch Disney Junior online", 
        'summary': ""},
    "615": {
        'url': NICKELODEON_JR, 
        'title': L('NickelodeonJrTitle'), 
        'subtitle': L('NickelodeonJrSubtitle'), 
        'summary': L('NickelodeonJrSummary')},
    "619": {
        'url': CARTOON_NITO, 
        'title': "Cartoonito", 
        'subtitle': "Watch Cartoonito online", 
        'summary': ""}}

group_names = [ 
    str(L('Entertainment')), 
    str(L('Movies')), 
    str(L('Sports')), 
    str(L('News')), 
    str(L('Documentaries')), 
    str(L('Kids'))]

groups = {
    str(L('Entertainment')): [ "106", "107", "108", "110", "122", "126" ],
    str(L('Lifestyle')): [ "243" ],
    str(L('Movies')): [ "301", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312" ],
    str(L('Sports')): [ "401", "402", "403", "404", "405", "408", "410", "411", "417", "442" ],
    str(L('News')): [ "501" ],
    str(L('Documentaries')): [ "526", "528", "529", "532", "553" ],
    str(L('Kids')): [ "601", "603", "604", "607", "609", "611", "615", "619" ]}

on_demand_channels = {
    str(L('Entertainment')): {
        'name': "SKYENTERTAINMENT",
        'categories': [ "Drama", "Action", "Sci Fi", "Comedy", "Arts", "Reality", "Game Shows" ]},
    str(L('Movies')): {
        'name': "SKYMOVIES",
        'categories': [ "Box Sets", "Action", "Family", "Comedy", "Crime and Thriller", "Indie", "Drama", "Modern Greats", "Horror", "Sci-Fi", "Classics"]},
    str(L('Sports')): {
        'name': "SKYSPORTS",
        'categories': [ "Football", "Soccer AM", "Formula 1", "Shows", "Cricket", "Rugby Union", "Rugby League", "Boxing", "Golf", "Tennis", "Darts", "Features"]},
    str(L('News')): {
        'name': "SKYNEWS",
        'categories': [ "News Specials", "News Features", "Showbiz"]},
    str(L('Documentaries')): {
        'name': "SKYDOCUMENTARIES",
        'categories': [ "Crime", "Engineering", "History", "Society and Civilisation"]},
    str(L('Kids')): {
        'name': "SKYKIDS",
        'categories': [ "Activities", "Adventure", "Animation", "Drama", "Entertainment and Comedy", "Factual", "Music", "Pre-School", "Teen"]}
}

####################################################################################################

# This function is initially called by the PMS framework to initialize the plugin. This includes
# setting up the Plugin static instance along with the displayed artwork.
def Start():

    # Initialize the plugin
    Plugin.AddViewGroup("List", viewMode = "List", mediaType = "items")
    Plugin.AddViewGroup("InfoList", viewMode = "InfoList", mediaType = "items")

    # Setup the artwork associated with the plugin
    ObjectContainer.art = R(ART)
    ObjectContainer.title1 = NAME
    ObjectContainer.view_group = "InfoList"

    DirectoryObject.art = R(ART)
    DirectoryObject.thumb = R(ICON)
    VideoClipObject.art = R(ART)
    VideoClipObject.thumb = R(ICON)

    HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'

# This main function will setup the displayed items. This will depend if the user is currently 
# logged in.
@handler('/video/skygo', NAME, art = ART, thumb = ICON)
def MainMenu():
    oc = ObjectContainer(view_group = "List")

    oc.add(DirectoryObject(key = Callback(LiveMenu, title = "Channels"), title = "Channels"))
    oc.add(DirectoryObject(key = Callback(OnDemandMainMenu, title = "Anytime+"), title = "Anytime+"))
    oc.add(SearchDirectoryObject(identifier="com.plexapp.plugins.skyplayer", title = L('Search'), prompt = L('SearchPrompt'), thumb = R(ICON_SEARCH)))
    
    # Preferences
    oc.add(PrefsObject(title = L('Preferences')))
    
    return oc

####################################################################################################

# This function will display the available live channels
@route('/video/skygo/live')
def LiveMenu(title):
    oc = ObjectContainer(title2 = title)

    # List all the different group names
    for group in group_names:
    
        oc.add(DirectoryObject(
            key = Callback(GroupMenu, group = group),
            title = group))

    return oc

# This function will display a specific group.
@route('/video/skygo/live/{group}')
def GroupMenu(group):
    oc = ObjectContainer(title2 = group)

    # Create a new item for every channel
    for channel_number in groups[group]:
        
        channel = channels[channel_number]
        
        # Attempt to determine the title and description of the show playing now and next. If
        # nothing is returned, then we should just assume failure and simply use the channel's
        # own information.
        now_and_next = NowAndNext(channel['url'])
        description = channel['summary']
        if now_and_next != "":
            description = "%s\n\nNow: %s\n%s\n\nNext: %s\n%s"
            description = description % (
                channel['summary'], 
                now_and_next['Now']['Title'], 
                now_and_next['Now']['Description'], 
                now_and_next['Next']['Title'], 
                now_and_next['Next']['Description'])

        oc.add(VideoClipObject(
            url = GenerateFullUrl(channel['url']),
            title = channel['title'],
            summary = description,
            thumb = CHANNEL_LOGO_URL % channel['url']))
    
    return oc

# This function will return details of what is currently playing, and what is next, for the given 
# channel. This information includes the name of the show, along with a brief description.
def NowAndNext(channel_url):
    epg = JSON.ObjectFromURL(EPG_URL % dict(time = dt.now().strftime('%Y%m%d%H%M'), channels = channel_url))

    # Check to see if we've received anything.
    if epg == "":
        return ""
    
    # Check to see if we have been given any channel.
    if epg.has_key('channels') == False:
        return ""
    
    channel_collection = epg['channels']

    # Check to see if we have been given any programs.
    if channel_collection.has_key('program') == False:
        return ""

    programs = channel_collection['program']

    # Ensure that we have at least two programs in order to display now and next.
    if len(programs) < 2:
        return ""

    # Determine the details of the titles which are "Now and Next"
    now_title = programs[0]['title']
    now_desc = ""
    if programs[0].has_key('shortDesc'):
        now_desc = programs[0]['shortDesc']

    next_title = programs[1]['title']
    next_desc = ""
    if programs[1].has_key('shortDesc'):
        next_desc = programs[1]['shortDesc']
    
    return { "Now" : { "Title": now_title, "Description": now_desc }, "Next" : { "Title": next_title, "Description": next_desc } }

# This function will generate a suitable URL for the required channel, using the appropriate quality
# setting currently selected by the user in their preferences.
def GenerateFullUrl(channelUrl):
    if Prefs['quality'] == "Auto":
        return (PLAYER_URL % channelUrl) + "&quality=4"
    elif Prefs['quality'] == "High":
        return (PLAYER_URL % channelUrl) + "&quality=3"
    elif Prefs['quality'] == "Medium":
        return (PLAYER_URL % channelUrl) + "&quality=2"
    else:
        return (PLAYER_URL % channelUrl) + "&quality=1"

####################################################################################################

# This function displays the first OnDemand menu. It contains a list of all the available channels.
@route('/video/skygo/ondemand')
def OnDemandMainMenu(title):
    oc = ObjectContainer(title2 = title)

    # List all the different group names
    for group in group_names:
        oc.add(DirectoryObject(
            key = Callback(OnDemandChannelMenu, group = group),
            title = group))
    
    return oc

# This function displays the available genres which can be played on demand.
@route('/video/skygo/ondemand/{group}')
def OnDemandChannelMenu(group):
    oc = ObjectContainer(title2 = group)

    channel_details = on_demand_channels[group]
    for category in channel_details['categories']:
        oc.add(DirectoryObject(
            key = Callback(OnDemandCategoryMenu, channel = group, category = category),
            title = category))

    return oc

# This function displays the titles available for the selected genre. If the found URL contains
# a reference to a series identifier, it will present the option to select an individual episode.
@route('/video/skygo/ondemand/{channel}/{category}')
def OnDemandCategoryMenu(channel, category):
    oc = ObjectContainer(title2 = category)

    on_demand_channels[channel]['name']
    for title_detail in TitleDetails(ON_DEMAND_URL % (on_demand_channels[channel]['name'], category.replace(' ', '_'))):
        
        url = title_detail['url']
        
        # We should only display content which actually comes from the skygo website. It's 
        # possible that some titles might actually be linked to the BBC
        if url.startswith("http://go.sky.com/vod") == False or "BBC" in title_detail['subtitle']:
            continue
        
        # If the associated URL is pointing to a series, then we need to transition into a sub-menu
        if url.find('/seriesId/') != -1:
            oc.add(DirectoryObject(
                key = Callback(OnDemandSeriesMenu, title = title_detail['title'], series_url = url),
                title = title_detail['title'],
                summary = title_detail['summary'],
                thumb = title_detail['image']))
        else:
            oc.add(VideoClipObject(
                url = url,
                title = title_detail['title'],
                summary = title_detail['summary'],
                thumb = title_detail['image']))

    return oc
             
# This function displays the known episode for the selected series.
def OnDemandSeriesMenu(title, series_url): 
    oc = ObjectContainer(title2 = title)
    
    for title_detail in TitleDetails(series_url):
        
        url = title_detail['url']
        
        # We should only display content which actually comes from the go website. It's 
        # possible that some titles might actually be linked to the BBC
        if url.startswith("http://go.sky.com/vod") == False:
            continue

        oc.add(VideoClipObject(
            url = url,
            title = title_detail['title'],
            summary = title_detail['summary'],
            thumb = title_detail['image']))
    
    # If there are no titles, we should warn the user.
    if len(oc) == 0:
        return MessageContainer(sender.itemTitle, L('ErrorNoTitles'))
    
    return oc

def TitleDetails(url):
    page = HTML.ElementFromURL(url)

    titles = []

    # Slots
    # These elements are normally located at the top of the page and contain the featured titles
    # available for the current category. 
    slots = page.xpath("//li[contains(concat(' ',normalize-space(@class),' '),' smallSlot ')]")
    for slot in slots:
        title = slot.xpath(".//h3/span/text()")[0]
        description = slot.xpath(".//div[@class='slotDetails']/div[@class='synopsis']/p/text()")[0]

        image = ""
        image_style = slot.xpath(".//div[@class='slotBkg']")[0].get('style')
        image_style_split = image_style.split("'")
        if len(image_style_split) == 3:
            image = image_style_split[1]
 
        # If the specified URL is relative, then translate it
        if image.startswith("http") == False:
            image = BASE_URL + String.Quote(image)
        
        # If the specified URL is relative, then translate it
        url = slot.xpath(".//a[contains(concat(' ',normalize-space(@class),' '),' slideButton ')]")[0].get('href')
        if url.startswith("http") == False:
            url = BASE_URL + url
    
        titles.append({
            'title': title, 
            'summary': description,
            'subtitle': "",
            'label': "Feature",
            'image': image,
            'url': url})

    # Promo Items
    # These are used most commonly when displayed list of series and episodes.
    items = page.xpath("//div[contains(concat(' ',normalize-space(@class),' '),' promoItem ')]")
    for item in items:
    
        try:
            title = item.xpath(".//h3")[0].get('title').strip()
        except:
            try:
                title = item.xpath(".//h3/a")[0].get('title').strip()
            except:
                title = item.xpath(".//h3//text()")[0].strip()

        # If the specified URL is relative, then translate it
        image = item.xpath(".//img")[0].get('src')
        if image.startswith("http") == False:
            image = BASE_URL + String.Quote(image)
        
        # If the specified URL is relative, then translate it
        url = item.xpath(".//a")[0].get('href')
        if url.startswith("http") == False:
            url = BASE_URL + url
        
        channel = ""
        try:
            channel = item.xpath(".//span[@class='broadcastChannel']/text()")[0]
        except:
            pass

        titles.append({
            'title': title, 
            'summary': "",
            'subtitle': channel,
            'label': "",
            'image': image,
            'url': url})

    return titles