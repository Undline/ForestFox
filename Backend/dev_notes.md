
The goal of dev logs is to keep notes throughout the development process. I may never look at them again, but it helps my process mentally.

# Backend

This file is meant to document backend development. This should include all of the business logic needed to make ForestFox run. Things such as inter-application communication and the current state of the UI.

## 2023.09.16

Downloaded a new spell check software because I am horrible at spelling. I am going to implement the inter-communication link which will act like a server using local host (127.0.0.1) in order to pass in commands from applications. There should be a program access list at some point so that not any un-authorized application can interrupt the UI while it's being used by another program, however at this time I am just going to return true so that any attempt to make a connection will be accepted. -Undline

## 2023.09.17

Earlier I was thinking that it made a lot of sense to take each widget type and assign it a 'slot' size and then from there define a structure for how pages are made, but I think this was a mistake. It should be up to the creator of the GSS file to make those decisions otherwise they wont own the UX just the UI. I believe at this point what I will do with this engine specifically is make a QGridLayout and have the GSS define it's partitioning. I also don't think I did a great job of explaining video or any other high level widgets. There should be a system that identifies other widgets that are connected to it; such as video suggestions. Maybe I should make a different widget type altogether and make video a sub-widget??? -Undline 