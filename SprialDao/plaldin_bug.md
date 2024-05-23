**Bug Submission*8
# Description
The current implementation assumes that the amount of PAL tokens transferred will be equal to the amount specified in the stake function. However, some ERC20 tokens may have a fee-on-transfer mechanism, causing the actual amount received to be less than the specified amount. This discrepancy can lead to incorrect minting of hPAL tokens and potential loss of funds.

# Attack Scenario\

A user stakes a token with a fee-on-transfer mechanism.
The stake function mints hPAL tokens based on the specified amount, not accounting for the transfer fee.
The contract receives fewer tokens than expected, leading to an imbalance and potential exploitation.
Attachments

Proof of Concept (PoC) File
pragma solidity ^0.8.10;

contract FeeOnTransferToken is ERC20 {
    constructor() ERC20("FeeOnTransferToken", "FOT") {}

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = amount / 100; // 1% fee
        uint256 amountAfterFee = amount - fee;
        _transfer(_msgSender(), recipient, amountAfterFee);
        _burn(_msgSender(), fee); // Burn the fee
        return true;
    }
}