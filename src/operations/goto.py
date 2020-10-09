#
# goto.py
#
# the pashmak project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
#
# This file is part of pashmak.
#
# pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
##################################################

def run(self, op: dict):
    ''' Changes program step to a section '''

    self.require_one_argument(op, 'goto operation requires section name argument')
    arg = op['args'][0]

    try:
        section_index = self.sections[arg]
    except:
        self.raise_error('SectionError', 'undefined section "' + str(arg) + '"', op)

    self.current_step = section_index-1
