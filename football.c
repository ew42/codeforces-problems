// https://codeforces.com/problemset/problem/96/A
// learning C right now

#include <stdio.h>

int main() {
	char str[100];
	char current_char = 'a';
	int count = 1;

	scanf("%s", str);

	for (int i = 0; str[i] != '\0'; i++) {
		if (str[i] != current_char) { //If different, restart count and change to that one
			current_char = str[i];
			count = 1;
		}
		else {
			++count;
			if (count == 7) {
				printf("YES\n");
				return 0;
			}
		}

	}
	printf("NO\n");
	
}


