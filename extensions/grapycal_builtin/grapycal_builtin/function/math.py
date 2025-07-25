from grapycal.sobjects.functionNode import FunctionNode
import math

class AdditionNode(FunctionNode):
    '''
    Adds a set of values together. The values can be of any addable type, such as numbers, NumPy arrays,
    PyTorch tensors, or strings.

    :inputs:
        - values: a set of values
        
    :outputs:
        - sum: sum of all values
    '''
    category = 'function/math'

    inputs = ['items']
    max_in_degree = [None]
    outputs = ['sum']
    display_port_names = False

    def build_node(self):
        super().build_node()
        self.label.set('+')
        self.label_offset.set(-.09)
        self.shape.set('round')

    def calculate(self, items):
        if len(items) == 0:
            summation = 0
        else:
            summation = items[0]
            for d in items[1:]:
                summation = summation + d #type: ignore
        return summation
    
class SubtractionNode(FunctionNode):
    '''
    Calculates sum(`B`) - sum(`A`).
    
    :inputs:
       - A: A set of values, `A`
       - B: A set of values, `B`
    
    :outputs:
        -  Difference: sum(`A`) - sum(`B`)
    '''
    category = 'function/math'
    inputs = ['a', 'b']
    max_in_degree = [None, None]
    outputs = ['a-b']
    display_port_names = False

    def build_node(self):
        super().build_node()
        self.label.set('-')
        self.label_offset.set(-.09)
        self.shape.set('round')

    def calculate(self, a,b):
        return sum(a) - sum(b)
    
class MultiplicationNode(FunctionNode):
    '''
    Multiplies a set of values together. The values can be of any multipliable type, such as numbers, NumPy arrays, or
    PyTorch tensors.

    :inputs:
        - values: a set of values
    
    :outputs:
        - product: product of all values
    '''
    category = 'function/math'
    inputs = ['items']
    max_in_degree = [None]
    outputs = ['product']
    display_port_names = False

    def build_node(self):
        super().build_node()
        self.label.set('*')
        self.label_offset.set(-.09)
        self.shape.set('round')

    def calculate(self, items):
        if len(items) == 0:
            product = 1
        else:
            product = items[0]
            for d in items[1:]:
                product = product * d
        return product
    
class DivisionNode(FunctionNode):
    '''
    Calculates product(`B`) / product(`A`).
    
    :inputs:
        - A: A set of values, `A`
        - B: A set of values, `B`

    :outputs:
        -  Quotient: product(`B`) / product(`A`)
    '''
    category = 'function/math'
    inputs = ['a', 'b']
    max_in_degree = [None,None]
    outputs = ['a/b']
    display_port_names = False
    
    def build_node(self):
        super().build_node()
        self.label.set('/')
        self.shape.set('round')

    def calculate(self, a, b):
        if len(a) == 0:
            nominator = 1
        else:
            nominator = a[0]
            for d in a[1:]:
                nominator *= d

        if len(b) == 0:
            denominator = 1
        else:
            denominator = b[0]
            for d in b[1:]:
                denominator *= d
        return nominator/denominator
                
#   PowerNode class implementation
class PowerNode(FunctionNode):
    '''
    Calculates sum(`B`) ** sum(`A`).
    
    :inputs:
       - A: A set of values, `A`
       - B: A set of values, `B`
    
    :outputs:
        -  Power: sum(`A`) ** sum(`B`)
    '''
    category = 'function/math'
    inputs = ['a', 'b']
    max_in_degree = [None, None]
    outputs = ['a**b']
    display_port_names = False

    def build_node(self):
        super().build_node()
        self.label.set('**')
        self.label_offset.set(-.09)
        self.shape.set('round')

    def calculate(self, a,b):
        return sum(a) ** sum(b)
    
#   MaxNode class implementation
class MaxNode(FunctionNode):
    '''
    Calculates max(sum(`B`), sum(`A`)).
    
    :inputs:
       - A: A set of values, `A`
       - B: A set of values, `B`
    
    :outputs:
        -  Power: max(sum(`A`), sum(`B`))
    '''
    category = 'function/math'
    inputs = ['a', 'b']
    max_in_degree = [None, None]
    outputs = ['max(a, b)']
    display_port_names = False

    def build_node(self):
        super().build_node()
        self.label.set('max')
        self.label_offset.set(-.09)
        
        self.shape.set('round')

    def calculate(self, a, b):
        return max(sum(a), sum(b))
    
#   MinNode class implementation
class MinNode(FunctionNode):
    '''
    Calculates min(sum(`B`), sum(`A`)).

    :inputs:
       - A: A set of values, `A`
       - B: A set of values, `
    
    :outputs:
        -  Power: min(sum(`A`), sum(`B`))
    '''
    category = 'function/math'
    inputs = ['a', 'b']
    max_in_degree = [None, None]
    outputs = ['min(a, b)']
    display_port_names = False

    def build_node(self):
        super().build_node()
        self.label.set('min')
        self.label_offset.set(-.09)
        self.shape.set('round')

    def calculate(self, a, b):
        return min(sum(a), sum(b))
        
        
class LogNode(FunctionNode):
    '''
    Calculate log(sum(`A`))
    '''
    category = 'function/math'
    inputs = ['a']
    max_in_degree = [None]
    outputs = ['log(a)']
    display_port_names = False

    def build_node(self):
        super().build_node()
        self.label.set('log')
        self.label_offset.set(-.09)
        self.shape.set('round')

    def calculate(self, a):
        return math.log(sum(a))

class SinNode(FunctionNode):
    '''
    Calculate sin(sum(`A`))
    '''
    category = 'function/math'
    inputs = ['a']
    max_in_degree = [None]
    outputs = ['sin(a)']
    display_port_names = False

    def build_node(self):
        super().build_node()
        self.label.set('sin')
        self.label_offset.set(-.09)
        self.shape.set('round')

    def calculate(self, a):
        return math.sin(sum(a))

class CosNode(FunctionNode):
    '''
    Calculate cos(sum(`A`))
    '''
    category = 'function/math'
    inputs = ['a']
    max_in_degree = [None]
    outputs = ['cos(a)']
    display_port_names = False
    
    def build_node(self):
        super().build_node()
        self.label.set('cos')

    def calculate(self, a):
        return math.cos(sum(a))

class TanNode(FunctionNode):
    '''
    Calculate tan(sum(`A`))
    '''
    category = 'function/math'
    inputs = ['a']
    max_in_degree = [None]

