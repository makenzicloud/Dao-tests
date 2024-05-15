/*
* Lets check for burn and mint correctness i.e functionality of burn and mint functions
*/

import "./IERC20.spec";
import "./IERC2612.spec";

methods {
    function burn(address,uint256)                  external;
    function mint(address,uint256)                  external;
   
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│Hook + Ghost : check balances                                                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/

ghost mathint sum_of_balances {
    init_state axiom sum_of_balances == 0;
}


// Let`s make sure that balance can not be bigger than totalSupply
hook Sload uint256 balance _balances[KEY address addr] {
    require sum_of_balances >= to_mathint(balance);
}

hook Sstore _balances[KEY address addr] uint256 newValue(uint256 oldValue ) {
    sum_of_balances = sum_of_balances;
}

/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│Invariant: totalSupply is the total of balances                                                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/

invariant totalSupplyMatchesBalances() 
    to_mathint(totalSupply()) == sum_of_balances;


/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│Invariant: balance 0x0 is 0                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/

invariant balanceZeroIsZero() 
    balanceOf(0x0) == 0;


/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│Rule: burn/mint are the only for total supply change                                                              │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule noTotalSupplyChange(env e) {
    requireInvariant totalSupplyMatchesBalances();

    method f;
    calldataarg args;

    uint256 totalSupplyBefore = totalSupply();
    f(e, args);
    uint256 totalSupplyAfter = totalSupply();

    assert totalSupplyAfter > totalSupplyBefore => f.selector == sig:mint(address,uint256).selector;
    assert totalSupplyAfter < totalSupplyBefore => f.selector == sig:burn(address,uint256).selector;

}

    






















