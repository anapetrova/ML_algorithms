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
## @deftypefn {Function File} {@var{retval} =} Jacobis (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Anastasia Petrova <ana@Ana.local>
## Created: 2015-10-18
function [x,iterations]=Jacobis(A,b,x,maxIter,tolerance)
%x is the initial guess. %maxIter is maximum number of iterations
%tolerance is desired accuracy

n=length(b);

iterations=maxIter;

for k=1:maxIter
  oldx=x; %save the old x
  x=b;
  for i=1:n
    for j=1:i-1
    x(i)=x(i)- A(i,j)*x(j);
    end
    for j=i+1:n
    x(i)=x(i)-A(i,j)*oldx(j);
    end
    x(i)=x(i)/A(i,i);
  end
  if norm(b - A*x)<tolerance
    iterations=k;
    break
  end
end

endfunction