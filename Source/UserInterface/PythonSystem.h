// Search:
			bool			bShowSalesText;

// Add:
#ifdef ENABLE_SHOW_NIGHT_SYSTEM
			int				bNightMode;
#endif

// Search:
		void							SetShowSalesTextFlag(int iFlag);

// Add:
#ifdef ENABLE_SHOW_NIGHT_SYSTEM
		void							SetNightMode(unsigned int level);
		int								GetNightMode();
#endif