/*
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Find and show a path for each method.                                                                               │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
*/
rule reachability(method f)
{
	env e;
	calldataarg args;
	f(e,args);
	satisfy true;
}