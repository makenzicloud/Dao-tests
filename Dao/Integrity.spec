rule noChangeToOtherUserBalance {
  method f; // Replace with "stakeAndIncreaseLock" for specific function testing
  calldataarg args;
  env e;
  address someUser;

  uint256 stakedBefore = allBalancesOf[someUser]; // Extract staked balance
//   uint256 someUserBalanceBefore = nativeBalances[someUser];

  f(e, args);

  // Assert that only the user's staked balance can change
  assert stakedBefore != e.allBalancesOf(someUser).staked =>
    someUser == e.msg.sender || f.contract == someUser;
}