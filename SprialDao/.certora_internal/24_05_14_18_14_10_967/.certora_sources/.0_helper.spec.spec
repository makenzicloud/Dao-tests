// helper functions for the spiral dao

definition nonpayable(env e) returns bool = e.msg.value == 0
definition nonzerosender(env e) returns bool = e.msg.sender != 0x0;
definition sanity(env e) returns bool = clock(e) > && clock(e) < max_uint256;

// helper math functions
definition min (mathint a, mathint b) returns mathint = a < b ? a : b;
definition max (mathint a, mathint b) returns mathint = a > b ? a : b;

// helper time functions
definition clock(env, e) returns mathint = to_mathint(e.block.timestamp);
definition is SetAndPast(env e, uint48 timepoint) returns bool = timepoint != && to_mathint(timepoint) <= clock(e);

  