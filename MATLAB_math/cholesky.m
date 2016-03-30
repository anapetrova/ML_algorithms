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
## @deftypefn {Function File} {@var{retval} =} cholesky (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Anastasia Petrova <ana@Ana.local>
## Created: 2015-10-11

function [retMat] = cholesky (mat)
retMat = triu(mat);
for i= 1:length(mat)
   for k = 1:i-1
      retMat(i,i) = retMat(i,i) - retMat(k,i)**2;
   endfor
   if retMat(i,i) <= 0
      error("Matrix is not positive definite");
   endif
   retMat(i,i) = sqrt(retMat(i,i));
   for j = i+1:length(mat)
      for k = 1:i-1
         retMat(i,j) = retMat(i,j) - retMat(k,i)*retMat(k,j);
      endfor
      retMat(i,j) = retMat(i,j)/retMat(i,i);
   endfor
endfor
endfunction
