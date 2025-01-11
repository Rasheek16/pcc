class InitialValue:
    """Base class for initial values."""
    pass

class Tentative(InitialValue):
    """Represents a tentative definition without an initializer."""
    
    def __init__(self,value=None):
        self.value=value
        # pass  # No additional attributes needed
    
    def __repr__(self):
        return "Tentative()"


class Initial(InitialValue):
    """Represents an initialized variable with a specific value."""
    
    def __init__(self, value):
        self.value = value  # You can adjust the type based on your needs
    
    def __repr__(self):
        return f"Initial(value={self.value})"


class NoInitializer(InitialValue):
    """Represents a variable without an initializer."""
    
    def __init__(self,value=None):
        self.value=value
        
        # pass  # No additional attributes needed
    
    def __repr__(self):
        return "NoInitializer()"


class IdentifierAttr:
    """Base class for identifier attributes."""
    pass


class FunAttr(IdentifierAttr):
    """Represents function attributes."""
    
    def __init__(self, defined: bool, global_scope: bool):
        self.defined = defined
        self.global_scope = global_scope
    
    def __repr__(self):
        return f"FunAttr(defined={self.defined}, global_scope={self.global_scope})"


class StaticAttr(IdentifierAttr):
    """Represents static variable attributes."""
    
    def __init__(self, init: InitialValue, global_scope: bool):
        self.init = init  # Should be an instance of InitialValue
        self.global_scope = global_scope
    
    def __repr__(self):
        return f"StaticAttr(init={self.init}, global_scope={self.global_scope})"


class LocalAttr(IdentifierAttr):
    """Represents local variables."""
    
    def __init__(self):
        pass  # No additional attributes needed
    
    def __repr__(self):
        return "LocalAttr()"
