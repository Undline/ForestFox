# ForestFox

## WARNING: 

This protocol is a work in process (WIP) and **will** change as needed. Please do NOT use this for any real projects at this time until a final release is submitted. A final release will be marked with .01 (or higher) at the end of the version number. The version number is represented using the date the version was finalized; at the time of writing this document we are on version 2023.09.10.00 (September 10th of 2023 version 00 (00 = Pre-Release)). *Also note that this readme file is not complete (there are more widgets to add) and will be updated as items are added or changed.* 

## Built with

- Python 3.11.3
- PyQT6

## Overview

The ForestFox project is meant to be a renderer for M3L (Multi-Media Mark-up Language) and GSS (Gloabal Style Sheets) as a means to create a common UI look and feel accross multiple applications. It does this by creating the structure of the UI inside M3L and then applying the skin via the GSS file. This is also used inside UndChain which is a decentalized cloud based blockchain that uses this as it's UI layer. While ForestFox is **NOT** meant to be the only renderer for M3L and GSS it is the first. Currently we use Python as the language of choice to implement this application along with QT6 as the backbone for the UI, however you can just as easily take another UI framework and implement this (you could even go as far as to use a game engine). This protocol (M3L and GSS) while maintained via myself it is meant to be an open standard that will evolve through time. Below are a list of keywords for M3L and I will also add examples of what that syntax will look like; both M3L and GSS are coded in a TOML like format.

## Modes

Inside of M3L / GSS you will have different mode types that can be activated either on user request or an input type (think going from M&K to Game Controller to tablet). Each of these modes can change the UI type that is shown on screen. The following modes are:

- **Application mode** -> This mode is a windowed mode and can be best thought of a standard desktop application, that has a title bar, minimize / maximize and menu bars

- **Dashbord mode** -> In this mode you will be in full screen (in the UI engine) that has a static window meaning you cannot scroll the window view virtically or horizontally (although a widget can still have a scroll). This mode would be best used for making overviews of data sets and is what will be switched to when you use a Game Controller. This mode isn't meant to have widgets that have higher order inputs, such as text inputs. It should be designed in such a way that a person with a gam controller can easily vavigate around.

- **Web mode** -> This mode was designed to give you a simlar look and feel as a normal website. It has vertical scroll only. *There is an option to place elements as STATIC so that they do not move when the user scrolls to a different section*

- **Desktop mode** -> This mode is designed for widescreen desktops and offers horizontal scroll and like Web mode you can place items as static so that they do not leave the screen as the user scrolls away *you can also paralax this so that when the user scrolls the leaves the view at a different rate as the main contenet*

## Widgets

- **Video** -> This element is meant to place a video widget on screen. There are multiple video modes to choose from (mini, normal, wide_screen and full_screen). 

- **Map** -> This element is meant to place a map widget on screen. Map widget are not only useful for showing maps, but could also be used as a system to graphically show points of intrest on a image (2D). 

- **Graph** -> This element is used to represet a graph widget on screen. Graphs that are currently included are line, chart, pie and fill.

- **Text Editor** -> This element is used to represent a Text Editor enviroment (not to be confused with Text area). This widget has the option of showing line numbers on the side and can also show the column nunber below.

- **Canvas** -> This is a element that allows a user to create any graphics or drawings on screen and allows the user to scroll on both directions. Use this for things like sketches and markups.