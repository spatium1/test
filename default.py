# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: SkymashiTV
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.kod1music'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI" 	#Popular Music Videos 
YOUTUBE_CHANNEL_ID_2 = "PLFgquLnL59alGXsEORxmchqRzVSR7VEQ2" 	#360° Videos 
YOUTUBE_CHANNEL_ID_3 = "PLFgquLnL59amEA53mO3KiIJRSNAzO-PRZ" 	#Top Tracks - United Kingdom 
YOUTUBE_CHANNEL_ID_4 = "PLXURZewXDI-bz70OcwxhdoEhQL4WofcNo"     #American Top 40
YOUTUBE_CHANNEL_ID_5 = "PLFgquLnL59alW3xmYiWRaoz0oM3H17Lth"     #New Music This Week 
YOUTUBE_CHANNEL_ID_6 = "PLFgquLnL59amI45Go39kM7ha2evwjOxzs"     #Country Hotlist 
YOUTUBE_CHANNEL_ID_7 = "PLFgquLnL59ak5gmnz28ZiMd59ryeTPXjT"     #Artist on the Rise 
YOUTUBE_CHANNEL_ID_8 = "PLFgquLnL59an74P4SOTWLT0wJEm5iJZmF"     #For Hip Hop Heads 
YOUTUBE_CHANNEL_ID_9 = "PLFgquLnL59am_fV6UH5rWPxcmrrhLnI_O"     #Go Slower 
YOUTUBE_CHANNEL_ID_10 = "PLFgquLnL59akYpPgfxzsw5jlPZ9R6HewT"    #Dance/EDM Hotlist 
YOUTUBE_CHANNEL_ID_11 = "PLFgquLnL59akuGGG_TKeg1t15YpSKbiEl"     #Top Tracks - India 
YOUTUBE_CHANNEL_ID_12 = "PLFgquLnL59amTdtEvjQOSlQozduow4qet"     #Alternative Hotlist 
YOUTUBE_CHANNEL_ID_13 = "PLFgquLnL59altZg1f_Kr1kGUYE6j-NE0M"     #Pop Hotlist 
YOUTUBE_CHANNEL_ID_14 = "PLFgquLnL59akXPIHrEZci0oouw4dArE0D"     #Electronic Hotlist 
YOUTUBE_CHANNEL_ID_15 = "PLFgquLnL59amVPzpNpN5bNLcZCld7JfI8"     #Indie Hotlist 
YOUTUBE_CHANNEL_ID_16 = "PLFgquLnL59anIJu29gI8F5j5jZwp9Fo7t"     #Metal Hotlist 
YOUTUBE_CHANNEL_ID_17 = "PLFgquLnL59akoLr7-OYYdTm4KWyhWqRBa"     #Rock Hotlist 
YOUTUBE_CHANNEL_ID_18 = "PLFgquLnL59annf9DmPBRYyrq7NE9I4vhX"     #Christian Music Hotlist 
YOUTUBE_CHANNEL_ID_19 = "PLFgquLnL59anST1VjqNObTmi8Hd_3MvoB"     #Pop Before it Breaks 
YOUTUBE_CHANNEL_ID_20 = "PLFgquLnL59am0KU-WTKFAw1qZrkfDI6Sb"     #Where Are They Now? 
YOUTUBE_CHANNEL_ID_21 = "PLFgquLnL59aneIaDaJkRbThYncv7oqQQK"     #Punk Rock Workout 
YOUTUBE_CHANNEL_ID_22 = "PLFgquLnL59anSrjfirkaHLyLd3QMQ5E5j"     #'90s Summer Hits 
YOUTUBE_CHANNEL_ID_23 = "PLFgquLnL59amxybxjut_5IbsOOuwB8agz"     #Top Tracks - Music Big Playlist
YOUTUBE_CHANNEL_ID_24 = "PLFgquLnL59an9fURg83fp7GEVmWqV8xPN"     #Inner Calm 
YOUTUBE_CHANNEL_ID_25 = "PLFgquLnL59amoo6nLhxDLCToL4Sh4RLcT"     #Feels Like Summertime 
YOUTUBE_CHANNEL_ID_26 = "PLFgquLnL59alA9lFJPRvJugngqT5ilxjL"     #Proud to Celebrate! 
YOUTUBE_CHANNEL_ID_27 = "PLFgquLnL59anA5zA5hzox9X8k7O-ivQbw"     #Remembering Tom Petty 
YOUTUBE_CHANNEL_ID_28 = "PLFgquLnL59alve50mIK9MuTr7LSoRvOJF"     #Live at One Love Manchester 
YOUTUBE_CHANNEL_ID_29 = "PLFgquLnL59an4RBRoO8rBtQGIPHHpX0Bv"     #Spotlight On: 2017 BET Awards 
YOUTUBE_CHANNEL_ID_30 = "PLFgquLnL59akb5WK0QyMaNxSfmZCgmqJM"     #Spotlight On: Valentine's Day Love 
YOUTUBE_CHANNEL_ID_31 = "PLFgquLnL59akvPBuQbiFVTAgHMSh63gV5"     #Spotlight On: David Bowie 
YOUTUBE_CHANNEL_ID_32 = "PLI8wLmUa7v4iUeTGD47Q2x3LeFpGxXoA1"     #Various Artists
YOUTUBE_CHANNEL_ID_33 = "UCoJiTP_P3ryjqUPPBuqyXPA"               #Kod1 Music

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Popular Music Videos ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="360° Videos ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Top Tracks - United Kingdom ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="American Top 40",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="New Music This Week ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Country Hotlist ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Artist on the Rise ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="For Hip Hop Heads ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Go Slower ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Dance/EDM Hotlist ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Top Tracks - India ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Alternative Hotlist ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Pop Hotlist ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Electronic Hotlist",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Indie Hotlist ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Metal Hotlist",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Rock Hotlist ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Christian Music Hotlist ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Pop Before it Breaks ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Where Are They Now? ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Punk Rock Workout ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="90s Summer Hits ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Top Tracks - Music Big Playlist",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Inner Calm ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Feels Like Summertime ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Proud to Celebrate! ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Remembering Tom Petty ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Live at One Love Manchester ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Spotlight On: 2017 BET Awards ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Spotlight On: Valentine's Day Love ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Spotlight On: David Bowie ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Various Artists",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Kod1 Music",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://www.dropbox.com/s/3ryv05rwx2lgctk/icon.png?dl=1",
		fanart="https://www.dropbox.com/s/r8ql21akfdx8ccv/fanart.jpg?dl=1",
        folder=True )
		
run()
