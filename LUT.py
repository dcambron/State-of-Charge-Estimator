##!python 3
class LUT(object):

	#  An array-like object that provides interpolated values between set points.
	def __init__(self, points):
		self.points = sorted(points)

	def __getitem__(self, x):
		if x < self.points[0][0]:
			return self.points[0][1]
		if x > self.points[-1][0]:
			return self.points[-1][1]
		lower_point, upper_point = self._GetBoundingPoints(x)
		return self._Interpolate(x, lower_point, upper_point)

	def _GetBoundingPoints(self, x):
		#    """Get the lower/upper points that bound x."""
		lower_point = None
		upper_point = self.points[0]
		for point  in self.points[1:]:
			lower_point = upper_point
			upper_point = point
			if x <= upper_point[0]:
				break
		return lower_point, upper_point

	def _Interpolate(self, x, lower_point, upper_point):
		#   """Interpolate a Y value for x given lower & upper bounding points."""
		slope = (float(upper_point[1] - lower_point[1]) /(upper_point[0] - lower_point[0]))
		return lower_point[1] + (slope * (x - lower_point[0]))