
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

## 2023.09.25

I started thinking more about how elements and widgets should work in this system. Specifically I was thinking more about how layouts should occur and I am debating on just how I am going to allow the GSS file to define them. I would like to place full control over the layouts on owner of the GSS file, but we can't tie ourselves down to one framework (especially if we ever plan to go 3D); also I'd like to have something a bit simpler for designers to use. What I am thinking is to create **sections** that allow the designer to block out a design framework that they can call on. Each section would have it's own allocated dimensions as defined by the designer. I would love to have it where a designer could make abstract shapes for their layouts, but for now we will be limited to rectangles. Maybe something like this:

```GSS
[Application.Top_Bar]
    type = "Section"
    area = {width: "parent.width", height: "200dp"}
    position: {x: "0", y: "top"}
```

Not sure if that would work well or not. *Note: The reasons why I called it Application.Top_Bar is that it indicates what view we are talking about (the application view) and it gives a unique ID to the section (since you have to have unique names for TOML tables). I like Kivy's dp measurement since it takes in account screen size and scales well, so we will use that regardless of the underlying framework we use.* I think what I should do at this point is go out and look at different UIs and try to mock them up (by hand) in M3L / GSS to make sure it can work. Should help me with defining what the language is.

Something else that pops in my head periodically is that by making this UI engine, would it limit new UI elements in the future? It makes me wonder if there should be an element that lets the M3L file define where items are placed. I worry about doing this for design continuity reasons. It would still have the same style as the GSS widgets, but would take the UX portion away from the designers. Maybe the correct solution would be to hold voting on new elements, but then you have to worry about to many elements entering the space and making the GSS files massive (they already will be) so I am not sure that is the solution either. -Undline

## 2023.09.26

What if whenever the window is resized (or change in orientation), you dynamically scale the widget / element by changing size, changing spacing or simply hide / add certain widgets from the view? Maybe we can assign priority to each element in the M3L to give the GSS a hint on what to emphasize. If there are no hints just go top down? 

Still trying to wrap my head around multi-display (not only on a device that has two monitors but also connected devices such as your phone or tablet). Having the user manually move the element / widget to another device is not very intuitive. Maybe when the user 'steps away' or leaves one device and starts using another we automatically switch? Would it be a good idea to allow the GSS creator the ability to decide if a user has another device connected (and active) to send over widgets needed to control the main element on screen to that device?

Make the language keywords and variable names case insensitive in order to discourage using the same variable name with different case and so you don't have to worry that keywords such as `true` and `True` are the same. -Undline 

## 2023.09.27

Mocking up what a video element could look like. Going to add that in with the Mock-up folder. Had a random thought and in regards to the rating system it doesn't make sense to allow a lesser rating than the one that was assigned by the creator so anytime a user assigns a rating to content it should be at or above that recommended age level. 

While I was mocking up the video element I realized a couple items that I was missing and things that could be added to make it more custom. One of which would be on pause the video could have a shade applied to it, that could be animated. -Undline