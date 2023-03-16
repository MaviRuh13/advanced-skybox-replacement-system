# Search: def Open(self):
		self.currentCubeNPC = 0

# Add:
		if app.ENABLE_SHOW_NIGHT_SYSTEM:
			if systemSetting.GetNightMode() == 0:
				systemSetting.SetNightMode(0)
				background.SetEnvironmentData(0)
			elif systemSetting.GetNightMode() == 1:
				systemSetting.SetNightMode(1)
				background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_MAVIRUH)
				background.SetEnvironmentData(1)
			elif systemSetting.GetNightMode() == 2:
				systemSetting.SetNightMode(2)
				background.RegisterEnvironmentData(2, constInfo.ENVIRONMENT_MAVIRUH2)
				background.SetEnvironmentData(2)
			elif systemSetting.GetNightMode() == 3:
				systemSetting.SetNightMode(3)
				background.RegisterEnvironmentData(3, constInfo.ENVIRONMENT_MAVIRUH3)
				background.SetEnvironmentData(3)
			elif systemSetting.GetNightMode() == 4:
				systemSetting.SetNightMode(4)
				background.RegisterEnvironmentData(4, constInfo.ENVIRONMENT_MAVIRUH4)
				background.SetEnvironmentData(4)
			elif systemSetting.GetNightMode() == 5:
				systemSetting.SetNightMode(5)
				background.RegisterEnvironmentData(5, constInfo.ENVIRONMENT_MAVIRUH5)
				background.SetEnvironmentData(5)
			elif systemSetting.GetNightMode() == 6:
				systemSetting.SetNightMode(6)
				background.RegisterEnvironmentData(6, constInfo.ENVIRONMENT_MAVIRUH6)
				background.SetEnvironmentData(6)
			elif systemSetting.GetNightMode() == 7:
				systemSetting.SetNightMode(7)
				background.RegisterEnvironmentData(7, constInfo.ENVIRONMENT_MAVIRUH7)
				background.SetEnvironmentData(7)
			elif systemSetting.GetNightMode() == 8:
				systemSetting.SetNightMode(8)
				background.RegisterEnvironmentData(8, constInfo.ENVIRONMENT_MAVIRUH8)
				background.SetEnvironmentData(8)
			else:
				systemSetting.SetNightMode(0)
				background.SetEnvironmentData(0)
