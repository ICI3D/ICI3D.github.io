use strict;
use 5.10.0;

while(<>){
	chomp;
	next if /SHADOW/;
	s/NOTE.*//;
	s/HIDE.*//;
	s/OPEN\b\s*//;
	say;
}
