#   Copyright 2011 OpenPlans and contributors
#
#   This file is part of OpenBlock
#
#   OpenBlock is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   OpenBlock is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with OpenBlock.  If not, see <http://www.gnu.org/licenses/>.
#

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import os.path
here = os.path.dirname(__file__)
with open(os.path.join(here, 'README.txt')) as file:
    long_description = file.read()
    # Add the generic OpenBlock README and the changelog.
    openblock_readme = os.path.join(here, '..', 'README.txt')
    if os.path.exists(openblock_readme):
        with open(openblock_readme) as openblock_readme:
            long_description += '\n\n'
            long_description += openblock_readme.read()
    release_notes = os.path.join(here, '..', 'docs', 'release_notes.rst')
    if os.path.exists(release_notes):
        with open(release_notes) as release_notes:
            long_description += '\n\n'
            long_description += release_notes.read()
    # Remove stuff that breaks vanilla rst (no sphinx)
    # and doesn't belong on a pypi page anyway.
    long_description = long_description.split('Older Changes')[0]
    open('/tmp/thing.rst', 'w').write(long_description)

VERSION="1.0.0"

setup(
    name='obdemo',
    version=VERSION,
    description="Demo website configuration for OpenBlock (hyperlocal news for Django)",
    long_description=long_description,
    license="GPLv3",
    keywords="openblock",
    maintainer="Paul Winkler (for OpenPlans)",
    maintainer_email="ebcode@groups.google.com",
    url="http://openblockproject.org/docs",
    install_requires=[
        # Assume all these packages are versioned together.
        "ebpub>=%s" % VERSION,
        "ebdata>=%s" % VERSION,
        "obadmin>=%s" % VERSION,
    ],
    dependency_links=[
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    exclude_package_data={'obdemo': ['settings.py']},
    entry_points="""
    """,
    classifiers=[
        #'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        ],
)
