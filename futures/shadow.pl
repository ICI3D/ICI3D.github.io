use strict;
use 5.10.0;

while(<>){
	chomp;
	next if /\bSHADOW\b/;
	s/\bNOTE\b.*//;
	s/\bHIDE\b.*//;
	s/\s*\bOPEN\b\s*/ /;
	say;
}
