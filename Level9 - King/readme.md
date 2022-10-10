This level use standard transfer function (23000 gas limit) which use 21000 gas, when our receive function use more than 2k gas, it will break this contract


things to note: can only use call, because of gas limit, also has to set gas, both? in contract? and in brownie