# Rasplex Remote

I use a Onkyo reciver and wanted to controll Rasplex with its remote.
The behaviour should be supported by Rasplex for a whole range of remotes but not for mine.
Frustrated with any documentation on how to fix this problem i decided to fix it myself.
Rasplex supplies a executable called `cec-client`, which listens to the cec input through hdmi from an outside source.
I enabled cec passtrough on my reciever and when I started the `cec-client` the commands from my remote showed in the terminal.
The scripit `autostart.sh` in `.config` pipes this output the the `remote.py` python script.

The `autostart.sh` should be placed in `/storage/.config/` such that Rasplex will start in on bootup.

The `remote.py` parses the commands from the `cec-client` and send a `jsonrpc` command to Rasplex.

More documentation about how to use `jsonrpc` for Rasplex can be found here: https://kodi.wiki/view/JSON-RPC_API/v8. (Rasplex is an altered version of Kodi)
When tweaking this software for use with your own remote, you should probably alter the `key_map` and `params_map` variables.
The are `key:value` where the key is parsed from  the `cec-client` input and the `value` the command or parameters I wanted to send to Rasplex.
