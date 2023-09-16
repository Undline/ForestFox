
The goal of dev logs is to keep notes throughout the development process. I may never look at them again, but it helps my process mentally.

# Backend

This file is meant to document backend development. This should include all of the business logic needed to make ForestFox run. Things such as inter-application communication and the current state of the UI.

## 2023.09.06

Downloaded a new spell check software because I am horrible at spelling. I am going to implement the inter-communication link which will act like a server using local host (127.0.0.1) in order to pass in commands from applications. There should be a program access list at some point so that not any un-authorized application can interrupt the UI while it's being used by another program, however at this time I am just going to return true so that any attempt to make a connection will be accepted.  