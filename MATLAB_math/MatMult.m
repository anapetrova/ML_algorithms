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
## @deftypefn {Function File} {@var{retval} =} MatMult (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Anastasia Petrova <ana@Ana.local>
## Created: 2015-09-28

function [product, flops] = MatMult (mat1, mat2)
   [m1, n1] = size(mat1);
   if size(mat1) ~= size(mat2) || m1 ~= n1
      error("The matrices are of different sizes, or not nxn matrices.");
   end
   n = m1;
   flops = 0;
   product = zeros(m1, n1);
   
   for i=1:n 
      for j=1:n
         for k=1:n
            product(i, j) = product(i, j) + mat1(i, k) * mat2(k, j);
            flops = flops + 2;
         end
      end
   end
endfunction
