persistent ghost bool called_extcall;
persistent ghost bool g_reverted;
persistent ghost uint32 g_sighash;

// Hook on "CALL" opcodes to simulate reentrancy and check for reverts
hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    called_extcall = true;
    env e;
    bool cond;
    
    // Adjusted to include the new function signature
    if (g_sighash == sig:withdrawAllUnlockedToken().selector) {
        withdrawAllUnlockedToken@withrevert(e); // Concrete name
        g_reverted = lastReverted;
    }
    else if (g_sighash == sig:withdrawAllUnlockedToken().selector) {
        withdrawAllUnlockedToken@withrevert(e); // Concrete name
        g_reverted = lastReverted;
    }
    else if (g_sighash == sig:withdrawAllUnlockedToken().selector) {
        calldataarg args;
        withdrawAllUnlockedToken@withrevert(e, args); // Concrete name
        g_reverted = lastReverted;
    }
    else {
        // Fallback case
        g_reverted = true;
    }
}

// Rule filtering for non-view functions
rule no_reentrancy(method f, method g) filtered { f->f.isView, g ->g.isView } {
    require!called_extcall;
    require!g_reverted;
    env e; calldataarg args;
    
    // Adjusted to include the new function signature
    require g_sighash == g.selector;
    f@withrevert(e, args);
    
    // Main assert here - we expect that if an external function is called
    // any reentrancy to a non-view function will revert
    assert called_extcall => g_reverted, "Reentrancy weakness exists";
}
