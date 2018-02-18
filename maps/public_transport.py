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
""" Configuration for the Public transport routes map.
"""

from db.configs import *
from os.path import join as os_join
from config.defaults import MEDIA_ROOT

MAPTYPE = 'routes'

# routes with at least one of the public transport names
ROUTEDB = RouteDBConfig()
ROUTEDB.schema = 'public_transport'
ROUTEDB.relation_subset = """
    tags->'type' IN ('route', 'route_master')
    AND (ARRAY['train', 'subway', 'monorail', 'tram', 'bus', 'trolleybus', 'aerialway', 'ferry']
     && ((regexp_split_to_array(tags->'route', ';')) || (regexp_split_to_array(tags->'route_master', ';')))
    	)"""

ROUTES = RouteTableConfig()
ROUTES.public_transport_map = { 'train': 0,
								'subway': 10,
								'monorail': 10,
								'tram': 20,
								'bus': 30 ,
								'trolleybus': 30,
								'aerialway': 40,
								'ferry': 50}
ROUTES.symbols = ( 'TextColorBelow',
                   'TextSymbol',
                   'ColorBox')

DEFSTYLE = RouteStyleTableConfig()

GUIDEPOSTS = GuidePostConfig()
GUIDEPOSTS.subtype = 'bicycle'
GUIDEPOSTS.require_subtype = True

NETWORKNODES = NetworkNodeConfig()
NETWORKNODES.node_tag = 'rcn_ref'

SYMBOLS = ShieldConfiguration()
SYMBOLS.symbol_outdir = os_join(MEDIA_ROOT, 'symbols/public_transport')
SYMBOLS.swiss_mobil_bgcolor = (0.66, 0.93, 1.0)
SYMBOLS.swiss_mobil_networks = ('rcn', 'ncn')
