# Add:
import maviruhInfo

WATER_BUTTONS_HEIGHT	= 265
XSMALL_BUTTON_WIDTH	= 20

# Search:
	"height" : 25*11+8,

# Change:
	"height" : 25*11+8+25,

# Search:
		"height" : 25*11+8,

# Change:
		"height" : 25*11+8+25,

# Search:
				{
					"name" : "salestext_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 240,

					"text" : uiScriptLocale.OPTION_SALESTEXT_VIEW_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

# Add:
				#--------------------------------------------------------------------
				{"name" : "skybox_mode","type" : "text","x" : LINE_LABEL_X,"y" : WATER_BUTTONS_HEIGHT+2,"text" : maviruhInfo.HAVA_MODU,},
				{"name" : "maviruh_skybox_0","type" : "radio_button","x" : LINE_DATA_X,"y" : WATER_BUTTONS_HEIGHT,"text" : "1","default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_skybox_1","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH,"y" : WATER_BUTTONS_HEIGHT,"text" : "2","default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_skybox_2","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*2,"y" : WATER_BUTTONS_HEIGHT,"text" : "3","default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_skybox_3","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*3,"y" : WATER_BUTTONS_HEIGHT,"text" : "4","default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_skybox_4","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*4,"y" : WATER_BUTTONS_HEIGHT,"text" : "5","default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_skybox_5","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*5,"y" : WATER_BUTTONS_HEIGHT,"text" : "6","default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_skybox_6","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*6,"y" : WATER_BUTTONS_HEIGHT,"text" : "7","default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_skybox_7","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*7,"y" : WATER_BUTTONS_HEIGHT,"text" : "8","default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
				{"name" : "maviruh_skybox_8","type" : "radio_button","x" : LINE_DATA_X+XSMALL_BUTTON_WIDTH*8,"y" : WATER_BUTTONS_HEIGHT,"text" : "9","default_image" : ROOT_PATH + "minimize_empty_button_01.sub","over_image" : ROOT_PATH + "minimize_empty_button_02.sub","down_image" : ROOT_PATH + "minimize_empty_button_03.sub",},
