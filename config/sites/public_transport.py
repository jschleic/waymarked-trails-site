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

from config.sites._common import *

_ = lambda x: x

RENDERER['source_type'] = "xml"
RENDERER['source'] = op.join(basedir, "maps/styles/hikingmap.xml")

TILE_STYLE['db_schema'] = 'public_transport'

TILE_CACHE['table'] = 'public_transport'

SITE = {
  'title' :  _('Hiking'),
  'tile_url' : local.TILE_BASE_URL + '/hiking',
  'description' :  _("Waymarked Trails shows hiking routes from the local to international level, with maps and information from OpenStreetMap."),
   'help' : {
     'source' : op.join(basedir, 'django/locale/%s/helppages.yaml'),
     'structure' : (("about", "hiking", "osm"),
                  ("rendering", "hikingroutes", "classification", "hikinglabels",
                   "hierarchy", "guideposts",
                     (("hierarchies", "text"),
                     ("osmc", "text"),
                     ("hikinglocal", "text", 
                        "czech", "germany", "hungary", "slovakia", "swiss", "italy", "uk"),
                     ("elevationprofiles", "general"),
                  )),
                  ("technical", "general", "translation"),
                  ("legal", "copyright", "usage", "disclaimer"),
                  ("acknowledgements", "text"),
                  ("contact", "text")
                 )
     }
   }

SITE.update(SITE_PUBLIC_TRANSPORT)
