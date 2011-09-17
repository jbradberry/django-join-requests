from distutils.core import setup
import os

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('joinrequests'):
    # Ignore dirnames that start with '.'
    dirnames[:] = [d for d in dirnames if not d.startswith('.')]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[13:] # Strip "joinrequests/" or "joinrequests\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(name='django-join-requests',
      description=
      'A pluggable app to allow users to request access to a resource',
      version="0.1.0dev",
      author='Jeff Bradberry',
      author_email='jeff.bradberry@gmail.com',
      url='http://github.com/jbradberry/django-join-requests',
      package_dir={'joinrequests': 'joinrequests'},
      packages=packages,
      package_data={'joinrequests': data_files},
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
      long_description=open('README.txt').read(),
      )
