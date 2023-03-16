// Search:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

// Add:
#ifdef ENABLE_SHOW_NIGHT_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_SHOW_NIGHT_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_SHOW_NIGHT_SYSTEM", 0);
#endif