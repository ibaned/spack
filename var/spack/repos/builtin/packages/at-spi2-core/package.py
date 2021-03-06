##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class AtSpi2Core(MesonPackage):
    """The At-Spi2 Core package provides a Service Provider Interface for the
       Assistive Technologies available on the GNOME platform and a library
       against which applications can be linked."""

    homepage = "http://www.linuxfromscratch.org/blfs/view/cvs/x/at-spi2-core.html"
    url      = "http://ftp.gnome.org/pub/gnome/sources/at-spi2-core/2.28/at-spi2-core-2.28.0.tar.xz"
    list_url = "http://ftp.gnome.org/pub/gnome/sources/at-spi2-core"
    list_depth = 1

    version('2.28.0', '9c42f79636ed1c0e908b7483d789b32e')

    depends_on('glib@2.56.1:')
    depends_on('dbus@1.12.8:')
    depends_on('libx11')
    depends_on('libxi')
    depends_on('libxtst', type='build')
    depends_on('recordproto', type='build')
    depends_on('inputproto', type='build')
    depends_on('fixesproto', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('python', type='build')

    def url_for_version(self, version):
        """Handle gnome's version-based custom URLs."""
        url = 'http://ftp.gnome.org/pub/gnome/sources/at-spi2-core'
        return url + '/%s/at-spi2-core-%s.tar.xz' % (version.up_to(2), version)

    def setup_environment(self, spack_env, run_env):
        # this avoids an "import site" error in the build
        spack_env.unset('PYTHONHOME')
