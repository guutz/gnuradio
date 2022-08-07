"""
Copyright 2008,2013 Free Software Foundation, Inc.
This file is part of GNU Radio

SPDX-License-Identifier: GPL-2.0-or-later

"""


from gi.repository import Gtk, Gdk, cairo
# import pycairo

from .. import Constants


def get_color(color_code):
    color = Gdk.RGBA()
    color.parse(color_code)
    return color.red, color.green, color.blue, color.alpha
    # chars_per_color = 2 if len(color_code) > 4 else 1
    # offsets = range(1, 3 * chars_per_color + 1, chars_per_color)
    # return tuple(int(color_code[o:o + 2], 16) / 255.0 for o in offsets)

#################################################################################
# fg colors
#################################################################################


HIGHLIGHT_COLOR = get_color('#FFFF00')
BORDER_COLOR = get_color('#AAAAAA')
BORDER_COLOR_DISABLED = get_color('#777777')
FONT_COLOR = get_color('#CCCCCC')

# Missing blocks stuff
MISSING_BLOCK_BACKGROUND_COLOR = get_color('#FFF2F2')
MISSING_BLOCK_BORDER_COLOR = get_color('#FF0000')

# Deprecated blocks
# a light warm yellow
BLOCK_DEPRECATED_BACKGROUND_COLOR = get_color('#FED86B')
# orange
BLOCK_DEPRECATED_BORDER_COLOR = get_color('#FF540B')

# Flow graph color constants
FLOWGRAPH_BACKGROUND_COLOR = get_color('#222222')
COMMENT_BACKGROUND_COLOR = get_color('#DDDDDD')
FLOWGRAPH_EDGE_COLOR = COMMENT_BACKGROUND_COLOR

# Block color constants
BLOCK_ENABLED_COLOR = get_color('#340000')
BLOCK_DISABLED_COLOR = get_color('#888888')
BLOCK_BYPASSED_COLOR = get_color('#A4AF31')

# Connection color constants
CONNECTION_ENABLED_COLOR = get_color('#FFFFFF')
CONNECTION_DISABLED_COLOR = get_color('#343434')
CONNECTION_ERROR_COLOR = get_color('#FF0000')

DEFAULT_DOMAIN_COLOR = get_color('#FFF000')


#################################################################################
# port colors
#################################################################################

PORT_TYPE_TO_COLOR = {key: get_color(
    color) for name, key, sizeof, color in Constants.CORE_TYPES}
PORT_TYPE_TO_COLOR.update((key, get_color(color))
                          for key, (_, color) in Constants.ALIAS_TYPES.items())


#################################################################################
# param box colors
#################################################################################
DARK_THEME_STYLES = b"""
                         #dtype_complex         { background-color: #3399FF; }
                         #dtype_real            { background-color: #FF8C69; }
                         #dtype_float           { background-color: #FF8C69; }
                         #dtype_int             { background-color: #00FF99; }

                         #dtype_complex_vector  { background-color: #3399AA; }
                         #dtype_real_vector     { background-color: #CC8C69; }
                         #dtype_float_vector    { background-color: #CC8C69; }
                         #dtype_int_vector      { background-color: #00CC99; }

                         #dtype_bool            { background-color: #00FF99; }
                         #dtype_hex             { background-color: #00FF99; }
                         #dtype_string          { background-color: #CC66CC; }
                         #dtype_id              { background-color: #222222; }
                         #dtype_stream_id       { background-color: #222222; }
                         #dtype_raw             { background-color: #222222; }

                         #enum_custom           { background-color: #222222; }
                     """
LIGHT_THEME_STYLES = b"""
                        #dtype_complex         { background-color: #3399FF; }
                        #dtype_real            { background-color: #FF8C69; }
                        #dtype_float           { background-color: #FF8C69; }
                        #dtype_int             { background-color: #00FF99; }
                        #dtype_complex_vector  { background-color: #3399AA; }
                        #dtype_real_vector     { background-color: #CC8C69; }
                        #dtype_float_vector    { background-color: #CC8C69; }
                        #dtype_int_vector      { background-color: #00CC99; }
                        #dtype_bool            { background-color: #00FF99; }
                        #dtype_hex             { background-color: #00FF99; }
                        #dtype_string          { background-color: #CC66CC; }
                        #dtype_id              { background-color: #333333; }
                        #dtype_stream_id       { background-color: #333333; }
                        #dtype_raw             { background-color: #333333; }
                        #enum_custom           { background-color: #333333; }
                    """
