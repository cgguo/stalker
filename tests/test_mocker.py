#-*- coding: utf-8 -*-
########################################################################
# 
# Copyright (C) 2010  Erkan Ozgur Yilmaz
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
# 
########################################################################



import mocker

mockerObj = mocker.Mocker()
obj = mockerObj.mock()

obj.hello()
mockerObj.result("Hi!")
mockerObj.count(0,1000)

mockerObj.replay()

obj.hello()
#'Hi!'

#obj.bye()
#Traceback (most recent call last):
#...
#mockerObj.MatchError: [Mocker] Unexpected expression: obj.bye

#mockerObj.restore()
#mockerObj.verify()