from google.appengine.ext import vendor
vendor.add('lib')

import os, sys, django



# Add any libraries install in the "lib" folder.


if os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Engine'):
	sys.path.insert(0, 'lib.zip')
else:
	if os.name == 'nt':
		os.name = None
		sys.platform = ''