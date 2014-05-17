#!C:\Perl64\bin\perl.exe

#use strict;
use Data::Dumper;
use Storable;
use JSON;
use CGI;


my $cgi=CGI->new;


print $cgi->header(-type=>"text/html");


my %res;

open (IN, "log/log.txt");
while (<IN>){
	my $tmp=$_;
	my @config=split(/_/, $tmp);
	$res{$config[4]}=$res{$config[4]}+1;
}




my @result;
my %color;

$color{"Accepted!"}='#66CD00';
$color{"Time Limit Excceeded!"}='#CD8500';
$color{"Wrong Answer!"}='#B22222';
$color{"Compile Error!"}='#828282';
$color{"Cheat!"}='#7A378B';

foreach my $key(keys %res){
	unless ($key eq ""){
		push @result, {name=>$key,y=>$res{$key}};
	}
}

my $json = new JSON;
print $json->encode(\@result);
close(IN);

