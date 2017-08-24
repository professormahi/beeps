# Beeps
### Fork from [https://github.com/ShaneMcC/beeps](https://github.com/ShaneMcC/beeps)

Here I added python code to run some beeps over linux beep command.

# Running
1. First install `beep` command on linux
2. Put `beeps` folder in `$HOME/.config/`
3. Run `./beeps.py <your lovely music you want>` you can change the name of the music to have more musics.

# Installation
1. Install `beep` command.
2. Put `beeps.py` in your PATH and create symbolic like to it named `beeps`.
3. Put `beeps` folder in `$HOME/.config/`
4. Run `beeps <your lovely music you want>` you can change the name of the music to have more musics.

# Use as an alarm
1. Install `beeps`.
2. Install `at`.
3. Create an alias named `alarm`; `alias alarm='echo "beeps alarm" | at'`.
4. Run `alarm <time>` to put your alarm.

# List of Songs
- aerodynamic  
- alarm  
- beveryhillscop
- ff-victory
- furelise
- imperialmarch
- mario
- mario-victory
- merrychristmas
- missionimpossible
- monkeyisland
- mythexe
- pacman
- phaser
- random
- ring
- sandstorm
- songoftime
- tetris

# Need to add new songs?
- Use [BeepBox](http://www.beepbox.co) to create your song!
- Export the song to `.midi` file.
- Use [mid2beep](https://github.com/Cqoicebordel/mid2beep) to convert song to `beep` command.
- Save the output to `~/.config/beeps` as a `.sh` file.
- Run `beeps <your song>`.
