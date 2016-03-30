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
## @deftypefn {Function File} {@var{retval} =} norm2 (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Anastasia Petrova <ana@Ana.local>
## Created: 2015-10-25

function [norm] = norm2 (A)
norm = 0;
for k = 1:100
  angle = k*(2*pi/100);
  x_k = [cos(angle); sin(angle)];
  product = A * x_k;
  temp_norm = sqrt(product(1)^2 + product(2)^2);
  if temp_norm > norm
    norm = temp_norm;
  endif
endfor

endfunction
