persistent ghost bool called_extcall;
persistent ghost bool g_reverted;
persistent ghost uint32 g_sighash;

// Hook on "CALL" opcodes to simulate reentrancy and check for reverts
hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    called_extcall = true;
    env e;
    bool cond;
    
    // Check if the function signature matches stakeAndLock(uint256,uint256)
    if (g_sighash == sig:stakeAndLock(uint256,uint256).selector) {
        calldataarg args;
        stakeAndLock@withrevert(e, args); // Call the function with revert check
        g_reverted = lastReverted;
    } else {
        // Fallback case
        g_reverted = true;
    }
}

// Rule filtering for non-view functions
rule no_reentrancy(method f, method g) filtered { f->f.isView, g->g.isView } {
    require !called_extcall;
    require !g_reverted;
    env e; calldataarg args;
    
    // Ensure the function signature matches the expected one
    require g_sighash == g.selector;
    f@withrevert(e, args);
    
    // Main assert - expect that if an external function is called
    // any reentrancy to a non-view function will revert
    assert called_extcall => g_reverted, "Reentrancy weakness exists";
}
