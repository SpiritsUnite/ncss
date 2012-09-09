import StringIO

class AndNode(Node):
	def get_description(self):
		return "AND"
	
	def evaluate(self, variables):
		return all(i.evaluate(variables) for i in self.get_children())


class OrNode(Node):
	def get_description(self):
		return "OR"
	
	def evaluate(self, variables):
		return any(i.evaluate(variables) for i in self.get_children())


class NotNode(Node):
	def __init__(self, child):
		self.child = [child]
	
	def get_children(self):
		return self.child
	
	def get_description(self):
		return "NOT"
	
	def evaluate(self, variables):
		return not self.get_children()[0].evaluate(variables)


class VarNode(Node):
	def __init__(self, variable):
		self._variable = variable
	
	def pprint(self, out, indent):
		out.write('%s%s\n' % (indent, self.get_description()))
	
	def get_description(self):
		return self._variable
	
	def evaluate(self, variables):
		return variables[self.get_description()]
