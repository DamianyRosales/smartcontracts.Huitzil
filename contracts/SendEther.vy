# @version ^0.3.0

@external
@payable
def sendEther(to: address):
    send(to, msg.value)