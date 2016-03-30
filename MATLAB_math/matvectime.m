n = 500;

for jay = 1:4
   if jay > 1
      oldtime = time;
   end
   
   A = randn(n, n);
   X = randn(n, n);
   t = cputime;
   
   for rep = 1:100
      b = A * X;
   end
   matrixsize = n
   time = cputime - t
      if jay > 1
         ratio = time/oldtime
      end
   n = 2 * n;
end
   