#!/bin/sh

cd /home/pi/kalliope_config/

# Disable all output
/usr/local/bin/kalliope start --run-synapse "snapcast-mute-all"

# Enable bedroom output at a low level.
/usr/local/bin/kalliope start --run-synapse "snapcast-unmute-bedroom"
/usr/local/bin/kalliope start --run-order "Volume de la musique à 30 dans la chambre"

# Start musique.
/usr/local/bin/kalliope start --run-synapse "play-music-hiphop"
#../kalliope/kalliope.py start --run-order "recherche musicale ben harper"

# Sleep 2m.
sleep 2m
/usr/local/bin/kalliope start --run-order "Volume de la musique à 40 dans la chambre"

# Sleep 5m.
sleep 5m

# Pause the music
/usr/local/bin/kalliope start --run-synapse "play-toggle"

# Run morning routine.
/usr/local/bin/kalliope start --run-synapse "Morning-update-auto"

# Unpause the music
/usr/local/bin/kalliope start --run-synapse "play-toggle"

# Sleep 5m.
sleep 5m
# Raise volume one last time, it's time get up.
/usr/local/bin/kalliope start --run-order "Volume de la musique à 50 dans la chambre"
/usr/local/bin/kalliope start --run-synapse "snapcast-unmute-all"
