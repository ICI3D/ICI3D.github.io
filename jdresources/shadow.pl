use strict;
use 5.10.0;

my %faculty;

while(<>){
	last if /^\s*$/;
	die ("Blank line needed at end of faculty file") if /--/;
	die ("Invalid faculty line (use tabs to delimit)?") unless /\t/;
	my ($tag, $name) = /(.*)\t(.*)/;
	$faculty{$tag} = $name;
}

while(<>){
	last if m|/HEAD|;
	die "/HEAD needed after shadow header" if /###.*Monday/;
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
	foreach my $tag (keys %faculty){
		s|\($tag\)|[$faculty{$tag}]($linktext/$tag/)|;
	}
	say;
}
