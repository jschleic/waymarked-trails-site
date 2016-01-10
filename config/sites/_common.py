# This file is part of the Waymarked Trails Map Project
# Copyright (C) 2015 Sarah Hoffmann
#
# This is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import os.path as op
basedir =  op.normpath(op.join(op.realpath(__file__), '../../..'))

TILE_CACHE = {
    'type' : "PostgresCache",
    'empty_tile' : { 'png' : op.join(basedir, 'maps/symbols/misc/empty.png') },
    'dba' : 'dbname=tiles'
}

RENDERER = {
    'tile_size' : (256, 256),
    'max_zoom' : 18
}

TILE_STYLE = {
    'db_name' : 'planet'
}

#############################################################################
#
# Local settings

try:
    import config.local as local
except ImportError:
    pass # no local settings provided

