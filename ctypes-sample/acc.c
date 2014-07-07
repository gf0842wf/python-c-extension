#include "acc.h"

unsigned long long acc() 
{
	unsigned long long s = 0;
	unsigned long long i = 0;
	for(i=0; i<100000000; i++)
	{
		s += i;
	}
	return s;
}
