# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_helper', [dirname(__file__)])
        except ImportError:
            import _helper
            return _helper
        if fp is not None:
            try:
                _mod = imp.load_module('_helper', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _helper = swig_import_helper()
    del swig_import_helper
else:
    import _helper
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
    if (not static) or hasattr(self,name):
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


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _helper.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _helper.SwigPyIterator_value(self)
    def incr(self, n = 1): return _helper.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _helper.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _helper.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _helper.SwigPyIterator_equal(self, *args)
    def copy(self): return _helper.SwigPyIterator_copy(self)
    def next(self): return _helper.SwigPyIterator_next(self)
    def __next__(self): return _helper.SwigPyIterator___next__(self)
    def previous(self): return _helper.SwigPyIterator_previous(self)
    def advance(self, *args): return _helper.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _helper.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _helper.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _helper.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _helper.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _helper.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _helper.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _helper.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Vector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Vector, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _helper.new_Vector(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _helper.delete_Vector
    __del__ = lambda self : None;
    def GetVal(self, *args): return _helper.Vector_GetVal(self, *args)
    def SetVal(self, *args): return _helper.Vector_SetVal(self, *args)
    def GetNumCols(self): return _helper.Vector_GetNumCols(self)
Vector_swigregister = _helper.Vector_swigregister
Vector_swigregister(Vector)

class Line(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Line, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Line, name)
    __repr__ = _swig_repr
    def iterator(self): return _helper.Line_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _helper.Line___nonzero__(self)
    def __bool__(self): return _helper.Line___bool__(self)
    def __len__(self): return _helper.Line___len__(self)
    def pop(self): return _helper.Line_pop(self)
    def __getslice__(self, *args): return _helper.Line___getslice__(self, *args)
    def __setslice__(self, *args): return _helper.Line___setslice__(self, *args)
    def __delslice__(self, *args): return _helper.Line___delslice__(self, *args)
    def __delitem__(self, *args): return _helper.Line___delitem__(self, *args)
    def __getitem__(self, *args): return _helper.Line___getitem__(self, *args)
    def __setitem__(self, *args): return _helper.Line___setitem__(self, *args)
    def append(self, *args): return _helper.Line_append(self, *args)
    def empty(self): return _helper.Line_empty(self)
    def size(self): return _helper.Line_size(self)
    def clear(self): return _helper.Line_clear(self)
    def swap(self, *args): return _helper.Line_swap(self, *args)
    def get_allocator(self): return _helper.Line_get_allocator(self)
    def begin(self): return _helper.Line_begin(self)
    def end(self): return _helper.Line_end(self)
    def rbegin(self): return _helper.Line_rbegin(self)
    def rend(self): return _helper.Line_rend(self)
    def pop_back(self): return _helper.Line_pop_back(self)
    def erase(self, *args): return _helper.Line_erase(self, *args)
    def __init__(self, *args): 
        this = _helper.new_Line(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _helper.Line_push_back(self, *args)
    def front(self): return _helper.Line_front(self)
    def back(self): return _helper.Line_back(self)
    def assign(self, *args): return _helper.Line_assign(self, *args)
    def resize(self, *args): return _helper.Line_resize(self, *args)
    def insert(self, *args): return _helper.Line_insert(self, *args)
    def reserve(self, *args): return _helper.Line_reserve(self, *args)
    def capacity(self): return _helper.Line_capacity(self)
    __swig_destroy__ = _helper.delete_Line
    __del__ = lambda self : None;
Line_swigregister = _helper.Line_swigregister
Line_swigregister(Line)


def print_py(*args):
  return _helper.print_py(*args)
print_py = _helper.print_py

def copy_py_to_vector(*args):
  return _helper.copy_py_to_vector(*args)
copy_py_to_vector = _helper.copy_py_to_vector

def copy_py_to_matrix(*args):
  return _helper.copy_py_to_matrix(*args)
copy_py_to_matrix = _helper.copy_py_to_matrix

def copy_matrix_to_py(*args):
  return _helper.copy_matrix_to_py(*args)
copy_matrix_to_py = _helper.copy_matrix_to_py


