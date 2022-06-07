# @version ^0.3.0

event DataChange:
    setter: indexed(address)
    value: String[10000]

storedData: public(String[10000])

@external
def __init__(_x: String[10000]):
  self.storedData = _x

@external
def set(_x: String[10000]):
  #assert self.storedData < 100, "Storage is locked when 100 or more is stored"
  self.storedData = _x
  log DataChange(msg.sender, _x)

@external
def reset():
  self.storedData = ""