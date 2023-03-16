// Search:
PyObject * systemIsShowSalesText(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonSystem::Instance().IsShowSalesText());
}

// Add:
#ifdef ENABLE_SHOW_NIGHT_SYSTEM
PyObject * systemGetNightMode(PyObject * poSelf, PyObject * poArgs){return Py_BuildValue("i", CPythonSystem::Instance().GetNightMode());}
PyObject * systemSetNightMode(PyObject * poSelf, PyObject * poArgs){int iFlag;if (!PyTuple_GetInteger(poArgs, 0, &iFlag))return Py_BuildException();CPythonSystem::Instance().SetNightMode(iFlag);return Py_BuildNone();}
#endif

// Search:
		{ "GetShadowLevel",				systemGetShadowLevel,			METH_VARARGS },
		{ "SetShadowLevel",				systemSetShadowLevel,			METH_VARARGS },

// Add:
#ifdef ENABLE_SHOW_NIGHT_SYSTEM
		{ "GetNightMode",				systemGetNightMode,				METH_VARARGS },
		{ "SetNightMode",				systemSetNightMode,				METH_VARARGS },
#endif