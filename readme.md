# ForestFox

## WARNING: 

This protocol is a work in process (WIP) and **will** change as needed. Please do NOT use this for any real projects at this time until a final release is submitted. A final release will be marked with .01 (or higher) at the end of the version number. The version number is represented using the date the version was finalized; at the time of writing this document we are on version 2023.09.10.00 (September 10th of 2023 version 00 (00 = Pre-Release)). *Also note that this readme file is not complete (there are more widgets to add) and will be updated as items are added or changed.* 

## Built with

- Python 3.11.3
- PyQt6

## Overview

The ForestFox project is meant to be a renderer for M3L (Multi-Media Mark-up Language) and GSS (Global Style Sheets) as a means to create a common UI look and feel across multiple applications. It does this by creating the structure of the UI inside M3L and then applying the skin via the GSS file. This is also used inside UndChain which is a decentralized cloud based blockchain that uses this as it's UI layer. While ForestFox is **NOT** meant to be the only renderer for M3L and GSS it is the first. Currently we use Python as the language of choice to implement this application along with QT6 as the backbone for the UI, however you can just as easily take another UI framework and implement this (you could even go as far as to use a game engine). This protocol (M3L and GSS) while maintained via myself it is meant to be an open standard that will evolve through time. Below are a list of keywords for M3L and I will also add examples of what that syntax will look like; both M3L and GSS are coded in a TOML like format.

## Modes

Inside of M3L / GSS you will have different mode types that can be activated either on user request or an input type (think going from M&K to Game Controller to tablet). Each of these modes can change the UI type that is shown on screen. The following modes are:

- **Application mode** -> This mode is a windowed mode and can be best thought of a standard desktop application, that has a title bar, minimize / maximize and menu bars

- **Dashboard mode** -> In this mode you will be in full screen (in the UI engine) that has a static window meaning you cannot scroll the window view vertically or horizontally (although a widget can still have a scroll). This mode would be best used for making overviews of data sets and is what will be switched to when you use a Game Controller. This mode isn't meant to have widgets that have higher order inputs, such as text inputs. It should be designed in such a way that a person with a gam controller can easily navigate around.

- **Web mode** -> This mode was designed to give you a similar look and feel as a normal website. It has vertical scroll only. *There is an option to place elements as STATIC so that they do not move when the user scrolls to a different section*

- **Desktop mode** -> This mode is designed for widescreen desktops and offers horizontal scroll and like Web mode you can place items as static so that they do not leave the screen as the user scrolls away *you can also parallax this so that when the user scrolls the leaves the view at a different rate as the main content*

## Widgets

Each widget will have a source key which indicates where the data is located that contains what that widget is supposed to do / display. This is done so that you can have dynamic content displayed. Widgets can also have event states that trigger when an action is applied?

- **Video** -> This element is meant to place a video widget on screen. There are multiple video modes to choose from (mini, normal, wide_screen and full_screen). What if we could set the background to be the current video that's playing? 

- **Goal Bar** -> This element is meant for creating a goal like structure; so things like monetary goals or interaction goals. So long as you can quantify the progress you can use this widget and when the goal is hit there will be an event played (as defined by the GSS). Goal bars use the progress bar widget and there are some items that you can connect by default inside UndChain such as donation interactions. Goals may go up or down as identified by the M3L.

- **Map** -> This element is meant to place a map widget on screen. Map widget are not only useful for showing maps, but could also be used as a system to graphically show points of interest on a image (2D). 

- **Timeline** -> This element creates a time line where you can add events that will show as a horizontal bar chart on screen. Time lines will have markers to indicate length and may have images within them per the GSS file. There is also options to add multiple lines down.

- **Graph** -> This element is used to represent a graph widget on screen. Graphs that are currently included are line, chart, pie and fill. Probably add node graphs to this list so you can show relationships between objects.

- **Table** -> This is meant to create a table of any size on the screen (if the columns and rows are too large than scroll bars will appear). This will use letters for columns and numbers for rows. This should make viewing databases easier as well as source data inside M3L files.

- **Text Editor** -> This element is used to represent a Text Editor environment (not to be confused with Text area). This widget has the option of showing line numbers on the side and can also show the column number below.

- **Canvas** -> This is a element that allows a user to create any graphics or drawings on screen and allows the user to scroll on both directions. Use this for things like sketches and markups. You can also add grid lines that allow shapes to snap in place.

- **GSS Emulator** -> This is meant to allow users to view a new GSS file within a different environment. This is mainly created so that when you create new pages you can view them with different GSS files to see if there are any conflicts with what you are submitting. *Hopefully it's not abused and used as a work-around for making pages that all have a different feel as that is the opposite of what is being done.*

- **Markdown** -> This element creates a view that can display markdown files. 

- **Cards** -> This element is for creating a card UI element. Cards may consist of a title, sub-title, image, button and a accent color (please note that the accent color can be ignored by a GSS file). Cards can also have 'backs'?

- **Poster** -> This element is just like a card except it's larger on screen. It has the exact same attributes. The advantage to using a poster is that you have more area to write text and the image can be slightly larger.

- **Notification** -> This element creates a temporary pop up and is meant to flash timely information on screen. There are three main types of toast: 
	1. Information 
	2. Warning 
	3. Error

- **Gallery** -> This element is to be used when you have a large set of images that you want to be shown. Images can be accompanied with descriptions with title and sub-title attributes

- **Title_bar** -> Is used in application mode so that you can customize what you would like the application bar to have. Some of those items include, search, settings, menu options (like File, Edit etc.). 

- **Top_Bar** -> This is meant to give an extended tool set to the user. Think something like the ribbon menu you see in applications such as office. A top bar can have a tools and sub-tools (listed as text, icons or both) just be aware that if the view area that the application is running on isn't wide enough some tools can be cut off. 

- **Tabs** -> Tabs is meant to create tabs in a document so that you can quickly switch between page views within your application. Inside tabs you can have a title or you can have a editable text bar and close.

- **Vertical_Tabs** -> This is just like tabs, but instead of having the tabs side by side, they are stacked in a column. *Need a better name for this one*

- **Chat** -> This widget creates a chat like environment. You can select if it's group chat or point to point. This has the option of allowing items such as GIFs as well as custom emotes depending on the provider.

- **Wiki** ->

- **Tiles** -> This widget is meant to take a collection of cards or posters and group them in the event you want to make a simple selection screen. This can be attached with a filter widget.

- **Poll** -> This widget allows users to vote on a particular item. Inside UndChain you can have the option of classifying which type of user can participate within the poll in order to decrease false feedback. These polls are also have an expiration; when the polls close only the results are shown.

## Sub-Widgets

These widgets are sub-components to widgets while they can operate on their own are normally apart of another widget.

- **Reaction** -> This sub-widget provides the ability to react to other widgets; for example reacting to a chat bubble.

- **Comment** -> 

- **Rating** -> This sub-widget is used as a means of identifying the type of content being viewed in regards to audience type. The content creator as well as the consumer of the content are able to post.

- **Color Picker** ->

# Multi-device control

The goal here is to make a UI that can span multiple-devices seamlessly with the same look and feel. Not sure how this is going to be implemented just yet, but it should feel just like having another screen attached on the machine you are currently using. Possibly like a supped up controller of sorts, that is tuned for the device that its being projected on. Also, as a means of taking your work environment with you (although if your on a smaller display like a phone this may limit your abilities)