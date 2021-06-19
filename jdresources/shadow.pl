use strict;
use 5.10.0;

my @faculty = qw(
	paradza bruce hargrove dushoff mthombothi scott borchering pulliam
	vanschalkwyk kassanjee pearson
);

my %faculty;

## Sorry to be lazy; faculty file must end with a blank line

while(<>){
	last if /^\s*$/;
	my $(tag, $name) = /(\S*)\s+(.*);
	say "$name ($tag)";
}

while(<>){
	last if m|/HEAD|;
}

my $linktext = "{{site.subdomainurl}}/team";

while(<>){
	chomp;
	## Use SHADOW for resources, events and event notes for future
	## It blocks the whole line
	## Save HIDE for things we're hoping to reveal this year
	## It only blocks things that follow it
	## NOTE for shorter (part-line) notes, to help the goal of getting rid of HIDE as workshop progresses
	next if /SHADOW/;
	s/HIDE.*//;
	s/NOTE.*//;
	foreach my $f (@faculty){
	s|\($f\)|[Masimba Paradza]($linktext/paradza/)|;
	}
	s|\(bruce\)|[Faikah Bruce]($linktext/bruce/)|;
	s|\(hargrove\)|[John Hargrove]($linktext/hargrove/)|;
	s|\(dushoff\)|[Jonathan Dushoff]($linktext/dushoff/)|;
	s|\(mthombothi\)|[Zinhle Mthombothi]($linktext/mthombothi/)|;
	s|\(scott\)|[Jim Scott]($linktext/scott/)|;
	s|\(borchering\)|[Becky Borchering]($linktext/borchering/)|;
	s|\(pulliam\)|[Juliet Pulliam]($linktext/pulliam/)|;
	s|\(vanschalkwyk\)|[Cari van Schalkwyk]($linktext/vanschalkwyk/)|;
	s|\(kassanjee\)|[Reshma Kassanjee]($linktext/kassanjee/)|;
	s|\(pearson\)|[Carl Pearson]($linktext/pearson/)|;
	say;
}
