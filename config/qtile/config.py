#
# ██████╗ ████████╗██╗██╗     ███████╗     ██████╗ ██████╗ ███╗   ██╗███████╗██╗ ██████╗
#██╔═══██╗╚══██╔══╝██║██║     ██╔════╝    ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║██╔════╝
#██║   ██║   ██║   ██║██║     █████╗      ██║     ██║   ██║██╔██╗ ██║█████╗  ██║██║  ███╗
#██║▄▄ ██║   ██║   ██║██║     ██╔══╝      ██║     ██║   ██║██║╚██╗██║██╔══╝  ██║██║   ██║
#╚██████╔╝   ██║   ██║███████╗███████╗    ╚██████╗╚██████╔╝██║ ╚████║██║     ██║╚██████╔╝
#╚══▀▀═╝    ╚═╝   ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝ ╚═════╝
#
# By SwordStal1ker411
#
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
import os

mod = "mod4"
terminal = "kitty"
myBrowser = "firefox"
myLauncher = "dmenu_run -p 'Run: '"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(myBrowser), desc="firefox"),
    Key([mod], "d", lazy.spawn(myLauncher), desc="Dmenu App Launcher"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

layouts = [
    layout.Columns(border_focus_stack=["#9ece6a", "#9ece6a"], border_width=3, margin=10),#fix coloring
    layout.Max(),
    layout.MonadTall(border_focus='#FFFFFF', margin=10),
]

# Names for the groups
group_names = 'WWW DEV SYS CHAT TTV ETC'.split()
# Creates the actual group names, sets the default layout
groups = [Group(name, layout='MonadTall') for name in group_names]
#Sets the keybinds to move windows to other groups and changing groups
for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
    Key([mod], indx, lazy.group[name].toscreen()),
    Key([mod, 'shift'], indx, lazy.window.togroup(name))]

#layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    #layout.MonadTall(border_focus='#FFFFFF', margin=10),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
#]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = []

screens = [
    Screen(
        top=bar.Bar(

            [


                widget.Sep(padding=6, background="1a1b26", foreground="1a1b26",),

                widget.Image(
                   filename='~/.config/qtile/icons/arch-logo.png',
                    scale="False",
                    margin=5,
                ),

                widget.GroupBox(font="Ubuntu Bold"),
                #widget.WindowName(),

                widget.Spacer(),

                widget.Systray(),

                widget.CurrentLayout(font="Ubuntu Bold", background="#cfc9c2"),

                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_checkupdates",
                    display_format="Updates: {updates}",
                    background="#cfc9c2",
                    font='Ubuntu Bold',
                ),

                widget.TextBox(text=''),
                widget.PulseVolume(background="#565f89", font='Ubuntu Bold',),

                widget.TextBox(text='Playing: ', background='#414868'),
                widget.Cmus(
                    background='#414868',
                    font='Ubuntu Bold',
                    play_color='#FFFFFF'
                ),

                widget.Clock(format="%Y-%m-%d %a %I:%M %p", background="#24283b", font='Ubuntu Bold'),
            ],
            26,
            background="#1a1b26",
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
