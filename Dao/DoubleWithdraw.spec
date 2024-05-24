rule noDoubleDutch(address user) {
    uint256 amount = allBalancesOf(user);
    env e;
    require e.msg.sender == user;
    claim(e, amount);
    uint256 x;
    claim@withrevert(e, x);
    assert lastReverted;
}