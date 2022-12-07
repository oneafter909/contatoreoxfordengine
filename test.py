#!/usr/bin/env python
# Contatore Oxford Engine (COX-E)
# Copyright (C) 2021-2022
# BIRBONE PRODUCTIONS
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This module is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.

import components.cox as cox

def main():
    t = input("Inserisci un testo:\n")
    print(cox.count(t))



main()