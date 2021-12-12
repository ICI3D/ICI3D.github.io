## Copied from DAIDD 2021 Jun 15 (Tue)
## Not changed 2021 Jun 15 (Tue)
use strict;
use 5.10.0;

my $old = 10;
my $new = shift @ARGV;

while(<>){
	chomp;
	if (/SAST/){
		## say;
		next;
	}
	my @ln = split/([0-9]{1,2}:[0-9]{2})/;
	foreach my $piece (@ln){
		next unless $piece =~ /[0-9]{1,2}:[0-9]{2}/;
		my ($x, $y) = $piece =~ /(.*):(.*)/;
		$x += $new-$old;
		$x += 24 if $x<0;
		$x -= 24 if $x>=24;
		$piece = sprintf("%02d:%02d", $x, $y);
	}
	say join "", @ln;
}
