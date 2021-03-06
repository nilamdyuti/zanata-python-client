#vim:set et sts=4 sw=4: 
# 
# Zanata Python Client
#
# Copyright (c) 2011 Jian Ni <jni@redhat.com>
# Copyright (c) 2011 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.
__all__ = (
    "Logger",
)

class Logger:
    def __init__(self):
        self.enable_infoprefix = False
        self.enable_warnprefix = True
        self.enable_errprefix = True
        self.warn_prefix = 'warning: '
        self.error_prefix = 'error: '
        self.info_prefix = '[INFO] '

    def info(self, message):
        if self.enable_infoprefix:
            print self.info_prefix+message
        else:
            print message

    def warn(self, message):
        if self.enable_warnprefix:
            print self.warn_prefix+message
        else:
            print message

    def error(self, message):
        if self.enable_errprefix:
            print self.error_prefix+message
        else:
            print message
    
