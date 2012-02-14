#!/usr/bin/env python

"""
python-dirtt - Directory Tree Templater
(c) 2012 Dashing Collective Inc. and contributors
Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

	btdirt	
	
	This is a generic command line tool to create a project template from an
	existing source tree
"""
import os
import sys
from optparse import OptionParser
from dirtt.util.introspection import *


def main():
	usage = "usage: %prog [-d PROJECT_ROOT]"
	version=__import__('dirtt').get_version()
	description="""Create a project template from an existing source tree."""
	parser = OptionParser(usage=usage, version=version, description=description)
	parser.add_option("-d", "--project-path", dest="project_path", help="Full path to project location.")
	(options, args) = parser.parse_args()
	if options.project_path:
		project_path = options.project_path
	else:
		project_path = None
		print "You must specify a project path with -d or --project-path to run this script."
		sys.exit(-6)

        pbuilder = ProjectBuilder(project_path)
        pbuilder.build_template()
	sys.exit(0)


if __name__ == "__main__":
	main()



