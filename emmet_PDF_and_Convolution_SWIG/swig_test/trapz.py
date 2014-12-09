# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_trapz', [dirname(__file__)])
        except ImportError:
            import _trapz
            return _trapz
        if fp is not None:
            try:
                _mod = imp.load_module('_trapz', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _trapz = swig_import_helper()
    del swig_import_helper
else:
    import _trapz
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Integrator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Integrator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Integrator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _trapz.delete_Integrator
    __del__ = lambda self : None;
    def integrate(self, *args): return _trapz.Integrator_integrate(self, *args)
Integrator_swigregister = _trapz.Integrator_swigregister
Integrator_swigregister(Integrator)

class Trapz(Integrator):
    __swig_setmethods__ = {}
    for _s in [Integrator]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trapz, name, value)
    __swig_getmethods__ = {}
    for _s in [Integrator]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Trapz, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _trapz.new_Trapz(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _trapz.delete_Trapz
    __del__ = lambda self : None;
    def integrate(self, *args): return _trapz.Trapz_integrate(self, *args)
Trapz_swigregister = _trapz.Trapz_swigregister
Trapz_swigregister(Trapz)

# This file is compatible with both classic and new-style classes.


