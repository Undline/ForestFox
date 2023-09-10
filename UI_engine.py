from typing import List

version = '2023.09.10.00'
engine = 0 #pyQT

def dashboard():
    '''This is called when the M3L file request a dashboard format. The dashboard by default 
    will go full screen and is NOT scrollable (although you can add scroll based widgets)
    The dashboard will contain a state which contains slots that house these widgets 
    inside. This creates a window'''
    pass

def page():
    '''This method is the generic form for a UndChain website. It differes from the 
    dashboard as it can scroll (only vertically). This is give creators a quick means 
    of developing pages that are hosted in the page chain, but can be used by any app.
    Like the dashbord it too has slots for widgets to reside although it differs as the
    slots can be infinite (you can have infinate scroll). Due to this you have a content
    buffer that holds slot details along with scroll position. This creates a window'''
    pass

def desktop():
    '''This is just like page except it's prurpose is for desktop and instead of vertical
    scroll this one is horizontal scroll. Just like pages you can have infinate scroll
    using the content buffer which tracks the widgets along with scroll position. 
    This creates a window'''
    pass

def loading_screen():
    '''This is a special method that should be utilized whenever you are loading content
    from a source. This fills the window and could show content behind it'''
    pass

def splash_screen():
    '''This can be ran at the begining of a application launch to provide something akin 
    to a loading screen to make the system apear to be more responsive.'''
    pass

def settings_menu():
    '''I am making this a special function since I want to have a unified way to get to 
    the settings menu'''
    pass
# I don't see a reason to create a version that allows for horizontal & vertical scroll
# as there are already widgets such as canvas that have that capability. If I am wrong
# it will be added above

# Templates

def video_template():
    '''This is a standard form template that provide the basic structure of a video / contnent
    application. The only thing that you procide in the M3L is the source to you're content.
    That source is a SQueeL database that is controled by the conent owner so that information
    could be moderated if that conent site wishes it. BASE OBJECTS: video player, sugested feed,
    chat controls, forum, reacts, cards'''
    pass

def wiki_template():
    '''Standard form for wiki. All you need is the source to the SQueeL database so that you can
    filter the information based on your paramaters. BASE OBJETCS: forum, images (galary),
    video player'''
    pass

# Widgets

def canvas_widget(slot_pos: List[int]):
    '''This is the canvas widget which is more a less a catch all for special content types
    that are not already defined. This is meant for creative applications such as drawing /
    CAD.'''
    pass

def background():
    '''This widget doesn't have a position because it's meant to stay static with the view 
    throughout the life of the current window view. Depending on the GSS file this image 
    will either be made darker or lighter *and* this may be a gif'''
    pass

def background_music():
    '''This widget doesn't have a position because it's meant to stay static with the view 
    throughout the life of the current window view. Depending on the GSS file this will 
    autoplay on screen types as identified widgets or view type (desktop / web)'''
    pass

def mini_map():
    '''This widget's position is identified by the GSS file and is used to help navigate around
    when the user is in controller mode.'''
    pass

def video(slot_pos: List[int], source: List[str]):
    '''This method creates a video player in the slot position that has been given. It's also
    sent the content sources as well and is responsible for gathering all of those stream(s)'''
    pass

def audio(slot_pos: List[int], source: List[str]):
    '''This method creates a audio player in the slot position that has been given. If that 
    slot postion is zero (or negative) then it will not show on screen. It's also sent
    the content sources as well and is responsible for gathering all of those stream(s)'''
    pass

def chat(slot_pos: List[int], source: str):
    '''This method creates a chat window in the slot position that has been given. It's also
    sent the content sources as well and is responsible for gathering all of those stream(s)'''
    pass

def loading_widget(slot_pos: List[int], widget_type: str):
    '''This is a loading widget to be a place holder for another widget'''
    pass

def label(slot_pos: List[int], source: str):
    '''This method create a text label in the identified slot *Slots can have offsets it's
    passed in as an array size 7*. The text is unicode and is passed in via source. If you
    would like to call out an address that has this text then use a source address. If you
    need to write a source address use the escape character forward slash (\)'''
    pass

def progress_bar(slot_pos: List[int], source: List[str]):
    '''This mehod creats a progress bar in the identifed slot position. Source contains the 
    min / max of the bar along with the item that is being monitored. Keep in mind that the 
    feel of the bar: the easing, color, transparency; Is all controlled by the GSS'''
    pass

def ratings(source: str):
    '''This widget is a part of certain widgets that are expected to have content verification
    needed (content that can have a rating associated with it such as video or a application 
    itself). The source is the contents location on chain and will be averaged based off of
    public rating.'''
    pass

def chat(slot_pos: List[int], source: str):
    '''This method creates a chat window that is contained in the slot position that is passed
    in. The source is the location on chain where the code that runs this content is held along
    with the database of messages.'''
    pass

def toast(source: List[str]):
    '''This method creates a toast message to show up to indicate that an event has happend (
    such as a message was receievd). This has no slot because this exists overtop of the GUI and
    is defined by the GSS file in how it is shown on screen'''
    pass

def message_box(type: int, source: List[str]):
    '''This method creates a message box on screen. There is no location identified as that is 
    determined by the GSS file (shown on top of the GUI). The message box type is sent in as an 
    ENUM. The default types are 0 = Information, 1 = Alert / Warning, 2 = Error. The source can 
    be manually defined or can come from somewhere else on chain '''
    pass

def graph(slot_pos: List[int], source: str):
    '''This method draws a graph on screen that has it's type identified in the cource file 
    along with the data set that is needed to make it. '''
    pass

def table(slot_pos: List[int], source: str):
    '''This method creates a 2D table that displays information that is contained in the source
    file. This could be from Squeel or a CSV file.'''
    pass

def left_tool_bar(source: str):
    '''This is for a left tool bar to be displayed on screen and is meant for application that 
    requires more specialized tools to work. Inside this tool bar you can contain more widgets
    if needed and has vertical scroll if needed.'''
    pass

def right_tool_bar(source: str):
    '''This is for a right tool bar to be displayed on screen and is meant for application that 
    requires more specialized tools to work. Inside this tool bar you can contain more widgets
    if needed and has vertical scroll if needed.'''
    pass

def bottom_tool_bar(source: str):
    '''This is for a bottom tool bar to be displayed on screen and is meant for application that 
    requires more specialized tools to work. Inside this tool bar you can contain more widgets
    if needed and has horizontal scroll if needed. This is really meant for things like timelines'''
    pass

def top_menu_bar(source: str):
    '''This is for a top tool bar to be displayed on screen and is meant for application that 
    requires more specialized tools to work. Inside this tool bar you can contain more widgets
    if needed and has horizontal scroll if needed. This should be used for things like tabs'''
    pass

def document(source: str):
    '''This method is for displaying documents on screen and is meant for things like license
    agreements or data sheets. This doesn't have a location because these are defined by the GSS 
    file. I would recomend that it's displayed in the center of the screen. '''
    pass

def map(source: str):
    '''This method is for displaying a map on screen and has it's location defined in the GSS file
    the source has items shuch as the legend, the map object itself along with landmarks highligters.
    The map itsent just for representing maps, but can also represent things such as blueprints.'''
    pass

def time_line(slot_pos: List[int], source: str):
    '''This method creates a time line widget which would normally go at the bottom of the screen
    but it could also go on the top. This can also be a be a sub-widget to a top or bottom 
    menu bar. Inside the source menu is what this timeline is linked to and the scaled that it's
    on. Each 'time stamp' represents an event so whatever it's connected to has to emit events'''
    pass

def vote(slot_pos: List[int], source: str):
    '''This method is somewhat similar to the radio button except it emits as soon as a selction
    is made and returns the active results as they happen.'''
    pass

def button(slot_pos: List[int], source: str):
    '''This widget can be contained in another widget or it can be it's own widget. In order
    to identify that is if the seventh item in the slot_pos is a non-zero. Each element is 
    index as they are drawn on screen (the zero widget is the window itself)'''
    pass

def card(slot_pos: List[int], source: str):
    '''This method is for placing a card UI element on screen in the specified slot position
    a card is a contained UI element that has a header title, a brief description, a small image
    and can contain a button'''
    pass

def game_area(source: str):
    '''This wont be implemented right now, but will be used to create simple games that can 
    run in the center of the screen or can take the whole screen over. It's much like the 
    canvas widget'''
    pass

def forum(slot_pos: List[int], source: str):
    '''This method is for a forum UI element that's source identifies which database to pull
    from and gives a local space for users to share contenet as well as videos'''
    pass

def ads(slot_pos: List[int], source: str):
    '''This method is for a ad UI element that's source identifies which database to pull
    am advertisement from. This is only used when AdCoin is not present, you're earning AdCoin 
    or you're in annonymous mode.'''
    pass

def taskbar():
    '''This widget is meant for the main dashboard so that you can launch applications from it
    or quickly switch from app to app'''
    pass

# These widgets are components that go inside other widgets. Some such as buttons are hybrids
# that can be used as a single object or it can be used inside another widget.

def hyperlink(location: str):
    '''This method is meant for creating a specialized button and on it's click event routes or
    executed based on the location that is passed in it. There is no location for this because it's
    a widget that is part of another widget.'''
    pass

def reactions(source: str):
    '''This method is meant for allowing users to react to content on chain which is also used to
    suggest content. This is a sub-widget that is attached to other widgets'''
    pass

def comments(source: str):
    '''This method is meant for allowing users to comment on content on chain which is also used to
    suggest content. This is a sub-widget that is attached to other widgets'''
    pass

def tags(source: str):
    '''This method is meant for allowing users to tag content on chain which is also used to
    suggest content. This is a sub-widget that is attached to other widgets'''
    pass

def drop_menu(source: str):
    '''This method gives you the ability to add fucntionality to a widget. When using M&K it's
    activated by right clicking the widget.'''
    pass

def check_box(source: str):
    '''This method creats a check box list which is identified from the source location. Inside
    the source is the call-back to where this information needs to go or do; if the goal is to
    have a event trigger once it's selected otherwise it can have a button as a trigger'''
    pass

def radio_buttons(source: str):
    '''This method creats a radio button list which is identified from the source location. Inside
    the source is the call-back to where this information needs to go or do; if the goal is to
    have a event trigger once it's selected otherwise it can have a button as a trigger'''
    pass

def navigation_bar(source: str):
    '''This method creates a navigation bar and is really meant for the page UI enviroment'''
    pass

def profile(source: str):
    '''This method creates a profile element inside of a widget. This should just be a user
    image that when clicked shows a small window below with user stats'''
    pass

# This section is the different type of UI interfaces. It's up to the M3L file to fully
# implement these interfaces, but some widget types naturally transfer over like cards

def controler():
    '''This module is meant to change the interface type in order to meet a controller type 
    interface (like a xbox or playstation controller). All the widgets should morph in this mode
    to meet this control type.'''
    pass

def mouse_amd_keyboard():
    '''This module is meant to change the interface type in order to meet a M&K control type 
    interface (mouse and keyboard). All the widgets should morph in this mode
    to meet this control type.'''
    pass

def touch():
    '''This module is meant to change the interface type in order to meet a touch screen type 
    interface (like a phone). All the widgets should morph in this mode to meet this control type.'''
    pass

def haptic_move():
    '''This module is meant to change the interface type in order to meet a non-display type 
    interface (like a watch or comething that has a small screen). All the widgets should morph 
    in this mode to meet this control type.'''
    pass