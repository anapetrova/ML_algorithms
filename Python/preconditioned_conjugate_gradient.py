import numpy as np


def preconditioned_cg(A, b, x_0, M_inv, num_iter):
	r = b - A.dot(x_0)
	z = M_inv.dot(r)
	p = z
	x = x_0

	for k in range(0, num_iter):
		r_old = r
		z_old = z
		
		a = float(r.T.dot(z) / p.T.dot(A.dot(p)))
		x = x + a * p
		r = r_old - a * A.dot(p)
		#exit here if r < epsilon
		
		z = M_inv.dot(r)
		beta = float(z.T.dot(r) / z_old.T.dot(r_old))
		p = z + beta * p

	return x

if __name__ == "__main__":
	A = np.matrix('1.0 2.0; 2.0 1.0')
	b = np.matrix('3.0; 5.0')

	x_0 = np.ones([2, 1], dtype=float)
	M_inv = A

	print preconditioned_cg(A, b, x_0, M_inv, 5)
			
		
