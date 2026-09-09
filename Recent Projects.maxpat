{
 "patcher": {
  "fileversion": 1,
  "appversion": {
   "major": 7,
   "minor": 3,
   "revision": 4,
   "architecture": "x64",
   "modernui": 1
  },
  "rect": [
   34.0,
   79.0,
   514.0,
   372.0
  ],
  "openrect": [
   0.0,
   0.0,
   0.0,
   169.0
  ],
  "bglocked": 0,
  "openinpresentation": 0,
  "default_fontsize": 10.0,
  "default_fontface": 0,
  "default_fontname": "Arial Bold",
  "gridonopen": 1,
  "gridsize": [
   8.0,
   8.0
  ],
  "gridsnaponopen": 1,
  "objectsnaponopen": 1,
  "statusbarvisible": 2,
  "toolbarvisible": 1,
  "lefttoolbarpinned": 0,
  "toptoolbarpinned": 0,
  "righttoolbarpinned": 0,
  "bottomtoolbarpinned": 0,
  "toolbars_unpinned_last_save": 0,
  "tallnewobj": 0,
  "boxanimatetime": 500,
  "enablehscroll": 1,
  "enablevscroll": 1,
  "devicewidth": 0.0,
  "description": "Lista los proyectos .als mas recientes y los abre. Requiere el watcher open_watcher.py (Documents/AbletonRecent).",
  "digest": "",
  "tags": "",
  "style": "",
  "subpatcher_template": "",
  "title": "Recent Projects",
  "boxes": [
   {
    "box": {
     "fontname": "Arial Bold",
     "fontsize": 10.0,
     "id": "obj-2",
     "maxclass": "newobj",
     "numinlets": 4,
     "numoutlets": 4,
     "outlettype": [
      "signal",
      "signal",
      "signal",
      "signal"
     ],
     "patching_rect": [
      266.0,
      120.0,
      86.0,
      20.0
     ],
     "style": "",
     "text": "plugout~ 1 2 3 4"
    }
   },
   {
    "box": {
     "fontname": "Arial Bold",
     "fontsize": 10.0,
     "id": "obj-1",
     "maxclass": "newobj",
     "numinlets": 4,
     "numoutlets": 4,
     "outlettype": [
      "signal",
      "signal",
      "signal",
      "signal"
     ],
     "patching_rect": [
      48.0,
      32.0,
      80.0,
      20.0
     ],
     "style": "",
     "text": "plugin~ 1 2 3 4"
    }
   },
   {
    "box": {
     "id": "obj-10",
     "maxclass": "comment",
     "patching_rect": [
      12.0,
      12.0,
      320.0,
      18.0
     ],
     "style": "",
     "text": "Proyectos recientes:",
     "numinlets": 1,
     "numoutlets": 0,
     "outlettype": []
    }
   },
   {
    "box": {
     "id": "obj-11",
     "maxclass": "umenu",
     "patching_rect": [
      20.0,
      40.0,
      320.0,
      22.0
     ],
     "style": "",
     "numinlets": 1,
     "numoutlets": 3,
     "outlettype": [
      "int",
      "",
      ""
     ],
     "parameter_enable": 0,
     "presentation": 1,
     "presentation_rect": [
      20.0,
      40.0,
      320.0,
      22.0
     ],
     "items": [],
     "fontname": "Arial",
     "fontsize": 11.0
    }
   },
   {
    "box": {
     "id": "obj-12",
     "maxclass": "newobj",
     "patching_rect": [
      30.0,
      130.0,
      140.0,
      20.0
     ],
     "style": "",
     "text": "js recent_loader.js",
     "numinlets": 3,
     "numoutlets": 1,
     "outlettype": [
      ""
     ]
    }
   },
   {
    "box": {
     "id": "obj-13",
     "maxclass": "button",
     "patching_rect": [
      20.0,
      90.0,
      150.0,
      24.0
     ],
     "style": "",
     "numinlets": 1,
     "numoutlets": 1,
     "outlettype": [
      "bang"
     ],
     "presentation": 1,
     "presentation_rect": [
      20.0,
      90.0,
      150.0,
      24.0
     ]
    }
   },
   {
    "box": {
     "id": "obj-14",
     "maxclass": "button",
     "patching_rect": [
      190.0,
      90.0,
      150.0,
      24.0
     ],
     "style": "",
     "numinlets": 1,
     "numoutlets": 1,
     "outlettype": [
      "bang"
     ],
     "presentation": 1,
     "presentation_rect": [
      190.0,
      90.0,
      150.0,
      24.0
     ]
    }
   },
   {
    "box": {
     "id": "obj-15",
     "maxclass": "newobj",
     "patching_rect": [
      30.0,
      160.0,
      90.0,
      20.0
     ],
     "style": "",
     "text": "loadbang",
     "numinlets": 0,
     "numoutlets": 1,
     "outlettype": [
      "bang"
     ]
    }
   },
   {
    "box": {
     "id": "obj-16",
     "maxclass": "comment",
     "patching_rect": [
      190.0,
      118.0,
      180.0,
      16.0
     ],
     "style": "",
     "text": "Abrir (cierra el set actual)",
     "numinlets": 1,
     "numoutlets": 0,
     "outlettype": []
    }
   },
   {
    "box": {
     "id": "obj-17",
     "maxclass": "comment",
     "patching_rect": [
      20.0,
      118.0,
      120.0,
      16.0
     ],
     "style": "",
     "text": "Recargar lista",
     "numinlets": 1,
     "numoutlets": 0,
     "outlettype": []
    }
   }
  ],
  "lines": [
   {
    "patchline": {
     "destination": [
      "obj-2",
      3
     ],
     "source": [
      "obj-1",
      3
     ]
    }
   },
   {
    "patchline": {
     "destination": [
      "obj-2",
      2
     ],
     "source": [
      "obj-1",
      2
     ]
    }
   },
   {
    "patchline": {
     "destination": [
      "obj-2",
      1
     ],
     "source": [
      "obj-1",
      1
     ]
    }
   },
   {
    "patchline": {
     "destination": [
      "obj-2",
      0
     ],
     "source": [
      "obj-1",
      0
     ]
    }
   },
   {
    "patchline": {
     "source": [
      "obj-13",
      0
     ],
     "destination": [
      "obj-12",
      0
     ]
    }
   },
   {
    "patchline": {
     "source": [
      "obj-15",
      0
     ],
     "destination": [
      "obj-12",
      0
     ]
    }
   },
   {
    "patchline": {
     "source": [
      "obj-11",
      0
     ],
     "destination": [
      "obj-12",
      1
     ]
    }
   },
   {
    "patchline": {
     "source": [
      "obj-14",
      0
     ],
     "destination": [
      "obj-12",
      2
     ]
    }
   },
   {
    "patchline": {
     "source": [
      "obj-12",
      0
     ],
     "destination": [
      "obj-11",
      0
     ]
    }
   }
  ],
  "dependency_cache": [],
  "latency": 0,
  "project": {
   "version": 1,
   "creationdate": 3605254137,
   "modificationdate": 3605254137,
   "viewrect": [
    0.0,
    0.0,
    300.0,
    500.0
   ],
   "autoorganize": 1,
   "hideprojectwindow": 1,
   "showdependencies": 1,
   "autolocalize": 0,
   "contents": {
    "patchers": {}
   },
   "layout": {},
   "searchpath": {},
   "detailsvisible": 0,
   "amxdtype": 1633771873,
   "readonly": 0,
   "devpathtype": 0,
   "devpath": ".",
   "sortmode": 0
  },
  "autosave": 0
 }
}