from dataclasses import dataclass
from typing import Optional, Tuple, Dict, ClassVar

@dataclass
class Target:
    id: str     # name, 'login'
    name: Optional[str] = None   # filename, 'login_icon'
    search_region: Optional[Tuple[int, int, int, int]] = None
    click_pos: Optional[Tuple[int, int]] = None
    
    # global registry: id - object
    registry: ClassVar[Dict[str, "Target"]] = {}
    
    def __post_init__(self):
        Target.registry[self.id] = self  # 自动注册
        if not self.click_pos and self.search_region:   # if has region, auto complete click_pos
            self.click_pos = (self.search_region[0] + self.search_region[2]) // 2, (self.search_region[1] + self.search_region[3]) // 2
    