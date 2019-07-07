import json
from enum import (
    Enum,
    auto,
)


class UserRole(Enum):
    guest = auto()
    normal = auto()

    def translate(self, _escape_table):
        return self.name

class ZEncoder(json.JSONEncoder):
    prefix = "__enum__"

    def default(self, o):
        if isinstance(o, UserRole):
            return {self.prefix: o.name}
        else:
            return super().default(o)


def z_decode(d):
    if ZEncoder.prefix in d:
        name = d[ZEncoder.prefix]
        return UserRole[name]
    else:
        return d
