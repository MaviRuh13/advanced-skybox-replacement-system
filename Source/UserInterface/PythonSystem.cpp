// Search:
void CPythonSystem::SetShowSalesTextFlag(int iFlag)
{
	m_Config.bShowSalesText = iFlag == 1 ? true : false;
}

// Add:
#ifdef ENABLE_SHOW_NIGHT_SYSTEM
int CPythonSystem::GetNightMode(){return m_Config.bNightMode;}
void CPythonSystem::SetNightMode(unsigned int level){m_Config.bNightMode = MIN(level, 9);}
#endif

// Search:
		else if (!stricmp(command, "SHOW_SALESTEXT"))
			m_Config.bShowSalesText = atoi(value) == 1 ? true : false;

// Add:
#ifdef ENABLE_SHOW_NIGHT_SYSTEM
		else if (!stricmp(command, "NIGHT_MODE"))
			m_Config.bNightMode = atoi(value);
#endif

// Search:
	fprintf(fp, "SHADOW_LEVEL				%d\n", m_Config.iShadowLevel);

// Add:
#ifdef ENABLE_SHOW_NIGHT_SYSTEM
	fprintf(fp, "NIGHT_MODE					%d\n", m_Config.bNightMode);
#endif
