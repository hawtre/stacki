# @copyright@
# Copyright (c) 2006 - 2017 Teradata
# All rights reserved. Stacki(r) v5.x stacki.com
# https://github.com/Teradata/stacki/blob/master/LICENSE.txt
# @copyright@
#

import os
import stack.commands


class Implementation(stack.commands.Implementation):
	"""Unmount the ISO image on linux"""
	
	def run(self, args):
		os.system('umount %s > /dev/null 2>&1' % self.owner.mountPoint)
