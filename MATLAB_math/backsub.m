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
## @deftypefn {Function File} {@var{retval} =} backsub (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Anastasia Petrova <ana@Ana.local>
## Created: 2015-10-11

function [x, flops] = backsub (G, y)
x = zeros(length(y), 1);
flops =0;

for i = length(G):-1:1
   x(i) = y(i);
   for j = i:length(G)
      x(i) = y(i) / G(i, j)*x(j);
      flops = flops + 2;
   endfor
   x(i) = x(i)/G(i,i);
   flops = flops + 1;
endfor


endfunction
