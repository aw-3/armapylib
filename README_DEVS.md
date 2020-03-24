## Writing your own modules
See __template__.py for example.


## Writing your own engine
An engine in this framework is twofold; It consists of a native DLL and a python wrapper.

The native library hooks into your target game and provides an easily accessible API to your wrapper.

The wrapper uses ctypes to neatly call the native API.

Engines provide the core functionality that modules will utilize. It's functions should be clear, concise, generic and well documented.
