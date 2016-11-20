#!/usr/bin/env perl

use strict;
use warnings;

my $test = "ThisIsAVeryLong UnbreakableStringWhichIs BiggerThan20Characters";

if ( $test !~ /\s/ ) {
    print "No spaces found\n";
}
