class USSDOption:
    def __init__(self, name:str, action: str, parent: str, childs: list[str], value: int, function ) -> None:
        self.name = name
        self.action = action
        self.parent = parent
        self.childs = childs
        self.value = value
        self.function = function
        
    def has_parent(self) -> bool:
        return self.parent is not None
        
    def has_childs(self) -> bool:
        return self.childs is not None
        
    def get_parent(self) -> str:
        return self.parent
        
    def get_action(self) -> str:
        return self.action
        
    def get_childs(self) -> list[str]:
        return self.childs
        
    def get_value(self) ->  int:
        return self.value
