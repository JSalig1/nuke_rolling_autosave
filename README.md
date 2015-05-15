## Nuke Rolling Auto Save

Make your copy of Nuke keep the latest 15 autosaves similar to After Effects.
Download the script and save it in your local Nuke scripts folder.

In your init.py file add:

    import nukescripts.rollingAutoSave15

#### Saving Auto Saves Locally

Some facilities prefer not to have project files and auto saves on a SAN.  You
can change your auto save preference to keep your auto save files locally away
from the main project file.

Within Nuke go to Edit > Preferences... Under General find the default autosave
comp file name:


Replace this text with the following:

    [getenv NUKE_TEMP_DIR]/[file tail [value root.name]].autosave

This will point your autosaves to the default NUKE_TEMP_DIRECTORY on your local
station.

#### Specifying a Custom Local Auto Save Directory (Windows7)

You can specify you own custom NUKE_TEMP_DIRECTORY location by changing your
local machines environment variable. On Windows 7 go to Control Panel and select
System. Click on Advanced System Settings and select the Advanced tab. Click on
Enviromnet Variables. Create a new user variable named NUKE_TEMP_DIR and fill in
the value:

    %USERPROFILE%\Custom\File\Path

As an example:

    %USERPROFILE%\My Documents\Nuke Temp Files

Now Nuke will autosave all project files locally keeping the latest 15 copies of
each project with timestamp information in the file name. All autosave files
open nativly in Nuke.

Happy (Safer) Compositing!
