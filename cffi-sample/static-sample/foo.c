#include "foo.h"

int test(void) {
	static int i = 0;
	i++;
	return i;
}

