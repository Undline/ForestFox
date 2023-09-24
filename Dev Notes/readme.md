
The goal of dev logs is to keep notes throughout the development process. I may never look at them again, but it helps my process mentally.

## 2023.09.16

I am going to implement the inter-communication link which will act like a server using local host (127.0.0.1) in order to pass in commands from applications. There should be a program access list at some point so that not any un-authorized application can interrupt the UI while it's being used by another program, however at this time I am just going to return true so that any attempt to make a connection will be accepted. -Undline

## 2023.09.17

Earlier I was thinking that it made a lot of sense to take each widget type and assign it a 'slot' size and then from there define a structure for how pages are made, but I think this was a mistake. It should be up to the creator of the GSS file to make those decisions otherwise they wont own the UX just the UI. I believe at this point what I will do with this engine specifically is make a QGridLayout and have the GSS define it's partitioning. I also don't think I did a great job of explaining video or any other high level widgets. There should be a system that identifies other widgets that are connected to it; such as video suggestions. Maybe I should make a different widget type altogether and make video a sub-widget??? What if on the code text editor we make it so that code is divided into blocks? This would help with multiple users editing the same codebase at the same time plus could make for some interesting UIs.-Undline 

## 2023.09.18

I am going to change the core UI engine to Kivy. One of the primary reasons is because after discovering that animations don't run well with normal QWidgets; it's also not possible to declare UI elements using QtQuick / QML. Kivy on the other hand can be declared and is fully open source, animations appear to work well and there is a strong community behind them. I need to do more testing before integrating Kivy, but I believe this is the best option for the project. -Undline

## 2023.09.19

Still learning Kivy; feeling pretty hopeful about implementing it here soon. I'm not going to post any updates until I have something useful to report. -Undline

## 2023.09.20

Had some ideas. First these developer notes need to move to their own folder since it seems like I am just dumping all the notes I have in this one file. Could re-name this to readme and then it would show in Github a bit nicer. Also, using the naming convention of Widget doesn't really explain what we are doing with these UI elements since they go beyond doing just one thing; for example the video element contains supplemental widgets with it, such as comments when running VOD and chat when streaming. Because of this I will need to re-structure the readme to reflect this change. -Undline