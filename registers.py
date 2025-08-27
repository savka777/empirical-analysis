import inspect
from dataclasses import dataclass
import random
from typing import Any, Callable, Dict, List, Optional, Union # Allows a variable to multiple types
import string

@dataclass
class ParameterInfo:
    name: str
    annotation : Optional[type]
    default : Any
    is_primary : bool = False 

class InputGeneratorRegistry:
    """Registery that registers data generators based on type"""    
    def __init__(self):
        # {list : <generate_list}
        # {Graph : <generate_graph}
        self.generators = {} 
        self.register_default()


    def register_default(self):
        """Add to Register dictionary"""
        self.register(list,self.generate_list)
        self.register(str,self.generate_string)

        # TODO: ADD graph, strings, trees, etc

    def register(self, type, generator):
        """Based on type, register appropriate generator"""
        self.generators[type] = generator

    def generate_list(self, size):
        l = []
        for _ in range(size):
            l.append(random.randint(1,1000))
        
        return l;

    def generate_string(self,size):
        return ''.join(random.choices(string.ascii_lowercase, k = size))

    def can_generate(self, type):
        if type in self.generators: 
            return True
        return False
    
    def generate_input(self, type, size):
        if type in self.generators:
            generator = self.generators[type] # Returns function based on type, i.e generate_list
            return generator(size)

        return ValueError("No generator has been created for type: ", type)


class FunctionAnalyzer:
    """Analyse the function, generate test inputs"""

    def __init__(self):
        self.registry = InputGeneratorRegistry()
    
    def analyze_function(self, func):
        """Analyze the function signatures"""
        signature = inspect.signature(func)
        parameters = []

        print("DEBUG: Analyzing the parameter types")

        for parameter_name, parameter in signature.parameters.items():
            # Skip *args or **kwargs
            if parameter.kind in (parameter.VAR_POSITIONAL, parameter.VAR_KEYWORD):
                continue
            
            parameter_info = ParameterInfo(
                name = parameter_name,
                annotation = parameter.annotation if parameter.annotation != parameter.empty else None,
                default = parameter.default if parameter.default != parameter.empty else None,    
            )

            parameters.append(parameter_info)

        # Might no make sense, leaving for now
        if parameters:
            parameters[0].is_primary = True
        
        return parameters

    def generate_test_input(self, func, size):
        "Generate Test input for a function at a given size"

        parameters = self.analyze_function(func)

        if not parameters:
            return () # Function has no parameters
        
        # Handling the first parameter, will need to extend for functions with more than 1 parameter
        parameter = parameters[0]

        print("DEBUG: Generating data for: ", parameter.annotation, " of size: " , size)

        # right now its only the one, later it will be many, many need to iterate and compare
        curr_parameter = parameter.annotation
        # Check if we have a generator for this parameter type
        if curr_parameter and self.registry.can_generate(curr_parameter):
            test_input = self.registry.generate_input(curr_parameter, size)
            print("DEBUG: Generated Input for: ", curr_parameter, " completed")
            return (test_input,)
        else:
            raise ValueError("Cannot generate input for parameter: ", curr_parameter)
        










