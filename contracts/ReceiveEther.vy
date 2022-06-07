# @version ^0.3.0

event Payment:
    sender: indexed(address)
    amount: uint256
    bal: uint256
    gasLeft: uint256

@external
@payable
def __default__():
    log Payment(msg.sender, msg.value, self.balance, msg.gas)