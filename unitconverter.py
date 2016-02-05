import sys
# -------------------------------------------------
# -------------------------------------------------
class UnitConverter:
	def mm2cm(self, input):
		return input * 0.1
	def cm2mm(self, input):
		return input / 0.1
		
	def in2cm(self, input):
		return input * 2.54
	def cm2in(self, input):
		return input / 2.54
		
	def ft2cm(self, input):
		return input * 30.48
	def cm2ft(self, input):
		return input / 30.48
		
	def yd2cm(self, input):
		return input * 91.44
	def cm2yd(self, input):
		return input / 91.44
		
	def m2cm(self, input):
		return input * 100
	def cm2m(self, input):
		return input / 100
		
	def km2cm(self, input):
		return input * 100000
	def cm2km(self, input):
		return input / 100000
		
	def mi2cm(self, input):
		return input * 160934
	def cm2mi(self, input):
		return input * 160934
		
	def nm2cm(self, input):
		return input * 185200
	def cm2nm(self, input):
		return input / 185200
# -------------------------------------------------
# -------------------------------------------------
if len(sys.argv) != 4:
	print("Error: Missing required arguments.", file=sys.stderr)
	exit()

inMeasurement = float(sys.argv[1])
inUnit = sys.argv[2].lower()
outUnit = sys.argv[3].lower()

try:
	unitConverter = UnitConverter()
	result = 0
	if inUnit == 'cm':
		result = inMeasurement
	else:
		cmMethodName = inUnit + "2cm"
		cmMethod = getattr(unitConverter, cmMethodName, None)
		
		if not cmMethod:
			raise Exception("Conversion is not supported.")

		result = cmMethod.__call__(inMeasurement)
		
	if outUnit == "cm":
		pass
	else:
		convertMethodName = "cm2" + outUnit
		convertMethod = getattr(unitConverter, convertMethodName, None)
		if not convertMethod:
			raise Exception("Conversion is not supported.")
		result = convertMethod.__call__(result)
	print(result, outUnit)
except Exception as ex:
	print(str(ex), file=sys.stderr)
	exit()





