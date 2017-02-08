#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

void print_usage();
int get_noun(char*,int,int*);
int get_verb(char*,int,int*);
int get_adjective(char*,int,int*);
int get_adverb(char*,int,int*);

int main(int argc, char** argv)
{
	int size = 20;
	int index = 0;
	bool flag = false;
	char current = 0;
	char* buf = NULL;
	FILE* mad_lib_f = NULL;

	if(argc != 2)
	{
		print_usage();
	}
	else
	{
		mad_lib_f = fopen(argv[1],"r");
		if(mad_lib_f == NULL)
		{
			printf("Error: file does not exist\n");
			goto cleanup;
		}

		buf = calloc(size,sizeof(char));
		if(buf == NULL)
		{
			printf("Error: failed to allocate buffer\n");
			goto cleanup;
		}

		current = fgetc(mad_lib_f);
		while(current != EOF)
		{
			if(current == '[')
			{
				flag = true;
			}
			else if(current == ']')
			{
				flag = false;
			}
			else if(flag)
			{
				flag = false;
				//add a special character to our list of blanks
				if(current == 'n')
				{
					index = get_noun(buf,index,&size);
				}
				else if(current == 'v')
				{
					index = get_verb(buf,index,&size);
				}
				else if(current == 'j')
				{
					index = get_adjective(buf,index,&size);
				}
				else if(current == 'd')
				{
					index = get_adverb(buf,index,&size);
				}
				else
				{
					printf("Error: unknown special character [%c]\n", current);
					buf[index++] = 'E';
				}

				if(index < 0)
				{
					goto cleanup;
				}
			}
			else
			{
				buf[index++] = current;
			}

			if(index >= size)
			{
				size = size * 2;
				buf = realloc(buf,size);
				if(!buf)
				{
					printf("Error: grow buffer failed, too much input\n");
					goto cleanup;
				}
			}
			current = fgetc(mad_lib_f);
		}

		printf("%s\n",buf);
		printf("Final Size: %d\n",index);

		cleanup:
		if(mad_lib_f)
		{
			fclose(mad_lib_f);
		}
		if(buf)
		{
			free(buf);
		}
	}

	return 0;
}

void print_usage()
{
	printf("Usage: ./MadLibs <madlib_file.txt>\n");
}

int get_noun(char* buf, int i, int* size)
{
	char c = 0;

	printf("Give me a noun: ");
	c = getc(stdin);
	while(c != '\n')
	{
		buf[i++] = c;
		if(i >= *size)
		{
			*size = *size * 2;
			buf = realloc(buf,*size);
			if(!buf)
			{
				printf("Error: grow buffer failed, too much input\n");
				return -i;
			}
		}
		c = getc(stdin);
	}

	return i;
}

int get_verb(char* buf, int i, int* size)
{
	char c = 0;

	printf("Give me a verb: ");
	c = getc(stdin);
	while(c != '\n')
	{
		buf[i++] = c;
		if(i >= *size)
		{
			*size = *size * 2;
			buf = realloc(buf,*size);
			if(!buf)
			{
				printf("Error: grow buffer failed, too much input\n");
				return -i;
			}
		}
		c = getc(stdin);
	}

	return i;
}

int get_adjective(char* buf, int i, int* size)
{
	char c = 0;

	printf("Give me an adjective: ");
	c = getc(stdin);
	while(c != '\n')
	{
		buf[i++] = c;
		if(i >= *size)
		{
			*size = *size * 2;
			buf = realloc(buf,*size);
			if(!buf)
			{
				printf("Error: grow buffer failed, too much input\n");
				return -i;
			}
		}
		c = getc(stdin);
	}

	return i;
}

int get_adverb(char* buf, int i, int* size)
{
	char c = 0;

	printf("Give me an adverb: ");
	c = getc(stdin);
	while(c != '\n')
	{
		buf[i++] = c;
		if(i >= *size)
		{
			*size = *size * 2;
			buf = realloc(buf,*size);
			if(!buf)
			{
				printf("Error: grow buffer failed, too much input\n");
				return -i;
			}
		}
		c = getc(stdin);
	}

	return i;
}
