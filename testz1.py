#!/usr/bin/python3.2

import os

object = os
methodlist = [method for method in dir(object) if
		callable(getattr(object, method))]
print("%s\n\n" % "\n".join(methodlist))
