<h3>Overview</h3>
The way that I see this working is:

A main "server" runs on a device on the network.
Other "devices" contact this server for authentication and whatnot.

I have several different ideas about the Main server... 
After my research, I think that the quickest/easiest way will be to run Pyro to do the network communications.

It will allow us to run different python remote objects on each device. 

<h3>Main Server</h3>
The main server needs to start up and establish itself as a name server. 
Then it needs to intitialize and start the openfour "listener" module. 
The "listener" module will then respond to commands. 
That way the devices will be able to easily and programmatically communicate with the main server.

<h3>Devices</h3>
Devices will need to start a "listening" function as well that will listen for commands from the main server and respond to them. 

The devices will communicate with the main server and be able to respond to commands from that server. 

<h4>notes</h4>
The Pyro event server and the Pyro name server need to be running.