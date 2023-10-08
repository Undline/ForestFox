# ForestFox

## WARNING: 

This protocol is a work in process (WIP) and **will** change as needed. Please do NOT use this for any real projects at this time until a final release is submitted. A final release will be marked with .01 (or higher) at the end of the version number. The version number is represented using the date the version was finalized; at the time of writing this document we are on version 2023.09.10.00 (September 10th of 2023 version 00 (00 = Pre-Release)). *Also note that this readme file is not complete (there are more widgets to add) and will be updated as items are added or changed.* 

## Built with

- Python 3.11.3
- Kivy

## Overview

The ForestFox project is meant to be a renderer for M3L (Multi-Media Mark-up Language) and GSS (Global Style Sheets) as a means to create a common UI look and feel across multiple applications. It does this by creating the structure of the UI inside M3L and then applying the skin via the GSS file. This is also used inside UndChain which is a decentralized cloud based blockchain that uses this as it's UI layer. While ForestFox is **NOT** meant to be the only renderer for M3L and GSS it is the first. Currently we use Python as the language of choice to implement this application along with QT6 as the backbone for the UI, however you can just as easily take another UI framework and implement this (you could even go as far as to use a game engine). This protocol (M3L and GSS) while maintained via myself it is meant to be an open standard that will evolve through time. Below are a list of keywords for M3L and I will also add examples of what that syntax will look like; both M3L and GSS are coded in a TOML like format.

## Modes

Inside of M3L / GSS you will have different mode types that can be activated either on user request or an input type (think going from M&K to Game Controller to tablet). Each of these modes can change the UI type that is shown on screen. The following modes are:

- **Application mode** -> This mode is a windowed mode and can be best thought of a standard desktop application, that has a title bar, minimize / maximize and menu bars

- **Dashboard mode** -> In this mode you will be in full screen (in the UI engine) that has a static window meaning you cannot scroll the window view vertically or horizontally (although a widget can still have a scroll). This mode would be best used for making overviews of data sets and is what will be switched to when you use a Game Controller. This mode isn't meant to have widgets that have higher order inputs, such as text inputs. It should be designed in such a way that a person with a gam controller can easily navigate around.

- **Web mode** -> This mode was designed to give you a similar look and feel as a normal website. It has vertical scroll only. *There is an option to place elements as STATIC so that they do not move when the user scrolls to a different section*

- **Desktop mode** -> This mode is designed for widescreen desktops and offers horizontal scroll and like Web mode you can place items as static so that they do not leave the screen as the user scrolls away *you can also parallax this so that when the user scrolls the leaves the view at a different rate as the main content*

## Elements

An Element is a UI object that contains more that one Widget in order to describe what that UI element does. 

- **Video Element** -> This element main goal is meant to place a video widget on screen. Other widgets include: reactions, goal bar, voting, quiz, comments / chat (depending if the content is being streamed), pop-ups (kind of like tool tips that a creator could use to add emphasis or create an interactive link to the content), close captioning (for now it would need to manually be entered, but at a later time it's expected to be auto generated via AI), rating which helps identify who the content is targeted to and video suggestions. As always the M3L could contain a blank for some of these items (for example video suggestions), those events should be handled by the GSS file as to what the UI looks like without those elements (if it matters; by default your other elements will just take up the empty space)

- **Video Catalog** -> This element is when a user is browsing multiple videos. It's just like item selector except there isn't a checkout.

- **Map** -> This element is meant to place a map widget on screen. Map elements are not only useful for showing maps, but could also be used as a system to graphically show points of interest on a image (2D). It consists of a 2D image widget that has tool tip widgets as 'landmarks' that can contain things that may contain links. There is also a marker widget that allows users to place there own landmarks and add details which can include the reaction widget. 

- **Background Audio** -> This element is meant specifically to play audio in the background and have no controls other than the mute option in the settings menu (hit escape once on PC). This is controlled solely by the GSS file and cannot be assigned by the M3L file as this is mean to create a mood for the environment. I would recommend muting background audio (this is the default action) when another media source is playing but that is up to the GSS file and the user. 

- **Spread Sheet** -> This element is meant to create a spread sheet and contains one or more table widgets as well as a tab widget, scroll widget, graph widget, and special text area widgets that are limited in size

- **Social Media** -> This element creates a social media like element that has a messaging widget, reaction widget, rating widget and mute widget.

- **Text Editor** -> This element is used to represent a Text Editor environment. This contains a label widget for the numbering of rows, a text area widget that contains syntax highlighting, a tree widget to show file structures, a status bar widget and search widget to find text that is contained within the active project.

- **Word Processor** -> This element is a lot like a text editor except i lacks the label widget to define which row your on and adds a spell check widget as well as a text modifier widget (when you left click (press and hold) you get commonly used options) 

- **GSS Emulator** -> This is meant to allow users to view a new GSS file within a different environment. This is mainly created so that when you create new pages you can view them with different GSS files to see if there are any conflicts with what you are submitting. *Hopefully it's not abused and used as a work-around for making pages that all have a different feel as that is the opposite of what is being done.*

- **Markdown** -> This element creates a view that can display markdown files. 

- **Tiles** -> This widget is meant to take a collection of cards or posters and group them in the event you want to make a simple selection screen. This can be attached with a filter widget.

- **Notification** -> This element creates a temporary pop up and is meant to flash timely information on screen. There are three main types of toast: 
	1. Information 
	2. Warning 
	3. Error

- **Gallery** -> This element is to be used when you have a large set of images that you want to be shown. Images can be accompanied with descriptions with title and sub-title attributes.

- **Menu Bar** -> The menu bar element contains icon widgets as well as buttons, sliders, divider, drop down menus, tabs and page slides (pop ups that can take up an entire screen). There can only be one menu bar per application.

- **Tools** -> Has the same elements as a menu bar but there can be up to three (ideally one on the left, right and bottom) with the bottom one having a special widget for a status bar and the side tool bars having vertical tabs.

- **Image Editor** -> This element type will have a canvas widget, Image widget, color picker and a tree widget (for selecting layers). 

- **Video Editor** -> This element is made to create cuts and transitions in videos. It has the same widgets as the Image Editor, but also has a timeline that is meant to chop / merge video clips. *This functionality will be implemented at a later time*

- **Node Graph** -> This element creates a node graph whose purpose is meant to mocking up ideas and showing relationships between various items. This will be using the grid widget, along with the shape widget and the arrow widget. This should also have a color picker widget. *Note: We should use Obsidian's open file format for these graph nodes*

- **Hero Section** -> This UI element is really being created for the web view, but could be useful in an application environment as a way to invite the user to use the product. Hero sections should include a call to action (button widget), may have a sub-action, may contain a image or icon as well as a header widget and a sub header widget that can only contain 256 characters.

- **Card Section** -> This is another UI element that is really meant for web view. This element creates a custom section that contains three cards and has it's own background widget.

- **Shopping Grid** -> This element is a collection of cards and should be used in places where users are expected to choose an item(s). This also comes with the cart widget that can keep track of items selected (if you are able to select more than one).

- **Article** -> This element is meant to produce long form text. It has header widget for things like titles, section headers for items that note a subject as well as paragraph widgets. *I am debating on if I should make this a book element instead and add items such as chapters...*

- **Documentation** -> This is just like the article element except it adds hyperlink widgets as well as table of contents. You also have the ability to add images, video and blueprints (maps)

- **Graph** -> This element is meant to display different graph types such as line, chart, pie, scatter and candles. This should have a canvas (so you can draw these shapes), as well as checkbox widgets, header widget, legend and bubble widget (so you can see detailed information when you hover over a data point)

- **Custom** -> I think this one is going to get abused but this is a element that M3L defined. Inside the M3L you need to define not only the widgets that you need, but also window resizing events since the GSS cannot anticipate what is or is not important for this custom element. You will also need to define your own states if you are wanting to add undo / redo functionality as well as the ability to perform revision control.








## Widgets

I previously called these Sub-Widgets, but the naming convention has changed. Widgets should be items that perform a single UI task and things such as video is one of those tasks. In events where we are describing something that is a collection of Widgets those will now be called elements (see above). This should make the terminology easier to understand. 

- **Video** -> There are multiple video modes to choose from (mini, normal, wide_screen and full_screen). This widget contains the ability to pause and play the content. 

- **Audio** -> This element is meant to play audio.

- **Goal Bar** -> This element is meant for creating a goal like structure; so things like monetary goals or interaction goals. So long as you can quantify the progress you can use this widget and when the goal is hit there will be an event played (as defined by the GSS). Goal bars use the progress bar widget and there are some items that you can connect by default inside UndChain such as donation interactions. Goals may go up or down as identified by the M3L.

- **Poll** -> This widget allows users to vote on a particular item. Inside UndChain you can have the option of classifying which type of user can participate within the poll in order to decrease false feedback. These polls are also have an expiration; when the polls close only the results are shown.

- **Timeline** -> This element creates a time line where you can add events that will show as a horizontal bar chart on screen. Time lines will have markers to indicate length and may have images within them per the GSS file. There is also options to add multiple lines down.

- **Graph** -> This element is used to represent a graph widget on screen. Graphs that are currently included are line, chart, pie and fill. Probably add node graphs to this list so you can show relationships between objects.

- **Table** -> This is meant to create a table of any size on the screen (if the columns and rows are too large than scroll bars will appear). This will use letters for columns and numbers for rows. This should make viewing databases easier as well as source data inside M3L files.

- **Canvas** -> This is a element that allows a user to create any graphics or drawings on screen and allows the user to scroll on both directions. Use this for things like sketches and markups. You can also add grid lines that allow shapes to snap in place.

- **Reaction** -> This sub-widget provides the ability to react to other widgets; for example reacting to a chat bubble.

- **Title_bar** -> Is used in application mode so that you can customize what you would like the application bar to have. Some of those items include, search, settings, menu options (like File, Edit etc.). 

- **Top_Bar** -> This is meant to give an extended tool set to the user. Think something like the ribbon menu you see in applications such as office. A top bar can have a tools and sub-tools (listed as text, icons or both) just be aware that if the view area that the application is running on isn't wide enough some tools can be cut off. 

- **Tabs** -> Tabs is meant to create tabs in a document so that you can quickly switch between page views within your application. Inside tabs you can have a title or you can have a editable text bar and close.

- **Vertical_Tabs** -> This is just like tabs, but instead of having the tabs side by side, they are stacked in a column. *Need a better name for this one*

- **Chat** -> This widget creates a chat like environment. You can select if it's group chat or point to point. This has the option of allowing items such as GIFs as well as custom emotes depending on the provider.

- **Cards** -> This widget is for creating a card UI element. Cards may consist of a title, sub-title, image, button and a accent color (please note that the accent color can be ignored by a GSS file). Cards can also have 'backs'?

- **Poster** -> This widget is just like a card except it's larger on screen. It has the exact same attributes. The advantage to using a poster is that you have more area to write text and the image can be slightly larger.

- **Tags** -> This widget also acts just like a card or a widget except it's meant more for mobile / small spaces as it's small vertically.  

- **Wiki** ->

- **Ad** -> It's a *gasp* ad widget. This is really meant for UndChain so that you can get AdCoin (in the event that you're out). This should really be used in refuel pages (sites) only; since it doesn't make sense to have ads run on your page (the coin will go to the viewer not the page owner). I will add a blocking mechanism just in case.  

- **Comment** -> This widget is a lot like the messaging widget, but I decided to make it's own thing because it needs to be styled differently. This widget allows the user to react to a previous comment, post a reply or add a comment.

- **Section** -> This widget is meant more so for web, but it used to indicate a division of content. This can contain any other widgets, an is similar to the call to action banner.

- **Rating** -> This sub-widget is used as a means of identifying the type of content being viewed in regards to audience type. The content creator as well as the consumer of the content are able to post.

- **Color Picker** ->

- **Button** -> It's a button widget

- **Divider** -> This widget type is only used by GSS files in order to logically divide up the screen into easy to use areas that UI elements can be placed. It should make it easier for designers to align and structure their UI elements on screen.

- **Grid Widget** -> This widget creates a grid table of whatever size and spaces out the 'grid points' within a certain amount (set by the GSS file) by default is 10px. The goal with the grid widget is to make it easier for aligning objects (as well as other widgets) on screen since they will lock onto those grid points. 

- **Layer** -> This widget goes with any element and allows the GSS creator to layer other UI widgets on top of existing widgets (like adding a button on top of a image). Be careful, because if you layer over something that needs an interaction it could be impossible to interact with that widget.

## Launcher

Think of the launcher much like a desktop for ForestFox, if you simply open ForestFox you will be taken to the launcher. Inside the launcher you should be able to launch application(s) that you have previously given permission to use from within ForestFox, rather than relying on the user to find the application in their normal desktop environment.

## Keyboard Controls

We should be able to set our own hot keys from within any application, but there are a few that cannot be re-mapped. Pressing escape on the keyboard (pause on a controller) once, must open the settings menu. Pressing it twice on the keyboard must return you to the launcher and three times should exit the application.

## Multi-device control

The goal here is to make a UI that can span multiple-devices seamlessly with the same look and feel. Not sure how this is going to be implemented just yet, but it should feel just like having another screen attached on the machine you are currently using. Possibly like a supped up controller of sorts, that is tuned for the device that its being projected on. Also, as a means of taking your work environment with you (although if your on a smaller display like a phone this may limit your abilities). Maybe the user controls what goes to another screen or should we allow controls that say if phone send chat (in GSS); would that make any sense? **Connected devices should show in the launcher for security purposes at minimum**