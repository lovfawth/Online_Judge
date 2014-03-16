#!C:\Perl64\bin\perl.exe

use Data::Dumper;
use Storable;
#my $pid=1001;
#my $i="dir probs\\".$pid."\\ /b";
#my @ret=`$i`;
#my $num=@ret;
#my @min=`dir probs\1001\ /ad/b`;
#my $minus=@min;
#print $num-$minus;
#
#print `fc 123.txt 321.txt`;
#FC: no differences encountered

my @ret;
push @ret, 1000;
store \@ret, "library.txt";
