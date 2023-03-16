# Search:
		self.RefreshShowSalesText()

# Add:
		if app.ENABLE_SHOW_NIGHT_SYSTEM:
			self.RefreshNightOption()

# Search:
		self.showsalesTextButtonList = []

# Add:
		if app.ENABLE_SHOW_NIGHT_SYSTEM:
			self.nightModeOptionButtonList = []

# Search:
			self.showsalesTextButtonList.append(GetObject("salestext_off_button"))

# Add:
			if app.ENABLE_SHOW_NIGHT_SYSTEM:
				self.nightModeOptionButtonList.append(GetObject("maviruh_skybox_0"))
				self.nightModeOptionButtonList.append(GetObject("maviruh_skybox_1"))
				self.nightModeOptionButtonList.append(GetObject("maviruh_skybox_2"))
				self.nightModeOptionButtonList.append(GetObject("maviruh_skybox_3"))
				self.nightModeOptionButtonList.append(GetObject("maviruh_skybox_4"))
				self.nightModeOptionButtonList.append(GetObject("maviruh_skybox_5"))
				self.nightModeOptionButtonList.append(GetObject("maviruh_skybox_6"))
				self.nightModeOptionButtonList.append(GetObject("maviruh_skybox_7"))
				self.nightModeOptionButtonList.append(GetObject("maviruh_skybox_8"))

# Search:
		self.showsalesTextButtonList[1].SAFE_SetEvent(self.__OnClickSalesTextOffButton)

# Add:
		if app.ENABLE_SHOW_NIGHT_SYSTEM:
			self.nightModeOptionButtonList[0].SAFE_SetEvent(self.__OnClickSykbox0Button)
			self.nightModeOptionButtonList[1].SAFE_SetEvent(self.__OnClickSykbox1Button)
			self.nightModeOptionButtonList[2].SAFE_SetEvent(self.__OnClickSykbox2Button)
			self.nightModeOptionButtonList[3].SAFE_SetEvent(self.__OnClickSykbox3Button)
			self.nightModeOptionButtonList[4].SAFE_SetEvent(self.__OnClickSykbox4Button)
			self.nightModeOptionButtonList[5].SAFE_SetEvent(self.__OnClickSykbox5Button)
			self.nightModeOptionButtonList[6].SAFE_SetEvent(self.__OnClickSykbox6Button)
			self.nightModeOptionButtonList[7].SAFE_SetEvent(self.__OnClickSykbox7Button)
			self.nightModeOptionButtonList[8].SAFE_SetEvent(self.__OnClickSykbox8Button)

# Search:
	def __OnClickSalesTextOffButton(self):
		systemSetting.SetShowSalesTextFlag(False)
		self.RefreshShowSalesText()

# Add:
	if app.ENABLE_SHOW_NIGHT_SYSTEM:
		def __OnClickSykbox0Button(self):
			systemSetting.SetNightMode(0)
			background.SetEnvironmentData(0)
			self.RefreshNightOption()
		def __OnClickSykbox1Button(self):
			systemSetting.SetNightMode(1)
			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_MAVIRUH)
			background.SetEnvironmentData(1)
			self.RefreshNightOption()
		def __OnClickSykbox2Button(self):
			systemSetting.SetNightMode(2)
			background.RegisterEnvironmentData(2, constInfo.ENVIRONMENT_MAVIRUH2)
			background.SetEnvironmentData(2)
			self.RefreshNightOption()
		def __OnClickSykbox3Button(self):
			systemSetting.SetNightMode(3)
			background.RegisterEnvironmentData(3, constInfo.ENVIRONMENT_MAVIRUH3)
			background.SetEnvironmentData(3)
			self.RefreshNightOption()
		def __OnClickSykbox4Button(self):
			systemSetting.SetNightMode(4)
			background.RegisterEnvironmentData(4, constInfo.ENVIRONMENT_MAVIRUH4)
			background.SetEnvironmentData(4)
			self.RefreshNightOption()
		def __OnClickSykbox5Button(self):
			systemSetting.SetNightMode(5)
			background.RegisterEnvironmentData(5, constInfo.ENVIRONMENT_MAVIRUH5)
			background.SetEnvironmentData(5)
			self.RefreshNightOption()
		def __OnClickSykbox6Button(self):
			systemSetting.SetNightMode(6)
			background.RegisterEnvironmentData(6, constInfo.ENVIRONMENT_MAVIRUH6)
			background.SetEnvironmentData(6)
			self.RefreshNightOption()
		def __OnClickSykbox7Button(self):
			systemSetting.SetNightMode(7)
			background.RegisterEnvironmentData(7, constInfo.ENVIRONMENT_MAVIRUH7)
			background.SetEnvironmentData(7)
			self.RefreshNightOption()
		def __OnClickSykbox8Button(self):
			systemSetting.SetNightMode(8)
			background.RegisterEnvironmentData(8, constInfo.ENVIRONMENT_MAVIRUH8)
			background.SetEnvironmentData(8)
			self.RefreshNightOption()
		def RefreshNightOption(self):
			if systemSetting.GetNightMode() == 0:
				self.nightModeOptionButtonList[0].Down()
				self.nightModeOptionButtonList[1].SetUp()
				self.nightModeOptionButtonList[2].SetUp()
				self.nightModeOptionButtonList[3].SetUp()
				self.nightModeOptionButtonList[4].SetUp()
				self.nightModeOptionButtonList[5].SetUp()
				self.nightModeOptionButtonList[6].SetUp()
				self.nightModeOptionButtonList[7].SetUp()
				self.nightModeOptionButtonList[8].SetUp()
			elif systemSetting.GetNightMode() == 1:
				self.nightModeOptionButtonList[0].SetUp()
				self.nightModeOptionButtonList[1].Down()
				self.nightModeOptionButtonList[2].SetUp()
				self.nightModeOptionButtonList[3].SetUp()
				self.nightModeOptionButtonList[4].SetUp()
				self.nightModeOptionButtonList[5].SetUp()
				self.nightModeOptionButtonList[6].SetUp()
				self.nightModeOptionButtonList[7].SetUp()
				self.nightModeOptionButtonList[8].SetUp()
			elif systemSetting.GetNightMode() == 2:
				self.nightModeOptionButtonList[0].SetUp()
				self.nightModeOptionButtonList[1].SetUp()
				self.nightModeOptionButtonList[2].Down()
				self.nightModeOptionButtonList[3].SetUp()
				self.nightModeOptionButtonList[4].SetUp()
				self.nightModeOptionButtonList[5].SetUp()
				self.nightModeOptionButtonList[6].SetUp()
				self.nightModeOptionButtonList[7].SetUp()
				self.nightModeOptionButtonList[8].SetUp()
			elif systemSetting.GetNightMode() == 3:
				self.nightModeOptionButtonList[0].SetUp()
				self.nightModeOptionButtonList[1].SetUp()
				self.nightModeOptionButtonList[2].SetUp()
				self.nightModeOptionButtonList[3].Down()
				self.nightModeOptionButtonList[4].SetUp()
				self.nightModeOptionButtonList[5].SetUp()
				self.nightModeOptionButtonList[6].SetUp()
				self.nightModeOptionButtonList[7].SetUp()
				self.nightModeOptionButtonList[8].SetUp()
			elif systemSetting.GetNightMode() == 4:
				self.nightModeOptionButtonList[0].SetUp()
				self.nightModeOptionButtonList[1].SetUp()
				self.nightModeOptionButtonList[2].SetUp()
				self.nightModeOptionButtonList[3].SetUp()
				self.nightModeOptionButtonList[4].Down()
				self.nightModeOptionButtonList[5].SetUp()
				self.nightModeOptionButtonList[6].SetUp()
				self.nightModeOptionButtonList[7].SetUp()
				self.nightModeOptionButtonList[8].SetUp()
			elif systemSetting.GetNightMode() == 5:
				self.nightModeOptionButtonList[0].SetUp()
				self.nightModeOptionButtonList[1].SetUp()
				self.nightModeOptionButtonList[2].SetUp()
				self.nightModeOptionButtonList[3].SetUp()
				self.nightModeOptionButtonList[4].SetUp()
				self.nightModeOptionButtonList[5].Down()
				self.nightModeOptionButtonList[6].SetUp()
				self.nightModeOptionButtonList[7].SetUp()
				self.nightModeOptionButtonList[8].SetUp()
			elif systemSetting.GetNightMode() == 6:
				self.nightModeOptionButtonList[0].SetUp()
				self.nightModeOptionButtonList[1].SetUp()
				self.nightModeOptionButtonList[2].SetUp()
				self.nightModeOptionButtonList[3].SetUp()
				self.nightModeOptionButtonList[4].SetUp()
				self.nightModeOptionButtonList[5].SetUp()
				self.nightModeOptionButtonList[6].Down()
				self.nightModeOptionButtonList[7].SetUp()
				self.nightModeOptionButtonList[8].SetUp()
			elif systemSetting.GetNightMode() == 7:
				self.nightModeOptionButtonList[0].SetUp()
				self.nightModeOptionButtonList[1].SetUp()
				self.nightModeOptionButtonList[2].SetUp()
				self.nightModeOptionButtonList[3].SetUp()
				self.nightModeOptionButtonList[4].SetUp()
				self.nightModeOptionButtonList[5].SetUp()
				self.nightModeOptionButtonList[6].SetUp()
				self.nightModeOptionButtonList[7].Down()
				self.nightModeOptionButtonList[8].SetUp()
			else:
				self.nightModeOptionButtonList[0].SetUp()
				self.nightModeOptionButtonList[1].SetUp()
				self.nightModeOptionButtonList[2].SetUp()
				self.nightModeOptionButtonList[3].SetUp()
				self.nightModeOptionButtonList[4].SetUp()
				self.nightModeOptionButtonList[5].SetUp()
				self.nightModeOptionButtonList[6].SetUp()
				self.nightModeOptionButtonList[7].SetUp()
				self.nightModeOptionButtonList[8].Down()
