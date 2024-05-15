/// @title IERC20 interface
/// @dev see 

methods {
    function totalSupply()                          external returns(uint) envfree;
    function balanceOf(address)                     external returns(uint) envfree;
    function allowance(address,address)             external returns(uint) envfree;
    function transfer(address,uint)                 external;
    function transferFrom(address,address,uint)     external;
    function approve(address,uint)                  external;
    function decimals()                            external returns(uint8) envfree;
    function symbol()                              external returns(string) envfree;
    function name()                                external returns(string) envfree;

}