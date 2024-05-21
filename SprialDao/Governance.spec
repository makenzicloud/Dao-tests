// If `setGovernance` changes the governance address, then it was called by the current governance
rule onlyGovernanceCanChangeGovernance {
    address oldGovernance; address newGovernance;
    env e;

    oldGovernance = governance;

    setGovernance(e, newGovernance);

    // Check if governance was updated and ensure it was done by the old governance
    assert governance == newGovernance => e.msg.sender == oldGovernance, "Only governance can change governance";
}

// ## Invariants ##

invariant governanceConsistency() 

    // preserved setGovernance(address newGovernance) with (env e) {
        oldGovernance = governance;
        setGovernance(e, newGovernance);
        assert governance == newGovernance => e.msg.sender == oldGovernance, "Only the current governance can change governance";
    

