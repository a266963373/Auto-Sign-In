from dataclasses import dataclass
from typing import Optional, Tuple, Dict, ClassVar, List

@dataclass
class Target:
    id: str     # name, 'login'
    name: Optional[str] = None   # filename, 'login_icon'
    search_region: Optional[Tuple[int, int, int, int]] = None
    click_pos: Optional[Tuple[int, int] | List[Tuple[int, int]]] = None
    # stage: Optional[str] = None   # stage, 'homepage'
    
    # global registry: id - object
    prefix: ClassVar[str] = ""   # ✨ 全局统一前缀
    registry: ClassVar[Dict[str, "Target"]] = {}
    
    def __post_init__(self):
        full_id = f"{self.prefix}:{self.id}" if self.prefix else self.id
        Target.registry[full_id] = self  # 🔥 注册用前缀+id
        
        if not self.click_pos and self.search_region:   # if has region, auto complete click_pos
            self.click_pos = (self.search_region[0] + self.search_region[2]) // 2, (self.search_region[1] + self.search_region[3]) // 2
        if not self.name:
            self.name = self.id

    @classmethod
    def get(cls, id: str):
        full_id = f"{cls.prefix}:{id}" if cls.prefix else id
        # print(full_id)
        return cls.registry.get(full_id, None)
