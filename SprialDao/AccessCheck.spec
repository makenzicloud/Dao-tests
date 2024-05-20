methods {
    // === View Methods ===
    
    // Get the address of the current owner
    function owner() external returns (address) envfree;
    
    // === Mutations ===

    // Renounce ownership of the contract
    function renounceOwnership() external returns(address) envfree;
    
    // Transfer ownership of the contract to a new owner
    function transferOwnership(address) external returns(address) envfree;
    
    // Internal method to transfer ownership (without access restriction)
    function _transferOwnership(address) internal returns(address) envfree;
    
    // Check if the caller is the owner (internal method)
    function _checkOwner() internal returns (bool) envfree;
    
    // == Formal Verification (FV) ==

    // Ensure that the owner is correctly set
    function ensure_owner_correctly_set() external returns(bool) envfree;
}
