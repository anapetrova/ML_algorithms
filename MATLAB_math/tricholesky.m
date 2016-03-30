## Copyright (C) 2015 Anastasia Petrova
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {Function File} {@var{retval} =} tricholesky (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Anastasia Petrova <ana@Ana.local>
## Created: 2015-10-12


function [retv, retw, flops, sqrts] = tricholesky (v, w)
retv = ones(length(v), 1);
retw = ones(length(w), 1);
flops = 0;
sqrts = 0;
retv(1) = sqrt(v(1));
sqrts = sqrts + 1;
for i = 2:length(v)
   retw(i-1) = w(i-1) / retv(i-1);
   retv(i) = sqrt(v(i) - retw(i-1)^2);

   sqrts = sqrts + 1;
   flops = flops + 3;
endfor


endfunction
